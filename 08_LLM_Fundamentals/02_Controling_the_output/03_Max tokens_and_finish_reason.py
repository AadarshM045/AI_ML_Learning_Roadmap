"""
===============================================================================
             MAX_COMPLETION_TOKENS & FINISH_REASON IN LLMs
===============================================================================

-------------------------------------------------------------------------------
1. max_completion_tokens
-------------------------------------------------------------------------------
  - Definition : Sets the maximum number of tokens the model can generate in a completion.
  - Scope      : Applies to the entire generated output (visible answer + hidden 
                 reasoning tokens for reasoning models).
  - Risk       : Setting this too low will truncate responses or result in empty outputs.

-------------------------------------------------------------------------------
2. finish_reason
-------------------------------------------------------------------------------
  - Indicates *why* the model stopped generating text.
  - Common Values:
      * "stop"   : Generation ended normally or reached a natural stopping condition.
      * "length" : Generation hit the `max_completion_tokens` limit before finishing.

-------------------------------------------------------------------------------
3. REASONING MODELS & CONTEXT WINDOW
-------------------------------------------------------------------------------
  - reasoning_effort ("low", "medium", "high") : Controls how many reasoning 
    tokens the model allocates before writing the final response.
  - Context Window : The total combined capacity of input prompt + generated tokens.
===============================================================================
"""
import os
from groq import Groq

# Initialize the Groq API client using the API key stored in system environment variables
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Define the conversation prompt/messages list sent to the model
prompt = [
    {
        "role": "user",
        "content": (
            "Write a one-sentence apology to a customer whose parcel is late."
        ),
    }
]

# Loop through two different completion token limits to observe behavior:
# - 30 tokens: Tight budget, likely to trigger the 'length' cutoff.
# - 300 tokens: Generous budget, allowing complete generation and reasoning.
for limit in (30, 300):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=prompt,
        # Caps total generated output (including hidden reasoning tokens)
        max_completion_tokens=limit,
        reasoning_effort="low",  # Sets the scale of model reasoning tokens allocated
    )

    # Extract the primary response choice object
    choice = response.choices[0]

    # Inspect the finish_reason to see why generation terminated
    if choice.finish_reason == "stop":
        # Generation completed successfully and hit an natural stop token
        print(f"[Limit: {limit}] Answer:", choice.message.content)

    elif choice.finish_reason == "length":
        # Generation hit the max_completion_tokens ceiling and was truncated
        print(
            f"[Limit: {limit}] Response was cut off. Increase the token limit.")

    else:
        # Handle any other edge-case stopping conditions
        print(f"[Limit: {limit}] Other stopping reason:", choice.finish_reason)
