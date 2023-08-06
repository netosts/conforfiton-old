# pylint: skip-file
import re
from pydantic import BaseModel, validator


class NewPerson(BaseModel):
    nm_pessoa: str
    ser: str
    tipo_pessoa: str
    cpf_cnpj: str
    rg: str = None
    uf_rg: str = None
    emp_personal: bool
    dt_nascimento: str = None
    ds_obs: str = None
    ds_email: str
    telefone: str = None

    @validator("*", pre=True, always=True)
    def check_none(cls, v):
      if v == "string" or v == "":
        return None
      return v
    
    @validator('nm_pessoa')
    def validate_nm_pessoa(cls, value):
      if len(value) > 60:
        raise ValueError("Name can't be more than 60 characters.")
      return value
    
    @validator('cpf_cnpj')
    def validate_cpf_cnpj(cls, value):
      if len(value) > 11:
        raise ValueError("Cpf can't be more than 11 characters.")
      return value
    
    @validator('rg')
    def validate_rg(cls, value, values):
      if value is not None and values.get('uf_rg') is None:
        raise ValueError("RG and UF must be together")
      if value is None and values.get('uf_rg') is not None:
        raise ValueError("RG and UF must be together")
      if value is not None and len(value) > 20:
        raise ValueError("Rg can't be more than 20 characters.")
      return value
    
    @validator('telefone')
    def validate_telefone(cls, value):
      if value is not None and len(value) > 11:
        raise ValueError("Telefone can't be more than 11 characters.")
      return value
    
    @validator('ds_email')
    def validate_email(cls, value):
      regex = r'(?:[a-z0-9+!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
      if not re.match(regex, value, re.IGNORECASE):
        raise ValueError('Invalid email format')
      if len(value) > 80:
        raise ValueError("Email can't be more than 80 characters.")
      return value

    @validator('ds_obs')
    def validate_ds_obs(cls, value):
      if value is not None and len(value) > 300:
        raise ValueError("dsObs can't be more than 300 characters.")
      return value