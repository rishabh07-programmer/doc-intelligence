I am building Project #5 of my Upwork AI portfolio — a Multi-agent Lead Generation 
and Outreach System. This is my background and what I've already built:

COMPLETED PROJECTS:
- Project #1: Hotel Rajendra restaurant management app (MERN, deployed on Vercel)
- Project #2: RAG Knowledge Base Chatbot (Python, FastAPI, Voyage AI embeddings, 
  ChromaDB, Claude API, deployed on Render)
- Project #4: DocIntel — AI Document Intelligence Platform (Gemini 2.5 Flash + 
  Claude Sonnet, FastAPI, deployed on Render at https://doc-intelligence-y65i.onrender.com)

MY SKILL LEVEL:
- Python: Intermediate
- FastAPI: Comfortable, used on two projects
- Claude API: Comfortable (RAG pipeline, risk analysis, prompt construction)
- Gemini API: Used for PDF extraction (native PDF input via google-genai SDK)
- Deployment: Render (backend) + Vercel (frontend), understand memory limits, 
  env variables, ephemeral storage
- Claude Code: Comfortable with CLAUDE.md, agentic workflows, git
- Frontend: Plain HTML/CSS/JS served from FastAPI

HARD LESSONS LEARNED (apply all of these from day one):
1. Check deployment memory limits before choosing any library — Render free tier 
   is 512MB. No local ML inference. API-based services only.
2. Check third-party API rate limits before building any feature.
3. Give specific UI design direction from the FIRST prompt — exact fonts, colors, 
   reference apps. Never vague adjectives like "clean and professional".
4. Deploy a hello-world to Render FIRST before writing real features.
5. Git init and first commit in Step 0. Commit after every working milestone.
6. Set CLAUDE.md from the start: no browser automation, concise terminal output.
7. Use cheapest suitable model (Haiku) during dev. Swap to Sonnet only for demo.
8. PowerShell has no && operator. Create a start.ps1 script for env variables.
9. Never build boring frontends — minimal but intentional design, good typography, 
   purposeful animations. Reference: Linear, Vercel, Notion design language.
10. Loading states must be animated — cycling text phrases + thin progress bar, 
    not static "loading..." text.

WHAT I WANT FOR THIS PROJECT:
- Scoped-down v1 first (not the full $3,500 version on day one)
- Tech stack explicitly checked against Render free tier before writing code
- Specific UI design direction in the first frontend prompt
- CLAUDE.md set up in Step 0
- Git commits after every milestone
- Haiku during dev, Sonnet for demo recording

PROJECT GOAL:
Multi-agent lead generation system:
- Input: a job title / industry / location
- Agent 1 (Gemini): researches and finds leads
- Agent 2 (Claude): writes personalized outreach emails per lead
- Output: results shown in a clean dashboard UI, exportable as CSV

Start with: propose a realistic scoped-down v1 and confirm the tech stack 
accounts for Render free tier limits before we write any code.
