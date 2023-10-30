# pylint: skip-file
from pydantic import BaseModel, Field, constr

from ..base_model.types import evaluated_at, protocol


class NewNeuromuscular(BaseModel):
    neuromuscular_protocol: protocol

    bench_press_lifted: int = Field(ge=0, le=800)
    bench_press_reps: int = Field(ge=0, le=15)
    bench_press_rm: float = Field(ge=0, le=1231)
    bench_press_points: int = Field(ge=0, le=10)

    barbell_curl_lifted: int = Field(ge=0, le=100)
    barbell_curl_reps: int = Field(ge=0, le=15)
    barbell_curl_rm: float = Field(ge=0, le=154)
    barbell_curl_points: int = Field(ge=0, le=10)

    pull_down_lifted: int = Field(ge=0, le=200)
    pull_down_reps: int = Field(ge=0, le=15)
    pull_down_rm: float = Field(ge=0, le=304)
    pull_down_points: int = Field(ge=0, le=10)

    leg_press_lifted: int = Field(ge=0, le=1000)
    leg_press_reps: int = Field(ge=0, le=15)
    leg_press_rm: float = Field(ge=0, le=1539)
    leg_press_points: int = Field(ge=0, le=10)

    leg_extension_lifted: int = Field(ge=0, le=300)
    leg_extension_reps: int = Field(ge=0, le=15)
    leg_extension_rm: float = Field(ge=0, le=462)
    leg_extension_points: int = Field(ge=0, le=10)

    leg_curl_lifted: int = Field(ge=0, le=250)
    leg_curl_reps: int = Field(ge=0, le=15)
    leg_curl_rm: float = Field(ge=0, le=385)
    leg_curl_points: int = Field(ge=0, le=10)

    total_points: int = Field(ge=0, le=60)
    classification: constr(max_length=15, strip_whitespace=True)

    created_at: evaluated_at


class UpdateNeuromuscular(BaseModel):
    neuromuscular_protocol: protocol


class NewNeuromuscularRml(BaseModel):
    neuromuscular_protocol: protocol

    sit_up: int = Field(ge=0, le=999, default=None)
    push_up: int = Field(ge=0, le=999, default=None)
    jump: int = Field(ge=0, le=999, default=None)

    sit_up_result: constr(max_length=15, strip_whitespace=True) = None
    push_up_result: constr(max_length=15, strip_whitespace=True) = None
    jump_result: constr(max_length=15, strip_whitespace=True) = None

    created_at: evaluated_at
