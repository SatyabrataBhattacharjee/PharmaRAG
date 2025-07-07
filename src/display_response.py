def display_rag_response(response: dict, query: str):
    print(f"You asked: {query}\n")
    print("Assistant's response:\n")
    print(response['result'].strip())

