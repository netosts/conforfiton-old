# pylint: skip-file
from pydantic import BaseModel
from datetime import datetime


class NewCardio(BaseModel):
    bpmRepouso: int
    bpmMaximo: int
    dtData: datetime