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
from RAG.embeddings import get_embeddings


def get_retriever(query, domain):
    vector_db = Chroma(
        persist_directory="vector_db",
        embedding_function=get_embeddings()
    )

    retriever = vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 6,
            "fetch_k": 20
        }
    )

    docs = retriever.invoke(query)

    # Build Context
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    # Collect unique sources
    sources = []

    for doc in docs:
        source = {
            "file": doc.metadata.get("filename"),
            "domain": doc.metadata.get("domain"),
            "page": doc.metadata.get("page")
        }

        if source not in sources:
            sources.append(source)

    return {
        "context": context,
        "sources": sources
    }