from services.embedding_service import get_embedding

embedding = get_embedding(
    "What is Artificial Intelligence?"
)

print(
    len(embedding)
)

print(
    embedding[:10]
)