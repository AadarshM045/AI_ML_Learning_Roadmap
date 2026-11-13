"""
===============================================================================
               LLM COST, PRICING, AND TOKENOMICS SUMMARY
===============================================================================

-------------------------------------------------------------------------------
1. THE COST FORMULA
-------------------------------------------------------------------------------
  Total Cost = (Prompt Tokens * Input Price) + (Completion Tokens * Output Price)
  * Prices are typically scaled per 1,000,000 (1 million) tokens.

-------------------------------------------------------------------------------
2. INPUT vs. OUTPUT TOKENS
-------------------------------------------------------------------------------
  - Input Tokens  : System prompts, user history, few-shot examples, and questions. 
                    Cheaper per token.
  - Output Tokens : The generated response. More expensive because generation 
                    requires active token-by-token computation.
  - Reasoning     : Internal reasoning / chain-of-thought tokens count as output tokens.

-------------------------------------------------------------------------------
3. TOKENIZER DIFFERENCES
-------------------------------------------------------------------------------
  - Different models (e.g., cl100k_base vs o200k_harmony) tokenize text differently.
  - Non-English text (e.g., Hindi, Nepali) can consume significantly more tokens 
    depending on the tokenizer vocabulary. Always rely on `response.usage` for billing.

-------------------------------------------------------------------------------
4. WAYS TO REDUCE COSTS
-------------------------------------------------------------------------------
  - Enforce brevity (e.g., request JSON lines instead of paragraphs).
  - Lower `reasoning_effort` for routine or straightforward tasks.
  - Trim long chat histories to shrink input prompt size.
  - Use smaller model variants when performance benchmarks permit.
  - Evaluate whether few-shot prompt examples justify their recurring token overhead.
===============================================================================
"""

from groq import Groq

client = Groq()
for model in client.models.list().data:
    if model.id in ("openai/gpt-oss-20b", "openai/gpt-oss-120b"):
        per_million_in = float(model.pricing["prompt"]) * 1_000_000
        per_million_out = float(model.pricing["completion"]) * 1_000_000

        print(
            f"{model.id}: "
            f"${per_million_in:.3f} in, "
            f"${per_million_out:.2f} out, "
            "per million tokens"
        )
