# pylint: skip-file
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from kink import di

# bootstrap config
# autopep8: off

from .bootstrap import bootstrap
bootstrap()

from .person.routes import person_router
from .weight.routes import peso_router
from .student.routes import student_router
from .user.routes import user_router
from .anamnese.routes import anamnese_router
from .rm_config.routes import rm_router

from .person.models import Person

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

app.include_router(user_router)
app.include_router(person_router)
app.include_router(peso_router)
app.include_router(student_router)
app.include_router(anamnese_router)
app.include_router(rm_router)


@app.get('/cpf_cnpj/{cpf}')  # CPF
async def count_cpf(cpf):  # how many of the specified CPF are in the database
    cpf = Person.where('cpf_cnpj', cpf).count()
    return cpf


@app.get('/rg/{rg}/{uf_rg}')  # RG in UF
async def count_rg(rg, uf_rg):  # how many of the specified RG in UF are in the database
    rg = Person.where('rg', rg).where('uf_rg', uf_rg).count()
    return rg


@app.get('/ds_email/{ds_email}')  # EMAIL
async def count_email(ds_email):  # how many of the specified Email are in the database
    email = Person.where('ds_email', ds_email).count()
    return email
