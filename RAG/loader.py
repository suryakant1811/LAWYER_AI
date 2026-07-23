# from langchain_community.document_loaders import DirectoryLoader, TextLoader 
# # imports a classes that can find and load multiple files from a folder using DirectoryLoader then textLoader that can read the contents of a single text/markdown file.

# def load_documents(root_folder):

#     loader = DirectoryLoader(
#         root_folder, # path where to  find
#         glob="**/*.md", # all files having .md 
#         loader_cls=TextLoader # to read 
#     )

#     documents = loader.load() #  Read all matching files and convert them into LangChain Document objects.

#     return documents

import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)


def load_documents(root_folder):

    documents = []

    for root, _, files in os.walk(root_folder):

        for file in files:

            path = os.path.join(root, file)

            extension = file.split(".")[-1].lower()

            if extension == "pdf":

                loader = PyPDFLoader(path)

            elif extension in ["md", "txt"]:

                loader = TextLoader(path, encoding="utf-8")

            else:

                continue

            docs = loader.load()

            domain = os.path.basename(root)

            for doc in docs:

                doc.metadata["domain"] = domain
                doc.metadata["filename"] = file

            documents.extend(docs)

    return documents