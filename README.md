# 💊 PharmaRAG

**PharmaRAG** is an intelligent **Retrieval-Augmented Generation (RAG)** powered medical assistant designed to answer **drug-related queries** with high relevance and safety. It combines a **FAISS-based vector retriever** with an **LLM** (e.g., Microsoft Phi) to ensure responses are grounded in trusted data, and avoids hallucination.

---

## 🚀 Features

- 🔎 Semantic search over curated drug data using FAISS
- 🧠 LLM-powered answers (Phi-3.5, DeepSeek, etc.)
- 📚 Prompt templating for safe, empathetic, and clear responses
- 💬 Handles greetings, vague queries, or spelling errors gracefully
- ✅ Only responds when confident; otherwise suggests consulting a professional

---

## 📂 Project Structure


PharmaRAG/
├── data/
│ ├── texts.json # Drug-related content
│ └── metadatas.json # Metadata for vector store
├── my_faiss_store/ # Saved FAISS index
├── src/
│ ├── embed_and_store.py # Build and save FAISS index
│ ├── load_retriever.py # Load FAISS vectorstore and retriever
│ ├── llm_wrapper.py # Custom Hugging Face LLM wrapper
│ ├── prompt_template.py # Prompt instructions for LLM
│ ├── rag_chain.py # Full RAG pipeline
│ └── display_response.py # Pretty output printing
├── requirements.txt
└── README.md


---

## 🧠 How It Works

1. **Data Loading**: Loads drug-related texts and metadata from `texts.json` and `metadatas.json`.
2. **Embedding**: Uses `all-MiniLM-L6-v2` via `HuggingFaceEmbeddings` to embed documents.
3. **Indexing**: Builds a FAISS vector index and saves it.
4. **Querying**: Uses LangChain's `RetrievalQA` to combine retrieval + response generation.
5. **LLM**: Calls the Hugging Face Inference API for models like `microsoft/Phi-3.5-mini-instruct`.

---

## 🔧 Installation

```bash
git clone https://github.com/yourusername/PharmaRAG.git
cd PharmaRAG

# Recommended environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

