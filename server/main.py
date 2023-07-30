# pylint: skip-file
from kink import di

# bootstrap the config and db inside di[]
from .bootstrap import bootstrap
bootstrap()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .person.routes import person_router
from .cardio.routes import cardio_router
from .peso.routes import peso_router
from .student.routes import student_router
from .user.routes import user_router

from .person.models import Person


app = FastAPI()

# CORS Middleware validation
# who has access to the backend ↓

app.add_middleware(
    CORSMiddleware,
    allow_origins=di["ORIGINS"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# home
@app.get('/')
async def home():
    return "Conforfit Database"

app.include_router(user_router)
app.include_router(person_router)
app.include_router(cardio_router)
app.include_router(peso_router)
app.include_router(student_router)

# CPF-CNPJ
@app.get('/cpfCnpj/{cpf}')
async def count_cpf(cpf):  # how many of the specified CPF are in the database
    cpf = Person.where('cpfCnpj', cpf).count()
    return cpf


# RG-UF
@app.get('/rg/{rg}/{ufRG}')
async def count_rg(rg, ufRG):  # how many of the specified RG in UF are in the database
    rg = Person.where('rg', rg).where('ufRG', ufRG).count()
    return rg


# EMAIL
@app.get('/dsEmail/{dsEmail}')
async def count_email(dsEmail):  # how many of the specified Email are in the database
    email = Person.where('dsEmail', dsEmail).count()
    return email
