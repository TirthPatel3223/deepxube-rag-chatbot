// ============================================================================
// GraphExplorer Component — Main Container
// ============================================================================
// Orchestrates the graph explorer page: loads graph data from the API,
// manages expansion/filter/selection state, and wires up the canvas,
// toolbar, and sidebar components.
// ============================================================================

import { useState, useEffect, useCallback, useRef } from "react";
import { fetchGraphData } from "../../services/api";
import GraphCanvas from "./GraphCanvas";
import GraphToolbar from "./GraphToolbar";
import GraphSidebar from "./GraphSidebar";
import "../../styles/graph-explorer.css";

// ── Module color palette ──────────────────────────────────────────────
const MODULE_COLORS = {
  "deepxube.base": "#6366f1",
  "deepxube.domains": "#22c55e",
  "deepxube.factories": "#f59e0b",
  "deepxube.heuristics": "#ef4444",
  "deepxube.logic": "#8b5cf6",
  "deepxube.nnet": "#06b6d4",
  "deepxube.pathfinding": "#ec4899",
  "deepxube.trainers": "#f97316",
  "deepxube.updaters": "#14b8a6",
  "deepxube.utils": "#64748b",
  "deepxube._cli": "#a78bfa",
  "deepxube._solve": "#a78bfa",
  "deepxube._train_cli": "#a78bfa",
  "deepxube.__main__": "#a78bfa",
  "deepxube.tests": "#78716c",
  "tests": "#78716c",
};

/**
 * Resolve the color for a node based on its module.
 * Walks from the most specific module path up to the top-level package.
 */
function getModuleColor(modulePath) {
  if (!modulePath) return "#64748b";
  // Try exact match first
  if (MODULE_COLORS[modulePath]) return MODULE_COLORS[modulePath];
  // Walk up the module path
  const parts = modulePath.split(".");
  for (let i = parts.length - 1; i >= 1; i--) {
    const prefix = parts.slice(0, i).join(".");
    if (MODULE_COLORS[prefix]) return MODULE_COLORS[prefix];
  }
  return "#64748b";
}

// ── Default edge kinds shown ──────────────────────────────────────────
const DEFAULT_EDGE_KINDS = new Set(["calls", "inherits"]);
const ALL_EDGE_KINDS = ["calls", "inherits", "reads_attr", "writes_attr", "registers", "raises"];

export default function GraphExplorer() {
  // ── Raw data from API ───────────────────────────────────────────────
  const [graphData, setGraphData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // ── Expansion state ─────────────────────────────────────────────────
  const [expandedModules, setExpandedModules] = useState(new Set());
  const [expandedClasses, setExpandedClasses] = useState(new Set());

  // ── Filtering / selection ───────────────────────────────────────────
  const [activeEdgeKinds, setActiveEdgeKinds] = useState(DEFAULT_EDGE_KINDS);
  const [selectedNode, setSelectedNode] = useState(null);
  const [searchQuery, setSearchQuery] = useState("");

  // ── Cytoscape ref for toolbar controls ──────────────────────────────
  const cyRef = useRef(null);

  // ── Load graph data on mount ────────────────────────────────────────
  useEffect(() => {
    let cancelled = false;
    setLoading(true);

    fetchGraphData()
      .then((data) => {
        if (!cancelled) {
          setGraphData(data);
          setLoading(false);
        }
      })
      .catch((err) => {
        if (!cancelled) {
          setError(err.message);
          setLoading(false);
        }
      });

    return () => {
      cancelled = true;
    };
  }, []);

  // ── Build visible elements from raw data + expansion state ──────────
  const visibleElements = useCallback(() => {
    if (!graphData) return { nodes: [], edges: [] };

    const rawNodes = graphData.nodes || [];
    const rawEdges = graphData.edges || [];
    const isSearching = searchQuery.trim().length > 0;
    const query = searchQuery.trim().toLowerCase();

    // ── Index raw nodes by ID ─────────────────────────────────────────
    const nodeById = {};
    rawNodes.forEach((n) => {
      nodeById[n.id] = n;
    });

    // ── Determine which nodes are visible ─────────────────────────────
    let visibleNodeIds;

    if (isSearching) {
      // Search mode: show all nodes matching the query (any level)
      visibleNodeIds = new Set();
      rawNodes.forEach((n) => {
        const nameMatch = (n.name || "").toLowerCase().includes(query);
        const moduleMatch = (n.module || "").toLowerCase().includes(query);
        const idMatch = (n.id || "").toLowerCase().includes(query);
        if (nameMatch || moduleMatch || idMatch) {
          visibleNodeIds.add(n.id);
        }
      });
    } else {
      // Hierarchy mode: modules → expand into classes/functions → expand into methods
      visibleNodeIds = new Set();

      rawNodes.forEach((n) => {
        const kind = n.kind;
        const mod = n.module || "";

        if (kind === "module") {
          visibleNodeIds.add(n.id);
        } else if (kind === "class") {
          // Show if parent module is expanded
          const moduleId = `module:${mod}`;
          if (expandedModules.has(moduleId)) {
            visibleNodeIds.add(n.id);
          }
        } else if (kind === "factory") {
          const moduleId = `module:${mod}`;
          if (expandedModules.has(moduleId)) {
            visibleNodeIds.add(n.id);
          }
        } else if (kind === "function" && !n.class_id) {
          // Standalone function (not a method)
          const moduleId = `module:${mod}`;
          if (expandedModules.has(moduleId)) {
            visibleNodeIds.add(n.id);
          }
        } else if (
          kind === "method" ||
          kind === "staticmethod" ||
          kind === "classmethod" ||
          (kind === "function" && n.class_id)
        ) {
          // Method-like: show if parent class is expanded
          if (n.class_id && expandedClasses.has(n.class_id)) {
            visibleNodeIds.add(n.id);
          }
        }
      });
    }

    // ── Build Cytoscape node elements ─────────────────────────────────
    const cyNodes = [];
    visibleNodeIds.forEach((id) => {
      const n = nodeById[id];
      if (!n) return;
      const color = getModuleColor(n.module);
      const isExpanded =
        (n.kind === "module" && expandedModules.has(n.id)) ||
        (n.kind === "class" && expandedClasses.has(n.id));

      cyNodes.push({
        data: {
          id: n.id,
          label: n.name || n.id,
          kind: n.kind,
          module: n.module || "",
          file: n.file || "",
          lineStart: n.line_start,
          lineEnd: n.line_end,
          isAbstract: n.is_abstract || false,
          docPath: n.doc_path || "",
          color,
          isExpanded,
          classId: n.class_id || null,
        },
      });
    });

    // ── Build a map: node ID → visible ancestor ID ─────────────────────
    // For edges whose endpoints aren't directly visible, map them up
    // to the nearest visible ancestor (module or expanded class).
    const nodeToVisibleAncestor = {};
    rawNodes.forEach((n) => {
      if (visibleNodeIds.has(n.id)) {
        nodeToVisibleAncestor[n.id] = n.id;
      } else if (!isSearching) {
        // Map to parent module
        const moduleId = `module:${n.module}`;
        if (visibleNodeIds.has(moduleId)) {
          nodeToVisibleAncestor[n.id] = moduleId;
        }
        // If parent class is visible but not expanded, map to class
        if (n.class_id && visibleNodeIds.has(n.class_id) && !expandedClasses.has(n.class_id)) {
          nodeToVisibleAncestor[n.id] = n.class_id;
        }
      }
    });

    // ── Build Cytoscape edge elements (with aggregation) ──────────────
    const cyEdges = [];
    const edgeIdSet = new Set();
    rawEdges.forEach((e) => {
      const kind = e.kind;

      // Only show edges with active kinds
      if (!activeEdgeKinds.has(kind)) return;

      const fromRaw = e.from;
      const toRaw = e.to;

      // Resolve to visible ancestors
      const from = nodeToVisibleAncestor[fromRaw];
      const to = nodeToVisibleAncestor[toRaw];

      // Both endpoints must resolve to something visible
      if (!from || !to) return;

      // No self-loops (common when aggregating to the same module)
      if (from === to) return;

      // Deduplicate aggregated edges
      const edgeId = `${from}→${to}→${kind}`;
      if (edgeIdSet.has(edgeId)) return;
      edgeIdSet.add(edgeId);

      cyEdges.push({
        data: {
          id: edgeId,
          source: from,
          target: to,
          kind,
        },
      });
    });

    return { nodes: cyNodes, edges: cyEdges };
  }, [graphData, expandedModules, expandedClasses, activeEdgeKinds, searchQuery]);

  // ── Event handlers ──────────────────────────────────────────────────

  const handleNodeClick = useCallback(
    (nodeData) => {
      const { id, kind } = nodeData;

      if (kind === "module") {
        // Toggle module expansion
        setExpandedModules((prev) => {
          const next = new Set(prev);
          if (next.has(id)) {
            next.delete(id);
            // Also collapse any classes inside this module
            setExpandedClasses((prevClasses) => {
              const nextClasses = new Set(prevClasses);
              graphData?.nodes?.forEach((n) => {
                if (n.kind === "class" && `module:${n.module}` === id) {
                  nextClasses.delete(n.id);
                }
              });
              return nextClasses;
            });
          } else {
            next.add(id);
          }
          return next;
        });
      } else if (kind === "class") {
        // Toggle class expansion
        setExpandedClasses((prev) => {
          const next = new Set(prev);
          if (next.has(id)) {
            next.delete(id);
          } else {
            next.add(id);
          }
          return next;
        });
      } else {
        // For functions/methods, select for the side panel
        setSelectedNode(nodeData);
      }
    },
    [graphData]
  );

  const handleNodeSelect = useCallback((nodeData) => {
    setSelectedNode(nodeData);
  }, []);

  const handleCloseSidebar = useCallback(() => {
    setSelectedNode(null);
  }, []);

  const handleToggleEdgeKind = useCallback((kind) => {
    setActiveEdgeKinds((prev) => {
      const next = new Set(prev);
      if (next.has(kind)) {
        next.delete(kind);
      } else {
        next.add(kind);
      }
      return next;
    });
  }, []);

  const handleSearchChange = useCallback((query) => {
    setSearchQuery(query);
  }, []);

  const handleResetLayout = useCallback(() => {
    if (cyRef.current) {
      cyRef.current.layout({
        name: "fcose",
        animate: true,
        animationDuration: 600,
        randomize: true,
        fit: true,
        padding: 30,
        idealEdgeLength: () => 60,
        nodeRepulsion: () => 4500,
        nodeSeparation: 30,
      }).run();
    }
  }, []);

  const handleFitToScreen = useCallback(() => {
    if (cyRef.current) {
      cyRef.current.animate({ fit: { padding: 50 } }, { duration: 400 });
    }
  }, []);

  const handleZoomIn = useCallback(() => {
    if (cyRef.current) {
      const cy = cyRef.current;
      cy.animate({ zoom: cy.zoom() * 1.3, center: cy.extent() }, { duration: 200 });
    }
  }, []);

  const handleZoomOut = useCallback(() => {
    if (cyRef.current) {
      const cy = cyRef.current;
      cy.animate({ zoom: cy.zoom() / 1.3, center: cy.extent() }, { duration: 200 });
    }
  }, []);

  // ── Render ──────────────────────────────────────────────────────────
  if (loading) {
    return (
      <div className="graph-explorer-loading">
        <div className="graph-loading-spinner" />
        <p>Loading code graph…</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="graph-explorer-error">
        <div className="graph-error-icon">⚠️</div>
        <h3>Failed to load graph</h3>
        <p>{error}</p>
        <button onClick={() => window.location.reload()}>Retry</button>
      </div>
    );
  }

  const elements = visibleElements();

  return (
    <div className="graph-explorer" id="graph-explorer">
      <GraphToolbar
        searchQuery={searchQuery}
        onSearchChange={handleSearchChange}
        activeEdgeKinds={activeEdgeKinds}
        allEdgeKinds={ALL_EDGE_KINDS}
        onToggleEdgeKind={handleToggleEdgeKind}
        onResetLayout={handleResetLayout}
        onFitToScreen={handleFitToScreen}
        onZoomIn={handleZoomIn}
        onZoomOut={handleZoomOut}
        nodeCount={elements.nodes.length}
        edgeCount={elements.edges.length}
      />

      <div className="graph-explorer-body">
        <GraphCanvas
          elements={elements}
          cyRef={cyRef}
          onNodeClick={handleNodeClick}
          onNodeSelect={handleNodeSelect}
          selectedNodeId={selectedNode?.id}
        />

        {selectedNode && (
          <GraphSidebar
            nodeData={selectedNode}
            onClose={handleCloseSidebar}
          />
        )}
      </div>
    </div>
  );
}
