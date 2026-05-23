# ============================================================================
# DeepXube RAG Chatbot - LangGraph Pipeline Definition
# ============================================================================
# Defines and compiles the complete LangGraph graph.
#
# Pipeline flow:
#
#   embed_query
#       │
#       ├─ (domain guide active?) ──► domain_guide ──► generate ──► log ──► END
#       │
#       ▼
#   scope_guard ──► (out of scope?) ──► END
#       │
#       ▼
#   faq_lookup ──► (faq hit?) ──► END
#       │
#       ▼
#   route_classifier
#       │
#       ├─ "code"         ──► code_retrieve ──► generate ──► cite_check ──► log ──► END
#       ├─ "papers"       ──► paper_retrieve ──► generate ──► cite_check ──► log ──► END
#       ├─ "both"         ──► code_retrieve ──► paper_retrieve ──► generate ──► cite_check ──► log ──► END
#       └─ "domain_guide" ──► domain_guide ──► generate ──► log ──► END
#
# Usage:
#   from app.pipeline.graph import run_pipeline
#   result = await run_pipeline(query="What is DeepCubeA?", session_id="abc")
# ============================================================================

import logging
from langgraph.graph import StateGraph, END
from app.models.state import PipelineState

# Import all nodes
from app.pipeline.nodes.embed_query import embed_query
from app.pipeline.nodes.scope_guard import scope_guard
from app.pipeline.nodes.faq_lookup import faq_lookup
from app.pipeline.nodes.route_classifier import route_classifier
from app.pipeline.nodes.code_retrieve import code_retrieve
from app.pipeline.nodes.paper_retrieve import paper_retrieve
from app.pipeline.nodes.domain_guide import domain_guide
from app.pipeline.nodes.generate import generate
from app.pipeline.nodes.cite_check import cite_check
from app.pipeline.nodes.log_node import log_node

# Import edge functions
from app.pipeline.edges import (
    check_domain_guide_active,
    after_scope_guard,
    after_faq_lookup,
    after_route_classifier,
    after_code_retrieve,
    after_domain_guide,
    after_cite_check,
)

logger = logging.getLogger(__name__)


def build_pipeline() -> StateGraph:
    """
    Build and compile the LangGraph pipeline.

    Returns:
        A compiled StateGraph ready to invoke.
    """
    # Create the graph with our state type
    graph = StateGraph(PipelineState)

    # ── Add all nodes ───────────────────────────────────────────────────
    graph.add_node("embed_query", embed_query)
    graph.add_node("scope_guard", scope_guard)
    graph.add_node("faq_lookup", faq_lookup)
    graph.add_node("route_classifier", route_classifier)
    graph.add_node("code_retrieve", code_retrieve)
    graph.add_node("paper_retrieve", paper_retrieve)
    graph.add_node("domain_guide", domain_guide)
    graph.add_node("generate", generate)
    graph.add_node("cite_check", cite_check)
    graph.add_node("log_node", log_node)

    # ── Set entry point ─────────────────────────────────────────────────
    graph.set_entry_point("embed_query")

    # ── Add edges ───────────────────────────────────────────────────────

    # After embed_query: check if we're in a domain guide session
    graph.add_conditional_edges(
        "embed_query",
        check_domain_guide_active,
        {
            "domain_guide": "domain_guide",
            "scope_guard": "scope_guard",
        },
    )

    # After scope_guard: out of scope → END, else → faq_lookup
    graph.add_conditional_edges(
        "scope_guard",
        after_scope_guard,
        {
            "end": END,
            "faq_lookup": "faq_lookup",
        },
    )

    # After faq_lookup: FAQ hit → END, else → route_classifier
    graph.add_conditional_edges(
        "faq_lookup",
        after_faq_lookup,
        {
            "end": END,
            "route_classifier": "route_classifier",
        },
    )

    # After route_classifier: fan out to retrieval path
    graph.add_conditional_edges(
        "route_classifier",
        after_route_classifier,
        {
            "code_retrieve": "code_retrieve",
            "paper_retrieve": "paper_retrieve",
            "domain_guide": "domain_guide",
        },
    )

    # After code_retrieve: if "both" → also do papers, else → generate
    graph.add_conditional_edges(
        "code_retrieve",
        after_code_retrieve,
        {
            "paper_retrieve": "paper_retrieve",
            "generate": "generate",
        },
    )

    # After paper_retrieve: always → generate
    graph.add_edge("paper_retrieve", "generate")

    # After domain_guide: → generate (with loaded context) or → scope_guard (re-route)
    graph.add_conditional_edges(
        "domain_guide",
        after_domain_guide,
        {
            "generate": "generate",
            "scope_guard": "scope_guard",
        },
    )

    # After generate: → cite_check
    graph.add_edge("generate", "cite_check")

    # After cite_check: retry → generate, else → log_node
    graph.add_conditional_edges(
        "cite_check",
        after_cite_check,
        {
            "generate": "generate",
            "log_node": "log_node",
        },
    )

    # After log_node: → END
    graph.add_edge("log_node", END)

    # ── Compile ─────────────────────────────────────────────────────────
    compiled = graph.compile()
    logger.info("LangGraph pipeline compiled successfully")
    return compiled


# ── Compiled pipeline instance ──────────────────────────────────────────
pipeline = build_pipeline()


async def run_pipeline(query: str, session_id: str = "") -> dict:
    """
    Run the full RAG pipeline for a user query.

    This is the main entry point called by the FastAPI endpoint.

    Args:
        query: The user's question or message.
        session_id: Optional session ID for conversation continuity.

    Returns:
        The final pipeline state dict containing:
          - response: The chatbot's answer
          - citations: List of citation dicts
          - session_id: The session ID
          - route: Which path was taken
          - is_faq_hit: Whether the FAQ cache was used
    """
    initial_state = {
        "query": query,
        "session_id": session_id or "",
    }

    # Run the pipeline
    result = await pipeline.ainvoke(initial_state)

    return result
