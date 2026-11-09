"""
=============================================================================
LESSON NOTES: System Prompts & Structured Instructions
=============================================================================

1. DEFINITION & PURPOSE
-----------------------------------------------------------------------------
A system prompt is an instruction message that defines the model's role, 
task, rules, and expected response format.

Purpose:
- Defines what the model should do.
- Provides rules and instructions.
- Explains categories and their meanings.
- Defines the expected output format.
- Can specify constraints and edge cases.
=============================================================================
"""


"""
=============================================================================
2. SYSTEM VS USER ROLES
-----------------------------------------------------------------------------
- system    : Instructions for the model (persona, behavior, rules).
- user      : Input, question, or specific task to execute.
- assistant : Generated response from the LLM.
=============================================================================
"""


"""
=============================================================================
3. VAGUE VS STRUCTURED PROMPTS
-----------------------------------------------------------------------------
- Vague Prompt     : Does not clearly define the task, rules, or expected output.
- Structured Prompt: Includes model role, clear task description, category 
                     definitions, examples, edge-case rules, output format, 
                     and limits/scales.
=============================================================================
"""


"""
=============================================================================
4. PRACTICAL EXAMPLE: TICKET CLASSIFICATION
-----------------------------------------------------------------------------
Demonstrating a structured system prompt for text classification returning JSON.
=============================================================================
"""


from groq import Groq
client = Groq()
MODEL = "openai/gpt-oss-120b"


def ask(messages, **settings):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        **settings
    )
    return response.choices[0].message.content


tickets = [
    ("I was charged twice for one order", "billing"),
    ("My parcel has not arrived", "shipping"),
    ("Can I get a refund for the blue mug?", "billing"),
    ("How do I change my password?", "other"),
    ("The parcel arrived but the box was crushed", "shipping"),
    ("The courier asked me to pay a delivery fee at the door", "billing"),
    ("I want to cancel my order before it ships", "other"),
]


structured = """
You sort customer support tickets for an online shop.

Categories:
- billing: payments, charges, refunds and fees.
- shipping: missing parcels, delivery delays and damaged boxes.
- other: unrelated requests and order cancellations before shipment.

Important rules:
- Delivery fees are billing issues.
- Cancelling an order before shipment is other.

Priority:
1 = Can wait
2 = Low
3 = Normal
4 = High
5 = Urgent

Return one JSON object:
{"category": "billing", "priority": 3}

Return JSON only.
"""


for text, expected in tickets:

    messages = [
        {"role": "system", "content": structured},
        {"role": "user", "content": text}
    ]

    answer = ask(messages, temperature=0)

    print(f"Expected: {expected:9} | Model: {answer}")


"""
=============================================================================
5. IMPORTANT LESSONS & BEST PRACTICES
-----------------------------------------------------------------------------
- More specific instructions can improve consistency across runs.
- Explicit edge-case rules help reduce classification mistakes.
- JSON formatting does not guarantee factual correctness (model can hallucinate 
  the category).
- Always validate both the output structure (JSON parsing) and the actual 
  classification logic.

Remember: A good system prompt tells the model what to do, how to do it, 
and what its response should look like.
=============================================================================
"""
