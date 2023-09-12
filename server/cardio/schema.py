# pylint: skip-file
from pydantic import BaseModel, Field, constr, validator
from ..base_model.types import created_at


class NewCardio(BaseModel):
    weight: float = Field(g=0, le=600)
    cardio_protocol: constr(max_length=21, strip_whitespace=True)

    created_at: created_at

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
        if value == "string" or value == "":
            return None
        return value


class UpdateCardio(BaseModel):
    cardio_protocol: constr(max_length=21, strip_whitespace=True)
