from services.llm_service import generate_answer

response = generate_answer(
    "Who won the first FIFA World Cup?"
)

print(response)