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
    intent_and_domain : str = ""

    # ===== Extracted Information =====
    # entities: dict[str, Any] = Field(default_factory=dict)
    follow_up_questions: list[str]
    # ===== Conversation =====
    additinal_information: list[str] = Field(default_factory=list)

    user_answers: str = ""

    route: str = ""

    retrieved_context: str = ""

    reasoning: str = ""

    action_plan: str = ""

    final_response: str = ""