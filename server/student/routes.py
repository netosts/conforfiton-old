# pylint: skip-file
from kink import di
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from datetime import datetime

from .model import Student
from .schema import NewStudent, UpdateAntropometria
from ..person.model import Person
from ..weight.model import Weight


student_router = APIRouter(prefix='/student')


def type_search(inputFilter):
    if inputFilter == 'inputName':
        return "name"
    elif inputFilter == 'inputCpf':
        return "cpf"


@student_router.post('/')
async def new_student(data: NewStudent):
    # CPF duplicate validation
    cpf = Person.where('cpf', data.cpf).count()
    if cpf > 0:
        return JSONResponse({
            "error": True,
            "data": "The provided CPF is already registered in the database."
        }, 409)

    # Email duplicate validation
    email = Person.where('email', data.email).count()
    if email > 0:
        return JSONResponse({
            "error": True,
            "data": "The provided Email is already registered in the database."
        }, 409)

    # Phone Number duplicate validation
    phone_number = Person.where('phone_number', data.phone_number).count()
    if phone_number > 0:
        return JSONResponse({
            "error": True,
            "data": "The provided Phone Number is already registered in the database."
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
                "data": f"Something went wrong while registering {person.name}'s WEIGHT."
            }, 422)

        student = Student()
        student.person_id = person.id
        student.personal_id = data.personal_id

    if student.save():
        return JSONResponse({
            "error": False,
            "data": f"{person.name} was successfully registered."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong and {person.name} could not be registered."
        }, 422)


# Get active Students + input bar value
@student_router.get('/active/{inputFilter}/{inputBar}/{limit}/{personal_id}')
async def inputbar_active_students(inputFilter, inputBar, limit, personal_id):
    # p = persons table
    # w = weights table
    # s = students table
    limit = int(limit)
    max_peso = di["db"].raw(
        'w."person_id" and w."created_at" = (select max("created_at") from weights where "person_id" = w."person_id")')

    students = di["db"].table('persons as p') \
        .join('students as s', 's.person_id', '=', 'p.id') \
        .where('s.personal_id', personal_id) \
        .left_join('weights as w', 'p.id', '=', max_peso) \
        .select('p.id', 'p.name', 'p.birth_date', 'p.height', 'p.gender', 'w.weight') \
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
    limit = int(limit)
    max_peso = di["db"].raw(
        'w."person_id" and w."created_at" = (select max("created_at") from weights where "person_id" = w."person_id")')

    students = di["db"].table('persons as p') \
                       .join('students as s', 's.person_id', '=', 'p.id') \
                       .where('s.personal_id', personal_id) \
                       .left_join('weights as w', 'p.id', '=', max_peso) \
                       .select('p.id', 'p.name', 'p.birth_date', 'p.height', 'p.gender', 'w.weight', 'p.deleted_at') \
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
    limit = int(limit)
    max_peso = di["db"].raw(
        'w."person_id" and w."created_at" = (select max("created_at") from weights where "person_id" = w."person_id")')

    students = di["db"].table('persons as p') \
                       .join('students as s', 's.person_id', '=', 'p.id') \
                       .where('s.personal_id', personal_id) \
                       .left_join('weights as w', 'p.id', '=', max_peso) \
                       .select('p.id', 'p.name', 'p.birth_date', 'p.height', 'p.gender', 'w.weight', 'p.deleted_at') \
                       .where('p.' + type_search(inputFilter), 'ilike', inputBar + '%') \
                       .order_by('p.created_at', 'desc') \
                       .limit(limit) \
                       .get()

    return students.serialize()


@student_router.get('/{person_id}')
async def find_student(person_id):
    newest_weight = Weight.where('person_id', person_id).max('created_at')
    if newest_weight:
        student = di["db"].table('persons') \
            .join('students', 'persons.person_id', '=', 'students.person_id') \
            .where('persons.person_id', person_id) \
            .join('weights', 'persons.person_id', '=', 'weights.person_id') \
            .where('weights.dtDas', newest_weight) \
            .first()
    else:
        student = di["db"].table('persons') \
            .join('students', 'persons.person_id', '=', 'students.person_id') \
            .where('persons.person_id', person_id) \
            .first()

    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "das": "Student not found."
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
            "das": "Student not found."
        }, 404)


@student_router.get("/avaliar/{person_id}")
async def get_student_for_avaliar_page(person_id):
    newest_weight = Weight.where('person_id', person_id).max('created_at')
    student = di["db"].table('persons as p') \
        .where('p.id', person_id) \
        .select('p.id', 'p.name', 'p.gender', 'w.weight', 'p.height', 'p.birth_date') \
        .join('weights as w', 'p.id', '=', 'w.person_id') \
        .where('w.created_at', newest_weight) \
        .first()

    if student:
        return student.serialize()
    else:
        return JSONResponse({
            "error": True,
            "das": "Student not found."
        }, 404)


@student_router.get("/antropometria_protocol/{person_id}")
async def get_antropometria_protocol(person_id):
    protocol = Student.select('antropometria_protocol').where(
        'person_id', person_id).first()
    return protocol.antropometria_protocol


@student_router.put("/antropometria_protocol/{person_id}")
async def update_antropometria_protocol(person_id, data: UpdateAntropometria):
    student = Student.find(person_id)
    student.antropometria_protocol = data.antropometria_protocol
    if student.save():
        return JSONResponse({
            "error": False,
            "data": f"Antropometria protocol was successfully updated."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong and Antropometria protocol could not be updated."
        }, 422)
