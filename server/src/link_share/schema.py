# pylint: skip-file
from enum import Enum
from pydantic import BaseModel, validator


class Status(str, Enum):
    Available = 'Available'
    Expired = 'Expired'
    Used = 'Used'


class NewLinkShare(BaseModel):
    personal_id: int
    status: Status

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
        if value == "string" or value == "":
            return None
        return value


class UpdateLinkShare(BaseModel):
    status: Status

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
        if value == "string" or value == "":
            return None
        return value
