# pylint: skip-file
import re
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, validator

from kink import di

# bootstrap the config and db inside di[]
from bootstrap import bootstrap
bootstrap()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from models.person import Person
from models.student import Student
from models.peso import Peso
from models.fqCardio import fqCardio
from models.address import Address

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
    empPersonal: bool
    dtNascimento: str = None
    dsObs: str = None
    dsEmail: str
    telefone: str = None
    # tbl_Aluno
    altura: int
    sexo: str
    tmCamisa: str = None
    fotoAluno: str = None
    ID_Empresa: int
    ID_Personal: int
    # tbl_peso
    peso: float = None
    dtData: datetime
    #tbl_fqCardio
    bpmRepouso: int = None
    bpmMaximo: int = None

    @validator("*", pre=True, always=True)
    def check_none(cls, v):
        if v == "string" or v == "":
            return None
        return v


# base model for pesos
class NewPeso(BaseModel):
    ID_Pessoa: int
    peso: float
    dtData: datetime


# base model for fqCario
class NewFqCardio(BaseModel):
    ID_Pessoa: int
    bpmRepouso: int
    bpmMaximo: int
    dtData: datetime


# base model for address
class NewAddress(BaseModel):
    ID_Pessoa: int
    rua: str
    numero: int
    complemento: str = None
    bairro: str
    cidade: str
    estado: str
    CEP: str
    pais: str

    @validator("*", pre=True, always=True)
    def check_none(cls, v):
        if v == "string" or v == "":
            return None
        return v
    

# base model for person
class NewPerson(BaseModel):
    nmPessoa: str
    ser: str
    tipoPessoa: str
    cpfCnpj: str
    rg: str = None
    ufRG: str = None
    empPersonal: bool
    dtNascimento: str = None
    dsObs: str = None
    dsEmail: str
    telefone: str = None

    @validator("*", pre=True, always=True)
    def check_none(cls, v):
        if v == "string" or v == "":
            return None
        return v
    

# FUNCTIONS
# Variables for query
def type_search(inputFilter):
        if inputFilter == 'inputName':
            return "nmPessoa"
        elif inputFilter == 'inputCpf':
            return "cpfCnpj"


# home
@app.get('/')
async def home():
    return "Conforfit Database"


# ------------------------------------------------------------------------------
# Students
@app.get('/students/active/{inputFilter}/{inputBar}/{limit}')  # get active students with input bar value
async def inputbar_active_students(inputFilter, inputBar, limit):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    limit = int(limit)
    max_peso = di["db"].raw('tp2."ID_Pessoa" and tp2."dtData" = (select max("dtData") from tbl_peso where "ID_Pessoa" = tp2."ID_Pessoa")')

    students = di["db"].table('tbl_Pessoa as tp') \
                       .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', max_peso) \
                       .select('tp.ID_Pessoa', 'tp.nmPessoa', 'tp.dtNascimento', 'ta.altura', 'ta.sexo', 'tp2.peso') \
                       .where_null('tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(limit) \
                       .get()
    
    return students.serialize()


@app.get('/students/inactive/{inputFilter}/{inputBar}/{limit}')  # get active students with input bar value
async def inputbar_inactive_students(inputFilter, inputBar, limit):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    limit = int(limit)
    max_peso = di["db"].raw('tp2."ID_Pessoa" and tp2."dtData" = (select max("dtData") from tbl_peso where "ID_Pessoa" = tp2."ID_Pessoa")')

    students = di["db"].table('tbl_Pessoa as tp') \
                       .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', max_peso) \
                       .select('tp.ID_Pessoa', 'tp.nmPessoa', 'tp.dtNascimento', 'ta.altura', 'ta.sexo', 'tp2.peso', 'tp.deleted_at') \
                       .where_not_null('tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(limit) \
                       .get()
    
    return students.serialize()


@app.get('/students/{inputFilter}/{inputBar}/{limit}')  # list all students
async def inputbar_all_students(inputFilter, inputBar, limit):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    limit = int(limit)
    max_peso = di["db"].raw('tp2."ID_Pessoa" and tp2."dtData" = (select max("dtData") from tbl_peso where "ID_Pessoa" = tp2."ID_Pessoa")')

    students = di["db"].table('tbl_Pessoa as tp') \
                       .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', max_peso) \
                       .select('tp.ID_Pessoa', 'tp.nmPessoa', 'tp.dtNascimento', 'ta.altura', 'ta.sexo', 'tp2.peso', 'tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(limit) \
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
        return JSONResponse("Student not found", 404)


@app.post('/student')  # create a new student
async def new_student(data: NewStudent):
    # name max length of 60
    if len(data.nmPessoa) > 60:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Name can't be more than 60 characters."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # cpf max length of 11
    if len(data.cpfCnpj) > 11:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Cpf can't be more than 11 characters."
        }
        return JSONResponse(content=error_message, status_code=422)

    # look for CPF duplicate
    cpf = Person.where('cpfCnpj', data.cpfCnpj).count()
    if cpf > 0:
        error_message = {
            "error": "Duplicate CPF",
            "message": "The provided CPF is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)
    
    # rg max length of 20
    if data.rg != None and len(data.rg) > 20:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Rg can't be more than 20 characters."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # RG and UF must be together
    if (data.rg != None and data.ufRG == None) or (data.rg == None and data.ufRG != None):
        error_message = {
            "error": "RG and UF must be together",
            "message": "The RG and UF can't be registered alone in the database."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # look for RG of specified UF duplicate
    if data.rg != None and data.ufRG != None:
        rg = Person.where('rg', data.rg).where('ufRG', data.ufRG).count()
        if rg > 0:
            error_message = {
                "error": "Duplicate RG in specified UF",
                "message": "The provided RG and UF are already registered in the database."
            }
            return JSONResponse(content=error_message, status_code=409)
        
    # telefone max length of 11
    if data.telefone != None and len(data.telefone) > 11:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Telefone can't be more than 11 characters."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # email max length of 80
    if len(data.dsEmail) > 80:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Email can't be more than 80 characters."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # email validation
    regex = r'(?:[a-z0-9+!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
    if not re.match(regex, data.dsEmail, re.IGNORECASE):
        error_message= {
            "error": "Email invaid",
            "message": "Email must be a valid email address."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # email duplicate validation
    email = Person.where('dsEmail', data.dsEmail).count()
    if email > 0:
        error_message = {
            "error": "Duplicate Email",
            "message": "The provided Email is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)
    
    # altura can't be negative or higher than 250cm
    if data.altura < 0 or data.altura > 250:
        error_message= {
            "error": "Altura invalid",
            "message": "Altura must be between 0cm and 250cm."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    altura_decimal = Decimal(str(data.altura))  # convert to decimal
    if altura_decimal.as_tuple().exponent < -1:  # check if altura has more than 1 decimal number
        error_message = {
            "error": "Altura invalid",
            "message": "Altura must have up to 1 decimal number."
        }
        return JSONResponse(content=error_message, status_code=422)

    # peso can't be negative or higher than 600kg
    if data.peso != None:
        if data.peso < 0 or data.peso > 600:
            error_message= {
                "error": "Peso invalid",
                "message": "Peso must be between 0kg and 600kg."
            }
            return JSONResponse(content=error_message, status_code=422)
        
        peso_decimal = Decimal(str(data.peso))  # convert to decimal
        if peso_decimal.as_tuple().exponent < -2:  # check if peso has more than 2 decimal numbers
            error_message = {
                "error": "Peso invalid",
                "message": "Peso must have up to 2 decimal numbers."
            }
            return JSONResponse(content=error_message, status_code=422)
        
    # bpmMaximo and bpmRepouso must be together
    if (data.bpmMaximo != None and data.bpmRepouso == None) or (data.bpmMaximo == None and data.bpmRepouso != None):
        error_message = {
            "error": "BPM Maximo and BPM Repouso must be together",
            "message": "The BPM Maximo and BPM Repouso can't be registered alone in the database."
        }
        return JSONResponse(content=error_message, status_code=422)
        
    # bpm maximo/repouso can't be negative or higher than 220
    if data.bpmMaximo != None and data.bpmRepouso != None:
        if data.bpmMaximo < 0 or data.bpmMaximo > 220:
            error_message= {
                "error": "BPM Maximo invalid",
                "message": "BPM Maximo must be between 0bpm and 220bpm."
            }
            return JSONResponse(content=error_message, status_code=422)
        
        if data.bpmRepouso < 0 or data.bpmRepouso > 220:
            error_message= {
                "error": "BPM Repouso invalid",
                "message": "BPM Repouso must be between 0bpm and 220bpm."
            }
            return JSONResponse(content=error_message, status_code=422)
        
    # dsObs max length of 300
    if data.dsObs != None and len(data.dsObs) > 300:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "dsObs can't be more than 300 characters."
        }
        return JSONResponse(content=error_message, status_code=422)

    person = Person()
    person.nmPessoa = data.nmPessoa
    person.ser = data.ser
    person.tipoPessoa = data.tipoPessoa
    person.cpfCnpj = data.cpfCnpj
    person.rg = data.rg
    person.ufRG = data.ufRG
    person.empPersonal = data.empPersonal
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
        student.tmCamisa = data.tmCamisa
        student.fotoAluno = data.fotoAluno
        student.ID_Empresa = data.ID_Empresa
        student.ID_Personal = data.ID_Personal
        student.save()

        if student.save():
            if data.peso != None:
                peso = Peso()
                peso.ID_Pessoa = person.ID_Pessoa
                peso.peso = data.peso
                peso.dtData = data.dtData
                peso.save()

            if data.bpmRepouso and data.bpmMaximo != None:
                cardio = fqCardio()
                cardio.ID_Pessoa = person.ID_Pessoa
                cardio.bpmRepouso = data.bpmRepouso
                cardio.bpmMaximo = data.bpmMaximo
                cardio.dtData = data.dtData
                cardio.save()

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
# Person
@app.post('/person')  # create a new person
async def new_person(data: NewPerson):
    # name max length of 60
    if len(data.nmPessoa) > 60:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Name can't be more than 60 characters."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # cpf max length of 11
    if len(data.cpfCnpj) > 11:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Cpf can't be more than 11 characters."
        }
        return JSONResponse(content=error_message, status_code=422)

    # look for CPF duplicate
    cpf = Person.where('cpfCnpj', data.cpfCnpj).count()
    if cpf > 0:
        error_message = {
            "error": "Duplicate CPF",
            "message": "The provided CPF is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)
    
    # rg max length of 20
    if data.rg != None and len(data.rg) > 20:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Rg can't be more than 20 characters."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # RG and UF must be together
    if (data.rg != None and data.ufRG == None) or (data.rg == None and data.ufRG != None):
        error_message = {
            "error": "RG and UF must be together",
            "message": "The RG and UF can't be registered alone in the database."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # look for RG of specified UF duplicate
    if data.rg != None and data.ufRG != None:
        rg = Person.where('rg', data.rg).where('ufRG', data.ufRG).count()
        if rg > 0:
            error_message = {
                "error": "Duplicate RG in specified UF",
                "message": "The provided RG and UF are already registered in the database."
            }
            return JSONResponse(content=error_message, status_code=409)
        
    # telefone max length of 11
    if data.telefone != None and len(data.telefone) > 11:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Telefone can't be more than 11 characters."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # email max length of 80
    if len(data.dsEmail) > 80:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "Email can't be more than 80 characters."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # email validation
    regex = r'(?:[a-z0-9+!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
    if not re.match(regex, data.dsEmail, re.IGNORECASE):
        error_message= {
            "error": "Email invaid",
            "message": "Email must be a valid email address."
        }
        return JSONResponse(content=error_message, status_code=422)
    
    # dsObs max length of 300
    if data.dsObs != None and len(data.dsObs) > 300:
        error_message= {
            "error": "Maximum length exceeded",
            "message": "dsObs can't be more than 300 characters."
        }
        return JSONResponse(content=error_message, status_code=422)

    person = Person()
    person.nmPessoa = data.nmPessoa
    person.ser = data.ser
    person.tipoPessoa = data.tipoPessoa
    person.cpfCnpj = data.cpfCnpj
    person.rg = data.rg
    person.ufRG = data.ufRG
    person.empPersonal = data.empPersonal
    person.dtNascimento = data.dtNascimento
    person.dsObs = data.dsObs
    person.dsEmail = data.dsEmail
    person.telefone = data.telefone
    person.save()

    return f"{person.nmPessoa} foi cadastrado(a) com sucesso!"


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
# fqCardios
@app.get('/fqcardios')  # list all cardios
async def list_fq_cardio():
    cardio = fqCardio.all()

    return cardio.serialize()


@app.post('/fqcardio')  # create a new fqcardio for a specific student using his id
async def new_cardio(data: NewFqCardio):
    cardio = fqCardio()
    cardio.ID_Pessoa = data.ID_Pessoa
    cardio.bpmRepouso = data.bpmRepouso
    cardio.bpmMaximo = data.bpmMaximo
    cardio.dtData = data.dtData
    cardio.save()

    return f"Frequência cardíaca cadastrada com sucesso!"


# ------------------------------------------------------------------------------
# Address
@app.get('/addresses')  # list all addresses
async def list_addresses():
    addresses = Address.all()

    return addresses.serialize()


@app.post('/address')  # create a new address for a specific student using his id
async def new_address(data: NewAddress):
    new_address = Address()
    new_address.ID_Pessoa = data.ID_Pessoa
    new_address.rua = data.rua
    new_address.numero = data.numero
    new_address.complemento = data.complemento
    new_address.bairro = data.bairro
    new_address.cidade = data.cidade
    new_address.estado = data.estado
    new_address.CEP = data.CEP
    new_address.pais = data.pais
    new_address.save()

    return f"Frequência cardíaca cadastrada com sucesso!"


# ------------------------------------------------------------------------------
# CPF-CNPJ
@app.get('/cpfCnpj/{cpf}')
async def count_cpf(cpf):  # how many of the specified CPF value are in the database
    cpf = Person.where('cpfCnpj', cpf).count()
    return cpf


# ------------------------------------------------------------------------------
# RG-UF
@app.get('/rg/{rg}/{ufRG}')
async def count_rg(rg, ufRG):  # how many of the specified RG in UF value are in the database
    rg = Person.where('rg', rg).where('ufRG', ufRG).count()
    return rg


# ------------------------------------------------------------------------------
# CPF-CNPJ
@app.get('/dsEmail/{dsEmail}')
async def count_email(dsEmail):  # how many of the specified CPF value are in the database
    email = Person.where('dsEmail', dsEmail).count()
    return email
