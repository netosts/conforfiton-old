# pylint: skip-file
import re
from enum import Enum
from pydantic import BaseModel, validator, constr
from datetime import date, timedelta, datetime


class Roles(str, Enum):
    Admin = 'Admin'
    Guest = 'Guest'


class NewGlobalEntity(BaseModel):
    name: constr(max_length=100, strip_whitespace=True)
    role: Roles
    email: constr(
        max_length=255,
        strip_whitespace=True,
        pattern=r'(?:[a-z0-9+!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
    )
    phone_number: constr(max_length=20, strip_whitespace=True)
    birth_date: date

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
