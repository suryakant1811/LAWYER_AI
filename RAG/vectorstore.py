from langchain_chroma import Chroma
from .embeddings import get_embeddings

def create_vector_db(chunks):
    embeddings = get_embeddings()
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./vector_db"
    )
    return db