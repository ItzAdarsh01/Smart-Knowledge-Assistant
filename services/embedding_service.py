from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

MODEL = os.getenv(
    "EMBED_MODEL"
)


def get_embedding(text):

    embedding = client.feature_extraction(
        text,
        model=MODEL
    )

    return embedding
