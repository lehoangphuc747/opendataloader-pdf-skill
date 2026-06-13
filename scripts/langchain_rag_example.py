#!/usr/bin/env python3
"""
LangChain Integration Example (from opendataloader-pdf official repo)
Demonstrates using the official langchain-opendataloader-pdf package
for seamless RAG pipeline integration.
"""

from pathlib import Path
from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_chunk(pdf_paths):
    """
    Load PDF(s) and return LangChain chunks ready for vector stores.
    """
    # 1. Create loader (automatically runs OpenDataLoader under the hood)
    loader = OpenDataLoaderPDFLoader(
        file_path=pdf_paths,
        format="markdown", # Use markdown for better chunking boundaries
        quiet=True,
    )

    # 2. Load documents
    documents = loader.load()
    print(f"Loaded {len(documents)} document(s)")

    # 3. Create a text splitter tailored for markdown
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )
    
    # 4. Split into chunks
    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} semantic chunks")
    
    return chunks

if __name__ == "__main__":
    # Example usage
    # Ensure you ran: pip install langchain-opendataloader-pdf langchain-text-splitters
    pdf_list = ["sample.pdf"]
    
    # Assuming sample.pdf exists, this will load it and print the first chunk.
    # chunks = load_and_chunk(pdf_list)
    # print(chunks[0].page_content)
    # print(chunks[0].metadata)
