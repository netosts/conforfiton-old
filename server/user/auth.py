# pylint: skip-file
from orator import DatabaseManager
from orator.exceptions import IntegrityError
from typing import Type

from fastapi import status
from fastapi.exceptions import HTTPException

from passlib.context import CryptContext
from jose import jwt, JWTError

from .models import User
from .schemas import NewUser

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class UserUseCases:
    def __init__(self, db: Type[DatabaseManager]):
        self.db = db
      
    
    def user_register(self, user: NewUser):
        user_model = User(
            username=user.username,
            password=pwd_context.hash(user.password)
        )
        try:
            user_model.save()
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='User already exists'
            )