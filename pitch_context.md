# DeepXube RAG Chatbot — Pitch Context

## 1. Who & why

- **Author of pitch:** Tirth Patel, student working with Prof. Forest Agostinelli (Univ. of South Carolina).
- **Audience of the presentation:** Prof. Agostinelli.
- **Prof.'s research:** DeepCubeA and DeepXube — algorithms that train heuristic functions (deep neural networks) to solve large-scale combinatorial puzzles (Rubik's Cube, sliding puzzles, planning problems with goal specifications, etc.).
- **Prof.'s stated need:** make the DeepXube codebase and algorithm **easily accessible** to outside users (researchers, students, practitioners) via his website.
- **My proposal:** build a Retrieval-Augmented Generation (RAG) chatbot, embeddable on his website, that answers user questions about (a) the DeepXube codebase, (b) the underlying research papers, and (c) common pre-curated questions — with low API cost and accurate citations.

## 2. What materials we already have

- **Codebase:** `deepxube-main/` — the full DeepXube Python library.
- **Auto-generated documentation:** `deepxube-main/docs/`
  - `functions/<module>/<Class>/<method>.md` — one Markdown file per function/method, with rich YAML frontmatter:
    - `qualified_name`, `file`, `line_start`, `line_end`, `class`, `module`
    - `parameters`, `returns`, `decorators`, `raises`
    - `callees` (resolved + unresolved), `reads_attrs`, `writes_attrs`
    - Followed by prose: docstring, signature, parameter table, source snippet.
  - `classes/`, `modules/` — class- and module-level Markdown summaries.
  - `graph.json` — the complete call/data-flow graph: nodes = functions/classes, edges = caller→callee relationships.
  - `cli_flags.json`, `missing_docstrings.md`, `skipped_trivial.md` — supporting metadata.
- **Research papers:** ~15 papers (DeepCubeA, DeepXube, related). Not yet ingested. PDFs assumed.
- **FAQ database:** to be hand-curated; format = `{question, canonical_answer, sources}`.

## 3. Goals & constraints

- **Accuracy first** — answers must cite the exact source (`file:line` for code, `paper §section` for papers).
- **Low API cost** — minimize LLM calls; reuse embeddings; serve cached answers when possible.
- **Polite refusal** for out-of-scope questions.
- **Multi-turn conversation** support, but with a strict token budget for history.
- **Embeddable** on Prof. Agostinelli's website as a chat widget.

## 4. Architecture — LangGraph pipeline

### 4.1 Stores (built once, offline)

| Store | Content | Backend | Why |
|---|---|---|---|
| **FAQ store** | `{question_embedding → canonical_answer, sources}` | Vector DB | Zero LLM cost on cache hits |
| **Code store** | One vector per function/class `.md` (rich metadata) | Vector DB + in-memory NetworkX graph from `graph.json` | Vector → semantic retrieval; graph → 1-hop caller/callee expansion without extra LLM call |
| **Paper store** | Section-level chunks of ~15 papers | Vector DB | Section-grained citations |

> **Why hybrid (vector + graph) for code:** Pure graph DBs like Neo4j are overkill for a few hundred nodes and add infrastructure cost. Vector DB handles the "what does X do?" semantic hit; the in-memory graph cheaply answers "what calls X / what does X call?" by traversing `graph.json`.

### 4.2 Routing — cheap embedding-based, not LLM-based

- One embedding call per user query, reused everywhere.
- **FAQ-first**: if cosine similarity to nearest FAQ ≥ τ_high (e.g. 0.92) → return cached answer, **no LLM call**.
- Else: a small classifier on the same embedding decides whether to fan out to {code, papers, both}.

### 4.3 The LangGraph

```
                ┌──────────────────────┐
                │   entry: user_query  │
                └──────────┬───────────┘
                           │
                  ┌────────▼─────────┐
                  │ embed_query      │  (1 embedding call, reused)
                  └────────┬─────────┘
                           │
                  ┌────────▼─────────┐
                  │ scope_guard      │──► out-of-scope? → polite_refuse → END
                  └────────┬─────────┘
                           │
                  ┌────────▼─────────┐
                  │ faq_lookup       │──► sim ≥ τ_high → return_cached → END
                  └────────┬─────────┘     (no LLM call)
                           │ (miss or borderline)
                  ┌────────▼─────────┐
                  │ route_classifier │  picks subset of {code, papers}
                  └────────┬─────────┘
                ┌──────────┼──────────┐
                ▼          ▼          ▼
         ┌──────────┐ ┌──────────┐   (parallel branches; LangGraph fan-out)
         │ code_    │ │ paper_   │
         │ retrieve │ │ retrieve │
         └────┬─────┘ └────┬─────┘
              │            │
         ┌────▼─────┐      │
         │ graph_   │      │   ← expand top-k hits with 1-hop
         │ expand   │      │     callers/callees from graph.json
         └────┬─────┘      │
              └─────┬──────┘
                    ▼
             ┌────────────┐
             │ rerank +   │   cross-encoder rerank (local model), dedupe
             │ dedupe     │
             └─────┬──────┘
                   ▼
             ┌────────────┐
             │ generate   │   LLM call w/ citations + rolling summary
             └─────┬──────┘
                   ▼
             ┌────────────┐
             │ cite_check │   verify every claim has a source;
             │            │   if not, retry once
             └─────┬──────┘
                   ▼
             ┌────────────┐
             │ log +      │   store {q, a, sources} for FAQ curation
             │ promote    │
             └─────┬──────┘
                   ▼
                  END
```

### 4.4 Conversation memory

- Rolling summary (≤200 tokens) + last 2 turns verbatim.
- Follow-ups like "where is that called from?" are resolved by prepending the summary to the new query and re-running retrieval — no growing transcript.

### 4.5 Citations

- **Code answers** cite `qualified_name` + `file:line_start` (pulled from frontmatter).
- **Paper answers** cite `paper_id §section`.
- `cite_check` is a structural/regex check, not an LLM call.

## 5. Cost minimization summary

| Step | LLM calls |
|---|---|
| Embed query | 0 (embedding only) |
| FAQ hit | **0** |
| FAQ miss → full path | **1** generate, + 1 retry max |
| Reranker | 0 (local cross-encoder) |
| Cite check | 0 (rule-based) |

Net: most repeated questions cost ~$0; novel questions cost a single small LLM call.

## 6. Tech stack — open / to be finalized

- **Vector DB candidates:** Chroma or LanceDB (local, free) for prototype; Pinecone/Weaviate if hosted scale needed.
- **Embedding model:** OpenAI `text-embedding-3-small` (cheap, strong) — final pick TBD.
- **LLM:** Claude Haiku 4.5 or GPT-4o-mini for generate step — final pick TBD.
- **Orchestration:** LangGraph.
- **Frontend:** chat widget on Prof. Agostinelli's website.

## 7. Roadmap

1. **Stage 1 (current):** finalize codebase docs (`deepxube-main/docs/` already auto-generated).
2. **Stage 2:** ingest pipeline — vectorize `.md` function docs + load `graph.json` into NetworkX.
3. **Stage 3:** ingest research papers (section-chunked).
4. **Stage 4:** seed FAQ store with ~30–50 hand-written entries.
5. **Stage 5:** build LangGraph nodes end-to-end, deploy behind a simple FastAPI endpoint.
6. **Stage 6:** embed widget on website; log queries; grow FAQ from approved misses.

## 8. Open decisions to flag in the talk

- Embedding + LLM provider lock-in.
- Hosted vs. self-hosted vector DB.
- FAQ curation workflow (manual weekly vs. auto-promotion with review).
- Whether the bot should also generate runnable code examples or stick to explanation + citation.

## 9. Why this approach is the right fit

- The auto-generated `.md` docs are **already perfect retrieval units**: structured frontmatter for filtering, prose for semantic match, source snippet for grounded answers.
- `graph.json` gives us **structural knowledge for free** — no need to ask the LLM "what calls this function?".
- FAQ-first routing aligns directly with the cost constraint.
- Section-chunked papers + per-function code docs give **citation granularity** users can verify.

