# ============================================================================
# DeepXube RAG Chatbot - FastAPI Application
# ============================================================================
# Main entry point for the backend server.
#
# Endpoints:
#   POST /api/chat    — Main chat endpoint (rate limited)
#   GET  /api/health  — Health check (collection stats, graph status)
#   POST /api/ingest  — Trigger re-ingestion of collections
#
# Run:
#   cd backend
#   uvicorn app.main:app --reload --port 8000
# ============================================================================

import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.config import settings
from app.models.schemas import (
    ChatRequest,
    ChatResponse,
    Citation,
    GraphResponse,
    HealthResponse,
    IngestRequest,
    IngestResponse,
    NodeDocsResponse,
)
from app.middleware.rate_limiter import limiter
from app.pipeline.graph import run_pipeline
from app.services.graph_store import graph_store
from app.services.vectordb import vectordb_service
from app.session.manager import session_manager
from app.ingestion.ingest_code import ingest_code_docs
from app.ingestion.ingest_papers import ingest_papers
from app.ingestion.ingest_faq import ingest_faq

# ── Logging ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)


# ── Lifespan (startup/shutdown) ─────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown events.

    On startup:
    - Load the code call graph from graph.json
    - Log collection statistics
    """
    # Startup
    logger.info("=" * 60)
    logger.info("DeepXube RAG Chatbot — Starting up")
    logger.info("=" * 60)

    # Load the code call graph
    graph_store.load()

    # Log collection stats
    stats = vectordb_service.get_collection_stats()
    logger.info(f"ChromaDB collections: {stats}")

    if all(v == 0 for v in stats.values()):
        logger.warning(
            "All collections are empty! Run ingestion first:\n"
            "  python -m app.ingestion.ingest_code\n"
            "  python -m app.ingestion.ingest_papers\n"
            "  python -m app.ingestion.ingest_faq"
        )

    yield

    # Shutdown
    logger.info("DeepXube RAG Chatbot — Shutting down")


# ── FastAPI App ─────────────────────────────────────────────────────────
app = FastAPI(
    title="DeepXube RAG Chatbot",
    description=(
        "A Retrieval-Augmented Generation chatbot for the DeepXube framework. "
        "Answers questions about the codebase, research papers, and guides "
        "users through creating new puzzle domains."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

# Rate limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS — allow the Vite dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",     # Vite dev server
        "http://localhost:3000",     # Alternative dev port
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Endpoints ───────────────────────────────────────────────────────────

@app.post("/api/chat", response_model=ChatResponse)
@limiter.limit(settings.RATE_LIMIT)
async def chat(request: Request, body: ChatRequest):
    """
    Main chat endpoint.

    Runs the full LangGraph pipeline: embed → scope guard → FAQ check →
    route → retrieve → generate → cite check → log.

    Rate limited to prevent API abuse (each non-FAQ query costs an LLM call).
    """
    logger.info(f"Chat request: query='{body.query[:60]}...' session={body.session_id}")

    try:
        result = await run_pipeline(
            query=body.query,
            session_id=body.session_id or "",
        )

        # Extract citations from result
        raw_citations = result.get("citations", [])
        citations = [
            Citation(
                source=c.get("source", ""),
                reference=c.get("reference", ""),
                type=c.get("type", ""),
            )
            for c in raw_citations
        ]

        return ChatResponse(
            response=result.get("response", "I couldn't generate a response."),
            citations=citations,
            session_id=result.get("session_id", ""),
            route=result.get("route", ""),
            is_faq_hit=result.get("is_faq_hit", False),
        )

    except Exception as e:
        logger.error(f"Pipeline error: {e}", exc_info=True)
        return ChatResponse(
            response=(
                "I encountered an error processing your request. "
                "Please try again in a moment."
            ),
            session_id=body.session_id or "",
            route="error",
        )


@app.get("/api/health", response_model=HealthResponse)
async def health():
    """
    Health check endpoint.

    Returns collection sizes, graph status, and active session count.
    Useful for monitoring and debugging.
    """
    stats = vectordb_service.get_collection_stats()
    return HealthResponse(
        status="ok",
        collections=stats,
        active_sessions=session_manager.get_active_session_count(),
        graph_loaded=graph_store.is_loaded,
        graph_nodes=graph_store.node_count,
    )


@app.post("/api/ingest", response_model=IngestResponse)
async def ingest(body: IngestRequest):
    """
    Trigger re-ingestion of one or all collections.

    This is an admin endpoint — in production, it should be protected.
    For development, it's open to allow easy re-indexing.
    """
    logger.info(f"Ingest request: target={body.target}, clear={body.clear_first}")

    details = {}

    if body.target in ("code", "all"):
        details["code"] = await ingest_code_docs(clear_first=body.clear_first)

    if body.target in ("papers", "all"):
        details["papers"] = await ingest_papers(clear_first=body.clear_first)

    if body.target in ("faq", "all"):
        details["faq"] = await ingest_faq(clear_first=body.clear_first)

    return IngestResponse(status="completed", details=details)


@app.get("/api/graph", response_model=GraphResponse)
async def get_graph():
    """
    Return the full code call-graph for visualization.

    Serves the graph.json data (778 nodes, 2518 edges) for the
    Cytoscape.js Graph Explorer. ~971KB, cacheable.
    """
    data = graph_store.get_full_graph_data()
    return GraphResponse(
        nodes=data.get("nodes", []),
        edges=data.get("edges", []),
    )


@app.get("/api/graph/node/{node_id:path}/docs", response_model=NodeDocsResponse)
async def get_node_docs(node_id: str):
    """
    Return the markdown documentation for a specific graph node.

    Used by the Graph Explorer side panel when a user clicks a node.
    The node_id is URL-encoded (e.g. "func:deepxube.base.domain.Domain.is_solved").
    """
    meta = graph_store.get_node_metadata(node_id)
    if not meta:
        return NodeDocsResponse(node_id=node_id, found=False)

    content = graph_store.get_node_doc_content(node_id)
    return NodeDocsResponse(
        node_id=node_id,
        doc_path=meta.get("doc_path"),
        content=content,
        found=content is not None,
    )


# ── Run directly ────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
    )
