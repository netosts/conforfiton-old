# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .model import Cardio
from .schema import NewCardio, UpdateCardio
from ..person.model import Person
from ..student.model import Student

cardio_router = APIRouter(prefix='/cardio')


@cardio_router.post('/{person_id}')
async def new_cardio(person_id, data: NewCardio):
    person = Person.select('id', 'name').where('id', person_id).first()

    if not person:
        return JSONResponse({
            "error": True,
            "data": "Person not found."
        }, 404)

    cardio = Cardio()

    cardio.person_id = person.id
    cardio.weight = data.weight
    cardio.cardio_protocol = data.cardio_protocol

    cardio.created_at = data.created_at

    if cardio.save():
        return JSONResponse({
            "error": False,
            "data": f"{person.name}'s Cardio successfully created."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong while registering {person.name}'s Cardio."
        }, 422)


@cardio_router.get("/protocol/{person_id}")
async def get_cardio_protocol(person_id):
    protocol = Student.select('cardio_protocol').where(
        'person_id', person_id).first()
    return protocol.cardio_protocol


@cardio_router.put("/protocol/{person_id}")
async def update_cardio_protocol(person_id, data: UpdateCardio):
    student = Student.find(person_id)
    student.cardio_protocol = data.cardio_protocol
    if student.save():
        return JSONResponse({
            "error": False,
            "data": f"Cardio protocol was successfully updated."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong and Cardio protocol could not be updated."
        }, 422)
