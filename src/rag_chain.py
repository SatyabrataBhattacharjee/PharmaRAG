from src.load_retriever import retriever
from src.llm_wrapper import HuggingFaceLLM
from src.prompt_template import prompt_template
from langchain.chains import RetrievalQA
from src.display_response import display_rag_response

# Set your Hugging Face token
hf_token = "hf_xxx"  # Replace with your real token

llm = HuggingFaceLLM(
    hf_api_key=hf_token,
    model="microsoft/Phi-3.5-mini-instruct",
    temperature=0.3,
    max_new_tokens=300
)

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt_template}
)

# Run test
if __name__ == "__main__":
    query = "Hello"
    response = rag_chain.invoke(query)
    display_rag_response(response, query)

