import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

models = client.models.list()
# print(models)
for model in models.data:
    print(model.id)

for owner in models.data:
    print(owner.owned_by)
models = {
    model.id: model
    for model in client.models.list().data
}

for name in ["openai/gpt-oss-20b", "openai/gpt-oss-120b"]:
    model = models[name]
    print(
        name,
        "| made by", model.owned_by,
        "| weights:", model.hugging_face_id
    )
print(model.context_window)
