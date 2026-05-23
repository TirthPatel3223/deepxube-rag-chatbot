# ============================================================================
# DeepXube RAG Chatbot - Session Manager
# ============================================================================
# In-memory session storage for development.
#
# Each session tracks:
#   - Conversation history (last 2 turns + rolling summary)
#   - Domain guide flow state (which stage the user is in)
#   - User's domain guide choices (state representation, actions, etc.)
#
# Sessions expire after SESSION_TIMEOUT_MINUTES of inactivity.
# For production, replace with Redis or SQLite.
#
# Usage:
#   from app.session.manager import session_manager
#   session = session_manager.get_or_create("session-123")
#   session_manager.update("session-123", rolling_summary="...")
# ============================================================================

import logging
import uuid
from datetime import datetime, timedelta
from typing import Optional
from app.config import settings

logger = logging.getLogger(__name__)


class SessionData:
    """
    Data stored for a single user session.

    Attributes:
        session_id: Unique identifier for this session.
        rolling_summary: Compressed summary of conversation history (≤200 tokens).
        conversation_history: Last 2 turns as list of {role, content} dicts.
        domain_guide_stage: Current stage in the domain guide flow.
            Values: "none", "overview", "template", "examples", "training"
        domain_guide_user_choices: Accumulated user decisions during domain guide.
            Keys: "representation", "action_space", "reversible", "template"
        created_at: When the session was created.
        last_active: When the session was last accessed.
    """

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.rolling_summary = ""
        self.conversation_history: list[dict] = []
        self.domain_guide_stage = "none"
        self.domain_guide_user_choices: dict = {}
        self.created_at = datetime.utcnow()
        self.last_active = datetime.utcnow()

    def is_in_domain_guide(self) -> bool:
        """Check if the user is currently in a domain guide flow."""
        return self.domain_guide_stage != "none"

    def add_turn(self, user_message: str, assistant_response: str) -> None:
        """
        Add a conversation turn and keep only the last 2 turns.

        Args:
            user_message: What the user said.
            assistant_response: What the assistant replied.
        """
        self.conversation_history.append(
            {"role": "user", "content": user_message}
        )
        self.conversation_history.append(
            {"role": "assistant", "content": assistant_response}
        )
        # Keep only last 2 turns (4 messages: 2 user + 2 assistant)
        if len(self.conversation_history) > 4:
            self.conversation_history = self.conversation_history[-4:]

        self.last_active = datetime.utcnow()

    def reset_domain_guide(self) -> None:
        """Clear domain guide state (e.g., when the user finishes or abandons)."""
        self.domain_guide_stage = "none"
        self.domain_guide_user_choices = {}

    def to_dict(self) -> dict:
        """Serialize session data for API responses or debugging."""
        return {
            "session_id": self.session_id,
            "rolling_summary": self.rolling_summary,
            "conversation_history": self.conversation_history,
            "domain_guide_stage": self.domain_guide_stage,
            "domain_guide_user_choices": self.domain_guide_user_choices,
            "created_at": self.created_at.isoformat(),
            "last_active": self.last_active.isoformat(),
        }


class SessionManager:
    """
    In-memory session storage.

    Stores session data in a dict keyed by session_id.
    Sessions expire after SESSION_TIMEOUT_MINUTES of inactivity.

    Thread safety: This is sufficient for single-process development.
    For production with multiple workers, use Redis.
    """

    def __init__(self):
        self._sessions: dict[str, SessionData] = {}
        self._timeout = timedelta(minutes=settings.SESSION_TIMEOUT_MINUTES)
        logger.info(
            f"SessionManager initialized. Timeout: {settings.SESSION_TIMEOUT_MINUTES} min"
        )

    def get_or_create(self, session_id: Optional[str] = None) -> SessionData:
        """
        Get an existing session or create a new one.

        If session_id is None or not found, a new session is created.
        Expired sessions are treated as not found.

        Args:
            session_id: Optional session ID to look up.

        Returns:
            The SessionData object (existing or newly created).
        """
        # Clean up expired sessions periodically
        self._cleanup_expired()

        if session_id and session_id in self._sessions:
            session = self._sessions[session_id]
            # Check expiration
            if datetime.utcnow() - session.last_active > self._timeout:
                logger.info(f"Session {session_id} expired, creating new one")
                del self._sessions[session_id]
            else:
                session.last_active = datetime.utcnow()
                return session

        # Create new session
        new_id = session_id or str(uuid.uuid4())
        session = SessionData(new_id)
        self._sessions[new_id] = session
        logger.info(f"Created new session: {new_id}")
        return session

    def update_summary(self, session_id: str, summary: str) -> None:
        """
        Update the rolling summary for a session.

        Args:
            session_id: The session to update.
            summary: The new rolling summary text.
        """
        if session_id in self._sessions:
            self._sessions[session_id].rolling_summary = summary
            self._sessions[session_id].last_active = datetime.utcnow()

    def update_domain_guide(
        self,
        session_id: str,
        stage: str,
        choices: Optional[dict] = None,
    ) -> None:
        """
        Update the domain guide state for a session.

        Args:
            session_id: The session to update.
            stage: The new domain guide stage.
            choices: Updated user choices dict (merged with existing).
        """
        if session_id in self._sessions:
            session = self._sessions[session_id]
            session.domain_guide_stage = stage
            if choices:
                session.domain_guide_user_choices.update(choices)
            session.last_active = datetime.utcnow()

    def get_active_session_count(self) -> int:
        """Return the number of active (non-expired) sessions."""
        self._cleanup_expired()
        return len(self._sessions)

    def _cleanup_expired(self) -> None:
        """Remove sessions that have been inactive longer than the timeout."""
        now = datetime.utcnow()
        expired = [
            sid
            for sid, session in self._sessions.items()
            if now - session.last_active > self._timeout
        ]
        for sid in expired:
            del self._sessions[sid]
        if expired:
            logger.info(f"Cleaned up {len(expired)} expired sessions")


# ── Singleton instance ──────────────────────────────────────────────────
session_manager = SessionManager()
