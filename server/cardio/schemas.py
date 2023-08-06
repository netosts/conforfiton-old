# pylint: skip-file
from pydantic import BaseModel
from datetime import datetime


class NewCardio(BaseModel):
    bpm_repouso: int
    bpm_maximo: int
    dt_data: datetime