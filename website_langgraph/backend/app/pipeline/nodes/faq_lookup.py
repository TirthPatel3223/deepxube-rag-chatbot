# ============================================================================
# Node: faq_lookup
# ============================================================================
# Checks the FAQ collection for a cached answer.
# Three outcomes:
#   1. similarity >= HIGH (0.92)      → FAQ hit, return cached answer (no LLM)
#   2. BORDERLINE <= sim < HIGH       → borderline, will regenerate but with
#                                       the FAQ answer as additional context
#   3. similarity < BORDERLINE (0.78) → miss, proceed to routing
# ============================================================================

import logging
from app.models.state import PipelineState
from app.services.vectordb import vectordb_service, COLLECTION_FAQ
from app.config import settings

logger = logging.getLogger(__name__)


async def faq_lookup(state: PipelineState) -> dict:
    """
    Look up the query in the FAQ cache.

    The FAQ collection stores pre-curated Q&A pairs. If the user's query
    is semantically similar enough to a cached question, we return the
    cached answer directly — zero LLM cost.

    Args:
        state: Pipeline state with query_embedding set.

    Returns:
        State updates: is_faq_hit, faq_answer, faq_similarity.
    """
    embedding = state["query_embedding"]

    results = vectordb_service.query(COLLECTION_FAQ, embedding, top_k=1)

    # No FAQ entries exist yet
    if not results["distances"] or not results["distances"][0]:
        logger.info("FAQ lookup: collection is empty")
        return {
            "is_faq_hit": False,
            "faq_answer": "",
            "faq_similarity": 0.0,
        }

    distance = results["distances"][0][0]
    similarity = 1.0 - distance
    faq_answer = results["documents"][0][0] if results["documents"][0] else ""

    # Extract the cached answer from metadata if stored there
    if results["metadatas"] and results["metadatas"][0]:
        metadata = results["metadatas"][0][0]
        if "answer" in metadata:
            faq_answer = metadata["answer"]

    logger.info(f"FAQ lookup: similarity={similarity:.3f}")

    if similarity >= settings.FAQ_SIM_THRESHOLD_HIGH:
        # Cache hit — return directly, no LLM needed
        logger.info("FAQ HIT — returning cached answer")
        return {
            "is_faq_hit": True,
            "faq_answer": faq_answer,
            "faq_similarity": similarity,
            "response": faq_answer,  # Short-circuit: set response directly
        }

    if similarity >= settings.FAQ_SIM_THRESHOLD_BORDERLINE:
        # Borderline — include FAQ answer as context but regenerate
        logger.info("FAQ BORDERLINE — will regenerate with FAQ context")
        return {
            "is_faq_hit": False,
            "faq_answer": faq_answer,
            "faq_similarity": similarity,
        }

    # Miss — no relevant FAQ
    return {
        "is_faq_hit": False,
        "faq_answer": "",
        "faq_similarity": similarity,
    }
