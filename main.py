from ollama import chat

messages = [
    {
        "role": "system",
        "content": (
            "Answer briefly in 1-3 sentences. "
            "Do not display your reasoning. "
            "Ask one short clarifying question if needed."
        ),
    }
]

while True:
    question = input("You: ").strip()

    if question.lower() in {"exit", "quit"}:
        break

    if not question:
        continue

    messages.append({"role": "user", "content": question})

    response = chat(
        model="qwen3.5:9b",
        messages=messages,
        think=False,
        options={"temperature": 0.2, "num_predict": 120},
    )

    answer = response.message.content
    print(f"Assistant: {answer}\n")

    messages.append({"role": "assistant", "content": answer})