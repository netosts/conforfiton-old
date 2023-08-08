# pylint: skip-file
import re
from decimal import Decimal
from pydantic import BaseModel, validator
from datetime import datetime, timedelta


class NewStudent(BaseModel):
    # tbl_pessoa
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
    # tbl_aluno
    altura: int
    sexo: str
    tm_camisa: str = None
    tm_shorts: str = None
    foto_aluno: str = None
    id_empresa: int
    id_personal: int
    # tbl_peso
    peso: float = None
    dt_data: datetime

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
      if value == "string" or value == "":
        return None
      return value
    
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
    
    @validator('rg', 'uf_rg')
    def validate_rg(cls, value):
      if value is not None and len(value) > 20:
        raise ValueError("Rg can't be more than 20 characters.")
      return value
    
    @validator('dt_nascimento')
    def validate_dat_of_birth(cls, value):
      date_pattern = r"^\d{4}-\d{2}-\d{2}$"
      if not re.match(date_pattern, value):
        raise ValueError("Date format is invalid.")
      parts = value.split("-")
      year = int(parts[0])
      month = int(parts[1])
      day = int(parts[2])
      current_date = datetime.now()
      input_date = datetime(year, month, day)
      max_age_date = current_date - timedelta(days=365 * 120)
      if input_date > current_date:
        raise ValueError("Age is invalid.")
      if input_date < max_age_date:
        raise ValueError("Maximum age exceeded.")
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

    @validator('ds_obs')
    def validate_ds_obs(cls, value):
      if value is not None and len(value) > 300:
        raise ValueError("ds_obs can't be more than 300 characters.")
      return value