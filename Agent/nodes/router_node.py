from state.state import ConversationState
from model import get_llm
from prompts.router_prompt import get_router_prompt

llm = get_llm()

def get_router_node(state: ConversationState):
    response = llm.invoke(get_router_prompt(state))
    state["route"] = response.content
    return state
