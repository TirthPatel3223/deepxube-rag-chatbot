// ============================================================================
// ChatWindow Component
// ============================================================================
// Main chat container. Manages the message list, sends queries to the
// backend, and displays responses with markdown formatting.
// ============================================================================

import { useState, useRef, useEffect } from "react";
import MessageBubble from "./MessageBubble";
import TypingIndicator from "./TypingIndicator";
import InputBar from "./InputBar";
import { sendMessage } from "../../services/api";
import exportChatPdf from "../../utils/exportChatPdf";
import "../../styles/chat.css";

const SUGGESTIONS = [
  "What is DeepCubeA?",
  "How do I add a new puzzle domain?",
  "Explain the training pipeline",
  "What does the Cube3 class do?",
];

export default function ChatWindow() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const messagesEndRef = useRef(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const handleSend = async (text) => {
    // Add user message immediately
    const userMessage = { role: "user", content: text };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);
    setError(null);

    try {
      const data = await sendMessage(text);

      // Add assistant response
      const assistantMessage = {
        role: "assistant",
        content: data.response,
        route: data.route,
        citations: data.citations,
        isFaqHit: data.is_faq_hit,
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      setError(err.message);
      // Add error as assistant message
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: `⚠️ ${err.message}`,
          route: "error",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-page">
      <div className="messages-container">
        {messages.length === 0 ? (
          <div className="messages-empty">
            <div style={{ fontSize: "2.5rem" }}>🧩</div>
            <h2>
              <span className="gradient-text">DeepXube</span> Assistant
            </h2>
            <p>
              Ask me about the DeepXube codebase, the underlying research
              papers, or get guided through creating your own puzzle domain.
            </p>
            <div className="suggestions">
              {SUGGESTIONS.map((suggestion, i) => (
                <button
                  key={i}
                  className="suggestion-chip"
                  onClick={() => handleSend(suggestion)}
                  id={`suggestion-${i}`}
                >
                  {suggestion}
                </button>
              ))}
            </div>
          </div>
        ) : (
          messages.map((msg, i) => (
            <MessageBubble key={i} message={msg} />
          ))
        )}
        {loading && <TypingIndicator />}
        <div ref={messagesEndRef} />
      </div>

      {messages.length > 0 && (
        <div className="chat-actions">
          <button
            className="download-pdf-btn"
            onClick={() => exportChatPdf(messages)}
            title="Download chat as PDF"
            id="download-pdf-btn"
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
              <polyline points="7 10 12 15 17 10" />
              <line x1="12" y1="15" x2="12" y2="3" />
            </svg>
            Download PDF
          </button>
        </div>
      )}

      <InputBar onSend={handleSend} disabled={loading} />
    </div>
  );
}
