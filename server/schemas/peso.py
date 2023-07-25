# pylint: skip-file
from pydantic import BaseModel
from datetime import datetime


class NewPeso(BaseModel):
    ID_Pessoa: int
    peso: float
    dtData: datetime