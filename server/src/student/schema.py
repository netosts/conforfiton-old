# pylint: skip-file
import re
from enum import Enum
from pydantic import BaseModel, validator, Field
from datetime import timedelta, datetime

from ..base_model.types import name, cpf, Genders, email, phone_number, birth_date, shirt_size, shorts_size, created_at


class Roles(str, Enum):
    Student = 'Student'


class NewStudent(BaseModel):
    name: name
    cpf: cpf
    gender: Genders
    role: Roles
    email: email
    phone_number: phone_number
    birth_date: birth_date
    shirt_size: shirt_size
    shorts_size: shorts_size
    address_picture: str = None

    height: int = Field(ge=100, le=250)
    weight: float = Field(ge=0, le=600)
    created_at: created_at

    personal_id: int

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


class EditStudent(BaseModel):
    name: name
    cpf: cpf
    phone_number: phone_number
    email: email
    gender: Genders
    birth_date: birth_date
    shirt_size: shirt_size
    shorts_size: shorts_size

    height: int = Field(ge=100, le=250)

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
