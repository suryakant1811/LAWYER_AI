from model import get_llm

from .prompt import get_markdown_prompt

llm = get_llm()


def generate_markdown(text):

    response = llm.invoke(

        get_markdown_prompt(text)

    )

    return response.content