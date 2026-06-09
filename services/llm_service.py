from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    token=os.getenv("HF_TOKEN")
)

MODEL = os.getenv("LLM_MODEL")


def generate_answer(prompt):

    response = client.chat_completion(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model=MODEL,
        max_tokens=500
    )

    return response.choices[0].message.content
