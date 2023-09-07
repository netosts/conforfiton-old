# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .model import Neuromuscular, NeuromuscularRml
from .schema import NewNeuromuscular, UpdateNeuromuscular, NewNeuromuscularRml
from ..person.model import Person
from ..student.model import Student

neuromuscular_router = APIRouter(prefix='/neuromuscular')


@neuromuscular_router.post('/{person_id}')
async def new_neuromuscular(person_id, data: NewNeuromuscular):
    person = Person.select('id', 'name').where('id', person_id).first()
    if not person:
        return JSONResponse({
            "error": True,
            "data": "Person not found."
        }, 404)

    neuromuscular = Neuromuscular()

    neuromuscular.person_id = person.id
    neuromuscular.neuromuscular_protocol = data.neuromuscular_protocol

    neuromuscular.bench_press_lifted = data.bench_press_lifted
    neuromuscular.bench_press_reps = data.bench_press_reps
    neuromuscular.bench_press_rm = data.bench_press_rm
    neuromuscular.bench_press_points = data.bench_press_points

    neuromuscular.barbell_curl_lifted = data.barbell_curl_lifted
    neuromuscular.barbell_curl_reps = data.barbell_curl_reps
    neuromuscular.barbell_curl_rm = data.barbell_curl_rm
    neuromuscular.barbell_curl_points = data.barbell_curl_points

    neuromuscular.pull_down_lifted = data.pull_down_lifted
    neuromuscular.pull_down_reps = data.pull_down_reps
    neuromuscular.pull_down_rm = data.pull_down_rm
    neuromuscular.pull_down_points = data.pull_down_points

    neuromuscular.leg_press_lifted = data.leg_press_lifted
    neuromuscular.leg_press_reps = data.leg_press_reps
    neuromuscular.leg_press_rm = data.leg_press_rm
    neuromuscular.leg_press_points = data.leg_press_points

    neuromuscular.leg_extension_lifted = data.leg_extension_lifted
    neuromuscular.leg_extension_reps = data.leg_extension_reps
    neuromuscular.leg_extension_rm = data.leg_extension_rm
    neuromuscular.leg_extension_points = data.leg_extension_points

    neuromuscular.leg_curl_lifted = data.leg_curl_lifted
    neuromuscular.leg_curl_reps = data.leg_curl_reps
    neuromuscular.leg_curl_rm = data.leg_curl_rm
    neuromuscular.leg_curl_points = data.leg_curl_points

    neuromuscular.total_points = data.total_points
    neuromuscular.created_at = data.created_at

    if neuromuscular.save():
        return JSONResponse({
            "error": False,
            "data": f"{person.name}'s Neuromsucular successfully registered."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong while registering {person.name}'s Neuromuscular."
        }, 422)


@neuromuscular_router.post('/rml/{person_id}')
async def new_neuromuscular(person_id, data: NewNeuromuscularRml):
    if data.sit_up is None and data.push_up is None and data.jump is None:
        return JSONResponse({
            "error": True,
            "data": "No value was passed to be registered."
        }, 422)

    person = Person.select('id', 'name').where('id', person_id).first()
    if not person:
        return JSONResponse({
            "error": True,
            "data": "Person not found."
        }, 404)

    neuromuscular_rml = NeuromuscularRml()

    neuromuscular_rml.person_id = person.id
    neuromuscular_rml.neuromuscular_protocol = data.neuromuscular_protocol

    neuromuscular_rml.sit_up = data.sit_up
    neuromuscular_rml.push_up = data.push_up
    neuromuscular_rml.jump = data.jump

    neuromuscular_rml.sit_up_result = data.sit_up_result
    neuromuscular_rml.push_up_result = data.push_up_result
    neuromuscular_rml.jump_result = data.jump_result

    neuromuscular_rml.created_at = data.created_at

    if neuromuscular_rml.save():
        return JSONResponse({
            "error": False,
            "data": f"{person.name}'s Neuromsucular RML successfully registered."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong while registering {person.name}'s Neuromuscular RML."
        }, 422)


@neuromuscular_router.get("/protocol/{person_id}")
async def get_neuromuscular_protocol(person_id):
    protocol = Student.select('neuromuscular_protocol').where(
        'person_id', person_id).first()
    return protocol.neuromuscular_protocol


@neuromuscular_router.put("/protocol/{person_id}")
async def update_neuromuscular_protocol(person_id, data: UpdateNeuromuscular):
    student = Student.find(person_id)
    student.neuromuscular_protocol = data.neuromuscular_protocol
    if student.save():
        return JSONResponse({
            "error": False,
            "data": f"Neuromuscular protocol was successfully updated."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong and Neuromuscular protocol could not be updated."
        }, 422)
