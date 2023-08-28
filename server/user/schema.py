# pylint: skip-file
from pydantic import BaseModel, validator, constr


class NewUser(BaseModel):
    password: constr(
        regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})')

    @validator("*", pre=True, always=True)
    def check_none(cls, value):
        if value == "string" or value == "":
            return None
        return value
