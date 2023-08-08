# pylint: skip-file
from typing import List, Optional
from pydantic import BaseModel, Field, constr


class JsonQ4(BaseModel):
    treinando: bool
    tempo: int = Field(ge=1, le=100)


class JsonQ13(BaseModel):
    day: str
    periods: Optional[List[int]] = Field(ge=1, le=3)


class NewAnamnese(BaseModel):
    q1: constr(max_length=255)
    q2: constr(max_length=100)
    q3: constr(max_length=100)
    q4: JsonQ4
    q5: constr(max_length=255)
    q6: constr(max_length=100)
    q7: constr(max_length=100)
    q8: constr(max_length=100)
    q9: constr(max_length=100)
    q10: constr(max_length=100)
    q11: constr(max_length=100)
    q12: int = Field(ge=0, le=7)
    q13: JsonQ13
    q14: bool
    q15: bool
    q16: constr(max_length=100)
    q17: int = Field(ge=1, le=10)
    q18: constr(max_length=100)
    q19: constr(max_length=100)
    q20: bool
    q21: constr(max_length=255) = None
    q22: constr(max_length=100)
    q23: constr(max_length=100)
    q24: constr(max_length=100)
    q25: constr(max_length=100)
    q26: constr(max_length=100)
    q27: constr(max_length=255) = None
