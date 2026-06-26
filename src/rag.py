import os
from dotenv import load_dotenv
from openai import OpenAI

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


# Load environment variables
load_dotenv()


# OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Load Chroma database
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)


def ask_question(question: str) -> str:

    # Retrieve top 3 similar chunks
    docs = db.similarity_search(question, k=3)

    # Print retrieved chunks (for debugging)
    for i, doc in enumerate(docs):
        print(f"\n===== Source {i+1} =====")
        print(doc.page_content)

    # Combine retrieved text into one context
    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, say:
"I don't know based on the provided documents."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
    model = "openrouter/free",
    max_tokens=200,
    temperature=0.2,
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

    return response.choices[0].message.content