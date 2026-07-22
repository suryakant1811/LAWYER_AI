from langgraph.graph import START, END, StateGraph
from nodes.router_node import get_router_node
from state.state import ConversationState
from nodes.question_node import get_question_node
from nodes.retriever_node import get_retriever_node
from nodes.reasoning_node import get_reasoning_node

graph = StateGraph(ConversationState)

graph.add_node("Router", get_router_node)
graph.add_node("Retriever", get_retriever_node)
graph.add_node("Reasoning", get_reasoning_node)

graph.add_edge(START, "Router")
graph.add_edge("Router", "Retriever")
graph.add_edge("Retriever", "Reasoning")
graph.add_edge("Reasoning", END)

workflow2 = graph.compile()
