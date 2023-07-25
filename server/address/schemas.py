# pylint: skip-file
from pydantic import BaseModel, validator


class NewAddress(BaseModel):
    ID_Pessoa: int
    rua: str
    numero: int
    complemento: str = None
    bairro: str
    cidade: str
    estado: str
    CEP: str
    pais: str

    @validator("*", pre=True, always=True)
    def check_none(cls, v):
        if v == "string" or v == "":
            return None
        return v