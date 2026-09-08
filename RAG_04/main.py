from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import ollama

loader = TextLoader("data.txt")
documents = loader.load()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_documents(documents, embeddings)

question = input("Ask a question: ")

docs = db.similarity_search(question, k=1)

context = docs[0].page_content

prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\nANSWER\n")
print(response["message"]["content"])
