from langchain_community.document_loaders import DirectoryLoader, TextLoader 
# imports a classes that can find and load multiple files from a folder using DirectoryLoader then textLoader that can read the contents of a single text/markdown file.

def load_documents(folder_path):

    loader = DirectoryLoader(
        folder_path, # path where to  find
        glob="**/*.md", # all files having .md 
        loader_reader=TextLoader # to read 
    )

    documents = loader.load() #  Read all matching files and convert them into LangChain Document objects.

    return documents