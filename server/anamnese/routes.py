# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models import Anamnese
from .schemas import NewAnamnese
from ..person.models import Person

from fastapi.encoders import jsonable_encoder
from .schemas import Period
import json

anamnese_router = APIRouter(prefix='/anamnese')


@anamnese_router.post('/')
async def new_anamnese(data: NewAnamnese):
    id_pessoa = Person.max('id_pessoa')
    anamnese = Anamnese()
    if not id_pessoa:
        return JSONResponse(
            {
                "error": True,
                "data": "Couldn't find id."
            }, 404)

    anamnese.id_pessoa = id_pessoa
    anamnese.q1 = data.q1.capitalize()
    anamnese.q2 = data.q2.capitalize()
    anamnese.q3 = data.q3.capitalize()
    anamnese.q4 = json.dumps(data.q4.__dict__)
    anamnese.q5 = data.q5.capitalize()
    anamnese.q6 = data.q6.capitalize()
    anamnese.q7 = data.q7.capitalize()
    anamnese.q8 = data.q8.capitalize()
    anamnese.q9 = data.q9.capitalize()
    anamnese.q10 = data.q10.capitalize()
    anamnese.q11 = data.q11.capitalize()
    anamnese.q12 = data.q12
    anamnese.q13 = json.dumps(jsonable_encoder(data.q13, custom_encoder={
        Period: lambda p: p.name}))
    anamnese.q14 = data.q14
    anamnese.q15 = data.q15
    anamnese.q16 = data.q16.capitalize()
    anamnese.q17 = data.q17
    anamnese.q18 = data.q18.capitalize()
    anamnese.q19 = data.q19.capitalize()
    anamnese.q20 = data.q20
    if data.q21 is not None:
        anamnese.q21 = data.q21.capitalize()
    else:
        anamnese.q21 = data.q21
    anamnese.q22 = data.q22.capitalize()
    anamnese.q23 = data.q23.capitalize()
    anamnese.q24 = data.q24
    anamnese.q25 = data.q25
    anamnese.q26 = data.q26.capitalize()
    if data.q27 is not None:
        anamnese.q27 = data.q27.capitalize()
    else:
        anamnese.q27 = data.q27

    if anamnese.save():
        return JSONResponse({
            "error": False,
            "data": "Anamnese successfully created."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": "An error occurred while creating Anamnese."
        }, 422)
