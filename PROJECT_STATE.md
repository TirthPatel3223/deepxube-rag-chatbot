# DeepXube RAG Chatbot — Project State

> **Purpose of this file:** drop-in context for any new LLM chat. Tells the model who I am, what the project is, what's done, what's planned, and what decisions are still open. Update at the end of each working session.

---

## 1. Who I am

- **Name:** Tirth Patel
- **Role:** Student working on a research-adjacent project for **Prof. Forest Agostinelli** (Univ. of South Carolina).
- **Email:** tirthpatel3223@gmail.com

## 2. What the project is

Prof. Agostinelli developed the **DeepCubeA** and **DeepXube** algorithms — deep-learning-trained heuristic functions that solve large-scale combinatorial puzzles (Rubik's Cube, sliding puzzles, goal-conditioned planning, etc.).

He wants the DeepXube codebase and algorithm to be **easily accessible** to outside users (researchers, students, practitioners) via his website.

**My proposal:** a Retrieval-Augmented Generation (RAG) chatbot, embeddable on his website, that answers user questions about:
1. The DeepXube **codebase** (functions, classes, call graph).
2. The underlying **research papers** (~15 papers).
3. **Common pre-curated questions** (FAQ cache to save API cost).

Built on **LangGraph**, optimized for **accuracy + low API cost**, with explicit citations.

## 3. Working directory layout

Root: `c:\Users\tirth\OneDrive\Desktop\Agentic_Systems\Professor Agostinelli Project\`

- `deepxube-main/` — the full DeepXube Python library (source).
- `deepxube-main/docs/` — auto-generated documentation (already built):
  - `functions/<module>/<Class>/<method>.md` — one Markdown file per function/method, with rich YAML frontmatter (`qualified_name`, `file`, `line_start`, `line_end`, `class`, `module`, `parameters`, `returns`, `decorators`, `raises`, `callees`, `reads_attrs`, `writes_attrs`) plus prose (docstring, signature, parameter table, source snippet).
  - `classes/`, `modules/` — class- and module-level Markdown summaries.
  - `graph.json` — full call/data-flow graph: nodes = functions/classes/modules, edges = caller→callee.
  - `cli_flags.json`, `missing_docstrings.md`, `skipped_trivial.md` — supporting metadata.
  - `deepxube-main/docs/context_files/ADDING_NEW_DOMAIN.md` — [NEW] Highly prescriptive, copy-pasteable "fill-in-the-blanks" template for adding new domains without needing to understand the underlying framework.
  - `deepxube-main/docs/context_files/TRAINING_GUIDE.md` — [NEW] Comprehensive guide detailing V/Q/Policy heuristic pathways, pathfinders (A*, Beam, Supervised), and exact CLI commands.
- `pitch_context.md` — full pitch context I generated, ready to feed to a presentation-design LLM.
- `PROJECT_STATE.md` — **this file**.

Research papers: **not yet uploaded** (planned ~15).

## 4. Architecture — current design

### 4.1 Stores (built once, offline)

**Single Vector DB, three collections.** All three logical stores live as separate **collections** (or namespaces) inside one vector DB instance. This keeps infrastructure simple (one process, one dependency) while preserving the routing, citation, and cost benefits of logical separation.

| Collection | Content | Backend | Why separate |
|---|---|---|---|
| **`faq`** | `{question_embedding → canonical_answer, sources}` | Vector DB collection | Short-circuit cache — zero LLM cost on hits; fundamentally different retrieval pattern (threshold match, not top-k) |
| **`code`** | One vector per function/class `.md` (rich metadata) | Vector DB collection **+** in-memory NetworkX graph from `graph.json` | Needs graph traversal (1-hop callers/callees) that other collections don't; citations use `file:line` format |
| **`papers`** | Section-level chunks of ~15 papers | Vector DB collection | Citations use `paper_id §section` format; keeps top-k focused on academic content without dilution from code docs |

**Why three collections, not one unified index:** (1) FAQ is a cache/short-circuit, not a retrieval source — merging it loses the zero-LLM-cost fast path. (2) Code retrieval has a second modality (graph expansion) that shouldn't run on paper queries. (3) Separate collections let the router query only the relevant subset, keeping top-k results focused instead of diluted across content types. (4) Citation formats differ by type and stay clean by construction.

**Why hybrid (vector + graph) for code:** pure graph DBs (Neo4j) are overkill for a few hundred nodes and add infra cost. Vector DB handles "what does X do?" semantic hit; in-memory graph cheaply answers "what calls X / what does X call?" via `graph.json` traversal.

### 4.2 Routing — embedding-based, not LLM-based

- One embedding call per user query, reused everywhere.
- **FAQ-first**: if cosine similarity to nearest FAQ ≥ τ_high (e.g. 0.92) → return cached answer, **no LLM call**.
- Borderline (e.g. 0.78) → **regenerate** (decided).
- Else → small classifier on the same embedding picks fan-out subset of {code, papers, both}.

### 4.3 LangGraph pipeline (current sketch)

```
user_query
   │
   ▼
embed_query           (1 embedding, reused)
   │
   ▼
scope_guard ──► out-of-scope → polite_refuse → END
   │
   ▼
faq_lookup ──► sim ≥ τ_high → return_cached → END   (no LLM call)
   │ (miss/borderline)
   ▼
route_classifier      picks {code, papers, both}
   │
   ├──► code_retrieve ──► graph_expand (1-hop callers/callees)
   └──► paper_retrieve
              │
              ▼
        rerank + dedupe   (local cross-encoder, no LLM)
              │
              ▼
        generate          (1 LLM call, w/ rolling-summary memory)
              │
              ▼
        cite_check        (rule-based; 1 retry budget)
              │
              ▼
        log + maybe-promote-to-FAQ
              │
              ▼
             END
```

### 4.4 Conversation memory

- Rolling summary (≤200 tokens) + last 2 turns verbatim.
- Multi-turn supported but token-budget-strict.
- Follow-ups ("where is that called from?") resolved by prepending summary to query and re-running retrieval — no growing transcript.

### 4.5 Citations

- **Code answers:** `qualified_name` + `file:line_start` (pulled from frontmatter).
- **Paper answers:** `paper_id §section`.
- `cite_check` is structural/regex, not an LLM call.

### 4.6 Out-of-scope handling

Polite refusal (decided).

## 5. Cost minimization summary

| Step | LLM calls |
|---|---|
| Embed query | 0 (embedding only) |
| FAQ hit | **0** |
| FAQ miss → full path | **1** generate, +1 retry max |
| Reranker | 0 (local cross-encoder) |
| Cite check | 0 (rule-based) |

## 6. Decisions made

- ✅ Fan-out to multiple sources, but FAQ-first short-circuit for cheap hits.
- ✅ Borderline FAQ similarity → regenerate (don't return cached).
- ✅ Hybrid code store: vector DB + NetworkX graph from `graph.json`.
- ✅ Function/class `.md` files = retrieval units (already built, perfect granularity).
- ✅ Section-level chunking for papers.
- ✅ Citations required (file:line for code, paper §section for papers).
- ✅ Multi-turn memory via rolling summary, strict token budget.
- ✅ Polite refusal for out-of-scope queries.
- ✅ LangGraph as orchestration framework.
- ✅ Single vector DB instance with three collections (`faq`, `code`, `papers`) — logical separation for routing/citations/cost, no extra infra.

## 7. Decisions still open

- ❓ **Embedding model** — leaning OpenAI `text-embedding-3-small`, not finalized.
- ❓ **Generation LLM** — leaning Claude Haiku 4.5 or GPT-4o-mini, not finalized.
- ❓ **Vector DB** — Chroma or LanceDB (local) for prototype; Pinecone/Weaviate if hosted scale needed. (Single instance, three collections — decided; specific product still open.)
- ❓ **FAQ curation workflow** — manual weekly review vs. auto-promote with approval queue.
- ❓ **Code-example generation** — should bot produce runnable examples or stick to explain + cite?
- ❓ **Router classifier** — embedding-similarity heuristic vs. small logistic regression on embeddings.
- ❓ **Frontend integration** — exact widget/embed mechanism for Prof. Agostinelli's website.

## 8. Roadmap (6 stages)

1. **Stage 1 — Codebase docs.** ✅ Done. `deepxube-main/docs/` is fully auto-generated.
2. **Stage 2 — Ingest pipeline.** ✅ Done. Code docs vectorized into ChromaDB; `graph.json` loaded into NetworkX.
3. **Stage 3 — Paper ingestion.** ✅ Done. 7 PDFs section-chunked and embedded into `papers` collection.
4. **Stage 4 — FAQ seed.** ✅ Done. Collection ready (empty, awaiting population).
5. **Stage 5 — LangGraph build + API + Frontend.** ✅ Done. Full pipeline wired end-to-end behind FastAPI. React frontend with chat + graph explorer.
   - Graph Explorer: Cytoscape.js visualization with fCoSE layout, module-level expansion, edge filtering, search, and click-to-inspect docs panel.
   - Remaining: preset subgraph tabs, workflow path highlighting, bidirectional chatbot↔graph sync, hierarchical layout toggle.
6. **Stage 6 — Deploy.** Embed widget on website; log queries; grow FAQ from approved misses. **Not started.**

## 9. Current status

- **Where I am:** end of Stage 5. Full RAG pipeline, chat UI, and graph explorer are functional on localhost.
- **Immediate next step:** testing, polish, and production deployment planning.
- **Graph explorer completed features:** module-level drill-down, edge kind filtering, search, docs side panel, module-based color coding.
- **Graph explorer deferred:** preset subgraph tabs (A*, Q search), workflow paths, chatbot↔graph sync, hierarchical layout.

## 10. Files I've already produced in this directory

- `pitch_context.md` — comprehensive context for designing a presentation deck for Prof. Agostinelli.
- `PROJECT_STATE.md` — this file. Drop-in context for fresh LLM chats.
- `deepxube-main/docs/context_files/ADDING_NEW_DOMAIN.md` — prescriptive fill-in-the-blanks template for adding new domains. Includes explicit instructions for the RAG LLM to bridge users to the training guide after domain creation.
- `deepxube-main/docs/context_files/TRAINING_GUIDE.md` — comprehensive training pathway guide for RAG.

## 11. How to use this file in a new LLM chat

Paste this whole file at the start of the conversation, then state what you want help with. The LLM will have:
- Who I am and who I'm working for.
- The project's purpose.
- Existing materials and where they live.
- The current architecture and the reasoning behind each choice.
- What's been decided vs. still open.
- Where I am on the roadmap.

Ask the LLM clarifying questions if the request is ambiguous; do not assume changes to the architecture without checking.
