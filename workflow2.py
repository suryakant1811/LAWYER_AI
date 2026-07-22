from langgraph.graph import START, END, StateGraph
from nodes.router_node import get_router_node
from state.state import ConversationState
from nodes.retriever_node import get_retriever_node
from nodes.reasoning_node import get_reasoning_node
from nodes.planner_node import get_planner_node
from nodes.rights_node import get_rights_node
from nodes.complaint_node import get_complain_node

graph = StateGraph(ConversationState)

graph.add_node("Router", get_router_node)
graph.add_node("Retriever", get_retriever_node)
graph.add_node("Reasoning", get_reasoning_node)
graph.add_node("Planner", get_planner_node)
graph.add_node("Rights", get_rights_node)
graph.add_node("Complain", get_complain_node)

graph.add_edge(START, "Router")
graph.add_edge("Router", "Retriever")
graph.add_edge("Retriever", "Reasoning")
graph.add_edge("Reasoning", "Planner")
graph.add_edge("Planner","Rights")
graph.add_edge("Rights","Complain")
graph.add_edge("Complain", END)

workflow2 = graph.compile()
