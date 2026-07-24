from model import get_llm
from prompts.rights_prompt import get_rights_prompt
from state.state import ConversationState

llm = get_llm()

def get_rights_node(state: ConversationState):
    print("We are on Rights Node")
    response = llm.invoke(get_rights_prompt(state))
    state['rights'] = response.content
    return state