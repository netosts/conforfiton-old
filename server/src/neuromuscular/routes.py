# pylint: skip-file
from kink import di
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
    neuromuscular.classification = data.classification
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


@neuromuscular_router.get('/student/{person_id}')
async def get_neuromuscular_for_student_page(person_id):
    neuro = Neuromuscular.select(
        'neuromuscular_protocol',
        'bench_press_lifted',
        'bench_press_reps',
        'bench_press_rm',
        'bench_press_points',
        'barbell_curl_lifted',
        'barbell_curl_reps',
        'barbell_curl_rm',
        'barbell_curl_points',
        'pull_down_lifted',
        'pull_down_reps',
        'pull_down_rm',
        'pull_down_points',
        'leg_press_lifted',
        'leg_press_reps',
        'leg_press_rm',
        'leg_press_points',
        'leg_extension_lifted',
        'leg_extension_reps',
        'leg_extension_rm',
        'leg_extension_points',
        'leg_curl_lifted',
        'leg_curl_reps',
        'leg_curl_rm',
        'leg_curl_points',
        'total_points',
        'classification',
        'created_at',
    ).where('person_id', person_id).order_by('created_at', 'desc').get().serialize()

    rml = NeuromuscularRml.select(
        'neuromuscular_protocol',
        'sit_up',
        'push_up',
        'jump',
        'sit_up_result',
        'push_up_result',
        'jump_result',
        'created_at',
    ).where('person_id', person_id).order_by('created_at', 'desc').get().serialize()

    combined_list = neuro + rml

    if len(combined_list) > 0:
        return sorted(combined_list, key=lambda x: x["created_at"], reverse=True)


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
