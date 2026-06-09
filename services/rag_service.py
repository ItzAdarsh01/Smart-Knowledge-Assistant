from services.retrieval_service import retrieve_chunks
from services.llm_service import generate_answer


def ask_question(question):

    results = retrieve_chunks(
        question
    )

    documents = results["documents"][0]

    context = "\n\n".join(
        documents
    )

    prompt = f"""
You are a document question answering system.

You must answer ONLY from the provided context.

Rules:

- Never use outside knowledge.
- Never guess.
- If answer is not explicitly present in context, say:

"I could not find the answer in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
"""

    answer = generate_answer(
        prompt
    )
    metadata = results["metadatas"][0]

    return {
        "answer": answer,
        "context": context,
        "sources": metadata
    }

