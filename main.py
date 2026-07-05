import json
import os

import anthropic
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from google import genai
from google.genai import types

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

EXTRACTION_PROMPT = """You are a document analysis expert. Analyze this document and return ONLY valid JSON
with this exact structure, no markdown, no explanation:
{
  'document_type': 'contract | invoice | report | unknown',
  'parties': ['name1', 'name2'],
  'dates': {'effective_date': '...', 'expiration_date': '...'},
  'key_amounts': [{'label': '...', 'amount': '...'}],
  'key_clauses': [{'title': '...', 'summary': '...'}],
  'raw_summary': 'One paragraph plain English summary of what this document is about'
}
Return null for any field you cannot find. Always return valid JSON."""


def extract_with_gemini(pdf_bytes: bytes) -> dict:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
            EXTRACTION_PROMPT,
        ],
    )
    text = response.text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        text = "\n".join(lines).strip()
    return json.loads(text.strip())


RISK_SYSTEM_PROMPT = "You are a legal and business risk analyst. Analyze documents and identify risks clearly."


def analyze_risks(extracted_data: dict) -> dict:
    try:
        client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        user_prompt = f"""Based on this extracted document data, identify risks and return ONLY valid JSON with no markdown:
{{
  'risk_flags': [
    {{'title': '...', 'severity': 'high | medium | low', 'explanation': '...'}}
  ],
  'overall_risk_level': 'high | medium | low',
  'recommendations': ['...', '...'],
  'analyst_summary': 'Two to three sentence plain English summary of the main risks.'
}}
Document data: {json.dumps(extracted_data)}"""

        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            system=RISK_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        text = response.content[0].text.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            lines = [l for l in lines if not l.strip().startswith("```")]
            text = "\n".join(lines).strip()
        return json.loads(text)
    except Exception as e:
        return {"error": "risk analysis failed", "detail": str(e)}


@app.get("/")
def health():
    return FileResponse("static/index.html")


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {"error": "invalid file type", "detail": "Only PDF files are accepted"}

    pdf_bytes = await file.read()

    if len(pdf_bytes) > MAX_FILE_SIZE:
        return {"error": "file too large", "detail": "File exceeds the 10MB upload limit"}

    try:
        extraction = extract_with_gemini(pdf_bytes)
    except Exception as e:
        return {"error": "extraction failed", "detail": str(e)}

    analysis = analyze_risks(extraction)

    return {"extraction": extraction, "analysis": analysis}
