from langgraph.graph import START, END, StateGraph
from nodes.intent_node import get_intent_node
from state.state import ConversationState
from nodes.question_node import get_question_node
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()
graph = StateGraph(ConversationState)

graph.add_node("Intent", get_intent_node)
graph.add_node("question", get_question_node)

graph.add_edge(START, "Intent")
graph.add_edge("Intent", "question")
graph.add_edge("question", END)

config = {
    "configurable": {
        "thread_id": "user-1"
    }
}

workflow = graph.compile(
    checkpointer=memory
)
