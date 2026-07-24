from .loader import load_documents
from .splitter import split_documents
from .vectorstore import create_vector_db

print("Loading documents...")

documents = load_documents("documents")

print(f"Loaded {len(documents)} documents")

print("Splitting documents...")

chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks")

print("Building Vector Database...")

create_vector_db(chunks)

print("Vector Database Created Successfully")