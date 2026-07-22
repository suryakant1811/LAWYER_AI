from langgraph.graph import START, END, StateGraph
from nodes.router_node import get_router_node
from state.state import ConversationState
from nodes.question_node import get_question_node

graph = StateGraph(ConversationState)

graph.add_node("Router", get_router_node)

graph.add_edge(START, "Router")

graph.add_edge("Router", END)

workflow2 = graph.compile()
