// ============================================================================
// GraphCanvas Component — Cytoscape.js Renderer
// ============================================================================
// Renders the graph using Cytoscape.js with the fCoSE force-directed layout.
// Handles node styling by kind/module, click events, and layout updates.
// ============================================================================

import { useEffect, useRef, useCallback } from "react";
import cytoscape from "cytoscape";
import fcose from "cytoscape-fcose";

// Register the fCoSE layout extension
cytoscape.use(fcose);

// ── Edge kind colors ──────────────────────────────────────────────────
const EDGE_COLORS = {
  calls: "#818cf8",
  inherits: "#f59e0b",
  reads_attr: "#22c55e",
  writes_attr: "#ef4444",
  registers: "#06b6d4",
  raises: "#f97316",
};

// ── Edge kind line styles ─────────────────────────────────────────────
const EDGE_STYLES = {
  calls: "solid",
  inherits: "solid",
  reads_attr: "dashed",
  writes_attr: "dashed",
  registers: "dotted",
  raises: "dotted",
};

// ── Cytoscape stylesheet ─────────────────────────────────────────────
const CY_STYLESHEET = [
  // --- Nodes ---
  {
    selector: "node",
    style: {
      label: "data(label)",
      "text-valign": "center",
      "text-halign": "center",
      "font-family": "Inter, sans-serif",
      "font-size": "11px",
      "font-weight": 500,
      color: "#f1f1f3",
      "text-outline-color": "data(color)",
      "text-outline-width": 2,
      "text-outline-opacity": 0.7,
      "background-color": "data(color)",
      "background-opacity": 0.85,
      "border-width": 2,
      "border-color": "data(color)",
      "border-opacity": 0.5,
      "overlay-opacity": 0,
      "transition-property": "background-opacity, border-width, width, height",
      "transition-duration": "0.15s",
    },
  },
  // Module nodes — larger, rounded rectangle
  {
    selector: 'node[kind = "module"]',
    style: {
      shape: "round-rectangle",
      width: 140,
      height: 45,
      "font-size": "13px",
      "font-weight": 600,
      "background-opacity": 0.9,
      "border-width": 2.5,
    },
  },
  // Expanded modules get a special indicator
  {
    selector: "node[?isExpanded]",
    style: {
      "border-width": 3,
      "border-style": "double",
      "border-color": "#f1f1f3",
      "background-opacity": 0.6,
    },
  },
  // Class nodes — ellipse, medium
  {
    selector: 'node[kind = "class"]',
    style: {
      shape: "ellipse",
      width: 110,
      height: 38,
      "font-size": "11px",
      "font-weight": 500,
    },
  },
  // Function nodes — diamond, small
  {
    selector: 'node[kind = "function"]',
    style: {
      shape: "diamond",
      width: 80,
      height: 40,
      "font-size": "10px",
    },
  },
  // Method nodes — small rounded rectangle
  {
    selector: 'node[kind = "method"], node[kind = "staticmethod"], node[kind = "classmethod"]',
    style: {
      shape: "round-rectangle",
      width: 100,
      height: 30,
      "font-size": "9px",
    },
  },
  // Factory nodes — hexagon, medium
  {
    selector: 'node[kind = "factory"]',
    style: {
      shape: "hexagon",
      width: 100,
      height: 40,
      "font-size": "10px",
      "font-weight": 500,
    },
  },
  // Abstract nodes — dashed border
  {
    selector: "node[?isAbstract]",
    style: {
      "border-style": "dashed",
    },
  },
  // Hovered node
  {
    selector: "node:active",
    style: {
      "background-opacity": 1,
      "border-width": 3,
      "overlay-opacity": 0.08,
    },
  },
  // Selected node
  {
    selector: "node.selected",
    style: {
      "border-width": 3,
      "border-color": "#f1f1f3",
      "background-opacity": 1,
      "overlay-opacity": 0.1,
      "overlay-color": "#818cf8",
    },
  },
  // Dimmed nodes (when a node is selected, others dim)
  {
    selector: "node.dimmed",
    style: {
      "background-opacity": 0.2,
      "border-opacity": 0.15,
      "text-opacity": 0.3,
    },
  },

  // --- Edges ---
  {
    selector: "edge",
    style: {
      width: 1.5,
      "line-color": "#4a4a5a",
      "target-arrow-color": "#4a4a5a",
      "target-arrow-shape": "triangle",
      "arrow-scale": 0.8,
      "curve-style": "bezier",
      opacity: 0.5,
      "transition-property": "opacity, line-color",
      "transition-duration": "0.15s",
    },
  },
  // Edge kinds with specific colors
  {
    selector: 'edge[kind = "calls"]',
    style: {
      "line-color": EDGE_COLORS.calls,
      "target-arrow-color": EDGE_COLORS.calls,
      "line-style": EDGE_STYLES.calls,
    },
  },
  {
    selector: 'edge[kind = "inherits"]',
    style: {
      "line-color": EDGE_COLORS.inherits,
      "target-arrow-color": EDGE_COLORS.inherits,
      "target-arrow-shape": "triangle-tee",
      "line-style": EDGE_STYLES.inherits,
      width: 2,
    },
  },
  {
    selector: 'edge[kind = "reads_attr"]',
    style: {
      "line-color": EDGE_COLORS.reads_attr,
      "target-arrow-color": EDGE_COLORS.reads_attr,
      "line-style": EDGE_STYLES.reads_attr,
      width: 1,
      opacity: 0.35,
    },
  },
  {
    selector: 'edge[kind = "writes_attr"]',
    style: {
      "line-color": EDGE_COLORS.writes_attr,
      "target-arrow-color": EDGE_COLORS.writes_attr,
      "line-style": EDGE_STYLES.writes_attr,
      width: 1,
      opacity: 0.35,
    },
  },
  {
    selector: 'edge[kind = "registers"]',
    style: {
      "line-color": EDGE_COLORS.registers,
      "target-arrow-color": EDGE_COLORS.registers,
      "line-style": EDGE_STYLES.registers,
    },
  },
  {
    selector: 'edge[kind = "raises"]',
    style: {
      "line-color": EDGE_COLORS.raises,
      "target-arrow-color": EDGE_COLORS.raises,
      "line-style": EDGE_STYLES.raises,
    },
  },
  // Dimmed edges
  {
    selector: "edge.dimmed",
    style: {
      opacity: 0.08,
    },
  },
  // Highlighted edges (connected to selected node)
  {
    selector: "edge.highlighted",
    style: {
      opacity: 0.9,
      width: 2.5,
    },
  },
];

export default function GraphCanvas({
  elements,
  cyRef,
  onNodeClick,
  onNodeSelect,
  selectedNodeId,
}) {
  const containerRef = useRef(null);
  const prevElementsRef = useRef({ nodes: [], edges: [] });

  // ── Initialize Cytoscape ────────────────────────────────────────────
  useEffect(() => {
    if (!containerRef.current) return;

    const cy = cytoscape({
      container: containerRef.current,
      elements: [],
      style: CY_STYLESHEET,
      layout: { name: "preset" },
      minZoom: 0.1,
      maxZoom: 5,
      boxSelectionEnabled: false,
      autoungrabify: false,
    });

    // Expose to parent via ref
    cyRef.current = cy;

    // ── Click handler ─────────────────────────────────────────────────
    cy.on("tap", "node", (evt) => {
      const nodeData = evt.target.data();
      const kind = nodeData.kind;

      // Module/class: expand/collapse on single click
      if (kind === "module" || kind === "class") {
        onNodeClick(nodeData);
      } else {
        // Function/method/factory: select for docs panel
        onNodeSelect(nodeData);
      }
    });

    // Right-click or secondary tap to open docs for module/class too
    cy.on("cxttap", "node", (evt) => {
      onNodeSelect(evt.target.data());
    });

    // Click background to deselect
    cy.on("tap", (evt) => {
      if (evt.target === cy) {
        onNodeSelect(null);
      }
    });

    // Clean up
    return () => {
      cy.destroy();
      cyRef.current = null;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // ── Update elements when they change ────────────────────────────────
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy) return;

    const prevNodes = prevElementsRef.current.nodes;
    const prevEdges = prevElementsRef.current.edges;
    const newNodes = elements.nodes;
    const newEdges = elements.edges;

    // Check if elements actually changed
    const prevNodeIds = new Set(prevNodes.map((n) => n.data.id));
    const newNodeIds = new Set(newNodes.map((n) => n.data.id));
    const prevEdgeIds = new Set(prevEdges.map((e) => e.data.id));
    const newEdgeIds = new Set(newEdges.map((e) => e.data.id));

    const nodesChanged =
      prevNodeIds.size !== newNodeIds.size ||
      [...newNodeIds].some((id) => !prevNodeIds.has(id)) ||
      [...prevNodeIds].some((id) => !newNodeIds.has(id));

    const edgesChanged =
      prevEdgeIds.size !== newEdgeIds.size ||
      [...newEdgeIds].some((id) => !prevEdgeIds.has(id)) ||
      [...prevEdgeIds].some((id) => !newEdgeIds.has(id));

    if (!nodesChanged && !edgesChanged) {
      // Update data on existing nodes (e.g., isExpanded flag)
      newNodes.forEach((n) => {
        const ele = cy.getElementById(n.data.id);
        if (ele.length) {
          ele.data(n.data);
        }
      });
      prevElementsRef.current = { nodes: newNodes, edges: newEdges };
      return;
    }

    // Batch update: remove old, add new
    cy.startBatch();

    // Remove elements no longer present
    const toRemoveEdges = cy.edges().filter((e) => !newEdgeIds.has(e.id()));
    const toRemoveNodes = cy.nodes().filter((n) => !newNodeIds.has(n.id()));
    toRemoveEdges.remove();
    toRemoveNodes.remove();

    // Add new nodes
    const existingNodeIds = new Set(cy.nodes().map((n) => n.id()));
    const nodesToAdd = newNodes.filter((n) => !existingNodeIds.has(n.data.id));
    if (nodesToAdd.length > 0) {
      cy.add(nodesToAdd);
    }

    // Update data on existing nodes
    newNodes.forEach((n) => {
      const ele = cy.getElementById(n.data.id);
      if (ele.length) {
        ele.data(n.data);
      }
    });

    // Add new edges
    const existingEdgeIds = new Set(cy.edges().map((e) => e.id()));
    const edgesToAdd = newEdges.filter((e) => !existingEdgeIds.has(e.data.id));
    if (edgesToAdd.length > 0) {
      cy.add(edgesToAdd);
    }

    cy.endBatch();

    // Run layout if nodes changed
    if (nodesChanged && cy.nodes().length > 0) {
      const layoutOpts = {
        name: "fcose",
        animate: prevNodes.length > 0,
        animationDuration: 500,
        randomize: prevNodes.length === 0,
        fit: true,
        padding: 30,
        // fCoSE-specific — tighter layout for readable node labels
        idealEdgeLength: () => 60,
        nodeRepulsion: () => 4500,
        nodeSeparation: 30,
        quality: "default",
      };

      cy.layout(layoutOpts).run();
    }

    prevElementsRef.current = { nodes: newNodes, edges: newEdges };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [elements]);

  // ── Highlight selected node and its neighbors ───────────────────────
  useEffect(() => {
    const cy = cyRef.current;
    if (!cy) return;

    // Clear previous highlights
    cy.elements().removeClass("selected dimmed highlighted");

    if (selectedNodeId) {
      const selected = cy.getElementById(selectedNodeId);
      if (selected.length) {
        selected.addClass("selected");

        // Find connected edges and neighbor nodes
        const connectedEdges = selected.connectedEdges();
        const neighbors = selected.neighborhood("node");

        // Dim everything else
        cy.elements().not(selected).not(connectedEdges).not(neighbors).addClass("dimmed");
        connectedEdges.addClass("highlighted");
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [selectedNodeId]);

  return (
    <div className="graph-canvas-container" id="graph-canvas">
      <div ref={containerRef} className="graph-canvas" />
    </div>
  );
}
