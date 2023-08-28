# pylint: skip-file
from pydantic import BaseModel


class NewWeight(BaseModel):
    peso: float
