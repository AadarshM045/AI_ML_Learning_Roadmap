"""
=============================================================================
LESSON NOTES: Prompt Evaluation Framework (Vague vs. Structured vs. Few-Shot)
=============================================================================

This script brings together everything you've learned to build a complete 
evaluation harness:
1. Reusable `ask()` function with keyword argument unpacking (`**settings`).
2. Pydantic validation (`Triage` model) to guarantee structural correctness.
3. Comparative prompt evaluation testing three different strategies:
   - "vague": Minimal, underspecified instructions.
   - "structured": Explicit categories, rules, and JSON formatting constraints.
   - "few-shot": Structured instructions + solved demonstration examples.
=============================================================================
"""

import os
from typing import Literal

from groq import Groq
from pydantic import BaseModel, Field, ValidationError


# 1. Connect to Groq
# (Ensure your GROQ_API_KEY environment variable is set in your terminal/IDE)
client = Groq(api_key=os.environ["GROQ_API_KEY"])

MODEL = "openai/gpt-oss-120b"


# 2. Create the expected output structure using Pydantic
class Triage(BaseModel):
    category: Literal["billing", "shipping", "other"]
    priority: int = Field(ge=1, le=5)


# 3. Validate the model's response against the Pydantic schema
def check(answer):
    try:
        return Triage.model_validate_json(answer)
    except ValidationError:
        return None


# 4. Reusable function to query the LLM
def ask(messages, **settings):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0,  # Zero temperature for deterministic classification
        **settings
    )
    return response.choices[0].message.content


# 5. Define system prompts (Vague vs. Structured)
vague = """
Classify the customer support ticket.
"""

structured = """
Classify the customer support ticket.

Choose exactly one category:
- billing
- shipping
- other

Assign a priority from 1 to 5:
- 1 = lowest priority
- 5 = highest priority

Return only a JSON object with these two fields:
- category
- priority
"""


# 6. Few-shot examples (demonstrating expected input-output patterns)
examples = [
    {
        "role": "user",
        "content": "I was charged twice for my subscription."
    },
    {
        "role": "assistant",
        "content": '{"category": "billing", "priority": 4}'
    },
    {
        "role": "user",
        "content": "My parcel has not arrived yet."
    },
    {
        "role": "assistant",
        "content": '{"category": "shipping", "priority": 3}'
    },
    {
        "role": "user",
        "content": "I want to delete my account."
    },
    {
        "role": "assistant",
        "content": '{"category": "other", "priority": 2}'
    },
]


# 7. Test dataset: Customer support tickets and expected ground-truth answers
tickets = [
    ("I was charged twice.", "billing"),
    ("Where is my parcel?", "shipping"),
    ("I want to delete my account.", "other"),
    ("My refund has not arrived.", "billing"),
    ("The courier delivery fee is too high.", "billing"),
    ("My package is damaged.", "shipping"),
    ("I want to cancel before shipment.", "other"),
]


# 8. Prepare different prompt configurations to test
candidates = {
    "vague": [
        {"role": "system", "content": vague}
    ],

    "structured": [
        {"role": "system", "content": structured}
    ],

    "few-shot": [
        {"role": "system", "content": structured},
        *examples  # Unpacks the list of demonstration dictionaries
    ],
}


# 9. Evaluation function to compute accuracy percentage for each strategy
def score(start_messages):
    right = 0

    for text, expected in tickets:
        # Combine base configuration with the current test ticket
        messages = start_messages + [
            {"role": "user", "content": text}
        ]

        answer = ask(messages)
        result = check(answer)

        # Check if Pydantic validation succeeded and the category matches expected
        if result is not None and result.category == expected:
            right += 1
        else:
            print("MISS:", text, "| expected:", expected, "| got:", answer)

    return right / len(tickets)


# 10. Run evaluation and compare prompt performance
print("\n--- Prompt Strategy Evaluation Results ---")
for label, start in candidates.items():
    accuracy = score(start)
    print(f"{label:10} {accuracy:.0%}")


# 11. Test Pydantic validation manually on a sample output string
test_answer = '{"category": "billing", "priority": 4}'

result = check(test_answer)

if result is not None:
    print("\nManual Validation Test: Valid response!")
    print("Category:", result.category)
    print("Priority:", result.priority)
else:
    print("\nManual Validation Test: Invalid response!")
