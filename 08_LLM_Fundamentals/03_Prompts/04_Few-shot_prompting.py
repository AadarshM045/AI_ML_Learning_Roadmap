"""
=============================================================================
LESSON NOTES: Few-Shot Prompting in LLMs & Python List Unpacking
=============================================================================

1. WHAT IS FEW-SHOT PROMPTING?
-----------------------------------------------------------------------------
When a system prompt alone isn't enough and the model makes mistakes, you can 
provide a few solved examples of the task inside the prompt. 

- Zero-shot  : Instructions only (Tell the model what to do).
- One-shot   : Instructions + one solved example.
- Few-shot   : Instructions + several solved examples (Tell and show how).
=============================================================================
"""

"""
=============================================================================
2. THE FEW-SHOT EXAMPLES STRUCTURE
-----------------------------------------------------------------------------
Examples are formatted as a list of alternating user prompts and assistant 
responses, demonstrating the expected output pattern.
=============================================================================
"""

from groq import Groq
examples = [
    {"role": "user", "content": "You took money from my card two times."},
    {"role": "assistant", "content": '{"category": "billing", "priority": 4}'},

    {"role": "user", "content": "Where is my delivery? It is a week late."},
    {"role": "assistant", "content": '{"category": "shipping", "priority": 3}'},

    {"role": "user", "content": "Can I change the email on my account?"},
    {"role": "assistant", "content": '{"category": "other", "priority": 2}'},
]


"""
=============================================================================
3. USING ITERABLE UNPACKING (*examples)
-----------------------------------------------------------------------------
To combine the system prompt, our examples list, and the current user ticket 
into a single `messages` list, we use the iterable unpacking operator `*`.

Without `*`: Inserts the list *itself* as a nested element: `[system, [ex1, ex2], ticket]`
With `*`: Unpacks each dictionary individually into the list: `[system, ex1, ex2, ticket]`
=============================================================================
"""


client = Groq()
MODEL = "openai/gpt-oss-120b"

structured_system_prompt = {
    "role": "system",
    "content": (
        "You are a customer support ticket classification assistant.\n"
        "Categories: billing, shipping, other.\n"
        "Output format strictly as JSON: {\"category\": \"<name>\", \"priority\": <1-5>}"
    )
}


def ask(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    return response.choices[0].message.content


# Sample incoming tickets to evaluate against our few-shot examples
tickets = [
    ("My package hasn't arrived and it's been 5 days!", "shipping"),
    ("The courier demanded an extra delivery fee at the door", "billing"),
    ("Cancel order before it ships", "other")
]

print("\n--- Running Few-Shot Classification Loop ---")
for text, expected in tickets:
    # Build the full message list using the unpacking operator (*)
    messages = [
        structured_system_prompt,
        *examples,
        {"role": "user", "content": text}
    ]

    prediction = ask(messages)
    print(f"Expected: {expected:<9} | Model Output: {prediction}")


"""
=============================================================================
4. KEY TAKEAWAYS & BEST PRACTICES
-----------------------------------------------------------------------------
- Few-shot prompting teaches a pattern using context, but it does NOT train 
  the model or change its internal weights (unlike fine-tuning).
- If edge-case mistakes occur (e.g., unexpected fee scenarios or cancellation 
  phrasing), adding targeted examples directly into your `examples` list can 
  improve accuracy.
- Keep example formats strictly aligned with your expected final output schema.
=============================================================================
"""
