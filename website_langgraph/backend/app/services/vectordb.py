# ============================================================================
# DeepXube RAG Chatbot - Vector Database Service
# ============================================================================
# ChromaDB wrapper managing three collections:
#   - faq:    FAQ question embeddings → cached answers
#   - code:   One vector per .md function/class doc (509 total)
#   - papers: Fixed-window chunks from 7 research PDFs
#
# ChromaDB persists data to disk at CHROMA_PERSIST_DIR.
# Collections are created on first access and reused thereafter.
#
# Usage:
#   from app.services.vectordb import vectordb_service
#   results = vectordb_service.query("code", embedding, top_k=5)
#   vectordb_service.add("code", docs, embeddings, metadatas, ids)
# ============================================================================

import logging
from typing import Optional
import chromadb
from app.config import settings

logger = logging.getLogger(__name__)

# Collection names used throughout the system
COLLECTION_FAQ = "faq"
COLLECTION_CODE = "code"
COLLECTION_PAPERS = "papers"


class VectorDBService:
    """
    ChromaDB vector database service.

    Manages three collections with different content types:
      - faq:    Short-circuit cache for common questions
      - code:   Function/class documentation from deepxube-main/docs/
      - papers: Chunked research paper content

    All collections use cosine similarity for distance calculation.
    Embedding dimension: 1536 (OpenAI text-embedding-3-small).
    """

    def __init__(self):
        """
        Initialize ChromaDB client with persistent storage.

        The database is stored at the path specified by CHROMA_PERSIST_DIR
        in the configuration. Data survives server restarts.
        """
        persist_path = str(settings.chroma_persist_abs)
        self._client = chromadb.PersistentClient(path=persist_path)
        logger.info(f"ChromaDB initialized at: {persist_path}")

        # Pre-create/get collections
        # Using cosine similarity (default for most embedding models)
        self._collections = {}
        for name in [COLLECTION_FAQ, COLLECTION_CODE, COLLECTION_PAPERS]:
            self._collections[name] = self._client.get_or_create_collection(
                name=name,
                metadata={"hnsw:space": "cosine"},
            )
            count = self._collections[name].count()
            logger.info(f"Collection '{name}': {count} documents")

    def query(
        self,
        collection_name: str,
        query_embedding: list[float],
        top_k: int = 5,
        where: Optional[dict] = None,
    ) -> dict:
        """
        Query a collection for the most similar documents.

        Args:
            collection_name: One of "faq", "code", or "papers".
            query_embedding: The query vector (1536 dims).
            top_k: Number of results to return.
            where: Optional metadata filter (ChromaDB where clause).

        Returns:
            ChromaDB query result dict with keys:
              - ids: list[list[str]]
              - documents: list[list[str]]
              - metadatas: list[list[dict]]
              - distances: list[list[float]]  (cosine distance, lower = more similar)

        Raises:
            KeyError: If collection_name is not recognized.
        """
        collection = self._collections[collection_name]

        query_params = {
            "query_embeddings": [query_embedding],
            "n_results": min(top_k, collection.count()) if collection.count() > 0 else 1,
        }
        if where:
            query_params["where"] = where

        # If collection is empty, return empty results
        if collection.count() == 0:
            return {
                "ids": [[]],
                "documents": [[]],
                "metadatas": [[]],
                "distances": [[]],
            }

        return collection.query(**query_params)

    def add(
        self,
        collection_name: str,
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
        ids: list[str],
    ) -> None:
        """
        Add documents to a collection.

        If a document with the same ID already exists, it is updated.

        Args:
            collection_name: One of "faq", "code", or "papers".
            documents: The text content of each document.
            embeddings: Pre-computed embedding vectors.
            metadatas: Metadata dicts for each document.
            ids: Unique string IDs for each document.

        Raises:
            KeyError: If collection_name is not recognized.
        """
        collection = self._collections[collection_name]
        collection.upsert(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )
        logger.info(
            f"Added/updated {len(ids)} documents in '{collection_name}'. "
            f"Total: {collection.count()}"
        )

    def get_collection_stats(self) -> dict[str, int]:
        """
        Get the number of documents in each collection.

        Returns:
            Dict mapping collection name to document count.
            Example: {"faq": 0, "code": 509, "papers": 250}
        """
        return {
            name: col.count() for name, col in self._collections.items()
        }

    def clear_collection(self, collection_name: str) -> None:
        """
        Delete all documents from a collection.

        Useful for re-ingestion. The collection structure is preserved.

        Args:
            collection_name: One of "faq", "code", or "papers".
        """
        self._client.delete_collection(collection_name)
        self._collections[collection_name] = self._client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )
        logger.info(f"Cleared collection '{collection_name}'")


# ── Singleton instance ──────────────────────────────────────────────────
vectordb_service = VectorDBService()
