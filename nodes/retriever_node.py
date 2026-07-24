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

from RAG.retrieve import get_retriever


def get_retriever_node(state):

    print("We are on Retriever Node")

    result = get_retriever(
        state["user_query"],
        state["route"]
    )

    state["retrieved_context"] = result["context"]
    state["sources"] = result["sources"]

    return state