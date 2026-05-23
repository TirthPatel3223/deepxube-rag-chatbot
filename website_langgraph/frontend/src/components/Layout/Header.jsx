// ============================================================================
// Header Component
// ============================================================================
// Top navigation bar with logo, page navigation, and new chat button.
// ============================================================================

import { NavLink } from "react-router-dom";
import { resetSession } from "../../services/api";
import "../../styles/layout.css";

export default function Header({ onNewChat }) {
  const handleNewChat = () => {
    resetSession();
    if (onNewChat) onNewChat();
    window.location.reload();
  };

  return (
    <header className="header" id="main-header">
      <div className="header-left">
        <div className="header-logo">DX</div>
        <div>
          <div className="header-title">DeepXube</div>
          <div className="header-subtitle">RAG Assistant</div>
        </div>
      </div>

      <nav className="header-nav">
        <NavLink
          to="/"
          className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}
          id="nav-chat"
        >
          💬 Chat
        </NavLink>
        <NavLink
          to="/graph"
          className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}
          id="nav-graph"
        >
          🔗 Graph Explorer
        </NavLink>
      </nav>

      <button className="new-chat-btn" onClick={handleNewChat} id="new-chat-btn">
        ✨ New Chat
      </button>
    </header>
  );
}
