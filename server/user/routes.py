# pylint: skip-file
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from ..person.models import Person
from .schemas import NewUser
from .models import User

from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 30

user_router = APIRouter(prefix='/user')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/token")


class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: str


# Authenticate User FUNCTIONS
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(username: str):
    user = User.where('username', username).first()
    if user:
        user = user.serialize()
    return user


def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.get("hashed_password")):
        return False
    return user
    

# Token FUNCTIONS
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         user_id: int = payload.get("id")
#         if username is None or user_id is None:
#             raise credentials_exception
#         return {'id': user_id, 'username': username }
#     except JWTError:
#         raise credentials_exception


# @user_router.get('/verify')
# async def verify_current_user(current_user: NewUser = Depends(get_current_user)):
#     return current_user


@user_router.post('/register')
async def new_user(data: NewUser):
    vl_person = Person.where('ID_Pessoa', data.ID_Pessoa).count()
    if vl_person == 0:
        error_message = {
            "error": "Person doesn't exist",
            "message": "Person with specified ID does not exist."
        }
        return JSONResponse(content=error_message, status_code=404)

    user = User()
    user.ID_Pessoa = data.ID_Pessoa
    user.username = data.username
    user.hashed_password = pwd_context.hash(data.hashed_password)
    user.save()

    return f"{user.username} foi cadastrado(a) com sucesso."


@user_router.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.get("username"), "id": user.get("ID_Pessoa")}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer", "user_id": user.get("ID_Pessoa")}