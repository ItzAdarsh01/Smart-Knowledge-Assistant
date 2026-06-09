from services.retrieval_service import retrieve_chunks

results = retrieve_chunks(
    "Who won the first FIFA World Cup?"
)

documents = results["documents"][0]

metadata = results["metadatas"][0]

for i, doc in enumerate(documents):

    print("\n")
    print("=" * 50)

    print(
        f"Page: {metadata[i]['page']}"
    )

    print(
        doc[:500]
    )