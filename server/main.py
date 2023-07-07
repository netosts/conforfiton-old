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
    ativo: bool = None
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


# home
@app.get('/')
async def home():
    return "hello world"


# ------------------------------------------------------------------------------
# Students
@app.get('/students')  # list all students
async def list_students():
    students = di["db"].table('tbl_Pessoa as tp') \
                       .join('tbl_Aluno as ta', 'tp.ID_Pessoa', '=', 'ta.ID_Pessoa') \
                       .order_by('tp.updated_at', 'desc') \
                       .get()

    return students.serialize()

@app.get('/students/limit')  # list a limited amount of students
async def limit_students():
    # distinct_peso = Peso.select(di["db"].raw('DISTINCT ON ("ID_Pessoa") *')) \
    #                     .order_by(di["db"].raw('"ID_Pessoa", "dtData"'), 'desc').get()

    query = di["db"].table('tbl_Pessoa as tp') \
                    .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                    .left_join('tbl_peso as tp2', 'tp2.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                    .order_by('tp.updated_at', 'desc') \
                    .order_by('tp2.dtData', 'desc')
                    
    students = query.get()

    # # Create a set to store unique students
    unique_students = list()

    # # Filter out duplicates
    filtered_students = []
    for student in students:
        if student[0] not in unique_students:
            unique_students.append(student[0])
            student_dict = {  # manually serialize [serialize() is bugged]
                "ID_Pessoa": student[0],
                "nmPessoa": student[1],
                "ativo": student[2],
                "ser": student[3],
                "tipoPessoa": student[4],
                "cpfCnpj": student[5],
                "rg": student[6],
                "ufRG": student[7],
                "dsRazaoSocial": student[8],
                "dsInscricaoEstadual": student[9],
                "dsInscricaoMunicipal": student[10],
                "isentoIE": student[11],
                "dtNascimento": student[12],
                "dsObs": student[13],
                "dsEmail": student[14],
                "telefone": student[15],
                "created_at": student[16],
                "updated_at": student[17],
                "deleted_at": student[18],
                # student[19] is ID_Pessoa
                "altura": student[20],
                "sexo": student[21],
                "fotoAluno": student[22],
                "ID_peso": student[23],
                # student[24] is ID_Pessoa
                "peso": student[25],
                "dtData": student[26],
            }
            filtered_students.append(student_dict)

    return filtered_students[:5]


@app.get('/students/peso')  # list all students with peso
async def list_students_and_peso():
    newest_peso = di["db"].table('tbl_peso').max('dtData')
    query = di["db"].table('tbl_Pessoa') \
                   .join('tbl_Aluno', 'tbl_Pessoa.ID_Pessoa', '=', 'tbl_Aluno.ID_Pessoa') \
                   .join('tbl_peso', 'tbl_Pessoa.ID_Pessoa', '=', 'tbl_peso.ID_Pessoa') \
                   .order_by('tbl_Pessoa.updated_at', 'desc')
    students = query.get()
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
    person.ativo = data.ativo
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
    person.ativo = data.ativo
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