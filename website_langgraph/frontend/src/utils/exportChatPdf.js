// ============================================================================
// Export Chat as PDF
// ============================================================================
// Uses jsPDF to generate a styled PDF of the full chat conversation.
// Includes branded header, timestamped messages, and automatic pagination.
// ============================================================================

import { jsPDF } from "jspdf";

/**
 * Strips markdown formatting to produce clean plain text for the PDF.
 */
function stripMarkdown(text) {
  return (
    text
      // Remove code blocks (``` ... ```)
      .replace(/```[\s\S]*?```/g, (match) => {
        const inner = match.replace(/```\w*\n?/g, "").replace(/```/g, "");
        return inner.trim();
      })
      // Remove inline code
      .replace(/`([^`]+)`/g, "$1")
      // Remove bold / italic
      .replace(/\*\*(.+?)\*\*/g, "$1")
      .replace(/\*(.+?)\*/g, "$1")
      .replace(/__(.+?)__/g, "$1")
      .replace(/_(.+?)_/g, "$1")
      // Remove headings markers
      .replace(/^#{1,6}\s+/gm, "")
      // Remove link syntax, keep text
      .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
      // Remove images
      .replace(/!\[([^\]]*)\]\([^)]+\)/g, "$1")
      // Remove horizontal rules
      .replace(/^---+$/gm, "")
      // Collapse multiple blank lines
      .replace(/\n{3,}/g, "\n\n")
      .trim()
  );
}

/**
 * Word-wrap a line to fit within maxWidth (in PDF units).
 * Returns an array of wrapped lines.
 */
function wrapLine(doc, text, maxWidth) {
  if (!text) return [""];
  const lines = doc.splitTextToSize(text, maxWidth);
  return lines;
}

/**
 * Export the current chat messages as a PDF and trigger a browser download.
 * @param {Array<{role: string, content: string, route?: string}>} messages
 */
export default function exportChatPdf(messages) {
  const doc = new jsPDF({
    orientation: "portrait",
    unit: "mm",
    format: "a4",
  });

  const pageWidth = doc.internal.pageSize.getWidth(); // 210
  const pageHeight = doc.internal.pageSize.getHeight(); // 297
  const margin = 18;
  const contentWidth = pageWidth - margin * 2;
  const lineHeight = 5.5;
  const bottomMargin = 25; // space reserved for footer

  let y = margin;

  // ── Colours ──────────────────────────────────────────────────────────
  const colors = {
    headerBg: [99, 102, 241],       // Indigo-500
    userAccent: [99, 102, 241],      // Indigo-500
    assistantAccent: [139, 92, 246], // Purple-500
    textDark: [30, 30, 40],
    textMuted: [120, 120, 135],
    bg: [250, 250, 252],
    divider: [220, 220, 230],
  };

  // ── Helper: add page footer ─────────────────────────────────────────
  const addFooter = () => {
    const pageNum = doc.getNumberOfPages();
    doc.setFontSize(8);
    doc.setTextColor(...colors.textMuted);
    doc.text(
      `Page ${pageNum}`,
      pageWidth / 2,
      pageHeight - 10,
      { align: "center" }
    );
    doc.text(
      "DeepXube RAG Assistant",
      margin,
      pageHeight - 10
    );
  };

  // ── Helper: check if we need a new page ─────────────────────────────
  const ensureSpace = (needed) => {
    if (y + needed > pageHeight - bottomMargin) {
      addFooter();
      doc.addPage();
      y = margin;
    }
  };

  // ── Header ──────────────────────────────────────────────────────────
  // Gradient header bar
  doc.setFillColor(...colors.headerBg);
  doc.rect(0, 0, pageWidth, 28, "F");

  // Title text
  doc.setFont("helvetica", "bold");
  doc.setFontSize(18);
  doc.setTextColor(255, 255, 255);
  doc.text("DeepXube Chat History", margin, 13);

  // Subtitle — date
  doc.setFont("helvetica", "normal");
  doc.setFontSize(10);
  doc.setTextColor(220, 220, 255);
  const now = new Date();
  const dateStr = now.toLocaleDateString("en-US", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });
  const timeStr = now.toLocaleTimeString("en-US", {
    hour: "2-digit",
    minute: "2-digit",
  });
  doc.text(`Exported on ${dateStr} at ${timeStr}`, margin, 21);

  y = 36;

  // ── Conversation stats line ─────────────────────────────────────────
  const userCount = messages.filter((m) => m.role === "user").length;
  const assistantCount = messages.filter((m) => m.role === "assistant").length;
  doc.setFontSize(9);
  doc.setTextColor(...colors.textMuted);
  doc.text(
    `${userCount} user message${userCount !== 1 ? "s" : ""} · ${assistantCount} assistant response${assistantCount !== 1 ? "s" : ""}`,
    margin,
    y
  );
  y += 8;

  // ── Divider ──────────────────────────────────────────────────────────
  doc.setDrawColor(...colors.divider);
  doc.setLineWidth(0.3);
  doc.line(margin, y, pageWidth - margin, y);
  y += 6;

  // ── Messages ────────────────────────────────────────────────────────
  messages.forEach((msg, index) => {
    const isUser = msg.role === "user";
    const label = isUser ? "You" : "DeepXube Assistant";
    const accentColor = isUser ? colors.userAccent : colors.assistantAccent;
    const cleanContent = stripMarkdown(msg.content);

    // Pre-compute wrapped lines so we know the block height
    const wrappedLines = wrapLine(doc, cleanContent, contentWidth - 8);
    const blockHeight = 8 + wrappedLines.length * lineHeight + 4;

    ensureSpace(blockHeight);

    // Accent bar (left side)
    doc.setFillColor(...accentColor);
    doc.roundedRect(margin, y, 2.5, Math.min(blockHeight - 2, 14), 1, 1, "F");

    // Role label
    doc.setFont("helvetica", "bold");
    doc.setFontSize(10);
    doc.setTextColor(...accentColor);
    doc.text(label, margin + 6, y + 4.5);

    // Route badge (if present on assistant messages)
    if (!isUser && msg.route && msg.route !== "error") {
      const labelWidth = doc.getTextWidth(label);
      doc.setFontSize(7);
      doc.setTextColor(...colors.textMuted);
      doc.text(`[${msg.route}]`, margin + 6 + labelWidth + 3, y + 4.5);
    }

    y += 8;

    // Message body
    doc.setFont("helvetica", "normal");
    doc.setFontSize(9.5);
    doc.setTextColor(...colors.textDark);

    wrappedLines.forEach((line) => {
      ensureSpace(lineHeight);
      doc.text(line, margin + 6, y);
      y += lineHeight;
    });

    y += 4;

    // Subtle divider between messages (except last)
    if (index < messages.length - 1) {
      ensureSpace(4);
      doc.setDrawColor(...colors.divider);
      doc.setLineWidth(0.15);
      doc.line(margin + 6, y, pageWidth - margin, y);
      y += 5;
    }
  });

  // ── Final footer ────────────────────────────────────────────────────
  addFooter();

  // ── Trigger download ────────────────────────────────────────────────
  const filename = `DeepXube_Chat_${now.toISOString().slice(0, 10)}.pdf`;
  doc.save(filename);
}
