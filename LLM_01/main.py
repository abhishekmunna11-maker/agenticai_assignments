import ollama

print("=== LLM Workflow ===")

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": user
            }
        ]
    )

    print("\nAI:", response["message"]["content"])
