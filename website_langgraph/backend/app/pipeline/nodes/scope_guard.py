# ============================================================================
# Node: scope_guard
# ============================================================================
# Checks whether the user's query is within the chatbot's scope.
# If the query is completely unrelated to DeepXube (code, papers, or domain
# creation), it sets is_out_of_scope=True and provides a polite refusal.
#
# Implementation: queries all 3 collections and checks if any result
# exceeds the SCOPE_GUARD_THRESHOLD. If none do, the query is out of scope.
# ============================================================================

import logging
from app.models.state import PipelineState
from app.services.vectordb import vectordb_service, COLLECTION_CODE, COLLECTION_PAPERS, COLLECTION_FAQ
from app.config import settings

logger = logging.getLogger(__name__)

# Polite refusal message for out-of-scope queries
REFUSAL_MESSAGE = (
    "I'm designed to help with questions about the **DeepXube** framework — "
    "its codebase, the underlying research papers, and creating new puzzle domains. "
    "Your question seems to be outside my area of expertise.\n\n"
    "Here are some things I can help with:\n"
    "- 🔍 **Code questions:** \"What does the `Cube3` class do?\"\n"
    "- 📄 **Research questions:** \"How does DeepCubeA solve the Rubik's Cube?\"\n"
    "- 🧩 **Domain creation:** \"How do I add a new puzzle to DeepXube?\"\n\n"
    "Could you rephrase your question?"
)


async def scope_guard(state: PipelineState) -> dict:
    """
    Check if the query is within the chatbot's scope.

    Queries all three ChromaDB collections with the query embedding.
    If the best similarity score across all collections is below the
    threshold, the query is deemed out-of-scope.

    Note: ChromaDB returns cosine *distance* (0 = identical, 2 = opposite).
    We convert to similarity: similarity = 1 - distance.

    Args:
        state: Pipeline state with query_embedding set.

    Returns:
        State updates: is_out_of_scope, response (if out of scope).
    """
    embedding = state["query_embedding"]
    threshold = settings.SCOPE_GUARD_THRESHOLD

    best_similarity = 0.0

    # Check each collection for any relevant match
    for collection_name in [COLLECTION_CODE, COLLECTION_PAPERS, COLLECTION_FAQ]:
        results = vectordb_service.query(
            collection_name, embedding, top_k=1
        )
        if results["distances"] and results["distances"][0]:
            # Convert cosine distance to similarity
            distance = results["distances"][0][0]
            similarity = 1.0 - distance
            best_similarity = max(best_similarity, similarity)

    is_out_of_scope = best_similarity < threshold
    logger.info(
        f"Scope guard: best_similarity={best_similarity:.3f}, "
        f"threshold={threshold}, out_of_scope={is_out_of_scope}"
    )

    if is_out_of_scope:
        return {
            "is_out_of_scope": True,
            "response": REFUSAL_MESSAGE,
        }

    return {"is_out_of_scope": False}
