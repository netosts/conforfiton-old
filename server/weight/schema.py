# pylint: skip-file
from pydantic import BaseModel, Field


class NewWeight(BaseModel):
    weight: float = Field(ge=0, le=600)
