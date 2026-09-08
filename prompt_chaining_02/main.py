import ollama

topic = input("Enter a topic: ")

# Step 1 - Summary
summary = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Summarize this topic:\n{topic}"
        }
    ]
)

summary_text = summary["message"]["content"]

print("\nSUMMARY\n")
print(summary_text)

# Step 2 - Key Points
keypoints = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Extract 5 key points from:\n{summary_text}"
        }
    ]
)

key_text = keypoints["message"]["content"]

print("\nKEY POINTS\n")
print(key_text)

# Step 3 - Questions
questions = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Create three questions based on:\n{summary_text}"
        }
    ]
)

print("\nQUESTIONS\n")
print(questions["message"]["content"])
