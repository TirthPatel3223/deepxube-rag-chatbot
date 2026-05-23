# DeepXube RAG Chatbot — File Guide

> Every folder and file in this project, with its role explained.

---

## Root: `website_langgraph/`

| File | Role |
|---|---|
| `README.md` | Quick-start guide (prerequisites, install, run) |
| `PROJECT_STATE.md` | Living project state document (architecture, decisions, status) |
| `FILE_GUIDE.md` | **This file** — index of every file and its purpose |

---

## Backend: `backend/`

| File | Role |
|---|---|
| `requirements.txt` | Python dependencies (FastAPI, LangGraph, OpenAI, ChromaDB, etc.) |
| `.env.example` | Template for environment variables (API keys, paths, thresholds) |
| `data/` | ChromaDB persistent storage directory |

### `backend/app/` — Application Package

| File | Role |
|---|---|
| `__init__.py` | Package marker |
| `main.py` | **FastAPI entry point.** Defines `/api/chat`, `/api/health`, `/api/ingest` endpoints. Handles CORS, rate limiting, and startup initialization. |
| `config.py` | **Central configuration.** All settings loaded from `.env`. No magic strings elsewhere. |

### `backend/app/models/` — Data Models

| File | Role |
|---|---|
| `state.py` | **LangGraph pipeline state.** TypedDict defining all fields that flow through the pipeline (query, embedding, route, retrieved docs, response, etc.). |
| `schemas.py` | **API schemas.** Pydantic models for request/response bodies (ChatRequest, ChatResponse, HealthResponse, etc.). |

### `backend/app/services/` — Core Services

| File | Role |
|---|---|
| `embedding.py` | **Embedding service.** OpenAI `text-embedding-3-small` (1536 dims). Single and batch embedding. No fallback. |
| `llm.py` | **LLM generation service.** OpenAI `gpt-4o-mini` primary, Claude Haiku fallback. Handles API differences transparently. |
| `vectordb.py` | **ChromaDB wrapper.** Manages 3 collections (`faq`, `code`, `papers`). Query, add, clear operations. Cosine similarity. |
| `graph_store.py` | **Code call graph.** Loads `graph.json` into NetworkX DiGraph. Provides 1-hop expansion (callers/callees) for code retrieval. |

### `backend/app/session/` — Session Management

| File | Role |
|---|---|
| `manager.py` | **In-memory session storage.** Tracks conversation history (last 2 turns + rolling summary), domain guide flow state, and user choices. Sessions expire after 30 min. |

### `backend/app/pipeline/` — LangGraph Pipeline

| File | Role |
|---|---|
| `graph.py` | **Pipeline definition.** Builds and compiles the full LangGraph graph with all nodes and conditional edges. Entry point: `run_pipeline()`. |
| `edges.py` | **Edge functions.** Conditional routing logic (scope guard, FAQ hit, route classifier, cite check retry). |

### `backend/app/pipeline/nodes/` — Pipeline Nodes

Each file is a single LangGraph node — a pure function that takes state and returns updates.

| File | Role |
|---|---|
| `embed_query.py` | Embeds the user's query (1 API call, reused everywhere). Loads session state. |
| `scope_guard.py` | Checks if the query is in-scope by comparing against all collections. Out-of-scope → polite refusal. |
| `faq_lookup.py` | Queries FAQ collection. ≥0.92 similarity → return cached answer (zero LLM cost). |
| `route_classifier.py` | Classifies query into `{code, papers, domain_guide, both}` using anchor phrase similarity. No LLM call. |
| `code_retrieve.py` | Vector search in `code` collection + 1-hop graph expansion for structural context. |
| `paper_retrieve.py` | Vector search in `papers` collection for relevant research paper chunks. |
| `domain_guide.py` | **Multi-turn domain creation guide.** Loads context files progressively (ADDING_NEW_DOMAIN → EXAMPLES → TRAINING_GUIDE). Manages staged flow. |
| `generate.py` | **Core LLM call.** Builds prompt from context + history, generates response. The ONLY node with an LLM call. |
| `cite_check.py` | **Citation verification.** Regex-based check for `[name](file:line)` and `[paper §section]`. 1 retry budget. |
| `log_node.py` | Logs the interaction and updates session state (conversation history, rolling summary, domain guide stage). |

### `backend/app/ingestion/` — Data Ingestion Scripts

| File | Role |
|---|---|
| `ingest_code.py` | Reads 509 `.md` code docs, extracts YAML frontmatter, embeds, stores in ChromaDB `code` collection. Run: `python -m app.ingestion.ingest_code` |
| `ingest_papers.py` | Reads 7 PDF papers, chunks into 500-token windows with 100-token overlap, embeds, stores in `papers` collection. Run: `python -m app.ingestion.ingest_papers` |
| `ingest_faq.py` | Loads FAQ from `data/faq_seed.json` (currently empty). Embeds questions, stores answers in metadata. Run: `python -m app.ingestion.ingest_faq` |

### `backend/app/middleware/` — Middleware

| File | Role |
|---|---|
| `rate_limiter.py` | IP-based rate limiting via `slowapi`. Default: 10 requests/minute. |

---

## Frontend: `frontend/`

| File | Role |
|---|---|
| `index.html` | HTML template with SEO meta tags |
| `package.json` | Node.js dependencies (React, React Router, React Markdown) |
| `vite.config.js` | Vite build configuration |

### `frontend/src/` — React Application

| File | Role |
|---|---|
| `main.jsx` | React entry point (renders App into DOM) |
| `App.jsx` | Root component with React Router (Chat + Graph pages) |
| `index.css` | **Global design system.** Dark theme, Inter font, glassmorphism, animations. |

### `frontend/src/components/Chat/` — Chat Components

| File | Role |
|---|---|
| `ChatWindow.jsx` | Main chat container. Message list, API calls, auto-scroll, suggestion chips. |
| `MessageBubble.jsx` | Single message display. Markdown rendering for assistant, plain text for user. |
| `InputBar.jsx` | Auto-resizing textarea with Enter-to-send. |
| `TypingIndicator.jsx` | Animated three-dot loading indicator. |

### `frontend/src/components/Layout/` — Layout Components

| File | Role |
|---|---|
| `Header.jsx` | Top nav bar with logo, Chat/Graph navigation, New Chat button. |

### `frontend/src/components/GraphExplorer/` — Graph Explorer

| File | Role |
|---|---|
| `GraphExplorer.jsx` | **Main container.** Loads graph data from API, manages expansion/filter/selection state, orchestrates canvas + toolbar + sidebar. |
| `GraphCanvas.jsx` | **Cytoscape.js renderer.** Force-directed layout (fCoSE), module-based color coding, click-to-expand (module→classes→methods), node selection with neighbor highlighting. |
| `GraphToolbar.jsx` | **Top toolbar.** Search input (filters nodes by name/module), edge kind toggle pills (calls+inherits default), zoom/layout controls, live node/edge count. |
| `GraphSidebar.jsx` | **Right-side docs panel.** Slides in on node selection. Fetches .md documentation from `GET /api/graph/node/{id}/docs`, renders via react-markdown. Shows kind badge, module, file, line numbers. |

### `frontend/src/utils/` — Utility Functions

| File | Role |
|---|---|
| `exportChatPdf.js` | **PDF export.** Generates a styled A4 PDF of the full chat conversation using jsPDF. Strips markdown, handles word-wrapping, multi-page overflow, branded header/footer. |

### `frontend/src/services/` — API Service Layer

| File | Role |
|---|---|
| `api.js` | Backend communication. `sendMessage()`, `checkHealth()`, `triggerIngest()`. Session ID persisted in localStorage. |

### `frontend/src/styles/` — Component Styles

| File | Role |
|---|---|
| `chat.css` | Chat page, message bubbles, typing indicator, input bar styles. |
| `layout.css` | Header, navigation, graph placeholder styles. |
