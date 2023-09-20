# pylint: skip-file
from pydantic import BaseModel, Field, constr, validator
from ..base_model.types import evaluated_at, protocol


class NewCardio(BaseModel):
    weight: float = Field(g=0, le=600)
    cardio_protocol: protocol

    l1_ellestad_conconi: int = Field(ge=0, le=220, default=None)
    l2_ellestad_conconi: int = Field(ge=0, le=220, default=None)
    l1_fc_max_percentage: float = Field(ge=0, le=100, default=None)
    l2_fc_max_percentage: float = Field(ge=0, le=100, default=None)
    distance: int = Field(ge=0, le=10000, default=None)
    time: int = Field(ge=0, le=60, default=None)
    fc_5min: int = Field(ge=0, le=220, default=None)
    vo2max: float = Field(ge=0, le=5000, default=None)
    vo2max_absolute: float = Field(ge=0, le=1000, default=None)
    vo2max_mets: float = Field(ge=0, le=1500, default=None)
    vvo2max: float = Field(ge=0, le=999, default=None)
    vvo2max_pace: float = Field(ge=0, le=99, default=None)
    vl1: float = Field(ge=0, le=999, default=None)
    vl1_pace: float = Field(ge=0, le=99, default=None)
    vl2: float = Field(ge=0, le=999, default=None)
    vl2_pace: float = Field(ge=0, le=99, default=None)
    elder_aerobic_power: constr(max_length=18, strip_whitespace=True) = None
    weekly_caloric_expenditure: int = Field(ge=0, le=10000)
    daily_caloric_expenditure: int = Field(ge=0, le=2000)

    created_at: evaluated_at

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
        if value == "string" or value == "":
            return None
        return value


class UpdateCardio(BaseModel):
    cardio_protocol: protocol
