# pylint: skip-file
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
from models.auth import User

from schemas.student import NewStudent
from schemas.peso import NewPeso
from schemas.cardio import NewFqCardio
from schemas.address import NewAddress
from schemas.person import NewPerson
from schemas.user import NewUser

from decouple import config


app = FastAPI()

# CORS Middleware validation
# who has access to the backend ↓
ORIGINS = config('ORIGINS')

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# FUNCTIONS
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
# Authentication
@app.post('/register')
async def new_user(data: NewUser):
    user = User()
    user.ID_Pessoa = data.ID_Pessoa
    user.username = data.username
    user.password = data.password
    user.save()

    return f'{user.username} foi cadastrado(a) com sucesso.'


@app.get('/test')
async def test():
    user = User.where('username', 'admin777').first()
    return user.password


@app.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/current/", response_model=NewUser)
async def read_users_current(
    current_user: Annotated[NewUser, Depends(get_current_user)]
):
    return current_user


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
    # look for CPF duplicate
    cpf = Person.where('cpfCnpj', data.cpfCnpj).count()
    if cpf > 0:
        error_message = {
            "error": "Duplicate CPF",
            "message": "The provided CPF is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)
    
    # look for RG of specified UF duplicate
    if data.rg != None and data.ufRG != None:
        rg = Person.where('rg', data.rg).where('ufRG', data.ufRG).count()
        if rg > 0:
            error_message = {
                "error": "Duplicate RG in specified UF",
                "message": "The provided RG and UF are already registered in the database."
            }
            return JSONResponse(content=error_message, status_code=409)
    
    # email duplicate validation
    email = Person.where('dsEmail', data.dsEmail).count()
    if email > 0:
        error_message = {
            "error": "Duplicate Email",
            "message": "The provided Email is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)

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
    # look for CPF duplicate
    cpf = Person.where('cpfCnpj', data.cpfCnpj).count()
    if cpf > 0:
        error_message = {
            "error": "Duplicate CPF",
            "message": "The provided CPF is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)
    
    # look for RG of specified UF duplicate
    if data.rg != None and data.ufRG != None:
        rg = Person.where('rg', data.rg).where('ufRG', data.ufRG).count()
        if rg > 0:
            error_message = {
                "error": "Duplicate RG in specified UF",
                "message": "The provided RG and UF are already registered in the database."
            }
            return JSONResponse(content=error_message, status_code=409)
        
    # email duplicate validation
    email = Person.where('dsEmail', data.dsEmail).count()
    if email > 0:
        error_message = {
            "error": "Duplicate Email",
            "message": "The provided Email is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)

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
# EMAIL
@app.get('/dsEmail/{dsEmail}')
async def count_email(dsEmail):  # how many of the specified CPF value are in the database
    email = Person.where('dsEmail', dsEmail).count()
    return email
