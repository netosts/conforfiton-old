# pylint: skip-file
from kink import di
from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from passlib import pwd

from .model import Student
from .schema import NewStudent, EditStudent
from ..person.model import Person
from ..weight.model import Weight

student_router = APIRouter(prefix='/student')


def type_search(inputFilter):
    if inputFilter == 'inputName':
        return "name"
    elif inputFilter == 'inputCpf':
        return "cpf"


@student_router.post('/photo')
async def upload_photo(file: UploadFile = None):
    if not file:
        return None

    try:
        bucket = 'photos'
        salt = pwd.genword(entropy=56, charset="ascii_62")
        file_name = salt + file.filename
        di["space_connection"].upload_fileobj(
            file.file, bucket, file_name, ExtraArgs={'ACL': 'public-read'})
        file_url = f"https://conforfiton-space.nyc3.digitaloceanspaces.com/{bucket}/{file_name}"
        return file_url
    except:
        return JSONResponse({
            "error": True,
            "msg": "Photo was not uploaded."
        }, 422)


@student_router.post('/')
async def new_student(data: NewStudent):
    # CPF duplicate validation
    cpf = Person.where('cpf', data.cpf).count()
    if cpf > 0:
        return JSONResponse({
            "error": True,
            "msg": "The provided CPF is already registered in the database."
        }, 409)

    # Email duplicate validation
    email = Person.where('email', data.email).count()
    if email > 0:
        return JSONResponse({
            "error": True,
            "msg": "The provided Email is already registered in the database."
        }, 409)

    # Phone Number duplicate validation
    phone_number = Person.where('phone_number', data.phone_number).count()
    if phone_number > 0:
        return JSONResponse({
            "error": True,
            "msg": "The provided Phone Number is already registered in the database."
        }, 409)

    person = Person()
    person.name = data.name.title()
    person.cpf = data.cpf
    person.gender = data.gender
    person.role = data.role
    person.email = data.email
    person.phone_number = data.phone_number
    person.birth_date = data.birth_date
    person.height = data.height
    person.shirt_size = data.shirt_size
    person.shorts_size = data.shorts_size
    person.address_picture = data.address_picture

    if person.save():
        weight = Weight()
        weight.person_id = person.id
        weight.weight = data.weight
        weight.created_at = data.created_at
        if not weight.save():
            return JSONResponse({
                "error": True,
                "msg": f"Something went wrong while registering {person.name}'s WEIGHT."
            }, 422)

        student = Student()
        student.person_id = person.id
        student.personal_id = data.personal_id

    if student.save():
        return JSONResponse({
            "error": False,
            "msg": f"{person.name} was successfully registered."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "msg": f"Something went wrong and {person.name} could not be registered."
        }, 422)


@student_router.put('/{person_id}')
async def edit_student(person_id, data: EditStudent):
    person = Person.find(person_id)
    person.name = data.name
    person.cpf = data.cpf
    person.phone_number = data.phone_number
    person.email = data.email
    person.birth_date = data.birth_date
    person.gender = data.gender
    person.shirt_size = data.shirt_size
    person.shorts_size = data.shorts_size
    person.height = data.height
    if person.save():
        return JSONResponse({
            "error": False,
            "msg": f"{person.name} was successfully edited."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "msg": f"Something went wrong and {person.name} was not edited."
        }, 422)


@student_router.put('/activate/{person_id}')
async def activate_student(person_id):
    person = Person.with_trashed().find(person_id)

    person.deleted_at = None

    if person.save():
        return JSONResponse({
            "error": False,
            "msg": f"{person.name} was successfully activated."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "msg": f"Something went wrong and {person.name} was not activated."
        }, 422)


# Get active Students + input bar value
@student_router.get('/active/{inputFilter}/{inputBar}/{limit}/{personal_id}')
async def inputbar_active_students(inputFilter, inputBar, limit, personal_id):
    # p = persons table
    # w = weights table
    # s = students table

    if inputBar == '*':
        inputBar = '%'

    limit = int(limit)
    max_peso = di["db"].raw(
        'w."person_id" and w."created_at" = (select max("created_at") from weights where "person_id" = w."person_id")')

    students = di["db"].table('persons as p') \
        .join('students as s', 's.person_id', '=', 'p.id') \
        .where('s.personal_id', personal_id) \
        .left_join('weights as w', 'p.id', '=', max_peso) \
        .select('p.id', 'p.name', 'p.birth_date', 'p.height', 'p.gender', 'w.weight', 'p.address_picture') \
        .where_null('p.deleted_at') \
        .where('p.' + type_search(inputFilter), 'ilike', inputBar + '%') \
        .order_by('p.created_at', 'desc') \
        .limit(limit) \
        .get()

    return students.serialize()


# Get inactive Students + input bar value
@student_router.get('/inactive/{inputFilter}/{inputBar}/{limit}/{personal_id}')
async def inputbar_inactive_students(inputFilter, inputBar, limit, personal_id):
    # p = pessoa
    # w = peso
    # s = student

    if inputBar == '*':
        inputBar = '%'

    limit = int(limit)
    max_peso = di["db"].raw(
        'w."person_id" and w."created_at" = (select max("created_at") from weights where "person_id" = w."person_id")')

    students = di["db"].table('persons as p') \
                       .join('students as s', 's.person_id', '=', 'p.id') \
                       .where('s.personal_id', personal_id) \
                       .left_join('weights as w', 'p.id', '=', max_peso) \
                       .select('p.id', 'p.name', 'p.birth_date', 'p.height', 'p.gender', 'w.weight', 'p.address_picture', 'p.deleted_at') \
                       .where_not_null('p.deleted_at') \
                       .where('p.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('p.created_at', 'desc') \
                       .limit(limit) \
                       .get()

    return students.serialize()


# List all students
@student_router.get('/{inputFilter}/{inputBar}/{limit}/{personal_id}')
async def inputbar_all_students(inputFilter, inputBar, limit, personal_id):
    # p = pessoa
    # w = peso
    # s = student

    if inputBar == '*':
        inputBar = '%'

    limit = int(limit)
    max_peso = di["db"].raw(
        'w."person_id" and w."created_at" = (select max("created_at") from weights where "person_id" = w."person_id")')

    students = di["db"].table('persons as p') \
                       .join('students as s', 's.person_id', '=', 'p.id') \
                       .where('s.personal_id', personal_id) \
                       .left_join('weights as w', 'p.id', '=', max_peso) \
                       .select('p.id', 'p.name', 'p.birth_date', 'p.height', 'p.gender', 'w.weight', 'p.address_picture', 'p.deleted_at') \
                       .where('p.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('p.created_at', 'desc') \
                       .limit(limit) \
                       .get()

    return students.serialize()


@student_router.get('/{person_id}')
async def find_student(person_id):
    newest_weight = Weight.where('person_id', person_id).max('created_at')
    student = di["db"].table('persons as p') \
        .select(
        "p.id",
        "p.name",
        "p.cpf",
        "p.gender",
        "p.role",
        "p.email",
        "p.phone_number",
        "p.birth_date",
        "p.height",
        "p.shirt_size",
        "p.shorts_size",
        "p.address_picture",
        "p.created_at",
        "p.updated_at",
        "p.deleted_at",
        "s.person_id",
        "s.personal_id",
        "s.neuromuscular_protocol",
        "s.antropometria_protocol",
        "s.cardio_protocol",
        "w.weight",
    ) \
        .join('students as s', 'p.id', '=', 's.person_id') \
        .where('p.id', person_id) \
        .join('weights as w', 'p.id', '=', 'w.person_id') \
        .where('w.created_at', newest_weight) \
        .first()

    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "msg": "Student not found."
        }, 404)


@student_router.get('/credentials/{person_id}')
async def get_student_credentials(person_id):
    student = Person.where('id', person_id).select(
        'id', 'name').first()

    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "msg": "Student not found."
        }, 404)


@student_router.get("/avaliar/{person_id}")
async def get_student_for_avaliar_page(person_id):
    newest_weight = Weight.where('person_id', person_id).max('created_at')
    student = di["db"].table('persons as p') \
        .where('p.id', person_id) \
        .select('p.id', 'p.name', 'p.gender', 'w.weight', 'p.height', 'p.birth_date', 'a.fc_max') \
        .join('weights as w', 'p.id', '=', 'w.person_id') \
        .where('w.created_at', newest_weight) \
        .left_join('anamneses as a', 'p.id', '=', 'a.person_id') \
        .first()

    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "msg": "Student not found."
        }, 404)


@student_router.delete("/soft/{person_id}")
async def soft_delete_student(person_id):
    student = Person.find(person_id)

    if student.delete():
        return JSONResponse({
            "error": False,
            "msg": f"${student.name} was successfully soft deleted."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "msg": "Student not found."
        }, 404)


@student_router.delete("/permanent/{person_id}")
async def permanent_delete_student(person_id):
    student = Person.where('id', person_id)

    if student.delete():
        return JSONResponse({
            "error": False,
            "msg": "Successfully permanently deleted."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "msg": "Student not found."
        }, 404)
