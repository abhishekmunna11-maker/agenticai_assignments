import ollama

task = input("Enter a task: ")

# Planning
plan = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Create a step-by-step plan for: {task}"
        }
    ]
)

plan_text = plan["message"]["content"]

print("\nPLAN\n")
print(plan_text)

# Execution
result = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": f"Now execute the following plan and provide the final result:\n{plan_text}"
        }
    ]
)

print("\nFINAL OUTPUT\n")
print(result["message"]["content"])
