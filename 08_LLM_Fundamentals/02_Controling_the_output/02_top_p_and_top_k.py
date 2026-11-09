"""
===============================================================================
       SAMPLING PARAMETERS: DIFFERENCES & PRACTICAL USE CASES
===============================================================================

-------------------------------------------------------------------------------
1. COMPARISON AT A GLANCE
-------------------------------------------------------------------------------
Parameter    | Controls                         | Dynamic or Fixed? | Typical Range
-------------+----------------------------------+-------------------+----------------
Temperature  | Probability shape / Randomness   | Continuous scale  | 0.0 - 2.0
top_p (Nucleus)| Cumulative probability cutoff  | Dynamic count     | 0.1 - 1.0
top_k        | Candidate pool truncation        | Fixed count       | 1 - 100

-------------------------------------------------------------------------------
2. KEY DIFFERENCES
-------------------------------------------------------------------------------
  - Temperature vs. top_p / top_k:
      * Temperature modifies the actual *probabilities* of tokens by scaling logits.
      * top_p and top_k *eliminate* candidates below a certain threshold before sampling.

  - top_p vs. top_k:
      * top_k keeps a rigid, constant number of tokens (e.g., exactly 40 tokens), 
        regardless of how confident the model is.
      * top_p dynamically adjusts the number of allowed tokens based on confidence. 
        If 2 tokens account for 90% probability, it only considers 2. If 50 tokens 
        are needed to reach 90%, it considers all 50.

-------------------------------------------------------------------------------
3. PRACTICAL USE CASES & RECOMMENDED COMBINATIONS
-------------------------------------------------------------------------------
  A. Code Generation & Math (Deterministic / Low Hallucination)
      - Settings : Temperature = 0.0 - 0.2, top_p = 0.95 (or default 1.0)
      - Reason   : You want high precision and exact logic with minimal randomness.

  B. Factual Q&A & Document Summarization
      - Settings : Temperature = 0.3 - 0.5, top_p = 0.9
      - Reason   : Maintains high fidelity to the text while allowing natural phrasing.

  C. Creative Writing, Brainstorming & Storytelling
      - Settings : Temperature = 0.8 - 1.0, top_p = 0.95 (or top_k = 40)
      - Reason   : Flattens probabilities for diverse vocabulary, while top_p/top_k 
                   cuts off extreme, nonsensical tokens.

-------------------------------------------------------------------------------
4. GOLDEN RULE / BEST PRACTICE
-------------------------------------------------------------------------------
  - Avoid adjusting both Temperature and top_p simultaneously when fine-tuning. 
  - Most LLM research labs (e.g., OpenAI, Anthropic) recommend altering 
    EITHER Temperature OR top_p, but keeping the other at its default value.
===============================================================================
"""

from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

prompt = [
    {
        "role": "user",
        "content": "Suggest a name for a small online shop that sells tea. Reply with the name only."
    }
]
for top_p in (1, 0.1):
    names = []
    for _ in range(2):
        responce = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=prompt,
            temperature=1.8,
            top_p=top_p
        )
        names.append(responce.choices[0].message.content)

    print(top_p, names)
