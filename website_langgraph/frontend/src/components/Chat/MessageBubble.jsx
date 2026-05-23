// ============================================================================
// MessageBubble Component
// ============================================================================
// Renders a single chat message (user or assistant) with markdown support.
// Assistant messages render markdown (code blocks, lists, tables, etc.)
// User messages render as plain text.
// ============================================================================

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function MessageBubble({ message }) {
  const isUser = message.role === "user";

  return (
    <div className={`message message--${message.role}`}>
      <div className="message-avatar">
        {isUser ? "You" : "DX"}
      </div>
      <div className="message-content">
        {isUser ? (
          // User messages: plain text
          <p>{message.content}</p>
        ) : (
          // Assistant messages: full markdown rendering
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {message.content}
          </ReactMarkdown>
        )}
        {/* Show route badge for assistant messages */}
        {!isUser && message.route && (
          <span className="message-route">{message.route}</span>
        )}
      </div>
    </div>
  );
}
