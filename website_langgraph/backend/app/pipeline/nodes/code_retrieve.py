# ============================================================================
# Node: code_retrieve
# ============================================================================
# Retrieves relevant code documentation from the 'code' ChromaDB collection.
# After vector retrieval, expands results with 1-hop graph neighbors
# (callers and callees) from the NetworkX call graph.
#
# This two-step process ensures the LLM gets not just the directly
# relevant function, but also the surrounding code context.
# ============================================================================

import logging
from app.models.state import PipelineState
from app.services.vectordb import vectordb_service, COLLECTION_CODE
from app.services.graph_store import graph_store
from app.config import settings

logger = logging.getLogger(__name__)


async def code_retrieve(state: PipelineState) -> dict:
    """
    Retrieve relevant code documentation.

    Step 1: Vector search in the 'code' collection (top_k results).
    Step 2: For each result, get its qualified_name and expand via the
            call graph (1-hop callers + callees).
    Step 3: Fetch the .md content for expanded nodes.

    Args:
        state: Pipeline state with query_embedding set.

    Returns:
        State updates: retrieved_docs, graph_expanded_docs.
    """
    embedding = state["query_embedding"]
    top_k = settings.CODE_RETRIEVE_TOP_K

    # Step 1: Vector search
    results = vectordb_service.query(COLLECTION_CODE, embedding, top_k=top_k)

    retrieved_docs = []
    if results["documents"] and results["documents"][0]:
        for i, doc in enumerate(results["documents"][0]):
            metadata = results["metadatas"][0][i] if results["metadatas"][0] else {}
            distance = results["distances"][0][i] if results["distances"][0] else 1.0
            retrieved_docs.append({
                "content": doc,
                "metadata": metadata,
                "source": "code",
                "score": 1.0 - distance,  # Convert distance to similarity
            })

    logger.info(f"Code vector search returned {len(retrieved_docs)} results")

    # Step 2: Graph expansion
    graph_expanded_docs = []
    if graph_store.is_loaded and retrieved_docs:
        # Get qualified names from results
        node_ids = []
        for doc in retrieved_docs:
            # The metadata should contain the function/class ID
            qname = doc["metadata"].get("qualified_name", "")
            if qname:
                # Convert qualified_name to graph node ID format
                node_id = f"func:{qname}"
                node_ids.append(node_id)

        if node_ids:
            # Expand to 1-hop neighbors
            expanded_ids = graph_store.expand_1hop(node_ids)
            # Remove nodes we already have
            new_ids = [nid for nid in expanded_ids if nid not in node_ids]

            logger.info(
                f"Graph expansion: {len(node_ids)} → {len(expanded_ids)} nodes "
                f"({len(new_ids)} new)"
            )

            # Fetch metadata for expanded nodes
            for node_id in new_ids[:5]:  # Limit expansion to 5 additional docs
                meta = graph_store.get_node_metadata(node_id)
                if meta:
                    graph_expanded_docs.append({
                        "content": f"[Graph neighbor] {meta.get('id', node_id)}",
                        "metadata": meta,
                        "source": "code_graph",
                        "score": 0.0,  # No similarity score for graph-expanded docs
                    })

    # Merge existing retrieved_docs with any from other routes
    existing_docs = state.get("retrieved_docs", [])
    all_docs = existing_docs + retrieved_docs

    return {
        "retrieved_docs": all_docs,
        "graph_expanded_docs": graph_expanded_docs,
    }
