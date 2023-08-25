# pylint: skip-file
from kink import di
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .model import Student
from .schema import NewStudent
from ..person.model import Person
from ..weight.model import Weight


student_router = APIRouter(prefix='/student')

# FUNCTIONS


def type_search(inputFilter):
    if inputFilter == 'inputName':
        return "nm_pessoa"
    elif inputFilter == 'inputCpf':
        return "cpf_cnpj"


# Get active Students + input bar value
@student_router.get('/active/{inputFilter}/{inputBar}/{limit}')
async def inputbar_active_students(inputFilter, inputBar, limit):
    # tp = pessoa
    # tp2 = peso
    # ta = aluno
    limit = int(limit)
    max_peso = di["db"].raw(
        'tp2."id_pessoa" and tp2."dt_data" = (select max("dt_data") from tbl_peso where "id_pessoa" = tp2."id_pessoa")')

    students = di["db"].table('tbl_pessoa as tp') \
                       .join('tbl_aluno as ta', 'ta.id_pessoa', '=', 'tp.id_pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.id_pessoa', '=', max_peso) \
                       .select('tp.id_pessoa', 'tp.nm_pessoa', 'tp.dt_nascimento', 'ta.altura', 'ta.sexo', 'tp2.peso') \
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
    max_peso = di["db"].raw(
        'tp2."id_pessoa" and tp2."dt_data" = (select max("dt_data") from tbl_peso where "id_pessoa" = tp2."id_pessoa")')

    students = di["db"].table('tbl_pessoa as tp') \
                       .join('tbl_aluno as ta', 'ta.id_pessoa', '=', 'tp.id_pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.id_pessoa', '=', max_peso) \
                       .select('tp.id_pessoa', 'tp.nm_pessoa', 'tp.dt_nascimento', 'ta.altura', 'ta.sexo', 'tp2.peso', 'tp.deleted_at') \
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
    max_peso = di["db"].raw(
        'tp2."id_pessoa" and tp2."dt_data" = (select max("dt_data") from tbl_peso where "id_pessoa" = tp2."id_pessoa")')

    students = di["db"].table('tbl_pessoa as tp') \
                       .join('tbl_aluno as ta', 'ta.id_pessoa', '=', 'tp.id_pessoa') \
                       .left_join('tbl_peso as tp2', 'tp.id_pessoa', '=', max_peso) \
                       .select('tp.id_pessoa', 'tp.nm_pessoa', 'tp.dt_nascimento', 'ta.altura', 'ta.sexo', 'tp2.peso', 'tp.deleted_at') \
                       .where('tp.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('tp.created_at', 'desc') \
                       .limit(limit) \
                       .get()

    return students.serialize()


# Find Student by ID
@student_router.get('/{id_pessoa}')
async def find_student(id_pessoa):
    newest_peso = Peso.where('id_pessoa', id_pessoa).max('dt_data')
    if newest_peso:
        student = di["db"].table('tbl_pessoa') \
            .join('tbl_aluno', 'tbl_pessoa.id_pessoa', '=', 'tbl_aluno.id_pessoa') \
            .where('tbl_pessoa.id_pessoa', id_pessoa) \
            .join('tbl_peso', 'tbl_pessoa.id_pessoa', '=', 'tbl_peso.id_pessoa') \
            .where('tbl_peso.dtData', newest_peso) \
            .first()
    else:
        student = di["db"].table('tbl_pessoa') \
            .join('tbl_aluno', 'tbl_pessoa.id_pessoa', '=', 'tbl_aluno.id_pessoa') \
            .where('tbl_pessoa.id_pessoa', id_pessoa) \
            .first()

    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "data": "Student not found."
        }, 404)


# Get Credentials of Student using his ID
@student_router.get('/credentials/{id_pessoa}')
async def get_student_credentials(id_pessoa):
    student = Person.where('id_pessoa', id_pessoa).select(
        'id_pessoa', 'nm_pessoa').first()

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
    cpf = Person.where('cpf_cnpj', data.cpf_cnpj).count()
    if cpf > 0:
        return JSONResponse({
            "error": True,
            "data": "The provided CPF is already registered in the database."
        }, 409)

    # Look for RG of specified UF duplicate
    if data.rg != None and data.uf_rg != None:
        rg = Person.where('rg', data.rg).where('uf_rg', data.uf_rg).count()
        if rg > 0:
            return JSONResponse({
                "error": True,
                "data": "The provided RG and UF are already registered in the database."
            }, 409)

    # RG and UF must be together
    if (data.rg is not None and data.uf_rg is None) or (data.rg is None and data.uf_rg is not None):
        return JSONResponse({
            "error": True,
            "data": "RG and UF must be together."
        }, 422)

    # Email duplicate validation
    email = Person.where('ds_email', data.ds_email).count()
    if email > 0:
        return JSONResponse({
            "error": True,
            "data": "The provided Email is already registered in the database."
        }, 409)

    person = Person()
    person.nm_pessoa = data.nm_pessoa.title()
    person.ser = data.ser
    person.tipo_pessoa = data.tipo_pessoa
    person.cpf_cnpj = data.cpf_cnpj
    person.rg = data.rg
    person.uf_rg = data.uf_rg
    person.emp_personal = data.emp_personal
    person.dt_nascimento = data.dt_nascimento
    person.ds_obs = data.ds_obs
    person.ds_email = data.ds_email
    person.telefone = data.telefone

    if person.save():
        student = Student()
        student.id_pessoa = person.id_pessoa
        student.altura = data.altura
        student.sexo = data.sexo
        student.tm_camisa = data.tm_camisa
        student.foto_aluno = data.foto_aluno
        student.id_empresa = data.id_empresa
        student.id_personal = data.id_personal

        if student.save():
            if data.peso != None:
                peso = Peso()
                peso.id_pessoa = person.id_pessoa
                peso.peso = data.peso
                peso.dt_data = data.dt_data
                peso.save()

            return JSONResponse({
                "error": False,
                "data": f"{person.nm_pessoa} foi cadastrado(a) com sucesso."
            }, 200)

        else:
            return JSONResponse({
                "error": True,
                "data": f"Houve um erro e {person.nm_pessoa} não foi cadastrado(a)."
            }, 422)


@student_router.get("/avaliar/{id_pessoa}")
async def get_student_for_avaliar_page(id_pessoa):
    newest_peso = Peso.where('id_pessoa', id_pessoa).max('dt_data')
    student = di["db"].table('tbl_pessoa as tp') \
        .where('tp.id_pessoa', id_pessoa) \
        .select('tp.id_pessoa', 'tp.nm_pessoa', 'ta.sexo', 'tp2.peso', 'ta.altura') \
        .join('tbl_peso as tp2', 'tp.id_pessoa', '=', 'tp2.id_pessoa') \
        .where('tp2.dt_data', newest_peso) \
        .join('tbl_aluno as ta', 'tp.id_pessoa', '=', 'ta.id_pessoa') \
        .first()

    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "data": "Student not found."
        }, 404)


# Update Student
# @student_router.put('/{id_pessoa}')
# async def update_student(id_pessoa, data: NewStudent):
#     person = Person.find(id_pessoa)
#     person.nm_pessoa = data.nm_pessoa
#     person.ser = data.ser
#     person.tipo_pessoa = data.tipo_pessoa
#     person.cpf_cnpj = data.cpf_cnpj
#     person.rg = data.rg
#     person.uf_rg = data.uf_rg
#     person.dt_nascimento = data.dt_nascimento
#     person.ds_obs = data.ds_obs
#     person.ds_email = data.ds_email
#     person.telefone = data.telefone
#     person.save()
#     if person.save():
#         student = Student.find(id_pessoa)
#         student.altura = data.altura
#         student.sexo = data.sexo
#         student.foto_aluno = data.foto_aluno
#         student.save()
#         if student.save():
#             peso = Peso()
#             peso.id_Pessoa = person.id_pessoa
#             peso.peso = data.peso
#             peso.dt_data = data.dt_data
#             if peso.peso != None or peso.peso > 0:
#                 peso.save()

#     return f"{person.nm_pessoa} foi atualizado(a) com sucesso!"
