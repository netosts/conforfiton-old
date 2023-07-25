# pylint: skip-file
from pydantic import BaseModel
from datetime import datetime


class NewFqCardio(BaseModel):
    ID_Pessoa: int
    bpmRepouso: int
    bpmMaximo: int
    dtData: datetime