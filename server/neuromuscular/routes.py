# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .model import Neuromuscular
from .schema import NewNeuromuscular
from ..person.model import Person


neuromuscular_router = APIRouter(prefix='/neuromuscular')


@neuromuscular_router.post('/{person_id}')
async def new_neuromuscular(person_id, data: NewNeuromuscular):
    person = Person.select('id', 'name').where('id', person_id).first()
    if not person:
        return JSONResponse("Student not found", 404)

    neuromuscular = Neuromuscular()

    neuromuscular.person_id = person.id

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

    neuromuscular.save()
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
