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
from langchain_core.documents import Document


def load_documents(folder_path):

    documents = []

    for root, _, files in os.walk(folder_path):

        for file in files:

            if not file.endswith(".md"):
                continue

            filepath = os.path.join(root, file)

            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()

            domain = os.path.basename(root)

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "domain": domain,
                        "source": file
                    }
                )
            )

    return documents