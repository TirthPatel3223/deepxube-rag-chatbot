# ============================================================================
# DeepXube RAG Chatbot - Embedding Service
# ============================================================================
# Provides text → vector embeddings using OpenAI's text-embedding-3-small.
#
# No fallback — if the OpenAI API is unreachable, an error is raised.
# The model produces 1536-dimensional vectors.
#
# Usage:
#   from app.services.embedding import embedding_service
#   vector = await embedding_service.embed("What is DeepCubeA?")
#   vectors = await embedding_service.embed_batch(["query1", "query2"])
# ============================================================================

import logging
from openai import AsyncOpenAI
from app.config import settings

logger = logging.getLogger(__name__)


class EmbeddingService:
    """
    OpenAI embedding service.

    Model: text-embedding-3-small (1536 dimensions)
    No fallback — raises an error if the API call fails.

    This service is used by:
      - Ingestion scripts (to embed code docs, papers, FAQ)
      - Pipeline nodes (to embed user queries)
    """

    def __init__(self):
        """Initialize the OpenAI async client."""
        self._client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self._model = settings.EMBEDDING_MODEL
        logger.info(f"EmbeddingService initialized with model: {self._model}")

    async def embed(self, text: str) -> list[float]:
        """
        Embed a single text string into a vector.

        Args:
            text: The text to embed.

        Returns:
            A list of floats representing the embedding vector (1536 dims).

        Raises:
            openai.OpenAIError: If the API call fails.
        """
        response = await self._client.embeddings.create(
            model=self._model,
            input=text,
        )
        return response.data[0].embedding

    async def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Embed multiple texts in a single API call.

        OpenAI supports batched embedding — this is more efficient than
        calling embed() in a loop.

        Args:
            texts: List of strings to embed.

        Returns:
            List of embedding vectors, one per input text.

        Raises:
            openai.OpenAIError: If the API call fails.
        """
        if not texts:
            return []

        # OpenAI has a limit on batch size; chunk if needed
        # (text-embedding-3-small supports up to 2048 inputs per call)
        batch_size = 2048
        all_embeddings = []

        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            response = await self._client.embeddings.create(
                model=self._model,
                input=batch,
            )
            # Results come back in the same order as inputs
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)

        return all_embeddings


# ── Singleton instance ──────────────────────────────────────────────────
embedding_service = EmbeddingService()
