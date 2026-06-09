import streamlit as st
import os
import pandas as pd

from services.rag_service import ask_question
from db.ingest import ingest_pdf
from db.chroma_store import collection


st.set_page_config(
    page_title="Smart Knowledge Assistant",
    page_icon="📚",
    layout="wide"
)

# =========================
# LOAD CHROMA DATA
# =========================

try:
    data = collection.get()

except:
    data = {
        "ids": [],
        "documents": [],
        "metadatas": []
    }

# =========================
# SIDEBAR
# =========================

st.sidebar.title(
    "📚 Knowledge Base Explorer"
)

total_chunks = len(
    data["ids"]
)

st.sidebar.metric(
    "Total Chunks",
    total_chunks
)

sources = set()

for meta in data["metadatas"]:

    if meta and "source" in meta:

        sources.add(
            meta["source"]
        )

st.sidebar.metric(
    "Documents",
    len(sources)
)

st.sidebar.subheader(
    "Indexed Documents"
)

for source in sorted(sources):

    st.sidebar.write(
        f"📄 {source}"
    )

# =========================
# MAIN TITLE
# =========================

st.title(
    "📚 Smart Knowledge Assistant"
)

st.write(
    "Upload PDF and ask questions"
)

# =========================
# KNOWLEDGE BASE EXPLORER
# =========================

with st.expander(
    "🔍 Knowledge Base Explorer"
):

    st.write(
        f"**Total Chunks:** {total_chunks}"
    )

    st.write(
        f"**Total Documents:** {len(sources)}"
    )

    if total_chunks > 0:

        preview_rows = []

        limit = min(
            10,
            total_chunks
        )

        for i in range(limit):

            preview_rows.append({

                "Source":
                data["metadatas"][i].get(
                    "source",
                    "Unknown"
                ),

                "Page":
                data["metadatas"][i].get(
                    "page",
                    "-"
                ),

                "Chunk Preview":
                data["documents"][i][:100]

            })

        df = pd.DataFrame(
            preview_rows
        )

        st.dataframe(
            df,
            use_container_width=True
        )

# =========================
# PDF UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    save_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(
        save_path,
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    st.success(
        f"{uploaded_file.name} uploaded successfully"
    )

    if st.button(
        "🚀 Process PDF"
    ):

        with st.spinner(
            "Creating chunks, embeddings and storing in ChromaDB..."
        ):

            success = ingest_pdf(
                save_path
            )

        if success:

            st.success(
                "PDF processed successfully"
            )

        else:

            st.warning(
                "PDF already indexed"
            )

# =========================
# QUESTION
# =========================

question = st.text_input(
    "Ask Question"
)

if st.button(
    "🔍 Ask"
):

    if question:

        with st.spinner(
            "Searching knowledge base..."
        ):

            response = ask_question(
                question
            )

        st.subheader(
            "Answer"
        )

        st.write(
            response["answer"]
        )

        st.subheader(
            "Sources"
        )

        for source in response["sources"]:

            st.write(
                f"📄 {source['source']} | Page {source['page']}"
            )