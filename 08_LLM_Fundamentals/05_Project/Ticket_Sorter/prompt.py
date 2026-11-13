from typing import Literal
from pydantic import BaseModel, ValidationError, Field


class Tragia(BaseModel):
    category: Literal["billing", "shipping", "other"]
    priority: int = Field(ge=1, le=5)


def check(answer):
    try:
        return Tragia.model_validate_json(answer)
    except ValidationError:
        return None


FORMAT = """Reply with one line of JSON and nothing else,like this :
{
"category":"shipping","priority":3
}
priority is 1(can wait) to 5(urgent).
"""

BEFORE = """You sort customer support tickets for an online shop.
Categories:
-billing:payments,charges,refunds
-shipping:parcels,delivery,damaged boxes
-other:anything else
""" + FORMAT
