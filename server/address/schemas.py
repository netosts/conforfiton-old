# pylint: skip-file
from pydantic import BaseModel, validator


class NewAddress(BaseModel):
    id_pessoa: int
    rua: str
    numero: int
    complemento: str = None
    bairro: str
    cidade: str
    estado: str
    cep: str
    pais: str

    @validator("*", pre=True, always=True)
    def check_none(cls, v):
        if v == "string" or v == "":
            return None
        return v