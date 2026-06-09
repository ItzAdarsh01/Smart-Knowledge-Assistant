import chromadb

client = chromadb.PersistentClient(
    path="chroma_data"
)

client.delete_collection(
    "knowledge_base"
)

print("Collection Deleted")