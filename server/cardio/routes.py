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

    cardio.fc_repouso = data.fc_repouso
    cardio.fc_max = data.fc_max
    cardio.l1 = data.l1
    cardio.l1_fc_max_percentage = data.l1_fc_max_percentage
    cardio.l2 = data.l2
    cardio.l2_fc_max_percentage = data.l2_fc_max_percentage
    cardio.distance = data.distance
    cardio.time = data.time
    cardio.fc_5min = data.fc_5min
    cardio.vo2max = data.vo2max
    cardio.vo2max_absolute = data.vo2max_absolute
    cardio.vo2max_mets = data.vo2max_mets
    cardio.vvo2max = data.vvo2max
    cardio.vvo2max_pace = data.vvo2max_pace
    cardio.vl1 = data.vl1
    cardio.vl1_pace = data.vl1_pace
    cardio.vl2 = data.vl2
    cardio.vl2_pace = data.vl2_pace
    cardio.elder_aerobic_power = data.elder_aerobic_power
    cardio.weekly_caloric_expenditure = data.weekly_caloric_expenditure
    cardio.daily_caloric_expenditure = data.daily_caloric_expenditure

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