// ============================================================================
// GraphSidebar Component — Node Documentation Panel
// ============================================================================
// Slides in from the right when a node is selected. Fetches and displays
// the .md documentation from the backend API, rendered as markdown.
// Shows node metadata (kind, module, file, line numbers) at the top.
// ============================================================================

import { useState, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { fetchNodeDocs } from "../../services/api";

// ── Kind badge colors ─────────────────────────────────────────────────
const KIND_BADGE_COLORS = {
  module: "#6366f1",
  class: "#22c55e",
  function: "#ec4899",
  method: "#818cf8",
  staticmethod: "#06b6d4",
  classmethod: "#f59e0b",
  factory: "#14b8a6",
};

export default function GraphSidebar({ nodeData, onClose }) {
  const [docContent, setDocContent] = useState(null);
  const [docLoading, setDocLoading] = useState(false);
  const [docError, setDocError] = useState(null);

  // ── Fetch docs when node changes ────────────────────────────────────
  useEffect(() => {
    if (!nodeData?.id) return;

    let cancelled = false;
    setDocLoading(true);
    setDocError(null);
    setDocContent(null);

    fetchNodeDocs(nodeData.id)
      .then((data) => {
        if (!cancelled) {
          if (data.found) {
            setDocContent(data.content);
          } else {
            setDocContent(null);
          }
          setDocLoading(false);
        }
      })
      .catch((err) => {
        if (!cancelled) {
          setDocError(err.message);
          setDocLoading(false);
        }
      });

    return () => {
      cancelled = true;
    };
  }, [nodeData?.id]);

  if (!nodeData) return null;

  const badgeColor = KIND_BADGE_COLORS[nodeData.kind] || "#64748b";

  return (
    <aside className="graph-sidebar" id="graph-sidebar">
      {/* ── Header ───────────────────────────────────────────────── */}
      <div className="graph-sidebar-header">
        <div className="graph-sidebar-title-row">
          <h3 className="graph-sidebar-title">{nodeData.label}</h3>
          <button
            className="graph-sidebar-close"
            onClick={onClose}
            aria-label="Close panel"
            id="graph-sidebar-close"
          >
            ✕
          </button>
        </div>

        <div className="graph-sidebar-meta">
          <span
            className="graph-sidebar-badge"
            style={{ backgroundColor: badgeColor }}
          >
            {nodeData.kind}
          </span>
          {nodeData.isAbstract && (
            <span className="graph-sidebar-badge graph-sidebar-badge-abstract">
              abstract
            </span>
          )}
        </div>
      </div>

      {/* ── Metadata ─────────────────────────────────────────────── */}
      <div className="graph-sidebar-metadata">
        {nodeData.module && (
          <div className="graph-meta-row">
            <span className="graph-meta-label">Module</span>
            <span className="graph-meta-value">
              <code>{nodeData.module}</code>
            </span>
          </div>
        )}
        {nodeData.file && (
          <div className="graph-meta-row">
            <span className="graph-meta-label">File</span>
            <span className="graph-meta-value">
              <code>{nodeData.file}</code>
            </span>
          </div>
        )}
        {nodeData.lineStart != null && (
          <div className="graph-meta-row">
            <span className="graph-meta-label">Lines</span>
            <span className="graph-meta-value">
              {nodeData.lineStart}–{nodeData.lineEnd}
            </span>
          </div>
        )}
      </div>

      {/* ── Documentation Content ────────────────────────────────── */}
      <div className="graph-sidebar-content">
        {docLoading && (
          <div className="graph-sidebar-loading">
            <div className="graph-loading-spinner small" />
            <span>Loading documentation…</span>
          </div>
        )}

        {docError && (
          <div className="graph-sidebar-error">
            <p>Failed to load docs: {docError}</p>
          </div>
        )}

        {!docLoading && !docError && docContent && (
          <div className="graph-sidebar-docs">
            <ReactMarkdown remarkPlugins={[remarkGfm]}>
              {docContent}
            </ReactMarkdown>
          </div>
        )}

        {!docLoading && !docError && !docContent && (
          <div className="graph-sidebar-empty">
            <p>No documentation available for this node.</p>
          </div>
        )}
      </div>
    </aside>
  );
}
