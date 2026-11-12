import time
from groq import Groq

client = Groq()

for request in [
    "Reply with one word: yes",
    "Write about 150 words on how parcels are delivered."
]:
    started = time.perf_counter()
    responce = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": request
            }
        ]

    )
    seconds = time.perf_counter()-started

    print(
        f"{responce.usage.completion_tokens} tokens in {seconds:.2f} seconds"
    )
