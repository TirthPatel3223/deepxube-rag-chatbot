# DeepXube RAG Chatbot — Project State

> **Last updated:** 2026-05-07
> **Purpose:** Drop-in context for any new LLM chat about this sub-project.

---

## 1. What This Is

A **Retrieval-Augmented Generation (RAG) chatbot** for the DeepXube framework, embeddable on Prof. Agostinelli's website. Answers questions about:
1. The DeepXube **codebase** (509 documented functions/classes)
2. The underlying **research papers** (7 PDFs)
3. **Common questions** (FAQ cache for zero-LLM-cost answers)
4. **Creating new puzzle domains** (step-by-step guide with code templates)

## 2. Architecture

### Tech Stack

| Component | Technology | Status |
|---|---|---|
| Orchestration | LangGraph | ✅ Built |
| Backend API | FastAPI | ✅ Built |
| Frontend | Vite + React | ✅ Built |
| Vector DB | ChromaDB (local, 3 collections) | ✅ Built |
| Embedding | OpenAI `text-embedding-3-small` | ✅ Built |
| LLM (primary) | OpenAI `gpt-4o-mini` | ✅ Built |
| LLM (fallback) | Anthropic Claude Haiku | ✅ Built |
| Graph traversal | NetworkX (from `graph.json`) | ✅ Built |
| Rate limiting | slowapi (10/min per IP) | ✅ Built |
| Graph visualization | Cytoscape.js (fCoSE layout) | ✅ Built |
| Graph docs panel | Click-to-inspect side panel | ✅ Built |
| Graph search | Filter nodes by name/module | ✅ Built |
| Graph edge filtering | Toggle calls/inherits/reads/writes/etc. | ✅ Built |
| Graph API | `GET /api/graph` + `GET /api/graph/node/{id}/docs` | ✅ Built |
| Reranker | ms-marco-MiniLM | ❌ Not yet |
| Preset subgraph tabs | A* search, Q search, etc. | ❌ Not yet |
| Workflow path highlighting | BFS traversal with presets | ❌ Not yet |
| Bidirectional sync | Chatbot ↔ Graph context | ❌ Not yet |
| Hierarchical layout | Dagre layout toggle | ❌ Not yet |
| Persistent sessions | SQLite/Redis | ❌ In-memory only |
| Deployment | Docker/hosted | ❌ Localhost only |

### LangGraph Pipeline Flow

```
user_query + session
     │
     ▼
embed_query ─── (domain guide active?) ──► domain_guide ──► generate ──► log ──► END
     │
     ▼
scope_guard ──► (out of scope?) ──► polite_refuse ──► END
     │
     ▼
faq_lookup ──► (FAQ hit, sim≥0.92?) ──► return_cached ──► END
     │
     ▼
route_classifier ──► {code, papers, domain_guide, both}
     │
     ├─ code_retrieve ──► (graph expand) ──► generate ──► cite_check ──► log ──► END
     ├─ paper_retrieve ──► generate ──► cite_check ──► log ──► END
     ├─ both ──► code_retrieve ──► paper_retrieve ──► generate ──► cite_check ──► log ──► END
     └─ domain_guide ──► generate ──► log ──► END
```

### Domain Guide Multi-Turn Flow

```
"none" → "overview"   : Load ADDING_NEW_DOMAIN.md overview, ask if user wants step-by-step
"overview" → "template": Load full ADDING_NEW_DOMAIN.md, walk through 3 decisions, serve template
"template" → "examples": Load matching section from EXAMPLES.md
"examples" → "training": Load TRAINING_GUIDE.md, guide through training decisions
"training" → "none"   : Flow complete, return to normal routing
```

## 3. ChromaDB Collections

| Collection | Content | Expected Size |
|---|---|---|
| `code` | 1 vector per .md function/class doc | ~509 docs |
| `papers` | 500-token chunks from 7 PDFs | ~150-350 chunks |
| `faq` | Pre-curated Q&A pairs | 0 (empty, ready for population) |

## 4. Decisions Made

- ✅ OpenAI-only embeddings (no fallback)
- ✅ OpenAI gpt-4o-mini primary, Claude Haiku fallback for LLM
- ✅ ChromaDB with 3 collections
- ✅ FAQ-first short-circuit (≥0.92 = cache hit, zero LLM cost)
- ✅ Embedding-based routing (no LLM call for routing)
- ✅ Domain guide as 4th route with staged context loading
- ✅ In-memory session management for dev
- ✅ Rate limiting from day one
- ✅ 1 .md file = 1 vector for code docs
- ✅ Fixed 500-token windows for paper chunks

## 5. What's NOT Built Yet

- [ ] **Preset subgraph tabs** — Bottom tabs for A* search, Q search, training pipeline subgraphs
- [ ] **Workflow path highlighting** — BFS traversal with preset paths
- [ ] **Bidirectional chatbot ↔ graph sync** — Click node → chat context, chat mentions → highlight nodes
- [ ] **Hierarchical layout toggle** — Dagre top-to-bottom layout option
- [ ] **Persistent sessions** — SQLite or Redis
- [ ] **Reranker** — ms-marco-MiniLM cross-encoder
- [ ] **FAQ auto-promotion** — Approval queue for generated answers
- [ ] **Docker containerization**
- [ ] **Production deployment** — Vercel/VM hosting

## 6. How to Run

```bash
# Backend
cd backend
pip install -r requirements.txt
cp .env.example .env  # Add API keys
python -m app.ingestion.ingest_code
python -m app.ingestion.ingest_papers
uvicorn app.main:app --reload --port 8000

# Frontend
cd frontend
npm install
npm run dev
```

## 7. File Structure

See `FILE_GUIDE.md` for a complete index of every file and its role.
