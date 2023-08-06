# pylint: skip-file
from kink import di
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models import Student
from .schemas import NewStudent
from ..person.models import Person
from ..peso.models import Peso
from ..cardio.models import Cardio


student_router = APIRouter(prefix='/student')

# FUNCTIONS
def type_search(inputFilter):
        if inputFilter == 'inputName':
            return "nm_pessoa"
        elif inputFilter == 'inputCpf':
            return "cpfCnpj"
        

# Get active Students + input bar value
@student_router.get('/active/{inputFilter}/{inputBar}/{limit}')
async def inputbar_active_students(inputFilter, inputBar, limit):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    limit = int(limit)
    max_peso = di["db"].raw('tp2."ID_Pessoa" and tp2."dtData" = (select max("dtData") from tbl_peso where "ID_Pessoa" = tp2."ID_Pessoa")')

    students = di["db"].table('tbl_pessoa as tp') \
                       .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', max_peso) \
                       .select('tp.ID_Pessoa', 'tp.nm_pessoa', 'tp.dtNascimento', 'ta.altura', 'ta.sexo', 'tp2.peso') \
                       .where_null('tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(limit) \
                       .get()
    
    return students.serialize()


# Get inactive Students + input bar value
@student_router.get('/inactive/{inputFilter}/{inputBar}/{limit}')
async def inputbar_inactive_students(inputFilter, inputBar, limit):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    limit = int(limit)
    max_peso = di["db"].raw('tp2."ID_Pessoa" and tp2."dtData" = (select max("dtData") from tbl_peso where "ID_Pessoa" = tp2."ID_Pessoa")')

    students = di["db"].table('tbl_pessoa as tp') \
                       .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', max_peso) \
                       .select('tp.ID_Pessoa', 'tp.nm_pessoa', 'tp.dtNascimento', 'ta.altura', 'ta.sexo', 'tp2.peso', 'tp.deleted_at') \
                       .where_not_null('tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(limit) \
                       .get()
    
    return students.serialize()


# List all students
@student_router.get('/{inputFilter}/{inputBar}/{limit}')
async def inputbar_all_students(inputFilter, inputBar, limit):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    limit = int(limit)
    max_peso = di["db"].raw('tp2."ID_Pessoa" and tp2."dtData" = (select max("dtData") from tbl_peso where "ID_Pessoa" = tp2."ID_Pessoa")')

    students = di["db"].table('tbl_pessoa as tp') \
                       .join('tbl_Aluno as ta', 'ta.ID_Pessoa', '=', 'tp.ID_Pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', max_peso) \
                       .select('tp.ID_Pessoa', 'tp.nm_pessoa', 'tp.dtNascimento', 'ta.altura', 'ta.sexo', 'tp2.peso', 'tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(limit) \
                       .get()
    
    return students.serialize()


# Find Student by ID
@student_router.get('/{ID_Pessoa}')
async def find_student(ID_Pessoa):
    newest_peso = Peso.where('ID_Pessoa', ID_Pessoa).max('dtData')
    if newest_peso:
        student = di["db"].table('tbl_pessoa') \
                        .join('tbl_Aluno', 'tbl_pessoa.ID_Pessoa', '=', 'tbl_Aluno.ID_Pessoa') \
                        .where('tbl_pessoa.ID_Pessoa', ID_Pessoa) \
                        .join('tbl_peso', 'tbl_pessoa.ID_Pessoa', '=', 'tbl_peso.ID_Pessoa') \
                        .where('tbl_peso.dtData', newest_peso) \
                        .first()
    else:
        student = di["db"].table('tbl_pessoa') \
                        .join('tbl_Aluno', 'tbl_pessoa.ID_Pessoa', '=', 'tbl_Aluno.ID_Pessoa') \
                        .where('tbl_pessoa.ID_Pessoa', ID_Pessoa) \
                        .first()
    
    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "data": "Student not found."
        }, 404)
    

# Get Credentials of Student using his ID
@student_router.get('/credentials/{ID_Pessoa}')
async def get_student_credentials(ID_Pessoa):
    student = Person.where('ID_Pessoa', ID_Pessoa).select('ID_Pessoa', 'nm_pessoa').first()
    
    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "data": "Student not found."
        }, 404)


# Create a new Student
@student_router.post('/')
async def new_student(data: NewStudent):
    # Look for CPF duplicate
    cpf = Person.where('cpfCnpj', data.cpfCnpj).count()
    if cpf > 0:
        return JSONResponse({
            "error": True,
            "message": "The provided CPF is already registered in the database."
        }, 409)

    # Look for RG of specified UF duplicate
    if data.rg != None and data.ufRG != None:
        rg = Person.where('rg', data.rg).where('ufRG', data.ufRG).count()
        if rg > 0:
            return JSONResponse({
                "error": True,
                "message": "The provided RG and UF are already registered in the database."
            }, 409)
            
    if (data.rg is not None and data.ufRG is None) or (data.rg is None and data.ufRG is not None):
        return JSONResponse({
            "error": True,
            "data": "RG and UF must be together."
        }, 422)
    
    # Email duplicate validation
    email = Person.where('dsEmail', data.dsEmail).count()
    if email > 0:
        return JSONResponse({
            "error": True,
            "data": "The provided Email is already registered in the database."
        }, 409)

    person = Person()
    person.nm_pessoa = data.nm_pessoa
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

    if person.save():
        student = Student()
        student.ID_Pessoa = person.ID_Pessoa
        student.altura = data.altura
        student.sexo = data.sexo
        student.tmCamisa = data.tmCamisa
        student.fotoAluno = data.fotoAluno
        student.ID_Empresa = data.ID_Empresa
        student.ID_Personal = data.ID_Personal

        if student.save():
            if data.peso != None:
                peso = Peso()
                peso.ID_Pessoa = person.ID_Pessoa
                peso.peso = data.peso
                peso.dtData = data.dtData
                peso.save()

            if data.bpmRepouso and data.bpmMaximo != None:
                cardio = Cardio()
                cardio.ID_Pessoa = person.ID_Pessoa
                cardio.bpmRepouso = data.bpmRepouso
                cardio.bpmMaximo = data.bpmMaximo
                cardio.dtData = data.dtData
                cardio.save()

        else:
            return JSONResponse({
                "error":True,
                "data": f"Houve um erro e {person.nm_pessoa} não foi cadastrado(a)."
            }, 422)
    
    return JSONResponse({
            "error":False,
            "data": f"{person.nm_pessoa} foi cadastrado(a) com sucesso."
        }, 200)


@student_router.get("/avaliar/{ID_Pessoa}")
async def get_student_for_avaliar_page(ID_Pessoa):
    newest_peso = Peso.where('ID_Pessoa', ID_Pessoa).max('dtData')
    student = di["db"].table('tbl_pessoa as tp') \
                    .where('tp.ID_Pessoa', ID_Pessoa) \
                    .select('tp.ID_Pessoa', 'tp.nm_pessoa', 'ta.sexo', 'tp2.peso') \
                    .join('tbl_peso as tp2', 'tp.ID_Pessoa', '=', 'tp2.ID_Pessoa') \
                    .where('tp2.dtData', newest_peso) \
                    .join('tbl_Aluno as ta', 'tp.ID_Pessoa', '=', 'ta.ID_Pessoa') \
                    .first()
    
    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "data": "Student not found."
        }, 404)


# Update Student
# @student_router.put('/{ID_Pessoa}')
# async def update_student(ID_Pessoa, data: NewStudent):
#     person = Person.find(ID_Pessoa)
#     person.nm_pessoa = data.nm_pessoa
#     person.ser = data.ser
#     person.tipoPessoa = data.tipoPessoa
#     person.cpfCnpj = data.cpfCnpj
#     person.rg = data.rg
#     person.ufRG = data.ufRG
#     person.dtNascimento = data.dtNascimento
#     person.dsObs = data.dsObs
#     person.dsEmail = data.dsEmail
#     person.telefone = data.telefone
#     person.save()
#     if person.save():
#         student = Student.find(ID_Pessoa)
#         student.altura = data.altura
#         student.sexo = data.sexo
#         student.fotoAluno = data.fotoAluno
#         student.save()
#         if student.save():
#             peso = Peso()
#             peso.ID_Pessoa = person.ID_Pessoa
#             peso.peso = data.peso
#             peso.dtData = data.dtData
#             if peso.peso != None or peso.peso > 0:
#                 peso.save()

#     return f"{person.nm_pessoa} foi atualizado(a) com sucesso!"
