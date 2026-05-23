# ============================================================================
# DeepXube RAG Chatbot - Rate Limiter
# ============================================================================
# IP-based rate limiting using slowapi.
# Protects the LLM API from abuse since every non-FAQ query costs money.
#
# Default: 10 requests per minute per IP address.
# Configurable via RATE_LIMIT in .env.
# ============================================================================

from slowapi import Limiter
from slowapi.util import get_remote_address
from app.config import settings

# Create the limiter instance
# Uses IP address as the key for rate limiting
limiter = Limiter(key_func=get_remote_address)
