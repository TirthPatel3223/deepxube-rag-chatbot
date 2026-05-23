# ============================================================================
# DeepXube RAG Chatbot - Graph Store Service
# ============================================================================
# Loads the code call-graph from graph.json into a NetworkX DiGraph.
# Provides 1-hop expansion for code retrieval: when a user asks about a
# function, we also retrieve its direct callers and callees.
#
# graph.json structure (simplified):
#   {
#     "nodes": [
#       {"id": "func:deepxube.domains.cube3.Cube3.is_solved", "type": "function", ...},
#       ...
#     ],
#     "edges": [
#       {"source": "func:...", "target": "func:...", "type": "calls"},
#       ...
#     ]
#   }
#
# Usage:
#   from app.services.graph_store import graph_store
#   callees = graph_store.get_callees("func:deepxube.domains.cube3.Cube3.is_solved")
#   expanded = graph_store.expand_1hop(["func:...", "func:..."])
# ============================================================================

import json
import logging
from pathlib import Path
import networkx as nx
from app.config import settings

logger = logging.getLogger(__name__)


class GraphStore:
    """
    In-memory code call-graph using NetworkX.

    Loaded from graph.json (auto-generated from the DeepXube codebase).
    Used by the code_retrieve pipeline node to expand retrieval results
    with structurally related functions (callers/callees).

    The graph is a directed graph where:
      - Nodes represent functions, classes, and modules
      - Edges represent call relationships (caller → callee)
    """

    def __init__(self):
        """Load graph.json into a NetworkX DiGraph."""
        self._graph = nx.DiGraph()
        self._loaded = False
        self._raw_data: dict = {}  # Cached raw JSON for the /api/graph endpoint

    def load(self, graph_json_path: Path = None) -> None:
        """
        Load the graph from a JSON file.

        Called once at startup. If the file doesn't exist, the graph
        remains empty (code retrieval still works, just without expansion).

        Args:
            graph_json_path: Path to graph.json. Defaults to config value.
        """
        if graph_json_path is None:
            graph_json_path = settings.graph_json_abs

        if not graph_json_path.exists():
            logger.warning(
                f"graph.json not found at {graph_json_path}. "
                "Code graph expansion will be disabled."
            )
            return

        with open(graph_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Cache the raw data for serving via the API
        self._raw_data = data

        # Add nodes with their metadata
        for node in data.get("nodes", []):
            node_id = node.get("id", "")
            self._graph.add_node(node_id, **node)

        # Add directed edges
        # NOTE: graph.json uses "from"/"to" keys (not "source"/"target")
        # and "kind" for the edge type (not "type")
        for edge in data.get("edges", []):
            source = edge.get("from", "")
            target = edge.get("to", "")
            if source and target:
                self._graph.add_edge(source, target, **edge)

        self._loaded = True
        logger.info(
            f"Graph loaded: {self._graph.number_of_nodes()} nodes, "
            f"{self._graph.number_of_edges()} edges"
        )

    def get_callees(self, node_id: str) -> list[str]:
        """
        Get all functions directly called by the given node.

        Args:
            node_id: The function/class ID (e.g. "func:deepxube.domains.cube3.Cube3.is_solved")

        Returns:
            List of callee node IDs. Empty if node not found.
        """
        if not self._graph.has_node(node_id):
            return []
        return list(self._graph.successors(node_id))

    def get_callers(self, node_id: str) -> list[str]:
        """
        Get all functions that directly call the given node.

        Args:
            node_id: The function/class ID.

        Returns:
            List of caller node IDs. Empty if node not found.
        """
        if not self._graph.has_node(node_id):
            return []
        return list(self._graph.predecessors(node_id))

    def expand_1hop(self, node_ids: list[str]) -> list[str]:
        """
        Expand a set of nodes to include all 1-hop neighbors.

        Given a list of node IDs (e.g. from vector search results),
        returns the original nodes PLUS all their direct callers and callees.
        Duplicates are removed.

        Args:
            node_ids: List of node IDs to expand.

        Returns:
            Deduplicated list of node IDs (originals + 1-hop neighbors).
        """
        expanded = set(node_ids)
        for node_id in node_ids:
            expanded.update(self.get_callees(node_id))
            expanded.update(self.get_callers(node_id))
        return list(expanded)

    def get_node_metadata(self, node_id: str) -> dict:
        """
        Get the metadata dict for a node.

        Args:
            node_id: The function/class/module ID.

        Returns:
            Node attribute dict, or empty dict if not found.
        """
        if self._graph.has_node(node_id):
            return dict(self._graph.nodes[node_id])
        return {}

    def get_full_graph_data(self) -> dict:
        """
        Return the raw graph JSON data (nodes + edges).

        Used by the /api/graph endpoint to serve the full graph
        structure to the frontend for Cytoscape.js visualization.

        Returns:
            The parsed graph.json dict, or empty dict if not loaded.
        """
        return self._raw_data

    def get_node_doc_content(self, node_id: str) -> str | None:
        """
        Read the .md documentation file for a specific node.

        Looks up the node's doc_path metadata, resolves it against
        the code docs directory, and returns the file content.

        Args:
            node_id: The node ID (e.g. "func:deepxube.base.domain.Domain.is_solved")

        Returns:
            The markdown content string, or None if not found.
        """
        meta = self.get_node_metadata(node_id)
        doc_path = meta.get("doc_path")
        if not doc_path:
            return None

        full_path = settings.code_docs_abs / doc_path
        if not full_path.exists():
            logger.warning(f"Doc file not found: {full_path}")
            return None

        try:
            return full_path.read_text(encoding="utf-8")
        except Exception as e:
            logger.error(f"Error reading doc file {full_path}: {e}")
            return None

    @property
    def is_loaded(self) -> bool:
        """Whether the graph has been loaded from disk."""
        return self._loaded

    @property
    def node_count(self) -> int:
        """Total number of nodes in the graph."""
        return self._graph.number_of_nodes()

    @property
    def edge_count(self) -> int:
        """Total number of edges in the graph."""
        return self._graph.number_of_edges()


# ── Singleton instance ──────────────────────────────────────────────────
graph_store = GraphStore()
