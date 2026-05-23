# ============================================================================
# DeepXube RAG Chatbot - LLM Generation Service
# ============================================================================
# Provides text generation with automatic fallback:
#   Primary:  OpenAI gpt-4o-mini
#   Fallback: Anthropic Claude Haiku
#
# Both providers are called with the same system prompt and user message.
# The service handles API differences (OpenAI vs Anthropic) transparently.
#
# Usage:
#   from app.services.llm import llm_service
#   response = await llm_service.generate(
#       system_prompt="You are a helpful assistant.",
#       user_message="What is DeepCubeA?",
#       context="... retrieved documents ..."
#   )
# ============================================================================

import logging
from openai import AsyncOpenAI
from anthropic import AsyncAnthropic
from app.config import settings

logger = logging.getLogger(__name__)


class LLMService:
    """
    LLM generation service with automatic fallback.

    Primary:  OpenAI gpt-4o-mini (fast, cheap)
    Fallback: Anthropic Claude Haiku (triggered if OpenAI fails)

    The fallback is triggered by any exception from the primary provider
    (network errors, rate limits, API errors, etc.).
    """

    def __init__(self):
        """Initialize both LLM clients."""
        self._openai_client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self._anthropic_client = AsyncAnthropic(api_key=settings.ANTHROPIC_API_KEY)
        self._primary_model = settings.LLM_MODEL_PRIMARY
        self._fallback_model = settings.LLM_MODEL_FALLBACK
        logger.info(
            f"LLMService initialized. "
            f"Primary: {self._primary_model}, "
            f"Fallback: {self._fallback_model}"
        )

    async def generate(
        self,
        system_prompt: str,
        user_message: str,
        context: str = "",
        max_tokens: int = 1024,
    ) -> str:
        """
        Generate a response using the LLM.

        Tries the primary model (OpenAI) first. If it fails for any reason,
        automatically falls back to the secondary model (Claude).

        Args:
            system_prompt: Instructions for the LLM's role and behavior.
            user_message: The user's query, optionally enriched with
                          conversation history.
            context: Retrieved documents/context to include in the prompt.
                     Injected between the system prompt and user message.
            max_tokens: Maximum tokens in the generated response.

        Returns:
            The generated response text.

        Raises:
            Exception: If BOTH primary and fallback fail.
        """
        # Build the full user message with context
        full_user_message = user_message
        if context:
            full_user_message = (
                f"CONTEXT (use this to answer the question):\n"
                f"---\n{context}\n---\n\n"
                f"USER QUESTION:\n{user_message}"
            )

        # Try primary (OpenAI)
        try:
            response = await self._generate_openai(
                system_prompt, full_user_message, max_tokens
            )
            logger.info("LLM response generated via primary (OpenAI)")
            return response
        except Exception as e:
            logger.warning(
                f"Primary LLM (OpenAI) failed: {e}. Falling back to Claude."
            )

        # Fallback (Anthropic Claude)
        try:
            response = await self._generate_anthropic(
                system_prompt, full_user_message, max_tokens
            )
            logger.info("LLM response generated via fallback (Claude)")
            return response
        except Exception as e:
            logger.error(f"Fallback LLM (Claude) also failed: {e}")
            raise RuntimeError(
                "Both primary (OpenAI) and fallback (Claude) LLMs failed. "
                f"Last error: {e}"
            ) from e

    async def _generate_openai(
        self, system_prompt: str, user_message: str, max_tokens: int
    ) -> str:
        """
        Generate using the OpenAI Chat Completions API.

        Args:
            system_prompt: The system message content.
            user_message: The user message content (includes context).
            max_tokens: Maximum response tokens.

        Returns:
            The assistant's response text.
        """
        response = await self._openai_client.chat.completions.create(
            model=self._primary_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            max_tokens=max_tokens,
            temperature=0.3,  # Low temperature for factual accuracy
        )
        return response.choices[0].message.content

    async def _generate_anthropic(
        self, system_prompt: str, user_message: str, max_tokens: int
    ) -> str:
        """
        Generate using the Anthropic Messages API.

        Anthropic uses a different API shape: system prompt is a top-level
        parameter, not a message in the list.

        Args:
            system_prompt: The system message content.
            user_message: The user message content (includes context).
            max_tokens: Maximum response tokens.

        Returns:
            The assistant's response text.
        """
        response = await self._anthropic_client.messages.create(
            model=self._fallback_model,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_message},
            ],
            max_tokens=max_tokens,
            temperature=0.3,
        )
        # Anthropic returns a list of content blocks
        return response.content[0].text


# ── Singleton instance ──────────────────────────────────────────────────
llm_service = LLMService()
