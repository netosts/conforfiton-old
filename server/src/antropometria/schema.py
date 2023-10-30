# pylint: skip-file
from pydantic import BaseModel, Field, constr, validator
from ..base_model.types import evaluated_at, protocol


class JsonCARisk(BaseModel):
    dc: float = Field(ge=0, le=999)
    diabetes_ii: float = Field(ge=0, le=999)
    hypertension: float = Field(ge=0, le=999)
    cancer: float = Field(ge=0, le=999)
    depression: float = Field(ge=0, le=999)
    metabolic_syndrome: float = Field(ge=0, le=999)


class NewAntropometria(BaseModel):
    weight: float = Field(g=0, le=600)
    antropometria_protocol: protocol

    # required
    abdominal_circumference: float = Field(ge=0, le=999)
    waist_circumference: float = Field(ge=0, le=999)
    hip_circumference: float = Field(ge=0, le=999)
    # nullable
    thighs_circumference: float = Field(ge=0, le=999, default=None)
    right_biceps_circumference: float = Field(ge=0, le=999, default=None)
    right_forearm_circumference: float = Field(ge=0, le=999, default=None)
    chest_skin_fold: float = Field(ge=0, le=999, default=None)
    abdominal_skin_fold: float = Field(ge=0, le=999, default=None)
    thighs_skin_fold: float = Field(ge=0, le=999, default=None)
    triceps_skin_fold: float = Field(ge=0, le=999, default=None)
    suprailiac_skin_fold: float = Field(ge=0, le=999, default=None)
    subscapularis_skin_fold: float = Field(ge=0, le=999, default=None)
    midaxillary_skin_fold: float = Field(ge=0, le=999, default=None)
    iliac_circumference: float = Field(ge=0, le=999, default=None)

    imc_result: float = Field(ge=0, le=99)
    imc_class: constr(max_length=30, strip_whitespace=True)
    ca_class: constr(max_length=30, strip_whitespace=True)
    ca_risk: JsonCARisk = None
    rcq_result: float = Field(ge=0, le=9)
    rcq_class: constr(max_length=30, strip_whitespace=True)
    rcae_result: float = Field(ge=0, le=2)
    rcae_class: constr(max_length=30, strip_whitespace=True)
    iac_result: float = Field(ge=0, le=99)
    iac_class: constr(max_length=30, strip_whitespace=True)
    pg_result: float = Field(ge=0, le=99)
    pg_class: constr(max_length=30, strip_whitespace=True)

    weight_goal: float = Field(ge=0, le=600)
    pg_goal: float = Field(ge=0, le=99)
    mig_result: float = Field(ge=0, le=99)
    mig_goal: int = Field(ge=0, le=100)
    fat_weight_result: float = Field(ge=0, le=200)
    fat_weight_goal: float = Field(ge=0, le=99)
    mig_weight_result: float = Field(ge=0, le=200)
    mig_weight_goal: float = Field(ge=0, le=200)

    created_at: evaluated_at

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
        if value == "string" or value == "":
            return None
        return value


class UpdateAntropometria(BaseModel):
    antropometria_protocol: protocol
