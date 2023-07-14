# pylint: skip-file
from datetime import date, datetime
from pydantic import BaseModel, validator
from typing import Union
import json
from kink import di

# bootstrap the config and db inside di[]
from bootstrap import bootstrap
bootstrap()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.person import Person
from models.student import Student
from models.peso import Peso

app = FastAPI()

# CORS Middleware validation
# who has access to the backend ↓
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


# Base Models
# base model for students
class NewStudent(BaseModel):
    # tbl_Pessoa
    nmPessoa: str
    ser: str
    tipoPessoa: str
    cpfCnpj: str
    rg: str = None
    ufRG: str = None
    dtNascimento: date = None
    dsObs: str = None
    dsEmail: str = None
    telefone: str = None
    # tbl_Aluno
    altura: int
    sexo: str
    fotoAluno: Union[dict, str] = None
    # tbl_peso
    peso: float = None
    dtData: datetime

    @validator("*", pre=True, always=True)
    def check_none(cls, v):
        if v == "string" or v == "":
            return None
        if isinstance(v, dict):
            return json.dumps(v)
        return v


# base model for pesos
class NewPeso(BaseModel):
    ID_Pessoa: int
    peso: float
    dtData: datetime


# Variables for query
def type_search(inputFilter):
        if inputFilter == 'inputName':
            return "nmPessoa"
        elif inputFilter == 'inputCpf':
            return "cpfCnpj"


# home
@app.get('/')
async def home():
    return "hello world"


# ------------------------------------------------------------------------------
# Students
@app.get('/students/{inputFilter}/{inputBar}')  # list all students
async def list_students(inputFilter, inputBar):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    max_peso = di["db"].raw('tp2."ID_Pessoa" and tp2."dtData" = (select max("dtData") from tbl_peso where "ID_Pessoa" = tp2."ID_Pessoa")')

    students = di["db"].table('tbl_Pessoa as tp') \
                       .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', max_peso) \
                       .select('tp.ID_Pessoa', 'tp.nmPessoa', 'tp.dtNascimento', 'ta.altura', 'ta.sexo', 'tp2.peso', 'tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(5) \
                       .get()
    
    return students.serialize()


@app.get('/students/active/{inputFilter}/{inputBar}')  # get active students with input bar value
async def inputbar_active_students(inputFilter, inputBar):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    max_peso = di["db"].raw('tp2."ID_Pessoa" and tp2."dtData" = (select max("dtData") from tbl_peso where "ID_Pessoa" = tp2."ID_Pessoa")')

    students = di["db"].table('tbl_Pessoa as tp') \
                       .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', max_peso) \
                       .select('tp.ID_Pessoa', 'tp.nmPessoa', 'tp.dtNascimento', 'ta.altura', 'ta.sexo', 'tp2.peso') \
                       .where_null('tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(5) \
                       .get()
    
    return students.serialize()


@app.get('/students/inactive/{inputFilter}/{inputBar}')  # get active students with input bar value
async def inputbar_active_students(inputFilter, inputBar):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    max_peso = di["db"].raw('tp2."ID_Pessoa" and tp2."dtData" = (select max("dtData") from tbl_peso where "ID_Pessoa" = tp2."ID_Pessoa")')

    students = di["db"].table('tbl_Pessoa as tp') \
                       .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', max_peso) \
                       .select('tp.ID_Pessoa', 'tp.nmPessoa', 'tp.dtNascimento', 'ta.altura', 'ta.sexo', 'tp2.peso') \
                       .where_not_null('tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(5) \
                       .get()
    
    return students.serialize()


@app.get('/student/{ID_Pessoa}')  # find student by id
async def find_student(ID_Pessoa):
    newest_peso = Peso.where('ID_Pessoa', ID_Pessoa).max('dtData')
    if newest_peso:
        student = di["db"].table('tbl_Pessoa') \
                        .join('tbl_Aluno', 'tbl_Pessoa.ID_Pessoa', '=', 'tbl_Aluno.ID_Pessoa') \
                        .where('tbl_Pessoa.ID_Pessoa', ID_Pessoa) \
                        .join('tbl_peso', 'tbl_Pessoa.ID_Pessoa', '=', 'tbl_peso.ID_Pessoa') \
                        .where('tbl_peso.dtData', newest_peso) \
                        .first()
    else:
        student = di["db"].table('tbl_Pessoa') \
                        .join('tbl_Aluno', 'tbl_Pessoa.ID_Pessoa', '=', 'tbl_Aluno.ID_Pessoa') \
                        .where('tbl_Pessoa.ID_Pessoa', ID_Pessoa) \
                        .first()
    
    if student:
        return student.serialize()
    else:
        return "Aluno não encontrado."


@app.post('/student')  # create a new student
async def new_student(data: NewStudent):
    person = Person()
    person.nmPessoa = data.nmPessoa
    person.ser = data.ser
    person.tipoPessoa = data.tipoPessoa
    person.cpfCnpj = data.cpfCnpj
    person.rg = data.rg
    person.ufRG = data.ufRG
    person.dtNascimento = data.dtNascimento
    person.dsObs = data.dsObs
    person.dsEmail = data.dsEmail
    person.telefone = data.telefone
    person.save()
    if person.save():
        student = Student()
        student.ID_Pessoa = person.ID_Pessoa
        student.altura = data.altura
        student.sexo = data.sexo
        student.fotoAluno = data.fotoAluno
        student.save()
        if student.save():
            peso = Peso()
            peso.ID_Pessoa = person.ID_Pessoa
            peso.peso = data.peso
            peso.dtData = data.dtData
            if peso.peso != None:
                peso.save()

    return f"{person.nmPessoa} foi cadastrado(a) com sucesso!"


@app.put('/student/{ID_Pessoa}')  # update student
async def update_student(ID_Pessoa, data: NewStudent):
    person = Person.find(ID_Pessoa)
    person.nmPessoa = data.nmPessoa
    person.ser = data.ser
    person.tipoPessoa = data.tipoPessoa
    person.cpfCnpj = data.cpfCnpj
    person.rg = data.rg
    person.ufRG = data.ufRG
    person.dtNascimento = data.dtNascimento
    person.dsObs = data.dsObs
    person.dsEmail = data.dsEmail
    person.telefone = data.telefone
    person.save()
    if person.save():
        student = Student.find(ID_Pessoa)
        student.altura = data.altura
        student.sexo = data.sexo
        student.fotoAluno = data.fotoAluno
        student.save()
        if student.save():
            peso = Peso()
            peso.ID_Pessoa = person.ID_Pessoa
            peso.peso = data.peso
            peso.dtData = data.dtData
            if peso.peso != None or peso.peso > 0:
                peso.save()

    return f"{person.nmPessoa} foi atualizado(a) com sucesso!"


@app.delete('/student/{ID_Pessoa}')
async def delete_student(ID_Pessoa):
    person = Person.find(ID_Pessoa)
    personName = person.nmPessoa
    person.delete()

    return f"{personName} foi deletado(a) com sucesso!"


# ------------------------------------------------------------------------------
# Peso
@app.get('/pesos')  # list all pesos
async def list_pesos():
    pesos = Peso.all()

    return pesos.serialize()


@app.post('/peso')  # create a new peso for a specific student using his id
async def new_peso(data: NewPeso):
    peso = Peso()
    peso.ID_Pessoa = data.ID_Pessoa
    peso.peso = data.peso
    peso.dtData = data.dtData
    peso.save()

    return f"Peso cadastrado com sucesso!"


# ------------------------------------------------------------------------------
# cpfCnpj
@app.get('/cpfCnpj')
async def list_cpfCnpj():  # list all cpf and cnpj in database
    cpfCnpj = di["db"].table('tbl_Pessoa').lists('cpfCnpj')
    return cpfCnpj.serialize()


# ------------------------------------------------------------------------------
# cpfCnpj
@app.get('/rg/{ufRG}')
async def list_rg(ufRG):  # list all RG of specific UF in database
    rg = di["db"].table('tbl_Pessoa as tp') \
                 .select('tp.rg') \
                 .where_not_null('tp.rg') \
                 .where('tp.ufRG', '=', ufRG) \
                 .lists('rg')
    return rg.serialize()


# @app.put('/person/{person_id}')
# async def find_person(person_id, data: NewPerson):
#     person = Person.find(person_id)
#     person.nmPessoa = data.nmPessoa
#     person.ativo = data.ativo
#     person.ser = data.ser
#     person.tipoPessoa = data.tipoPessoa
#     person.cpfCnpj = data.cpfCnpj
#     person.rg = data.rg
#     person.ufRG = data.ufRG
#     person.dsRazaoSocial = data.dsRazaoSocial
#     person.dsInscricaoEstadual = data.dsInscricaoEstadual
#     person.dsInscricaoMunicipal = data.dsInscricaoMunicipal
#     person.isentoIE = data.isentoIE
#     person.dtNascimento = data.dtNascimento
#     person.dsObs = data.dsObs
#     person.dsEmail = data.dsEmail
#     person.telefone = data.telefone
#     person.save()

#     return person.serialize()


# @app.delete('/person/{person_id}')
# async def delete_person(person_id):
#     person = Person.find(person_id)
#     personName = person.nmPessoa
#     person.delete()

#     return f"{personName} foi deletado!"
