// ============================================================================
// DeepXube RAG Chatbot - API Service Layer
// ============================================================================
// Handles all communication with the FastAPI backend.
// Manages session ID persistence via localStorage.
//
// Usage:
//   import { sendMessage, checkHealth } from './services/api';
//   const response = await sendMessage("What is DeepCubeA?");
// ============================================================================

const API_BASE = "http://localhost:8000";

/**
 * Get or create a session ID.
 * Persisted in localStorage so conversations survive page refresh.
 */
function getSessionId() {
  let sessionId = localStorage.getItem("deepxube_session_id");
  if (!sessionId) {
    sessionId = crypto.randomUUID();
    localStorage.setItem("deepxube_session_id", sessionId);
  }
  return sessionId;
}

/**
 * Start a new session (clears the stored session ID).
 */
export function resetSession() {
  localStorage.removeItem("deepxube_session_id");
}

/**
 * Send a chat message to the backend.
 *
 * @param {string} query - The user's message.
 * @returns {Promise<Object>} The response object:
 *   { response, citations, session_id, route, is_faq_hit }
 * @throws {Error} If the API request fails.
 */
export async function sendMessage(query) {
  const sessionId = getSessionId();

  const res = await fetch(`${API_BASE}/api/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      query,
      session_id: sessionId,
    }),
  });

  if (!res.ok) {
    if (res.status === 429) {
      throw new Error(
        "Rate limit exceeded. Please wait a moment before sending another message."
      );
    }
    throw new Error(`API error: ${res.status} ${res.statusText}`);
  }

  const data = await res.json();

  // Update session ID if the server assigned a new one
  if (data.session_id) {
    localStorage.setItem("deepxube_session_id", data.session_id);
  }

  return data;
}

/**
 * Check the backend health status.
 *
 * @returns {Promise<Object>} Health info:
 *   { status, collections, active_sessions, graph_loaded, graph_nodes }
 */
export async function checkHealth() {
  const res = await fetch(`${API_BASE}/api/health`);
  if (!res.ok) {
    throw new Error("Backend is not reachable");
  }
  return res.json();
}

/**
 * Trigger ingestion of one or all collections.
 *
 * @param {string} target - "code", "papers", "faq", or "all".
 * @param {boolean} clearFirst - Whether to clear before re-ingesting.
 * @returns {Promise<Object>} Ingestion result.
 */
export async function triggerIngest(target = "all", clearFirst = false) {
  const res = await fetch(`${API_BASE}/api/ingest`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ target, clear_first: clearFirst }),
  });
  if (!res.ok) {
    throw new Error(`Ingest failed: ${res.status}`);
  }
  return res.json();
}

/**
 * Fetch the full code call-graph for Cytoscape.js visualization.
 *
 * @returns {Promise<Object>} The graph data:
 *   { nodes: [...], edges: [...] }
 */
export async function fetchGraphData() {
  const res = await fetch(`${API_BASE}/api/graph`);
  if (!res.ok) {
    throw new Error(`Failed to fetch graph: ${res.status}`);
  }
  return res.json();
}

/**
 * Fetch the markdown documentation for a specific graph node.
 *
 * @param {string} nodeId - The node ID (e.g. "func:deepxube.base.domain.Domain.is_solved")
 * @returns {Promise<Object>} The node docs:
 *   { node_id, doc_path, content, found }
 */
export async function fetchNodeDocs(nodeId) {
  const encodedId = encodeURIComponent(nodeId);
  const res = await fetch(`${API_BASE}/api/graph/node/${encodedId}/docs`);
  if (!res.ok) {
    throw new Error(`Failed to fetch node docs: ${res.status}`);
  }
  return res.json();
}
