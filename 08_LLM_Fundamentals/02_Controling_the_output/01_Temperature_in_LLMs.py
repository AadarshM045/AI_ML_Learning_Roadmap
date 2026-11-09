"""
===============================================================================
                       TEMPERATURE IN LLMs — FROM THE BASICS
===============================================================================

Key Concept:
Temperature controls the shape of the probability distribution when an LLM 
samples its next token(which controls how strongly an LLM favours high-probability token).
It determines whether the model strongly favors the 
most likely token or gives more opportunities to less likely candidates.

-------------------------------------------------------------------------------
1. HOW TEMPERATURE WORKS
-------------------------------------------------------------------------------
Temperature ($T$) divides each raw logit ($s_i$) before applying the softmax function:

                     exp(s_i / T)
          P(i) = --------------------
                  sum(exp(s_j / T))

* Note: Temperature does not alter the model's original logits; it only 
  changes how those logits are scaled into probabilities.

-------------------------------------------------------------------------------
2. LOW vs. HIGH TEMPERATURE
-------------------------------------------------------------------------------
  - Low Temperature (e.g., 0.2 or 0):
      - Amplifies differences between scores (dividing by a small $T$ acts like 
        multiplying the scores).
      - Strongly favors the top-scoring token (approaching deterministic greedy decoding).
      - Result: Predictable, consistent, and factual responses.

  - Reference Temperature (1.0):
      - Leaves the original logit scores and probabilities unchanged.

  - High Temperature (e.g., 1.8):
      - Compresses the differences between scores.
      - Gives lower-scoring candidates a significantly higher relative probability.
      - Result: Greater variety and diversity in output, but increased risk 
        of erratic or off-topic tokens.

-------------------------------------------------------------------------------
3. PRACTICAL USAGE IN APIS (e.g., Groq)
-------------------------------------------------------------------------------
In real-world development, you do not manually calculate softmax or scale logits. 
You simply pass the temperature parameter directly into the API call:

  response = client.chat.completions.create(
      model="openai/gpt-oss-120b",
      messages=prompt,
      temperature=0.7
  )
===============================================================================
"""
import os
from groq import Groq


client = Groq(api_key=os.environ["GROQ_API_KEY"])

prompt = [
    {
        "role": "user",
        "content": "Suggest a name for a small online shop that sells tea. Reply with the name only.",
    }
]


for temperature in (0, 0.5, 1.0, 1.5, 2.0):
    names = []
    for _ in range(5):
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b", messages=prompt, temperature=temperature
        )
        names.append(response.choices[0].message.content)
    print(f"Temp {temperature}: {names}")

"""
===============================================================================
            TEMPERATURE GUIDELINES & BEST PRACTICES IN LLMs
===============================================================================

-------------------------------------------------------------------------------
1. TEMPERATURE RANGE & SUITABLE USE CASES
-------------------------------------------------------------------------------
  - Temperature 0.0 – 0.3 (Very Predictable):
      * Behavior : Strongly favors top-scoring tokens (greedy/near-greedy).
      * Use Case : Data extraction, text classification, sorting, factual summaries.
  
  - Temperature 0.5 – 0.7 (Balanced / Mild Variation):
      * Behavior : Allows some natural token variation while keeping output stable.
      * Use Case : General-purpose conversational responses and task execution.

  - Temperature 0.7 – 1.0 (Higher Variety):
      * Behavior : Flattens probabilities for more diverse token selection.
      * Use Case : Creative writing, explanations, and general chat.

  - Temperature > 1.0 (Adventurous / High Exploration):
      * Behavior : Significantly flattens the distribution; lower-scoring tokens rise.
      * Use Case : Brainstorming, ideation, and creative naming. 
      * Warning  : Excessively high temperatures increase incoherence and erratic tokens.

-------------------------------------------------------------------------------
2. CRITICAL WARNING: TEMPERATURE != KNOWLEDGE
-------------------------------------------------------------------------------
  - Temperature does NOT give the model new facts, increase intelligence, or 
    fix hallucinations. 
  - It only adjusts the sampling randomness of the logits already computed by the model.

-------------------------------------------------------------------------------
3. SPECIAL SETTINGS
-------------------------------------------------------------------------------
  - Temperature = 0.0 : Handled by APIs as a special greedy-decoding setting 
                        (deterministically picks the highest-scoring token).
  - Temperature = 3.0 : Flattens the distribution drastically, making even unlikely 
                        candidates (like "moon" in our earlier example) quite probable.
===============================================================================
"""
