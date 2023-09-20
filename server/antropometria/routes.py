# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .model import Antropometria
from .schema import NewAntropometria, UpdateAntropometria
from ..person.model import Person
from ..student.model import Student

import json

antropometria_router = APIRouter(prefix='/antropometria')


@antropometria_router.post('/{person_id}')
async def new_antropometria(person_id, data: NewAntropometria):
    person = Person.select('id', 'name').where('id', person_id).first()

    if not person:
        return JSONResponse({
            "error": True,
            "data": "Person not found."
        }, 404)

    antropometria = Antropometria()

    antropometria.person_id = person.id
    antropometria.weight = data.weight
    antropometria.antropometria_protocol = data.antropometria_protocol

    antropometria.abdominal_circumference = data.abdominal_circumference
    antropometria.waist_circumference = data.waist_circumference
    antropometria.hip_circumference = data.hip_circumference
    antropometria.thighs_circumference = data.thighs_circumference
    antropometria.right_biceps_circumference = data.right_biceps_circumference
    antropometria.right_forearm_circumference = data.right_forearm_circumference
    antropometria.chest_skin_fold = data.chest_skin_fold
    antropometria.abdominal_skin_fold = data.abdominal_skin_fold
    antropometria.thighs_skin_fold = data.thighs_skin_fold
    antropometria.triceps_skin_fold = data.triceps_skin_fold
    antropometria.suprailiac_skin_fold = data.suprailiac_skin_fold
    antropometria.subscapularis_skin_fold = data.subscapularis_skin_fold
    antropometria.midaxillary_skin_fold = data.midaxillary_skin_fold
    antropometria.iliac_circumference = data.iliac_circumference

    antropometria.imc_result = data.imc_result
    antropometria.imc_class = data.imc_class
    antropometria.ca_class = data.ca_class

    if data.ca_risk is not None:
        antropometria.ca_risk = json.dumps(data.ca_risk.__dict__)
    else:
        antropometria.ca_risk = data.ca_risk

    antropometria.rcq_result = data.rcq_result
    antropometria.rcq_class = data.rcq_class
    antropometria.rcae_result = data.rcae_result
    antropometria.rcae_class = data.rcae_class
    antropometria.iac_result = data.iac_result
    antropometria.iac_class = data.iac_class
    antropometria.pg_result = data.pg_result
    antropometria.pg_class = data.pg_class

    antropometria.pg_goal = data.pg_goal
    antropometria.weight_goal = data.weight_goal
    antropometria.mig_result = data.mig_result
    antropometria.mig_goal = data.mig_goal
    antropometria.fat_weight_result = data.fat_weight_result
    antropometria.fat_weight_goal = data.fat_weight_goal
    antropometria.mig_weight_result = data.mig_weight_result
    antropometria.mig_weight_goal = data.mig_weight_goal

    antropometria.created_at = data.created_at

    if antropometria.save():
        return JSONResponse({
            "error": False,
            "data": f"{person.name}'s Antropometria successfully created."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong while registering {person.name}'s Antropometria."
        }, 422)


@antropometria_router.get("/protocol/{person_id}")
async def get_antropometria_protocol(person_id):
    protocol = Student.select('antropometria_protocol').where(
        'person_id', person_id).first()
    return protocol.antropometria_protocol


@antropometria_router.get('/student/{person_id}')
async def get_antropometria_for_student_page(person_id):
    antropometria = Antropometria.select(
        'weight',
        'antropometria_protocol',
        'abdominal_circumference',
        'waist_circumference',
        'hip_circumference',
        'thighs_circumference',
        'right_biceps_circumference',
        'right_forearm_circumference',
        'chest_skin_fold',
        'abdominal_skin_fold',
        'thighs_skin_fold',
        'triceps_skin_fold',
        'suprailiac_skin_fold',
        'subscapularis_skin_fold',
        'midaxillary_skin_fold',
        'iliac_circumference',
        'imc_result',
        'imc_class',
        'ca_class',
        'ca_risk',
        'rcq_result',
        'rcq_class',
        'rcae_result',
        'rcae_class',
        'iac_result',
        'iac_class',
        'pg_result',
        'pg_class',
        'pg_goal',
        'weight_goal',
        'mig_result',
        'mig_goal',
        'fat_weight_result',
        'fat_weight_goal',
        'mig_weight_result',
        'mig_weight_goal',
        'created_at'
    ).where('person_id', person_id).order_by('created_at', 'desc').get().serialize()
    return antropometria


@antropometria_router.put("/protocol/{person_id}")
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
