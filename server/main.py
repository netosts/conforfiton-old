# pylint: skip-file
from datetime import date
from pydantic import BaseModel, validator
from bootstrap import bootstrap
from kink import di

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

bootstrap()
from models.person import Person

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class NewPerson(BaseModel):
    nmPessoa: str
    ativo: bool = None
    ser: str
    tipoPessoa: str
    cpfCnpj: str
    rg: str = None
    ufRG: str = None
    dsRazaoSocial: str = None
    dsInscricaoEstadual: str = None
    dsInscricaoMunicipal: str = None
    isentoIE: bool = None
    dtNascimento: date
    dsObs: str = None
    dsEmail: str = None
    telefone: str = None

    @validator("*", pre=True, always=True)
    def check_none(cls, v):
        return v if v != "string" else None


@app.get('/')
async def home():
    return "hello world 222"


@app.get('/person/{person_id}')
async def find_person(person_id):
    person = Person.find(person_id)
    return person.serialize()


@app.get('/persons')
async def list_persons():
    query = di["db"].table('tbl_Pessoa').order_by('ID_Pessoa')
    persons = query.get()
    return persons.serialize()


@app.post('/person')
async def new_person(data: NewPerson):
    person = Person()
    person.nmPessoa = data.nmPessoa
    person.ativo = data.ativo
    person.ser = data.ser
    person.tipoPessoa = data.tipoPessoa
    person.cpfCnpj = data.cpfCnpj
    person.rg = data.rg
    person.ufRG = data.ufRG
    person.dsRazaoSocial = data.dsRazaoSocial
    person.dsInscricaoEstadual = data.dsInscricaoEstadual
    person.dsInscricaoMunicipal = data.dsInscricaoMunicipal
    person.isentoIE = data.isentoIE
    person.dtNascimento = data.dtNascimento
    person.dsObs = data.dsObs
    person.dsEmail = data.dsEmail
    person.telefone = data.telefone
    person.save()
    return "OK! Pessoa criada na tabela 'tbl_Pessoa'..."


@app.put('/person/{person_id}')
async def find_person(person_id, data: NewPerson):
    person = Person.find(person_id)
    person.nmPessoa = data.nmPessoa
    person.ativo = data.ativo
    person.ser = data.ser
    person.tipoPessoa = data.tipoPessoa
    person.cpfCnpj = data.cpfCnpj
    person.rg = data.rg
    person.ufRG = data.ufRG
    person.dsRazaoSocial = data.dsRazaoSocial
    person.dsInscricaoEstadual = data.dsInscricaoEstadual
    person.dsInscricaoMunicipal = data.dsInscricaoMunicipal
    person.isentoIE = data.isentoIE
    person.dtNascimento = data.dtNascimento
    person.dsObs = data.dsObs
    person.dsEmail = data.dsEmail
    person.telefone = data.telefone
    person.save()

    return person.serialize()


@app.delete('/person/{person_id}')
async def delete_person(person_id):
    person = Person.find(person_id)
    personName = person.nmPessoa
    person.delete()

    return f"{personName} foi deletado!"