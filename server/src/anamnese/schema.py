# pylint: skip-file
from typing import List
from pydantic import BaseModel, Field, constr, validator
from enum import IntEnum


class Period(IntEnum):
    MORNING = 1
    AFTERNOON = 2
    NIGHT = 3


class JsonQ4(BaseModel):
    training: bool
    time: str


class JsonQ13(BaseModel):
    day: str
    periods: List[Period]


class NewAnamnese(BaseModel):
    menstruation: bool = None
    iud: bool = None
    physical_limitation: constr(max_length=255)
    diabetes: bool
    hypertension: bool

    fc_repouso: int = Field(ge=0, le=220, default=None)
    fc_max: int = Field(ge=0, le=220)
    l1: int = Field(ge=0, le=220, default=None)
    l2: int = Field(ge=0, le=220, default=None)

    q1: constr(max_length=100)
    q2: constr(max_length=100) = None
    q3: constr(max_length=100)
    q4: JsonQ4
    q5: constr(max_length=255)
    q6: constr(max_length=255)
    q7: constr(max_length=255)
    q8: constr(max_length=100)
    q9: constr(max_length=100)
    q10: constr(max_length=100)
    q11: constr(max_length=100)
    q12: int = Field(ge=0, le=7)
    q13: List[JsonQ13]
    q14: bool
    q15: bool
    q16: constr(max_length=255)
    q17: int = Field(ge=1, le=10)
    q18: constr(max_length=100)
    q19: constr(max_length=100)
    q20: bool
    q21: constr(max_length=255) = None
    q22: constr(max_length=100)
    q23: constr(max_length=255)
    q24: bool
    q25: bool
    q26: constr(max_length=100)
    q27: constr(max_length=255) = None

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
        if value == "string" or value == "":
            return None
        return value
