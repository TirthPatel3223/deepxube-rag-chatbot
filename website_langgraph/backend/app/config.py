# ============================================================================
# DeepXube RAG Chatbot - Configuration
# ============================================================================
# Central configuration loaded from environment variables (.env file).
# All configurable values live here — no magic strings in other modules.
#
# Usage:
#   from app.config import settings
#   print(settings.OPENAI_API_KEY)
# ============================================================================

import os
from pathlib import Path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file from the backend/ directory
_backend_dir = Path(__file__).resolve().parent.parent
load_dotenv(_backend_dir / ".env")


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.

    All paths are resolved relative to the backend/ directory.
    Thresholds and limits have sensible defaults that can be overridden.
    """

    # ── API Keys ────────────────────────────────────────────────────────
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""

    # ── Embedding Model ─────────────────────────────────────────────────
    # OpenAI only — no fallback. Produces 1536-dimensional vectors.
    EMBEDDING_MODEL: str = "text-embedding-3-small"

    # ── LLM Models ──────────────────────────────────────────────────────
    # Primary: OpenAI gpt-4o-mini
    # Fallback: Anthropic Claude Haiku (used if OpenAI call fails)
    LLM_MODEL_PRIMARY: str = "gpt-4o-mini"
    LLM_MODEL_FALLBACK: str = "claude-haiku-4-5-20241022"

    # ── Paths (resolved relative to backend/ directory) ─────────────────
    CODE_DOCS_PATH: str = "../../deepxube-main/docs"
    PAPERS_PATH: str = "../../Research_Papers"
    CONTEXT_FILES_PATH: str = "../../deepxube-main/docs/context_files"
    GRAPH_JSON_PATH: str = "../../deepxube-main/docs/graph.json"
    CHROMA_PERSIST_DIR: str = "./data/chromadb"

    # ── Similarity Thresholds ───────────────────────────────────────────
    # FAQ lookup: >= HIGH → return cached answer (zero LLM cost)
    FAQ_SIM_THRESHOLD_HIGH: float = 0.92
    # FAQ lookup: between BORDERLINE and HIGH → regenerate with FAQ context
    FAQ_SIM_THRESHOLD_BORDERLINE: float = 0.78
    # Scope guard: below this → out-of-scope, polite refusal
    SCOPE_GUARD_THRESHOLD: float = 0.30

    # ── Rate Limiting ───────────────────────────────────────────────────
    RATE_LIMIT: str = "10/minute"

    # ── Memory ──────────────────────────────────────────────────────────
    ROLLING_SUMMARY_MAX_TOKENS: int = 200
    SESSION_TIMEOUT_MINUTES: int = 30

    # ── Server ──────────────────────────────────────────────────────────
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # ── Retrieval ───────────────────────────────────────────────────────
    CODE_RETRIEVE_TOP_K: int = 5
    PAPER_RETRIEVE_TOP_K: int = 5

    # ── Paper Chunking ──────────────────────────────────────────────────
    PAPER_CHUNK_TOKENS: int = 500
    PAPER_CHUNK_OVERLAP_TOKENS: int = 100

    def resolve_path(self, relative_path: str) -> Path:
        """Resolve a relative path against the backend/ directory."""
        return (_backend_dir / relative_path).resolve()

    @property
    def code_docs_abs(self) -> Path:
        return self.resolve_path(self.CODE_DOCS_PATH)

    @property
    def papers_abs(self) -> Path:
        return self.resolve_path(self.PAPERS_PATH)

    @property
    def context_files_abs(self) -> Path:
        return self.resolve_path(self.CONTEXT_FILES_PATH)

    @property
    def graph_json_abs(self) -> Path:
        return self.resolve_path(self.GRAPH_JSON_PATH)

    @property
    def chroma_persist_abs(self) -> Path:
        return self.resolve_path(self.CHROMA_PERSIST_DIR)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# ── Singleton instance ──────────────────────────────────────────────────
# Import this everywhere: from app.config import settings
settings = Settings()
