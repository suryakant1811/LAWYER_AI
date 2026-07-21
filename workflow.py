from langgraph.graph import START, END, StateGraph
from nodes.intent_node import get_intent_node
from state.state import ConversationState

graph = StateGraph(ConversationState)

graph.add_node("Intent", get_intent_node)


graph.add_edge(START, "Intent")
graph.add_edge("Intent", END)

workflow = graph.compile()
