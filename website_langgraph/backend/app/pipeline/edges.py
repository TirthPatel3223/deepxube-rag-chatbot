# ============================================================================
# DeepXube RAG Chatbot - Pipeline Edge Functions
# ============================================================================
# Conditional edge functions used by LangGraph to determine which node
# to execute next based on the current pipeline state.
#
# Each function takes the PipelineState and returns a string indicating
# the next node (or END to terminate).
# ============================================================================

import logging
from app.models.state import PipelineState

logger = logging.getLogger(__name__)


def check_domain_guide_active(state: PipelineState) -> str:
    """
    After embed_query: check if we're in an active domain guide session.

    If the session has domain_guide_stage != "none", skip normal routing
    and go directly to the domain_guide node.

    Returns:
        "domain_guide" if in active domain guide session.
        "scope_guard" otherwise (continue normal flow).
    """
    stage = state.get("domain_guide_stage", "none")
    if stage != "none":
        logger.info(f"Active domain guide session (stage={stage}) — skipping routing")
        return "domain_guide"
    return "scope_guard"


def after_scope_guard(state: PipelineState) -> str:
    """
    After scope_guard: check if the query was out of scope.

    Returns:
        "end" if out of scope (response already set to polite refusal).
        "faq_lookup" otherwise.
    """
    if state.get("is_out_of_scope", False):
        return "end"
    return "faq_lookup"


def after_faq_lookup(state: PipelineState) -> str:
    """
    After faq_lookup: check if we got a FAQ cache hit.

    Returns:
        "end" if FAQ hit (response already set to cached answer).
        "route_classifier" otherwise.
    """
    if state.get("is_faq_hit", False):
        return "end"
    return "route_classifier"


def after_route_classifier(state: PipelineState) -> str:
    """
    After route_classifier: fan out to the appropriate retrieval path.

    Returns:
        "code_retrieve" for code route.
        "paper_retrieve" for papers route.
        "domain_guide" for domain guide route.
        "code_retrieve" for "both" route (papers will run after).
    """
    route = state.get("route", "code")

    if route == "domain_guide":
        return "domain_guide"
    elif route == "papers":
        return "paper_retrieve"
    elif route == "both":
        return "code_retrieve"  # Code first, then papers
    else:  # "code"
        return "code_retrieve"


def after_code_retrieve(state: PipelineState) -> str:
    """
    After code_retrieve: check if we also need papers (fan-out "both").

    Returns:
        "paper_retrieve" if route is "both".
        "generate" otherwise.
    """
    route = state.get("route", "code")
    if route == "both":
        return "paper_retrieve"
    return "generate"


def after_domain_guide(state: PipelineState) -> str:
    """
    After domain_guide: proceed to generate (unless flow completed).

    If domain_guide set the stage back to "none" (flow completed and
    user sent a follow-up), re-route through normal flow.

    Returns:
        "generate" if context was loaded for generation.
        "scope_guard" if domain guide flow completed (re-route).
    """
    context = state.get("context_for_llm", "")
    if context:
        return "generate"
    # Flow completed, no context → re-route through normal pipeline
    return "scope_guard"


def after_cite_check(state: PipelineState) -> str:
    """
    After cite_check: retry generation or proceed to logging.

    Returns:
        "generate" if needs_retry is True (max 1 retry).
        "log_node" otherwise.
    """
    if state.get("needs_retry", False):
        return "generate"
    return "log_node"
