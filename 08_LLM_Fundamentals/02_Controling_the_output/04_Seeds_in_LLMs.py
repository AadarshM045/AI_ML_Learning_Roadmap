from groq import Groq

client = Groq()

prompt = [
    {
        "role": "user",
        "content": "Write a six-word slogan for a small online tea shop."
    }
]

# Experiment 1: Without a seed
print("WITHOUT SEED")

for run in range(3):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=prompt,
        temperature=1
    )

    print(run, response.choices[0].message.content)


# Experiment 2: With seed 42
print("\nWITH SEED 42")

for run in range(3):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=prompt,
        temperature=1,
        seed=42
    )

    print(run, response.choices[0].message.content)


# Experiment 3: Temperature 0
print("\nTEMPERATURE 0")

for run in range(3):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=prompt,
        temperature=0
    )

    print(run, response.choices[0].message.content)
