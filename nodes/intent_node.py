from model import get_llm
from prompts.intent_prompt import get_intent_prompt
from state.state import ConversationState

llm = get_llm()

def get_intent_node(state: ConversationState):
    print("we are on intent node")
    user_input = state["user_query"]
    prompt = get_intent_prompt(user_input)
    response = llm.invoke(prompt)
    state["intent"] = response.content
    print("Exiting intent node")
    return state
