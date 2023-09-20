# pylint: skip-file
from pydantic import BaseModel, validator

from ..base_model.types import email, phone_number


class NewCompany(BaseModel):
    brand_name: str
    business_name: str
    # cnpj: None
    # exempt_sr: None
    # state_registration: None
    # uf: None
    # email: None
    # phone_number: None

    @validator("*")
    def check_none(cls, value):
        if value == "string" or value == 'stringstrin' or value == "":
            return None
        return value
