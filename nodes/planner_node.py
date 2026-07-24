from model import get_llm
from prompts.planner_prompt import get_planner_prompt
from state.state import ConversationState

llm = get_llm()

def get_planner_node(state: ConversationState):
    print("We are on Planner Node")
    response = llm.invoke(get_planner_prompt(state))
    state["action_plan"] = response.content
    return state