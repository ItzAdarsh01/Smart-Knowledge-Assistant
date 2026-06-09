from db.chroma_store import collection
from services.embedding_service import get_embedding


def retrieve_chunks(
    query,
    top_k=3
):

    query_embedding = get_embedding(
        query
    )

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],

        n_results=top_k
    )

    return results