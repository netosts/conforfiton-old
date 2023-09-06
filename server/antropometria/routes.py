# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .model import Antropometria
from .schema import NewAntropometria
from ..person.model import Person

from fastapi.encoders import jsonable_encoder
from .schema import JsonCA_Risk
import json

antropometria_router = APIRouter(prefix='/antropometria')


@antropometria_router.post('/{person_id}')
async def new_antropometria(person_id, data: NewAntropometria):
    person = Person.select('id', 'name').where('id', person_id).first()
    if not person:
        return JSONResponse("Student not found", 404)

    antropometria = Antropometria()

    antropometria.person_id = person.id
    antropometria.weight = data.weight
    antropometria.antropometria_protocol = data.antropometria_protocol
    antropometria.abs = data.abs
    antropometria.waist = data.waist
    antropometria.hip = data.hip
    antropometria.thighs = data.thighs
    antropometria.right_biceps = data.right_biceps
    antropometria.right_forearm = data.right_forearm
    antropometria.chest = data.chest
    antropometria.triceps = data.triceps
    antropometria.suprailiac = data.suprailiac
    antropometria.subcapularis = data.subcapularis
    antropometria.midaxillary = data.midaxillary
    antropometria.imc_result = data.imc_result
    antropometria.imc_class = data.imc_class
    antropometria.ca_class = data.ca_class
    antropometria.ca_risk = json.dumps(jsonable_encoder(data.ca_risk, custom_encoder={
        JsonCA_Risk.dc,
        JsonCA_Risk.diabetes_ii,
        JsonCA_Risk.hypertension,
        JsonCA_Risk.cancer,
        JsonCA_Risk.depression,
        JsonCA_Risk.metabolic_syndrome,
    }))
    antropometria.rcq_result = data.rcq_result
    antropometria.rcq_class = data.rcq_class
    antropometria.rcae_class = data.rcae_class
    antropometria.iac_result = data.iac_result
    antropometria.iac_class = data.iac_class
    antropometria.pg_result = data.pg_result
    antropometria.pg_class = data.pg_class

    if antropometria.save():
        return JSONResponse({
            "error": False,
            "data": f"{person.name}'s Antropometria successfully created."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": "Something went wrong while registering {person.name}'s Antropometria."
        }, 422)
