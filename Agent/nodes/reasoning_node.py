from model import get_llm
from prompts.reasoning_prompt import get_reasoning_prompt
from state.state import ConversationState
llm = get_llm()

def get_reasoning_node(state: ConversationState):
    print("We are on Reasoning Node")
    response = llm.invoke(get_reasoning_prompt(state))
    state['reasoning'] = response.content
    return state