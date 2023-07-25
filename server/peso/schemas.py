# pylint: skip-file
from pydantic import BaseModel
from datetime import datetime


class NewPeso(BaseModel):
    peso: float
    dtData: datetime