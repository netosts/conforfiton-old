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
    regex=r'[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$'
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
