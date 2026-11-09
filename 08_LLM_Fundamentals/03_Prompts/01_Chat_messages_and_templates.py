from groq import Groq

client = Groq()

system = {
    "role": "system",
    "content": "You are FinCoach, a personal finance assistant. Reply in one short sentence."
}

first = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        system,
        {
            "role": "user",
            "content": "My monthly take-home is ₹1,20,000."
        }
    ],
)

print(first.choices[0].message.content)

second = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        system,
        {
            "role": "user",
            "content": "What is my monthly take-home?"
        }
    ],
)

print(second.choices[0].message.content)

history = [
    system,

    {
        "role": "user",
        "content": "My monthly take-home is ₹1,20,000."
    },

    {
        "role": "assistant",
        "content": first.choices[0].message.content
    },

    {
        "role": "user",
        "content": "What is my monthly take-home? Built a plan for me"
    }
]

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=history
)

print(response.choices[0].message.content)
