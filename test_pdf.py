from services.pdf_service import extract_text_from_pdf

text = extract_text_from_pdf(
    "uploads/FIFA_World_Cup_Guide.pdf"
)

print(text[:1000])