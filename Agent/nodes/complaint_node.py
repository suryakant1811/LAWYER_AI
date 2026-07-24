from model import get_llm
from prompts.complaint_prompt import get_complaint_prompt
from state.state import ConversationState

llm = get_llm()

def get_complain_node(state: ConversationState):
    print("We are on complain Node")
    response = llm.invoke(get_complaint_prompt(state))
    state['complaint'] = response.content
    return state