"""
=============================================================================
LESSON NOTES: Structured JSON Outputs & Pydantic Validation in Python
=============================================================================

This script demonstrates how to:
1. Enforce JSON output format using Groq's `response_format={"type": "json_object"}`.
2. Validate and parse the LLM's response at runtime using Pydantic (`BaseModel`, 
   `Field`, `Literal`, and `model_validate_json`).
=============================================================================
"""

import os
from groq import Groq
from pydantic import BaseModel, Field, ValidationError
from typing import Literal

# 1. Connect to Groq
# (Ensure your GROQ_API_KEY environment variable is set in your terminal/IDE)
client = Groq(api_key=os.environ["GROQ_API_KEY"])

MODEL = "openai/gpt-oss-120b"


# 2. Define the expected output structure using Pydantic
class Triage(BaseModel):
    category: Literal["billing", "shipping", "other"]
    priority: int = Field(ge=1, le=5)


# 3. Validate the JSON response function
def check(answer):
    try:
        return Triage.model_validate_json(answer)
    except ValidationError:
        return None


# 4. Define the system prompt
system = """
You are a customer support ticket classifier.

Classify each ticket into exactly one category:
- billing
- shipping
- other

Assign a priority from 1 to 5:
- 1 = lowest priority
- 5 = highest priority

Return only a JSON object containing:
- category
- priority
"""


# 5. Get the customer ticket
ticket = "I was charged twice for my subscription."


# 6. Prepare messages
messages = [
    {"role": "system", "content": system},
    {"role": "user", "content": ticket}
]


# 7. Ask the LLM with JSON mode enabled
response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    temperature=0,
    response_format={"type": "json_object"}
)


# 8. Extract the model's answer
answer = response.choices[0].message.content

print("Raw response:")
print(answer)


# 9. Validate the response using Pydantic
result = check(answer)


# 10. Display the validated result
if result is not None:
    print("\nValidated output:")
    print("Category:", result.category)
    print("Priority:", result.priority)
else:
    print("\nInvalid response! Could not validate the output.")
