# DeepXube RAG Chatbot — Website + LangGraph

A Retrieval-Augmented Generation chatbot for the DeepXube framework, built with **LangGraph** (backend pipeline), **FastAPI** (API server), and **Vite + React** (frontend).

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- OpenAI API key
- Anthropic API key (for LLM fallback)

### 1. Backend Setup

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your API keys

# Run ingestion (required before first use)
python -m app.ingestion.ingest_code
python -m app.ingestion.ingest_papers
python -m app.ingestion.ingest_faq

# Start the server
uvicorn app.main:app --reload --port 8000
```

### 2. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start dev server
npm run dev
# → Opens at http://localhost:5173
```

### 3. Use the Chatbot

Open http://localhost:5173 in your browser and start asking questions!

## Architecture

See `PROJECT_STATE.md` for detailed architecture documentation.
See `FILE_GUIDE.md` for a description of every file and folder.
