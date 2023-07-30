# pylint: skip-file
import re
from decimal import Decimal
from pydantic import BaseModel, validator
from datetime import datetime


class NewStudent(BaseModel):
    # tbl_Pessoa
    nmPessoa: str
    ser: str
    tipoPessoa: str
    cpfCnpj: str
    rg: str = None
    ufRG: str = None
    empPersonal: bool
    dtNascimento: str = None
    dsObs: str = None
    dsEmail: str
    telefone: str = None
    # tbl_Aluno
    altura: int
    sexo: str
    tmCamisa: str = None
    fotoAluno: str = None
    ID_Empresa: int
    ID_Personal: int
    # tbl_peso
    peso: float = None
    dtData: datetime
    #tbl_fqCardio
    bpmRepouso: int = None
    bpmMaximo: int = None

    @validator("*", pre=True, always=True)
    def check_none(cls, v):
      if v == "string" or v == "":
        return None
      return v
    
    @validator('nmPessoa')
    def validate_nmPessoa(cls, value):
      if len(value) > 60:
        raise ValueError("Name can't be more than 60 characters.")
      return value
    
    @validator('cpfCnpj')
    def validate_cpfCnpj(cls, value):
      if len(value) > 11:
        raise ValueError("Cpf can't be more than 11 characters.")
      return value
    
    @validator('rg', 'ufRG')
    def validate_rg(cls, value):
      if value is not None and len(value) > 20:
        raise ValueError("Rg can't be more than 20 characters.")
      return value
    
    @validator('telefone')
    def validate_telefone(cls, value):
      if value is not None and len(value) > 11:
        raise ValueError("Telefone can't be more than 11 characters.")
      return value
    
    @validator('dsEmail')
    def validate_email(cls, value):
      regex = r'(?:[a-z0-9+!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
      if not re.match(regex, value, re.IGNORECASE):
        raise ValueError('Invalid email format')
      if len(value) > 80:
        raise ValueError("Email can't be more than 80 characters.")
      return value

    @validator('altura')
    def validate_altura(cls, value):
      if value < 0 or value > 250:
        raise ValueError("Altura must be between 0cm and 250cm.")
      altura_decimal = Decimal(str(value))
      if altura_decimal.as_tuple().exponent < -1:
        raise ValueError("Altura must have up to 1 decimal number.")
      return altura_decimal

    @validator('peso')
    def validate_peso(cls, value):
      if value is not None and (value < 0 or value > 600):
        raise ValueError("Peso must be between 0kg and 600kg.")
      if value is not None:
        peso_decimal = Decimal(str(value))
        if peso_decimal.as_tuple().exponent < -2:
          raise ValueError("Peso must have up to 2 decimal numbers.")
      return value

    @validator('bpmMaximo', 'bpmRepouso')
    def validate_bpm(cls, value):
      if value is not None and (value < 0 or value > 220):
        raise ValueError("BPM must be between 0bpm and 220bpm.")
      return value

    @validator('dsObs')
    def validate_dsObs(cls, value):
      if value is not None and len(value) > 300:
        raise ValueError("dsObs can't be more than 300 characters.")
      return value