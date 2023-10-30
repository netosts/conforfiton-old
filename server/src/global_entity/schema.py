# pylint: skip-file
import re
from enum import Enum
from pydantic import BaseModel, validator
from datetime import timedelta, datetime

from ..base_model.types import name, email, phone_number, birth_date


class Roles(str, Enum):
    Admin = 'Admin'
    Guest = 'Guest'
    Owner = 'Owner'
    Demo = 'Demo'


class NewGlobalEntity(BaseModel):
    name: name
    role: Roles
    email: email
    phone_number: phone_number
    birth_date: birth_date

    @validator("*")
    def check_none(cls, value):
        if value == "string" or value == 'stringstrin' or value == "":
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
