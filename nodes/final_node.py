from model import get_llm
from prompts.final_prompt import get_final_prompt

llm = get_llm()

def get_final_node(state):

    print("We are on Final Node")

    response = llm.invoke(get_final_prompt(state))

    state["final_response"] = response.content

    return state