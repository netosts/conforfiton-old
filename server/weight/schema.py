# pylint: skip-file
from pydantic import BaseModel, Field

from ..base_model.types import created_at


class NewWeight(BaseModel):
    weight: float = Field(ge=0, le=600)
    created_at: created_at
