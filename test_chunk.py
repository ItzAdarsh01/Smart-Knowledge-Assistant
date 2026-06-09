from services.pdf_service import extract_text_from_pdf
from services.chunk_service import create_chunks

pages = extract_text_from_pdf(
    "uploads/FIFA_World_Cup_Guide.pdf"
)

chunks = create_chunks(
    pages
)

print("Total Pages:", len(pages))

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")

print(chunks[0])