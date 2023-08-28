# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from datetime import datetime

from .model import Weight
from .schema import NewWeight
from ..person.model import Person


weight_router = APIRouter(prefix='/weight')


@weight_router.post('/{person_id}')
async def new_weight(person_id, data: NewWeight):
    person = Person.find(person_id)
    if not person:
        return JSONResponse("Person not found", 404)

    weight = Weight()
    weight.person_id = person.person_id
    weight.weight = data.weight
    weight.created_at = datetime
    if weight.save():
        return JSONResponse({
            "error": False,
            "data": f"{person.name}'s Weight successfully registered."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong while registering {person.name}'s WEIGHT."
        }, 422)
