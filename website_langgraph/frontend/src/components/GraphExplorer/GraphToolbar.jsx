// ============================================================================
// GraphToolbar Component — Search, Edge Filters & Controls
// ============================================================================
// Provides search input for filtering the graph, edge kind toggle pills,
// zoom/layout control buttons, and a live node/edge count display.
// ============================================================================

// ── Edge kind display labels ──────────────────────────────────────────
const EDGE_KIND_LABELS = {
  calls: "Calls",
  inherits: "Inherits",
  reads_attr: "Reads",
  writes_attr: "Writes",
  registers: "Registers",
  raises: "Raises",
};

const EDGE_KIND_COLORS = {
  calls: "#818cf8",
  inherits: "#f59e0b",
  reads_attr: "#22c55e",
  writes_attr: "#ef4444",
  registers: "#06b6d4",
  raises: "#f97316",
};

export default function GraphToolbar({
  searchQuery,
  onSearchChange,
  activeEdgeKinds,
  allEdgeKinds,
  onToggleEdgeKind,
  onResetLayout,
  onFitToScreen,
  onZoomIn,
  onZoomOut,
  nodeCount,
  edgeCount,
}) {
  return (
    <div className="graph-toolbar" id="graph-toolbar">
      {/* ── Search ──────────────────────────────────────────────── */}
      <div className="graph-toolbar-section graph-search-section">
        <div className="graph-search-wrapper">
          <span className="graph-search-icon">🔍</span>
          <input
            type="text"
            className="graph-search-input"
            id="graph-search-input"
            placeholder="Search nodes…"
            value={searchQuery}
            onChange={(e) => onSearchChange(e.target.value)}
          />
          {searchQuery && (
            <button
              className="graph-search-clear"
              onClick={() => onSearchChange("")}
              aria-label="Clear search"
            >
              ✕
            </button>
          )}
        </div>
      </div>

      {/* ── Edge Kind Toggles ──────────────────────────────────── */}
      <div className="graph-toolbar-section graph-edge-filters">
        <span className="graph-toolbar-label">Edges:</span>
        {allEdgeKinds.map((kind) => {
          const isActive = activeEdgeKinds.has(kind);
          return (
            <button
              key={kind}
              className={`graph-edge-pill ${isActive ? "active" : ""}`}
              onClick={() => onToggleEdgeKind(kind)}
              style={{
                "--pill-color": EDGE_KIND_COLORS[kind],
              }}
              id={`edge-toggle-${kind}`}
            >
              {EDGE_KIND_LABELS[kind] || kind}
            </button>
          );
        })}
      </div>

      {/* ── Layout Controls ────────────────────────────────────── */}
      <div className="graph-toolbar-section graph-controls">
        <button className="graph-control-btn" onClick={onZoomIn} title="Zoom In" id="graph-zoom-in">
          +
        </button>
        <button className="graph-control-btn" onClick={onZoomOut} title="Zoom Out" id="graph-zoom-out">
          −
        </button>
        <button className="graph-control-btn" onClick={onFitToScreen} title="Fit to Screen" id="graph-fit">
          ⊡
        </button>
        <button className="graph-control-btn" onClick={onResetLayout} title="Reset Layout" id="graph-reset">
          ↻
        </button>

        <div className="graph-stats">
          <span className="graph-stat">{nodeCount} nodes</span>
          <span className="graph-stat-separator">·</span>
          <span className="graph-stat">{edgeCount} edges</span>
        </div>
      </div>
    </div>
  );
}
