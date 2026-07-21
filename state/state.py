from typing import Any

from langgraph.graph import MessagesState
from pydantic import Field


class ConversationState(MessagesState):
    """
    Shared state for the entire workflow.

    Every node receives this state,
    updates it,
    and returns it.
    """

    # ===== User =====
    user_query: str = ""

    # ===== Understanding =====
    intent: str = ""
    domain: str = ""
    confidence: float = 0.0

    # ===== Extracted Information =====
    entities: dict[str, Any] = Field(default_factory=dict)

    # ===== Conversation =====
    missing_information: list[str] = Field(default_factory=list)

    # ===== Retrieval =====
    retrieved_documents: list[Any] = Field(default_factory=list)

    # ===== Planning =====
    action_plan: list[str] = Field(default_factory=list)

    # ===== Final Answer =====
    response: str = ""

    # ===== Metadata =====
    metadata: dict[str, Any] = Field(default_factory=dict)