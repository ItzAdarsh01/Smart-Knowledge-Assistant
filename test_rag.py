from services.rag_service import ask_question

response = ask_question(
    "Who won the first FIFA World Cup?"
)

print("\nANSWER:\n")

print(response["answer"])