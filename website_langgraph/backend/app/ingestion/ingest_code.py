# ============================================================================
# DeepXube RAG Chatbot - Code Documentation Ingestion
# ============================================================================
# Reads all .md function/class docs from deepxube-main/docs/functions/,
# extracts YAML frontmatter metadata, embeds the full content, and stores
# each document as one vector in the ChromaDB 'code' collection.
#
# Total: ~509 .md files across 48 module directories.
# Each file has rich YAML frontmatter (qualified_name, file, line_start,
# line_end, class, module, parameters, etc.) plus prose (docstring,
# signature, parameter table, source snippet).
#
# Run:
#   python -m app.ingestion.ingest_code
# ============================================================================

import asyncio
import logging
import yaml
from pathlib import Path
from app.config import settings
from app.services.embedding import embedding_service
from app.services.vectordb import vectordb_service, COLLECTION_CODE

logger = logging.getLogger(__name__)


def _extract_frontmatter(content: str) -> tuple[dict, str]:
    """
    Extract YAML frontmatter from a .md file.

    Files look like:
        ---
        id: "func:deepxube.domains.cube3.Cube3.is_solved"
        kind: "method"
        ...
        ---
        # Prose content...

    Args:
        content: Full .md file content.

    Returns:
        Tuple of (frontmatter_dict, prose_content).
        If no frontmatter found, returns ({}, full_content).
    """
    if not content.startswith("---"):
        return {}, content

    # Find the closing ---
    end_idx = content.find("---", 3)
    if end_idx == -1:
        return {}, content

    yaml_str = content[3:end_idx].strip()
    prose = content[end_idx + 3:].strip()

    try:
        frontmatter = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError as e:
        logger.warning(f"Failed to parse YAML frontmatter: {e}")
        frontmatter = {}

    return frontmatter, prose


def _collect_md_files(docs_path: Path) -> list[Path]:
    """
    Recursively collect all .md files from the functions/, classes/,
    and modules/ directories.

    Args:
        docs_path: Path to deepxube-main/docs/

    Returns:
        List of Path objects to .md files.
    """
    md_files = []
    for subdir in ["functions", "classes", "modules"]:
        search_dir = docs_path / subdir
        if search_dir.exists():
            md_files.extend(search_dir.rglob("*.md"))

    return md_files


async def ingest_code_docs(clear_first: bool = False) -> dict:
    """
    Ingest all code documentation .md files into ChromaDB.

    Args:
        clear_first: If True, clear the collection before ingesting.

    Returns:
        Summary dict with counts and any errors.
    """
    docs_path = settings.code_docs_abs

    if not docs_path.exists():
        logger.error(f"Code docs path not found: {docs_path}")
        return {"status": "error", "message": f"Path not found: {docs_path}"}

    if clear_first:
        vectordb_service.clear_collection(COLLECTION_CODE)

    # Collect all .md files
    md_files = _collect_md_files(docs_path)
    logger.info(f"Found {len(md_files)} .md files to ingest")

    if not md_files:
        return {"status": "warning", "message": "No .md files found", "count": 0}

    # Process in batches for efficient embedding
    batch_size = 50
    total_ingested = 0
    errors = []

    for batch_start in range(0, len(md_files), batch_size):
        batch_files = md_files[batch_start : batch_start + batch_size]

        documents = []
        metadatas = []
        ids = []

        for md_path in batch_files:
            try:
                content = md_path.read_text(encoding="utf-8")
                frontmatter, prose = _extract_frontmatter(content)

                # Use the full content (frontmatter + prose) for embedding
                # This gives the best semantic matching
                doc_text = content

                # Build metadata from frontmatter
                metadata = {
                    "qualified_name": str(frontmatter.get("qualified_name", "")),
                    "module": str(frontmatter.get("module", "")),
                    "file": str(frontmatter.get("file", "")),
                    "line_start": int(frontmatter.get("line_start", 0)),
                    "line_end": int(frontmatter.get("line_end", 0)),
                    "kind": str(frontmatter.get("kind", "")),
                    "class_name": str(frontmatter.get("class", "")),
                    "visibility": str(frontmatter.get("visibility", "")),
                }

                # Use qualified_name as ID (unique per function/class)
                doc_id = frontmatter.get("id", str(md_path.relative_to(docs_path)))

                documents.append(doc_text)
                metadatas.append(metadata)
                ids.append(str(doc_id))

            except Exception as e:
                logger.warning(f"Failed to process {md_path}: {e}")
                errors.append({"file": str(md_path), "error": str(e)})

        if documents:
            # Embed the batch
            try:
                embeddings = await embedding_service.embed_batch(documents)

                # Store in ChromaDB
                vectordb_service.add(
                    COLLECTION_CODE,
                    documents=documents,
                    embeddings=embeddings,
                    metadatas=metadatas,
                    ids=ids,
                )
                total_ingested += len(documents)
                logger.info(
                    f"Ingested batch {batch_start//batch_size + 1}: "
                    f"{len(documents)} docs (total: {total_ingested})"
                )
            except Exception as e:
                logger.error(f"Failed to embed/store batch: {e}")
                errors.append({"batch": batch_start, "error": str(e)})

    result = {
        "status": "success",
        "total_files": len(md_files),
        "ingested": total_ingested,
        "errors": len(errors),
        "error_details": errors[:10],  # Cap error details
    }
    logger.info(f"Code ingestion complete: {result}")
    return result


# ── CLI entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = asyncio.run(ingest_code_docs(clear_first=True))
    print(f"\nIngestion result: {result}")
