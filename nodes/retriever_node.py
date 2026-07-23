# from pathlib import Path

# def get_retriever_node(state):

#     print("We are on Retriever Node")
#     route = state["route"]
#     knowledge_path = Path("knowledge") / route
#     documents = []
#     for file in knowledge_path.glob("*.md"):
#         with open(file, "r", encoding="utf-8") as f:
#             documents.append(f.read())
#     state["retrieved_context"] = "\n\n".join(documents)
#     return state

from RAG.retrieve import retrieve


def get_retriever_node(state):

    print("We are on Retriever Node")

    docs = retrieve(state["user_query"])

    context = ""

    for doc in docs:

        context += doc.page_content
        context += "\n\n"

    state["retrieved_context"] = context

    return state