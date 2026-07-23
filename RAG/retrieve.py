# from langchain_chroma import Chroma

# from .embeddings import get_embeddings


# def retrieve(query):

#     db = Chroma(
#         persist_directory="./vector_db",
#         embedding_function=get_embeddings()
#     )

#     # docs = db.similarity_search(
#     #     query,
#     #     k=5
#     # )

#     docs =  db.as_retriever(
#         search_kwargs={
#             "k": 5
#         }
#     )

#     return docs

from langchain_chroma import Chroma
from .embeddings import get_embeddings


def retrieve(query):

    db = Chroma(
        persist_directory="./vector_db",
        embedding_function=get_embeddings()
    )

    retriever = db.as_retriever(
        search_kwargs={
            "k":2
        }
    )

    docs = retriever.invoke(query)

    return docs