import os
from groq import Groq

client = Groq()
Question = input("What is on ypur mind?")

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": Question
        }
    ],
)

print(response.choices[0].message.content)
