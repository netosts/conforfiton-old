# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..person.model import Person
from ..personal.model import Personal
from .schema import NewGlobalEntity

global_entity_router = APIRouter(prefix='/global_entity')


@global_entity_router.post('/')
async def new_global_entity(data: NewGlobalEntity):
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
    person.role = data.role
    person.email = data.email
    person.phone_number = data.phone_number
    person.birth_date = data.birth_date

    if person.save():
        if data.role == 'Admin' or data.role == 'Demo':
            personal = Personal()
            personal.person_id = person.id
            personal.company_id = 1
            personal.cref = None
            personal.status = 'Accepted'
            if personal.save():
                return JSONResponse({
                    "error": False,
                    "data": f"{person.name} was successfully registered."
                }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong and {person.name} could not be registered."
        }, 422)
