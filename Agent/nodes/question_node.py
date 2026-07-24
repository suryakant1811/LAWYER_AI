from state.state import ConversationState
from model import get_llm
from prompts.question_prompt import get_question_prompt

llm = get_llm()

def get_question_node(state: ConversationState):
    print("we are on question node")
    prompt = get_question_prompt(state)
    response = llm.invoke(prompt)
    state["follow_up_questions"] = response.content
    return state
