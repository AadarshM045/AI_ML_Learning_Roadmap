"""
===============================================================================
               GENERATING TEXT IN LLMs — AUTOREGRESSIVE & STREAMING
===============================================================================

Key Concept:
Text generation in LLMs is not a single-step operation. It is an iterative, 
autoregressive process where the model predicts the next token, appends it 
to the input context, and uses that updated context to predict the subsequent token.

-------------------------------------------------------------------------------
1. THE AUTOREGRESSIVE GENERATION LOOP (DICTIONARY DEMO)
-------------------------------------------------------------------------------
  - Dictionary Representation: Maps words to dictionaries of possible next 
                               words and their respective probabilities.
  - Negative Indexing (`words[-1]`): Accesses the last generated word in the list 
                                   to use as the current context key.
  - Greedy Selection (`max`): Uses `max(options, key=options.get)` to pick the 
                                candidate with the highest probability.
  - Stopping Condition: The loop runs (`while words[-1] in next_word`) until 
                        the current word has no further mapped entries (or in 
                        real LLMs, until an End-of-Sequence / EOS token is hit).

-------------------------------------------------------------------------------
2. STREAMING RESPONSES (API CONCEPT)
-------------------------------------------------------------------------------
  - Complete Response : Waiting until the LLM generates the entire output before 
                        displaying anything to the user.
  - Streaming Response: Receiving and rendering generated text chunks in real-time 
                        as the model produces them via an API (e.g., Groq API), 
                        providing a faster and more fluid user experience.
===============================================================================
"""
from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Tell all about youeself"
        }
    ],
    stream=True,
)
for chunk in response:
    piece = chunk.choices[0].delta.content
    if piece:
        print(piece, end="|")
