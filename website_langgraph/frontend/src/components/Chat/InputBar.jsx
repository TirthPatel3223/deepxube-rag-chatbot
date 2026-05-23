// ============================================================================
// InputBar Component
// ============================================================================
// Chat input with auto-resizing textarea and send button.
// Sends on Enter (Shift+Enter for newline).
// ============================================================================

import { useState, useRef } from "react";

export default function InputBar({ onSend, disabled }) {
  const [text, setText] = useState("");
  const textareaRef = useRef(null);

  const handleSubmit = () => {
    const trimmed = text.trim();
    if (!trimmed || disabled) return;
    onSend(trimmed);
    setText("");
    // Reset textarea height
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  const handleInput = (e) => {
    setText(e.target.value);
    // Auto-resize textarea
    const el = e.target;
    el.style.height = "auto";
    el.style.height = Math.min(el.scrollHeight, 120) + "px";
  };

  return (
    <div className="input-bar">
      <div className="input-wrapper">
        <textarea
          ref={textareaRef}
          value={text}
          onChange={handleInput}
          onKeyDown={handleKeyDown}
          placeholder="Ask about DeepXube..."
          rows={1}
          disabled={disabled}
          id="chat-input"
        />
        <button
          className="send-button"
          onClick={handleSubmit}
          disabled={!text.trim() || disabled}
          aria-label="Send message"
          id="send-button"
        >
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={2}>
            <path d="M22 2L11 13" />
            <path d="M22 2L15 22L11 13L2 9L22 2Z" />
          </svg>
        </button>
      </div>
    </div>
  );
}
