import time
from groq import Groq
from prompt import AFTER, BEFORE, EXAMPLES, TICKETS, check

MODEL = "openai/gpt-oss-120b"
client = Groq()

prices = next(
    model.pricing
    for model in client.models.list().data
    if model.id == MODEL
)


def sort_ticket(system, text):
    messages = [
        {
            "role": "system",
            "content": system
        },
        *EXAMPLES,
        {
            "role": "user",
            "content": text
        }
    ]
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content, response.usage


def run(label, system):
    right, token_in, token_out = 0, 0, 0
    started = time.perf_counter()
    print(label)

    for text, expected in TICKETS:
        answer, usage = sort_ticket(system, text)
        token_in += usage.prompt_tokens
        token_out += usage.completion_tokens

        result = check(answer)

        ok = result is not None and expected == result.category
        right += ok

        print(f"{'ok ' if ok else 'Bad'} {expected:9} {answer}")
        seconds = time.perf_counter() - started
        cost = (
            token_in * float(prices["prompt"])
            + token_out * float(prices["completion"])
        )

    print(
        f"  accuracy {right}/{len(TICKETS)}, "
        f"{token_in} tokens in, {token_out} out, "
        f"${cost:.6f}, {seconds / len(TICKETS):.2f} seconds a ticket"
    )


run("before", BEFORE)

run("after", AFTER)
