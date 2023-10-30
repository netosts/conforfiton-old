# pylint: skip-file
from kink import di
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from jose import jwt
from passlib import pwd
from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel

from ..person.model import Person
from .schema import NewUser
from .model import User


user_router = APIRouter(prefix='/user')

pwd_context = pbkdf2_sha256
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/token")


class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: str


# Authenticate User FUNCTIONS
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(email: str):
    user = Person.select('id', 'email', 'users.salt_password', 'users.hash_password').where('email', email).join(
        'users', 'users.person_id', '=', 'persons.id').first()
    return user


def authenticate_user(email: str, password: str):
    user = get_user(email)
    if not user:
        return False
    if not verify_password(password+":"+user.salt_password, user.hash_password):
        return False
    return user


# Token FUNCTIONS
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, di["SECRET_KEY"], algorithm=di["ALGORITHM"])


# def get_current_user(token: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, di["SECRET_KEY"], algorithms=[di["ALGORITHM"]])
#         email: str = payload.get("sub")
#         user_id: int = payload.get("id")
#         if email is None or user_id is None:
#             raise credentials_exception
#         return {'id': user_id, 'email': email }
#     except JWTError:
#         raise credentials_exception


# @user_router.get('/verify')
# async def verify_current_user(current_user: NewUser = Depends(get_current_user)):
#     return current_user


# REGISTER
@user_router.post('/register/{email}')
async def new_user(email, data: NewUser):
    person = Person.select('id', 'name').where(
        'email', email).first()
    if not person:
        return JSONResponse({
            "error": True,
            "data": "Person with specified ID does not exist."
        }, 404)

    user = User()
    user.person_id = person.id
    salt = pwd.genword(entropy=56, charset="ascii_62")
    user.hash_password = pwd_context.hash(data.password+":"+salt)
    user.salt_password = salt

    if user.save():
        return JSONResponse({
            "error": False,
            "data": f"{person.name} User was successfully registered."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong while registering {person.name}'s User."
        }, 422)


# LOGIN
@user_router.post('/token', response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=di["ACCESS_TOKEN_EXP"])
    access_token = create_access_token(
        data={"sub": user.email, "id": user.id}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer", "user_id": user.id}
