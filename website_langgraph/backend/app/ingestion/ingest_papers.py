# ============================================================================
# DeepXube RAG Chatbot - Research Paper Ingestion
# ============================================================================
# Reads PDF research papers, chunks them into fixed-size token windows,
# embeds each chunk, and stores in the ChromaDB 'papers' collection.
#
# Chunking strategy: fixed token windows (500 tokens, 100 overlap).
# Each chunk gets metadata: paper_id, paper_title, chunk_index, page_numbers.
#
# Run:
#   python -m app.ingestion.ingest_papers
# ============================================================================

import asyncio
import logging
from pathlib import Path
import fitz  # PyMuPDF
import tiktoken
from app.config import settings
from app.services.embedding import embedding_service
from app.services.vectordb import vectordb_service, COLLECTION_PAPERS

logger = logging.getLogger(__name__)

# Tokenizer for counting tokens (matches OpenAI's tokenizer)
_tokenizer = tiktoken.get_encoding("cl100k_base")


def _extract_text_from_pdf(pdf_path: Path) -> list[dict]:
    """
    Extract text from a PDF, page by page.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of dicts: [{page_num: int, text: str}, ...]
    """
    doc = fitz.open(str(pdf_path))
    pages = []
    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        if text.strip():
            pages.append({"page_num": page_num + 1, "text": text})
    doc.close()
    return pages


def _chunk_text(
    pages: list[dict],
    chunk_tokens: int = 500,
    overlap_tokens: int = 100,
) -> list[dict]:
    """
    Chunk page text into fixed-size token windows with overlap.

    The text from all pages is concatenated, then split into chunks of
    `chunk_tokens` tokens with `overlap_tokens` overlap between consecutive
    chunks. Each chunk records which pages it spans.

    Args:
        pages: List of {page_num, text} dicts from _extract_text_from_pdf.
        chunk_tokens: Target tokens per chunk.
        overlap_tokens: Overlap between consecutive chunks.

    Returns:
        List of {text, page_numbers, chunk_index} dicts.
    """
    # Build a list of (token, page_num) pairs
    token_page_pairs = []
    for page in pages:
        tokens = _tokenizer.encode(page["text"])
        for token in tokens:
            token_page_pairs.append((token, page["page_num"]))

    if not token_page_pairs:
        return []

    # Create chunks with overlap
    chunks = []
    chunk_index = 0
    start = 0
    step = chunk_tokens - overlap_tokens

    while start < len(token_page_pairs):
        end = min(start + chunk_tokens, len(token_page_pairs))
        chunk_pairs = token_page_pairs[start:end]

        # Decode tokens back to text
        chunk_token_ids = [pair[0] for pair in chunk_pairs]
        chunk_text = _tokenizer.decode(chunk_token_ids)

        # Track which pages this chunk spans
        page_nums = sorted(set(pair[1] for pair in chunk_pairs))

        chunks.append({
            "text": chunk_text,
            "page_numbers": page_nums,
            "chunk_index": chunk_index,
        })

        chunk_index += 1
        start += step

    return chunks


def _derive_paper_title(pdf_path: Path, first_page_text: str) -> str:
    """
    Try to extract the paper title from the first page text.

    Heuristic: the title is usually the first non-empty line that's
    long enough to be a title. Falls back to the filename.

    Args:
        pdf_path: Path to the PDF (fallback source for title).
        first_page_text: Text of the first page.

    Returns:
        Best-guess paper title string.
    """
    lines = first_page_text.strip().split("\n")
    for line in lines:
        line = line.strip()
        # Skip very short lines (page numbers, headers) and URLs
        if len(line) > 20 and not line.startswith("http"):
            return line[:200]  # Cap length
    # Fallback: use filename without extension
    return pdf_path.stem.replace("_", " ")


async def ingest_papers(clear_first: bool = False) -> dict:
    """
    Ingest all research papers from the papers directory.

    Args:
        clear_first: If True, clear the collection before ingesting.

    Returns:
        Summary dict with counts and any errors.
    """
    papers_path = settings.papers_abs
    chunk_tokens = settings.PAPER_CHUNK_TOKENS
    overlap_tokens = settings.PAPER_CHUNK_OVERLAP_TOKENS

    if not papers_path.exists():
        logger.error(f"Papers path not found: {papers_path}")
        return {"status": "error", "message": f"Path not found: {papers_path}"}

    if clear_first:
        vectordb_service.clear_collection(COLLECTION_PAPERS)

    # Find all PDFs
    pdf_files = list(papers_path.glob("*.pdf"))
    logger.info(f"Found {len(pdf_files)} PDFs to ingest")

    if not pdf_files:
        return {"status": "warning", "message": "No PDF files found", "count": 0}

    total_chunks = 0
    errors = []

    for pdf_path in pdf_files:
        try:
            logger.info(f"Processing: {pdf_path.name}")

            # 1. Extract text from PDF
            pages = _extract_text_from_pdf(pdf_path)
            if not pages:
                logger.warning(f"No text extracted from {pdf_path.name}")
                continue

            # 2. Derive paper metadata
            paper_id = pdf_path.stem
            paper_title = _derive_paper_title(pdf_path, pages[0]["text"])
            logger.info(f"  Title: {paper_title[:60]}...")

            # 3. Chunk the text
            chunks = _chunk_text(pages, chunk_tokens, overlap_tokens)
            logger.info(f"  Chunks: {len(chunks)}")

            if not chunks:
                continue

            # 4. Embed and store chunks
            documents = [chunk["text"] for chunk in chunks]
            embeddings = await embedding_service.embed_batch(documents)

            metadatas = [
                {
                    "paper_id": paper_id,
                    "paper_title": paper_title,
                    "chunk_index": chunk["chunk_index"],
                    "page_numbers": str(chunk["page_numbers"]),
                    "total_chunks": len(chunks),
                }
                for chunk in chunks
            ]
            ids = [f"{paper_id}_chunk_{chunk['chunk_index']}" for chunk in chunks]

            vectordb_service.add(
                COLLECTION_PAPERS,
                documents=documents,
                embeddings=embeddings,
                metadatas=metadatas,
                ids=ids,
            )
            total_chunks += len(chunks)

        except Exception as e:
            logger.error(f"Failed to process {pdf_path.name}: {e}")
            errors.append({"file": pdf_path.name, "error": str(e)})

    result = {
        "status": "success",
        "total_pdfs": len(pdf_files),
        "total_chunks": total_chunks,
        "errors": len(errors),
        "error_details": errors,
    }
    logger.info(f"Paper ingestion complete: {result}")
    return result


# ── CLI entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = asyncio.run(ingest_papers(clear_first=True))
    print(f"\nIngestion result: {result}")
