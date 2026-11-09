"""
===============================================================================
               NEXT-TOKEN PREDICTION & SOFTMAX — FROM THE BASICS
===============================================================================

Key Concept:
Next-token prediction is the core task of an LLM: given the text so far, it 
assigns a probability to every token in its vocabulary of coming next.

-------------------------------------------------------------------------------
1. SCORES (LOGITS) vs. PROBABILITIES
-------------------------------------------------------------------------------
  - Logits (Scores) : Raw, unnormalized numerical values produced by the model. 
                      Can be positive or negative; do not sum to 1.
  - Probabilities   : Normalized values between 0 and 1 that sum up to 1.0 (100%), 
                      interpretable as real-world chances.

-------------------------------------------------------------------------------
2. THE SOFTMAX FUNCTION
-------------------------------------------------------------------------------
Converts logits into probabilities using the formula:
                    exp(s_i)
        P(i) = ------------------
                sum(exp(s_j))

  - math.exp(score) : Makes every score positive and stretches gaps between values.
  - Dividing by sum : Normalizes the values so the total equals 1.0.

-------------------------------------------------------------------------------
3. DECODING STRATEGIES
-------------------------------------------------------------------------------
  - Greedy Decoding : Always selecting the highest-probability token 
                      (max(probs, key=probs.get)). Deterministic (same every time).
  - Random Sampling : Picking tokens weighted by their probabilities, allowing 
                      variation across multiple runs (controlled by temperature).

-------------------------------------------------------------------------------
4. API PROVIDER NOTE (e.g., Groq)
-------------------------------------------------------------------------------
  - Some providers/models (like Groq's `gpt-oss`) refuse requests with `logprobs=True` 
    with a 400 error. Always check model documentation before relying on token probabilities.
===============================================================================
"""

import math


def softmax(scores):
    """Converts raw scores (logits) into a normalized probability distribution

    that sums up to 1.0 using the softmax formula.
    """
    exps = {word: math.exp(score) for word, score in scores.items()}
    total = sum(exps.values())
    return {word: e / total for word, e in exps.items()}


# 1. Raw scores (logits) for the words after "The cat sat on the"
scores = {"mat": 4.0, "floor": 3.1, "sofa": 2.6, "roof": 1.2, "moon": -1.5}

print("=== 1. RAW SCORES (LOGITS) ===")
for word, score in scores.items():
    print(f"{word:6} {score}")

# 2. Convert scores to probabilities using Softmax
probs = softmax(scores)

print("\n=== 2. PROBABILITIES ===")
for word, p in probs.items():
    print(f"{word:6} {p:.3f}")

print("sum:", round(sum(probs.values()), 3))

# 3. Pick the likeliest word using greedy decoding
best = max(probs, key=probs.get)
print("\n=== 3. GREEDY DECODING ===")
print("The likeliest next word:", best)
