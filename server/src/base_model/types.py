# pylint: skip-file
from enum import Enum
from pydantic import constr
from datetime import datetime, date


class Genders(str, Enum):
    Male = 'Male'
    Female = 'Female'


name = constr(max_length=100, strip_whitespace=True)
cpf = constr(min_length=11, max_length=11)
email = constr(
    max_length=255,
    strip_whitespace=True,
    regex=r'(?:[a-z0-9+!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
)
phone_number = constr(
    min_length=11,
    max_length=11,
    strip_whitespace=True,
    regex=r'^\d{11}$'
)
birth_date = str
shirt_size = constr(max_length=3, strip_whitespace=True)
shorts_size = constr(max_length=8, strip_whitespace=True)

created_at = datetime
evaluated_at = date

protocol = constr(max_length=50, strip_whitespace=True)
