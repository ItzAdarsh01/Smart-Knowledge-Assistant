import os
from db.chroma_store import collection

from services.pdf_service import extract_text_from_pdf
from services.chunk_service import create_chunks
from services.embedding_service import get_embedding



def ingest_pdf(pdf_path):
    filename = os.path.basename(pdf_path)
    existing = collection.get(where={"source": filename})
    if existing["ids"]:
        print(f"{filename} already indexed")
        return False

    pages = extract_text_from_pdf(
        pdf_path
    )

    chunks = create_chunks(
        pages
    )

    for chunk in chunks:

        embedding = get_embedding(
            chunk["text"]
        )

        collection.add(
            ids=[
                str(chunk["chunk_id"])
            ],

            documents=[
                chunk["text"]
            ],

            embeddings=[
                embedding
            ],

            metadatas=[
                {
                    "page": chunk["page"],
                    "source": filename
                }
            ]
        )

    print(
        f"{len(chunks)} chunks stored"
    )
    return True