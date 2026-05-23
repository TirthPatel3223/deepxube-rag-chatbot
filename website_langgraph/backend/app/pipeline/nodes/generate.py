# ============================================================================
# Node: generate
# ============================================================================
# The core LLM generation node. Takes retrieved context (from code/paper
# retrieval or domain guide) and produces the chatbot's response.
#
# This is the ONLY node that makes an LLM call (besides retries).
# All other processing is done via embeddings, vector search, or rules.
# ============================================================================

import logging
from app.models.state import PipelineState
from app.services.llm import llm_service

logger = logging.getLogger(__name__)

# ── Default system prompt for code/paper queries ───────────────────────
DEFAULT_SYSTEM_PROMPT = """You are the DeepXube Assistant — an expert on the DeepXube framework, its codebase, and the underlying research papers.

RULES:
1. Answer based ONLY on the provided context. Do not make up information.
2. Include citations for every factual claim:
   - For code: use the format [qualified_name](file:line)
   - For papers: use the format [paper_title §section]
3. If the context doesn't contain enough information to answer, say so honestly.
4. Use markdown formatting for code blocks, lists, and emphasis.
5. Keep answers concise but thorough.
6. When showing code, include the relevant function signature and explain what it does.

ROLE: You help users understand and use the DeepXube framework for solving combinatorial puzzles with deep learning."""


async def generate(state: PipelineState) -> dict:
    """
    Generate the chatbot's response using the LLM.

    Builds the prompt from:
    - System prompt (default or domain-guide-specific)
    - Rolling summary (conversation context)
    - Retrieved documents or domain guide context
    - The user's query

    Args:
        state: Pipeline state with context_for_llm or retrieved_docs set.

    Returns:
        State update: response.
    """
    query = state["query"]
    system_prompt = state.get("system_prompt", DEFAULT_SYSTEM_PROMPT)
    rolling_summary = state.get("rolling_summary", "")
    conversation_history = state.get("conversation_history", [])
    faq_answer = state.get("faq_answer", "")

    # ── Build context ───────────────────────────────────────────────────
    # Context can come from two sources:
    # 1. Domain guide: pre-set in context_for_llm by the domain_guide node
    # 2. Retrieval: assembled from retrieved_docs

    context = state.get("context_for_llm", "")

    if not context:
        # Build context from retrieved documents
        retrieved_docs = state.get("retrieved_docs", [])
        graph_docs = state.get("graph_expanded_docs", [])

        context_parts = []

        # Add retrieved documents
        for i, doc in enumerate(retrieved_docs):
            source_type = doc.get("source", "unknown")
            metadata = doc.get("metadata", {})
            score = doc.get("score", 0)

            # Format based on source type
            if source_type == "code":
                qname = metadata.get("qualified_name", "unknown")
                file_ref = metadata.get("file", "")
                line = metadata.get("line_start", "")
                context_parts.append(
                    f"[CODE DOC {i+1}] {qname} ({file_ref}:{line}) "
                    f"[relevance: {score:.2f}]\n{doc['content']}"
                )
            elif source_type == "papers":
                paper_id = metadata.get("paper_id", "unknown")
                title = metadata.get("paper_title", "")
                pages = metadata.get("page_numbers", "")
                context_parts.append(
                    f"[PAPER {i+1}] {title or paper_id} (pages: {pages}) "
                    f"[relevance: {score:.2f}]\n{doc['content']}"
                )
            else:
                context_parts.append(
                    f"[SOURCE {i+1}] [relevance: {score:.2f}]\n{doc['content']}"
                )

        # Add graph-expanded docs (lower priority)
        for doc in graph_docs:
            context_parts.append(
                f"[RELATED CODE] {doc.get('metadata', {}).get('id', '')}\n"
                f"{doc['content']}"
            )

        context = "\n\n---\n\n".join(context_parts)

    # Add borderline FAQ answer as additional context if present
    if faq_answer and not state.get("is_faq_hit", False):
        context = (
            f"[SIMILAR FAQ ANSWER - may be relevant but regenerate a fresh response]\n"
            f"{faq_answer}\n\n---\n\n{context}"
        )

    # ── Build user message with conversation history ────────────────────
    user_message_parts = []

    # Add rolling summary for multi-turn context
    if rolling_summary:
        user_message_parts.append(
            f"[CONVERSATION CONTEXT]\n{rolling_summary}"
        )

    # Add recent turns for immediate context
    if conversation_history:
        recent = "\n".join(
            f"{turn['role'].upper()}: {turn['content']}"
            for turn in conversation_history[-4:]  # Last 2 turns
        )
        user_message_parts.append(f"[RECENT CONVERSATION]\n{recent}")

    # Add the current query
    user_message_parts.append(query)
    user_message = "\n\n".join(user_message_parts)

    # ── Generate response ───────────────────────────────────────────────
    logger.info(f"Generating response (context length: {len(context)} chars)")

    response = await llm_service.generate(
        system_prompt=system_prompt,
        user_message=user_message,
        context=context,
        max_tokens=1500,
    )

    return {"response": response}
