import json
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load texts and metadata
with open("data/texts.json", "r", encoding="utf-8") as f:
    texts = json.load(f)

with open("data/metadatas.json", "r", encoding="utf-8") as f:
    metadatas = json.load(f)

# Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Build FAISS vectorstore
vectorstore = FAISS.from_texts(texts=texts, embedding=embedding_model, metadatas=metadatas)
vectorstore.save_local("my_faiss_store")

