// ============================================================================
// TypingIndicator Component
// ============================================================================
// Animated three-dot indicator shown while waiting for the backend response.
// ============================================================================

export default function TypingIndicator() {
  return (
    <div className="typing-indicator">
      <div className="message-avatar" style={{
        background: "var(--bg-tertiary)",
        border: "1px solid var(--border-medium)",
        color: "var(--accent-primary)",
        width: 32, height: 32, borderRadius: "50%",
        display: "flex", alignItems: "center", justifyContent: "center",
        fontSize: "0.8rem", fontWeight: 600, flexShrink: 0
      }}>
        DX
      </div>
      <div className="typing-dots">
        <div className="typing-dot" />
        <div className="typing-dot" />
        <div className="typing-dot" />
      </div>
    </div>
  );
}
