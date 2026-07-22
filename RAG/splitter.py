from langchain_text_splitters import RecursiveCharacterTextSplitter
# breaks large documents into smaller chunks.

def split_documents(documents):
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 150
    )

    chunk = splitter.split_documents(documents)

    return chunk