# ============================================================================
# Node: route_classifier
# ============================================================================
# Classifies the user's query into one of four routes:
#   - "code"         → retrieve from code docs + graph expansion
#   - "papers"       → retrieve from research paper chunks
#   - "domain_guide" → enter the domain creation guide flow
#   - "both"         → retrieve from both code and papers
#
# Implementation: embedding similarity against anchor phrases.
# Each route has a set of representative phrases. The query embedding
# is compared against all anchors, and the route with the highest
# average similarity wins.
#
# This avoids an LLM call for routing (embedding reuse = zero extra cost).
# ============================================================================

import logging
import numpy as np
from app.models.state import PipelineState
from app.services.embedding import embedding_service

logger = logging.getLogger(__name__)

# ── Anchor phrases for each route ───────────────────────────────────────
# These are embedded once at startup and cached.
# More anchors = better classification but more startup cost.

ROUTE_ANCHORS = {
    "domain_guide": [
        "how do I add a new puzzle domain",
        "create a new domain for my puzzle",
        "add my puzzle to deepxube",
        "implement a new domain",
        "how to create a domain file",
        "template for a new puzzle",
        "I want to add my own puzzle",
        "steps to create a new domain",
        "guide me through adding a domain",
        "domain creation tutorial",
    ],
    "code": [
        "what does this function do",
        "how is this class implemented",
        "explain the code for",
        "what methods does this class have",
        "show me the source code",
        "how does the training loop work",
        "what parameters does this function take",
        "where is this function defined",
        "code implementation of",
        "call graph for",
    ],
    "papers": [
        "research paper about",
        "what does the paper say about",
        "explain the algorithm from the paper",
        "DeepCubeA algorithm",
        "deep learning for combinatorial puzzles",
        "publication results",
        "experimental results from the paper",
        "academic reference for",
        "how does the heuristic search work theoretically",
        "what is approximate value iteration",
    ],
}

# Cache for anchor embeddings (populated on first use)
_anchor_embeddings: dict[str, list[list[float]]] = {}


async def _get_anchor_embeddings() -> dict[str, list[list[float]]]:
    """
    Embed all anchor phrases (once, then cached).

    Returns:
        Dict mapping route name to list of anchor embeddings.
    """
    global _anchor_embeddings
    if _anchor_embeddings:
        return _anchor_embeddings

    logger.info("Computing route anchor embeddings (one-time)...")
    for route, phrases in ROUTE_ANCHORS.items():
        embeddings = await embedding_service.embed_batch(phrases)
        _anchor_embeddings[route] = embeddings

    logger.info("Route anchor embeddings cached.")
    return _anchor_embeddings


def _cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    a_np = np.array(a)
    b_np = np.array(b)
    dot = np.dot(a_np, b_np)
    norm = np.linalg.norm(a_np) * np.linalg.norm(b_np)
    if norm == 0:
        return 0.0
    return float(dot / norm)


async def route_classifier(state: PipelineState) -> dict:
    """
    Classify the user's query into a retrieval route.

    Computes cosine similarity between the query embedding and each
    route's anchor embeddings. The route with the highest average
    similarity wins.

    Special case: if both "code" and "papers" score above 0.5, route
    is set to "both" (fan-out to both collections).

    Args:
        state: Pipeline state with query_embedding set.

    Returns:
        State update: route (one of "code", "papers", "domain_guide", "both").
    """
    query_embedding = state["query_embedding"]
    anchor_embeddings = await _get_anchor_embeddings()

    # Compute average similarity for each route
    route_scores = {}
    for route, embeddings in anchor_embeddings.items():
        similarities = [
            _cosine_similarity(query_embedding, anchor)
            for anchor in embeddings
        ]
        route_scores[route] = np.mean(similarities)

    logger.info(f"Route scores: {route_scores}")

    # Check if both code and papers score high → fan-out to both
    code_score = route_scores.get("code", 0)
    papers_score = route_scores.get("papers", 0)
    domain_score = route_scores.get("domain_guide", 0)

    # Domain guide takes priority if it's the top scorer
    if domain_score > code_score and domain_score > papers_score:
        selected_route = "domain_guide"
    elif code_score > 0.5 and papers_score > 0.5:
        # Both are relevant — fan-out
        selected_route = "both"
    elif code_score >= papers_score:
        selected_route = "code"
    else:
        selected_route = "papers"

    logger.info(f"Route selected: {selected_route}")
    return {"route": selected_route}
