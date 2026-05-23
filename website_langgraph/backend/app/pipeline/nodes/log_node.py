# ============================================================================
# Node: log_node
# ============================================================================
# Final node in the pipeline. Performs two tasks:
# 1. Logs the query, route, and response for observability
# 2. Updates the session with the new conversation turn and rolling summary
#
# Future: could also handle FAQ auto-promotion (flagging high-quality
# generated responses for potential FAQ curation).
# ============================================================================

import logging
from app.models.state import PipelineState
from app.session.manager import session_manager
from app.services.llm import llm_service

logger = logging.getLogger(__name__)


async def log_node(state: PipelineState) -> dict:
    """
    Log the interaction and update session state.

    This is always the last node before END. It:
    1. Logs the query, route, and response length for monitoring
    2. Updates the session's conversation history (keeps last 2 turns)
    3. Generates a rolling summary of the conversation (for multi-turn)
    4. Updates domain guide state if applicable

    Args:
        state: Complete pipeline state after generation.

    Returns:
        Empty dict (final node, no downstream consumers).
    """
    session_id = state.get("session_id", "")
    query = state.get("query", "")
    route = state.get("route", "")
    response = state.get("response", "")
    domain_guide_stage = state.get("domain_guide_stage", "none")
    domain_guide_choices = state.get("domain_guide_user_choices", {})

    # ── 1. Log the interaction ──────────────────────────────────────────
    logger.info(
        f"INTERACTION | session={session_id[:8]}... | route={route} | "
        f"query_len={len(query)} | response_len={len(response)} | "
        f"faq_hit={state.get('is_faq_hit', False)}"
    )

    # ── 2. Update session ───────────────────────────────────────────────
    session = session_manager.get_or_create(session_id)
    session.add_turn(query, response)

    # ── 3. Update rolling summary ───────────────────────────────────────
    # Only generate a new summary if we have conversation history
    if len(session.conversation_history) >= 4:
        try:
            summary_prompt = (
                "Summarize this conversation in 1-2 sentences. Focus on what "
                "topics were discussed and what the user is trying to accomplish. "
                "Be concise (max 50 words)."
            )
            history_text = "\n".join(
                f"{turn['role']}: {turn['content'][:200]}"
                for turn in session.conversation_history
            )
            new_summary = await llm_service.generate(
                system_prompt=summary_prompt,
                user_message=history_text,
                max_tokens=100,
            )
            session_manager.update_summary(session_id, new_summary)
        except Exception as e:
            # Summary generation is non-critical — don't fail the pipeline
            logger.warning(f"Failed to generate rolling summary: {e}")

    # ── 4. Update domain guide state ────────────────────────────────────
    if domain_guide_stage != "none":
        session_manager.update_domain_guide(
            session_id, domain_guide_stage, domain_guide_choices
        )
    elif session.is_in_domain_guide() and domain_guide_stage == "none":
        # Domain guide flow completed — reset
        session.reset_domain_guide()

    return {}
