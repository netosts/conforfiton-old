# pylint: skip-file
import re
from pydantic import BaseModel, validator


class NewUser(BaseModel):
    ID_Pessoa: int
    username: str
    hashed_password: str

    @validator('username')
    def validate_username(cls, username):
        regex = r'^[a-zA-Z0-9_-]{3,20}$'
        if not re.match(regex, username):
            raise ValueError("Invalid username. It must be 3 to 20 characters long and can contain only alphanumeric characters, underscore, or hyphen.")
        
        return username
    
    @validator('hashed_password')
    def validate_hashed_password(cls, hashed_password):
        regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})'
        if not re.match(regex, hashed_password):
            raise ValueError("Invalid hashed_password. It must contain at least one lowercase letter, one uppercase letter, one numeric character, one special character, and must be eight characters or longer.")
        
        return hashed_password