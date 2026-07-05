# AI Document Intelligence Platform — Project #4 (Upwork portfolio)

## What this is
Upload a PDF (contract/invoice/report) → Gemini 2.5 Flash extracts structured
JSON → Claude analyzes risks + summarizes → results shown in UI, JSON downloadable.

## Hard rules
- NEVER use browser automation tools for testing. Rishabh tests manually in his own browser.
- Keep terminal responses short: what was done, the result, any errors. Never repeat project context back.
- Use claude-haiku-4-5 for all Claude API calls during development. Sonnet only for final demo.
- Deployment target is Render free tier: 512MB RAM. Never add a library that does
  local ML inference. Prefer API calls. Check package weight before adding dependencies.
- No database in v1. App is stateless. Do not add persistence unless asked.
- Only build what is asked. No extra features, placeholder UI, or fake elements.
- Commit to git after every working milestone.

## Stack
- Backend: Python, FastAPI, served with uvicorn
- Extraction: Gemini 2.5 Flash via google-genai SDK (native PDF input, 10MB upload cap)
- Reasoning: Claude Haiku via anthropic SDK
- Frontend: plain HTML/CSS/JS served from FastAPI (same pattern as RAG chatbot)
- Deploy: Render free tier
- API keys: environment variables only (GEMINI_API_KEY, ANTHROPIC_API_KEY)

## Design direction (frontend)
Fonts: Fraunces (headings) + Inter (body), via Google Fonts.
Colors: bg #faf9f6, text #1a1a2e, accent #166534, risk-medium #d97706, risk-high #dc2626.
Layout: two-column results — extracted field cards left, risk flags + summary right.
Style: legal-tech. Thin 1px borders, generous whitespace, no shadows/gradients.