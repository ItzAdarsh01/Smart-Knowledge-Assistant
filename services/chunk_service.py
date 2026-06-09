from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    all_chunks = []

    chunk_id = 1

    for page in pages:

        page_chunks = splitter.split_text(
            page["text"]
        )

        for chunk in page_chunks:

            all_chunks.append(
                {
                    "chunk_id": chunk_id,
                    "page": page["page"],
                    "text": chunk
                }
            )

            chunk_id += 1

    return all_chunks