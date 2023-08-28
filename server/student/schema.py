# pylint: skip-file
import re
from decimal import Decimal
from enum import Enum
from pydantic import BaseModel, validator, constr, Field
from datetime import date, timedelta, datetime


class Genders(str, Enum):
    Male = 'Male'
    Female = 'Female'


class Roles(str, Enum):
    Student = 'Student'


class NewStudent(BaseModel):
    name: constr(max_length=100, strip_whitespace=True)
    cpf: constr(min_length=11, max_length=11)
    gender: Genders
    role: Roles
    email: constr(
        max_length=255,
        strip_whitespace=True,
        regex=r'(?:[a-z0-9+!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
    )
    phone_number: constr(max_length=20, strip_whitespace=True)
    birth_date: date
    height: int = Field(ge=0, le=250)
    shirt_size: constr(max_length=3, strip_whitespace=True)
    shorts_size: constr(max_length=3, strip_whitespace=True)
    profile_picture: str = None

    weight: float = Field(ge=0, le=600)

    # id of company and/or personal
    company_id: int = None
    personal_id: int = None

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
        if value == "string" or value == "":
            return None
        return value

    @validator('birth_date')
    def validate_birth_date(cls, value):
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

    @validator('weight')
    def validate_weight(cls, value):
        if value is not None:
            peso_decimal = Decimal(str(value))
            if peso_decimal.as_tuple().exponent < -2:
                raise ValueError("Weight must have up to 2 decimal numbers.")
        return value
