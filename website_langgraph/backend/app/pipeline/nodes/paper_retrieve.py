# ============================================================================
# Node: paper_retrieve
# ============================================================================
# Retrieves relevant research paper chunks from the 'papers' collection.
# Each chunk has metadata including paper_id, paper_title, chunk_index,
# and page_numbers for citation generation.
# ============================================================================

import logging
from app.models.state import PipelineState
from app.services.vectordb import vectordb_service, COLLECTION_PAPERS
from app.config import settings

logger = logging.getLogger(__name__)


async def paper_retrieve(state: PipelineState) -> dict:
    """
    Retrieve relevant research paper chunks.

    Queries the 'papers' ChromaDB collection and returns the top-k
    most similar chunks. Each chunk includes metadata for citation.

    Args:
        state: Pipeline state with query_embedding set.

    Returns:
        State update: retrieved_docs (appended to existing).
    """
    embedding = state["query_embedding"]
    top_k = settings.PAPER_RETRIEVE_TOP_K

    results = vectordb_service.query(COLLECTION_PAPERS, embedding, top_k=top_k)

    retrieved_docs = []
    if results["documents"] and results["documents"][0]:
        for i, doc in enumerate(results["documents"][0]):
            metadata = results["metadatas"][0][i] if results["metadatas"][0] else {}
            distance = results["distances"][0][i] if results["distances"][0] else 1.0
            retrieved_docs.append({
                "content": doc,
                "metadata": metadata,
                "source": "papers",
                "score": 1.0 - distance,
            })

    logger.info(f"Paper search returned {len(retrieved_docs)} results")

    # Merge with existing retrieved_docs (may include code docs from fan-out)
    existing_docs = state.get("retrieved_docs", [])
    all_docs = existing_docs + retrieved_docs

    return {"retrieved_docs": all_docs}
