# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .model import Antropometria
from .schema import NewAntropometria
from ..person.model import Person

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
    antropometria.chest_skinfold = data.chest_skinfold
    antropometria.abdominal_skinfold = data.abdominal_skinfold
    antropometria.thighs_skinfold = data.thighs_skinfold
    antropometria.triceps_skinfold = data.triceps_skinfold
    antropometria.suprailiac_skinfold = data.suprailiac_skinfold
    antropometria.subscapularis_skinfold = data.subscapularis_skinfold
    antropometria.midaxillary_skinfold = data.midaxillary_skinfold
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
    antropometria.rcae_class = data.rcae_class
    antropometria.iac_result = data.iac_result
    antropometria.iac_class = data.iac_class
    antropometria.pg_result = data.pg_result
    antropometria.pg_class = data.pg_class

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
