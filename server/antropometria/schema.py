# pylint: skip-file
from typing import List
from decimal import Decimal
from pydantic import BaseModel, Field, constr, validator
from ..base_model.types import created_at


class JsonCA_Risk(BaseModel):
    dc: str
    diabetes_ii: str
    hypertension: str
    cancer: str
    depression: str
    metabolic_syndrome: str


class NewAntropometria(BaseModel):
    weight: float = Field(g=0, le=600)

    antropometria_protocol: constr(max_length=21, strip_whitespace=True)
    abs: float = Field(ge=0, le=999)
    waist: float = Field(ge=0, le=999)
    hip: float = Field(ge=0, le=999)
    thighs: float = Field(ge=0, le=999, default=None)
    right_biceps: float = Field(ge=0, le=999, default=None)
    right_forearm: float = Field(ge=0, le=999, default=None)
    chest: float = Field(ge=0, le=999, default=None)
    triceps: float = Field(ge=0, le=999, default=None)
    suprailiac: float = Field(ge=0, le=999, default=None)
    subcapularis: float = Field(ge=0, le=999, default=None)
    midaxillary: float = Field(ge=0, le=999, default=None)

    imc_result: float = Field(ge=0, le=200)
    imc_class: constr(max_length=30, strip_whitespace=True)
    ca_class: constr(max_length=30, strip_whitespace=True)
    ca_risk: List[JsonCA_Risk] = None
    rcq_result: float = Field(ge=0, le=200)
    rcq_class: constr(max_length=30, strip_whitespace=True)
    rcae_class: constr(max_length=30, strip_whitespace=True)
    iac_result: float = Field(ge=0, le=200)
    iac_class: constr(max_length=30, strip_whitespace=True)
    pg_result: float = Field(ge=0, le=100)
    pg_class: constr(max_length=30, strip_whitespace=True)

    created_at: created_at

    @validator('weight', 'abs', 'waist', 'hip', 'thighs', 'right_biceps', 'right_forearm', 'chest', 'triceps', 'suprailiac', 'subcapularis', 'midaxillary', 'rcq_result')
    def validate_weight(cls, value):
        if value is not None:
            decimal = Decimal(str(value))
            if decimal.as_tuple().exponent < -2:
                raise ValueError("Values must have up to 2 decimal numbers.")
        return value

    @validator('imc_result', 'iac_result', 'pg_result')
    def validate_weight(cls, value):
        if value is not None:
            decimal = Decimal(str(value))
            if decimal.as_tuple().exponent < -1:
                raise ValueError("Values must have up to 1 decimal numbers.")
        return value
