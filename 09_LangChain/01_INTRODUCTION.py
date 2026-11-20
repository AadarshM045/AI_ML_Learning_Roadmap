from groq import Groq

client = Groq()
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "What is machine learning? give me and in 5 bullet points"
        }
    ]
)

print(response.choices[0].message.content)
