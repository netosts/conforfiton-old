# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from datetime import datetime

from .model import Person
from ..student.model import Student
from ..personal.model import Personal
from ..weight.model import Weight

person_router = APIRouter(prefix='/person')


# @person_router.post('/')
# async def new_person(data: NewPerson):
#     # CPF duplicate validation
#     cpf = Person.where('cpf', data.cpf).count()
#     if cpf > 0:
#         return JSONResponse({
#             "error": True,
#             "data": "The provided CPF is already registered in the database."
#         }, 409)

#     # Email duplicate validation
#     email = Person.where('email', data.email).count()
#     if email > 0:
#         return JSONResponse({
#             "error": True,
#             "data": "The provided Email is already registered in the database."
#         }, 409)

#     # Phone Number duplicate validation
#     phone_number = Person.where('phone_number', data.phone_number).count()
#     if phone_number > 0:
#         return JSONResponse({
#             "error": True,
#             "data": "The provided Phone Number is already registered in the database."
#         }, 409)

#     person = Person()
#     person.name = data.name.capitalize()
#     person.cpf = data.cpf
#     person.gender = data.gender
#     person.role = data.role
#     person.email = data.email
#     person.phone_number = data.phone_number
#     person.birth_date = data.birth_date
#     person.shirt_size = data.shirt_size
#     person.shorts_size = data.shorts_size
#     person.address_picture = data.address_picture

#     user = User()
#     user.person_id = person.id

#     person_id = Person.select('id').where('email', email)

#     if data.role == 'Student':
#         if data.height is None or data.weight is None:
#             return JSONResponse({
#                 "error": True,
#                 "data": "Student height and weight are necessary."
#             }, 422)
#         person_role = Student()
#         person_role.person_id = person.id
#         person_role.company_id = data.company_id
#         person_role.personal_id = data.personal_id
#     elif data.role == 'Personal':
#         person_role = Personal()
#         person_role.person_id = person.id
#         person_role.company_id = data.company_id

#     person.height = data.height
#     if data.weight is not None:
#         weight = Weight()
#         weight.person_id = person.id
#         weight.weight = data.weight
#         weight.created_at = datetime
#         if not weight.save():
#             return JSONResponse({
#                 "error": True,
#                 "data": f"Something went wrong while creating {person.name}'s WEIGHT."
#             }, 422)

#     if person.save() and person_role.save():
#         return JSONResponse({
#             "error": False,
#             "data": f"{person.name} was successfully registered."
#         }, 200)
#     else:
#         return JSONResponse({
#             "error": True,
#             "data": f"Something went wrong and {person.name} could not be registered."
#         }, 422)


@person_router.delete('/{id_pessoa}')
async def delete_person(id_pessoa):
    person = Person.find(id_pessoa)
    personName = person.nm_pessoa
    person.delete()

    return f"{personName} foi deletado(a) com sucesso!"
