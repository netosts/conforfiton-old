# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .model import Personal
from .schema import NewPersonal
from ..person.model import Person


personal_router = APIRouter(prefix='/personal')


@personal_router.post('/')
async def new_personal(data: NewPersonal):
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
    person.name = data.name.capitalize()
    person.cpf = data.cpf
    person.gender = data.gender
    person.role = data.role
    person.email = data.email
    person.phone_number = data.phone_number
    person.birth_date = data.birth_date
    person.shirt_size = data.shirt_size
    person.shorts_size = data.shorts_size
    person.profile_picture = data.profile_picture

    personal = Personal()
    personal.person_id = person.id
    personal.company_id = data.company_id

    if person.save() and personal.save():
        return JSONResponse({
            "error": False,
            "data": f"{person.name} was successfully registered."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong and {person.name} could not be registered."
        }, 422)
