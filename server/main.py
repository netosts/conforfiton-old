# pylint: skip-file
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from kink import di

# bootstrap config
# autopep8: off

from .bootstrap import bootstrap
bootstrap()

from .global_entity.routes import global_entity_router
from .company.routes import company_router
from .person.routes import person_router
from .weight.routes import weight_router
from .student.routes import student_router
from .user.routes import user_router
from .anamnese.routes import anamnese_router
from .rm_config.routes import rm_router
from .neuromuscular.routes import neuromuscular_router
from .personal.routes import personal_router

from .person.model import Person

# autopep8: on


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


@app.get('/')
async def home():
    return "Conforfit Database"

app.include_router(company_router)
app.include_router(global_entity_router)
app.include_router(user_router)
app.include_router(person_router)
app.include_router(student_router)
app.include_router(weight_router)
app.include_router(anamnese_router)
app.include_router(rm_router)
app.include_router(neuromuscular_router)
app.include_router(personal_router)


@app.get('/cpf/{cpf}')  # CPF
async def count_cpf(cpf):  # how many of the specified CPF are in the database
    cpf = Person.where('cpf', cpf).count()
    return cpf


@app.get('/email/{email}')  # EMAIL
async def count_email(email):  # how many of the specified Email are in the database
    email = Person.where('email', email).count()
    return email


@app.get('/phone_number/{phone_number}')  # PHONE_NUMBER
# how many of the specified Phone number are in the database
async def count_phone_number(phone_number):
    phone_number = Person.where('phone_number', phone_number).count()
    return phone_number
