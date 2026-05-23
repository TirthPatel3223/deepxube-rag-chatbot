# ============================================================================
# DeepXube RAG Chatbot - FAQ Ingestion
# ============================================================================
# Loads FAQ entries from a JSON file and stores them in the ChromaDB
# 'faq' collection. Currently empty — the code is structured so that
# populating faq_seed.json with entries will automatically work.
#
# Expected JSON format:
#   [
#     {
#       "question": "What is DeepCubeA?",
#       "answer": "DeepCubeA is a deep learning algorithm...",
#       "sources": ["paper:Agostinelli2019", "code:deepxube.base.domain"]
#     },
#     ...
#   ]
#
# Run:
#   python -m app.ingestion.ingest_faq
# ============================================================================

import asyncio
import json
import logging
from pathlib import Path
from app.config import settings
from app.services.embedding import embedding_service
from app.services.vectordb import vectordb_service, COLLECTION_FAQ

logger = logging.getLogger(__name__)

# Path to the FAQ seed file (relative to backend/)
FAQ_SEED_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "faq_seed.json"


async def ingest_faq(clear_first: bool = False) -> dict:
    """
    Ingest FAQ entries from faq_seed.json into ChromaDB.

    Each FAQ entry's QUESTION is embedded (not the answer). This way,
    when a user asks a similar question, we match against the cached
    question and return the paired answer.

    Args:
        clear_first: If True, clear the collection before ingesting.

    Returns:
        Summary dict with counts and any errors.
    """
    if clear_first:
        vectordb_service.clear_collection(COLLECTION_FAQ)

    # Check if the seed file exists
    if not FAQ_SEED_PATH.exists():
        # Create an empty seed file as a template
        FAQ_SEED_PATH.parent.mkdir(parents=True, exist_ok=True)
        FAQ_SEED_PATH.write_text("[]", encoding="utf-8")
        logger.info(f"Created empty FAQ seed file: {FAQ_SEED_PATH}")
        return {
            "status": "success",
            "message": "FAQ seed file created (empty). Populate it with entries.",
            "count": 0,
        }

    # Load entries
    try:
        with open(FAQ_SEED_PATH, "r", encoding="utf-8") as f:
            entries = json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in FAQ seed file: {e}")
        return {"status": "error", "message": f"Invalid JSON: {e}"}

    if not entries:
        logger.info("FAQ seed file is empty — nothing to ingest")
        return {"status": "success", "message": "No entries to ingest", "count": 0}

    logger.info(f"Ingesting {len(entries)} FAQ entries")

    # Embed the questions (not the answers)
    questions = [entry["question"] for entry in entries]
    embeddings = await embedding_service.embed_batch(questions)

    # Store with the answer in metadata (the document is the question,
    # but the metadata contains the cached answer to return)
    documents = questions
    metadatas = [
        {
            "answer": entry["answer"],
            "sources": json.dumps(entry.get("sources", [])),
        }
        for entry in entries
    ]
    ids = [f"faq_{i}" for i in range(len(entries))]

    vectordb_service.add(
        COLLECTION_FAQ,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )

    result = {
        "status": "success",
        "count": len(entries),
    }
    logger.info(f"FAQ ingestion complete: {result}")
    return result


# ── CLI entry point ─────────────────────────────────────────────────────
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    result = asyncio.run(ingest_faq(clear_first=True))
    print(f"\nIngestion result: {result}")
