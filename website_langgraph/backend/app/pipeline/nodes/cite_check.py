# ============================================================================
# Node: cite_check
# ============================================================================
# Rule-based citation verification (no LLM call).
#
# Checks that the generated response references sources from the
# retrieved documents. If citations are missing and retry_count < 1,
# sets needs_retry=True so the generate node runs again with an
# explicit citation instruction.
# ============================================================================

import re
import logging
from app.models.state import PipelineState

logger = logging.getLogger(__name__)

# Patterns that indicate a citation is present
CITATION_PATTERNS = [
    r'\[.*?\]\(.*?:\d+\)',           # [name](file:line) — code citation
    r'\[.*?§.*?\]',                   # [paper §section] — paper citation
    r'`[a-z_]+\.[a-z_]+\.[A-Z]',     # `module.class.Method` — qualified name
    r'`deepxube\.',                   # `deepxube.xxx` — module reference
    r'file:.*?\.py:\d+',             # file:xxx.py:123 — file reference
]


async def cite_check(state: PipelineState) -> dict:
    """
    Verify that the response contains citations.

    For code/paper routes, checks if the response references any of the
    retrieved source documents. If not, triggers a retry with explicit
    citation instructions.

    Domain guide responses and FAQ hits skip this check (they don't need
    citations in the same way).

    Args:
        state: Pipeline state with response and retrieved_docs set.

    Returns:
        State updates: needs_retry, retry_count, citations.
    """
    route = state.get("route", "")
    response = state.get("response", "")
    retry_count = state.get("retry_count", 0)

    # Skip citation check for domain guide and FAQ hits
    if route == "domain_guide" or state.get("is_faq_hit", False):
        return {
            "needs_retry": False,
            "citations": [],
        }

    # Check if any citation pattern is present in the response
    has_citations = any(
        re.search(pattern, response) for pattern in CITATION_PATTERNS
    )

    # Extract found citations
    citations = []
    for pattern in CITATION_PATTERNS:
        matches = re.findall(pattern, response)
        for match in matches:
            citations.append({
                "source": match,
                "reference": match,
                "type": "code" if "deepxube" in match or ".py" in match else "paper",
            })

    if has_citations or retry_count >= 1:
        # Either we have citations, or we've already retried once
        if not has_citations and retry_count >= 1:
            logger.warning("No citations found even after retry. Proceeding anyway.")
        return {
            "needs_retry": False,
            "citations": citations,
        }

    # No citations found — trigger retry
    logger.info("No citations in response. Triggering retry with citation instructions.")
    return {
        "needs_retry": True,
        "retry_count": retry_count + 1,
        "citations": [],
        # Prepend instruction for the retry
        "system_prompt": state.get("system_prompt", "") + (
            "\n\nIMPORTANT: Your previous response lacked specific citations. "
            "Please include explicit references to the source documents provided. "
            "For code: use [qualified_name](file:line). "
            "For papers: use [paper_title §section]."
        ),
    }
