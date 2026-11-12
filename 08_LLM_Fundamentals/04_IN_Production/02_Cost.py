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
