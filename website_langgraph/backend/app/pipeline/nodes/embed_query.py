# ============================================================================
# Node: embed_query
# ============================================================================
# First node in the pipeline. Embeds the user's query into a vector.
# This embedding is reused by faq_lookup, scope_guard, route_classifier,
# code_retrieve, and paper_retrieve — no redundant API calls.
# ============================================================================

import logging
from app.models.state import PipelineState
from app.services.embedding import embedding_service
from app.session.manager import session_manager

logger = logging.getLogger(__name__)


async def embed_query(state: PipelineState) -> dict:
    """
    Embed the user's query and load session data into the pipeline state.

    This is always the first node. It does two things:
    1. Calls the OpenAI embedding API to get the query vector.
    2. Loads conversation history and domain guide state from the session.

    Args:
        state: Current pipeline state with 'query' and 'session_id' set.

    Returns:
        State updates: query_embedding, rolling_summary, conversation_history,
        domain_guide_stage, domain_guide_user_choices.
    """
    query = state["query"]
    session_id = state.get("session_id", "")

    # 1. Embed the query
    logger.info(f"Embedding query: {query[:80]}...")
    embedding = await embedding_service.embed(query)

    # 2. Load session data
    session = session_manager.get_or_create(session_id)

    return {
        "query_embedding": embedding,
        "session_id": session.session_id,
        "rolling_summary": session.rolling_summary,
        "conversation_history": session.conversation_history,
        "domain_guide_stage": session.domain_guide_stage,
        "domain_guide_user_choices": session.domain_guide_user_choices,
        "retry_count": 0,
        "needs_retry": False,
    }
