# pylint: skip-file
from pydantic import BaseModel, Field

from ..base_model.types import created_at


class NewNeuromuscular(BaseModel):
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

    created_at: created_at
