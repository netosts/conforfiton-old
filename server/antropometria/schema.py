# pylint: skip-file
from decimal import Decimal
from pydantic import BaseModel, Field, constr, validator
from ..base_model.types import created_at


class JsonCARisk(BaseModel):
    dc: float = Field(ge=0, le=999)
    diabetes_ii: float = Field(ge=0, le=999)
    hypertension: float = Field(ge=0, le=999)
    cancer: float = Field(ge=0, le=999)
    depression: float = Field(ge=0, le=999)
    metabolic_syndrome: float = Field(ge=0, le=999)


class NewAntropometria(BaseModel):
    weight: float = Field(g=0, le=600)
    antropometria_protocol: constr(max_length=21, strip_whitespace=True)

    # required
    abdominal_circumference: float = Field(ge=0, le=999)
    waist_circumference: float = Field(ge=0, le=999)
    hip_circumference: float = Field(ge=0, le=999)
    # nullable
    thighs_circumference: float = Field(ge=0, le=999, default=None)
    right_biceps_circumference: float = Field(ge=0, le=999, default=None)
    right_forearm_circumference: float = Field(ge=0, le=999, default=None)
    chest_skinfold: float = Field(ge=0, le=999, default=None)
    abdominal_skinfold: float = Field(ge=0, le=999, default=None)
    thighs_skinfold: float = Field(ge=0, le=999, default=None)
    triceps_skinfold: float = Field(ge=0, le=999, default=None)
    suprailiac_skinfold: float = Field(ge=0, le=999, default=None)
    subscapularis_skinfold: float = Field(ge=0, le=999, default=None)
    midaxillary_skinfold: float = Field(ge=0, le=999, default=None)
    iliac_circumference: float = Field(ge=0, le=999, default=None)

    imc_result: float = Field(ge=0, le=99)
    imc_class: constr(max_length=30, strip_whitespace=True)
    ca_class: constr(max_length=30, strip_whitespace=True)
    ca_risk: JsonCARisk = None
    rcq_result: float = Field(ge=0, le=9)
    rcq_class: constr(max_length=30, strip_whitespace=True)
    rcae_class: constr(max_length=30, strip_whitespace=True)
    iac_result: float = Field(ge=0, le=99)
    iac_class: constr(max_length=30, strip_whitespace=True)
    pg_result: float = Field(ge=0, le=100)
    pg_class: constr(max_length=30, strip_whitespace=True)

    created_at: created_at

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
        if value == "string" or value == "":
            return None
        return value

    @validator(
        'abdominal_circumference',
        'waist_circumference',
        'hip_circumference',
        'thighs_circumference',
        'right_biceps_circumference',
        'right_forearm_circumference',
        'chest_skinfold',
        'abdominal_skinfold',
        'thighs_skinfold',
        'triceps_skinfold',
        'suprailiac_skinfold',
        'subscapularis_skinfold',
        'midaxillary_skinfold',
        'iliac_circumference',
        'imc_result',
        'rcq_result',
        'iac_result',
    )
    def validate_two_decimals(cls, value):
        if value is not None:
            decimal = Decimal(str(value))
            if decimal.as_tuple().exponent < -2:
                raise ValueError("Values must have up to 2 decimal numbers.")
        return value

    @validator('pg_result')
    def validate_one_decimal(cls, value):
        if value is not None:
            decimal = Decimal(str(value))
            if decimal.as_tuple().exponent < -1:
                raise ValueError("Values must have up to 1 decimal number.")
        return value


class UpdateAntropometria(BaseModel):
    antropometria_protocol: constr(max_length=21, strip_whitespace=True)
