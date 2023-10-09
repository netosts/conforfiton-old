# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .model import Anamnese
from .schema import NewAnamnese
from ..person.model import Person
from ..student.model import Student

from fastapi.encoders import jsonable_encoder
from .schema import Period
import json

anamnese_router = APIRouter(prefix='/anamnese')


@anamnese_router.post('/{email}')
async def new_anamnese(email, data: NewAnamnese):
    person = Person.select('id', 'name').where('email', email).first()

    if not person:
        return JSONResponse({
            "error": True,
            "msg": "Person not found."
        }, 404)

    student = Student.find(person.id)

    anamnese = Anamnese()

    anamnese.person_id = person.id

    anamnese.menstruation = data.menstruation
    anamnese.iud = data.iud
    anamnese.physical_limitation = data.physical_limitation
    anamnese.diabetes = data.diabetes
    anamnese.hypertension = data.hypertension

    anamnese.fc_repouso = data.fc_repouso
    anamnese.fc_max = data.fc_max
    anamnese.l1 = data.l1
    anamnese.l2 = data.l2

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
    student.personal_goal = data.q26.capitalize()

    if data.q27 is not None:
        anamnese.q27 = data.q27.capitalize()
    else:
        anamnese.q27 = data.q27

    if anamnese.save():
        return JSONResponse({
            "error": False,
            "msg": f"{person.name}'s Anamnese successfully created."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "msg": f"An error occurred while creating {person.name}'s Anamnese."
        }, 422)


@anamnese_router.post('/student/{person_id}')
async def new_student_anamnese(person_id, data: NewAnamnese):
    person = Person.select('id', 'name').where('id', person_id).first()

    if not person:
        return JSONResponse({
            "error": True,
            "msg": "Person not found."
        }, 404)

    student = Student.find(person.id)

    anamnese = Anamnese()

    anamnese.person_id = person.id

    anamnese.menstruation = data.menstruation
    anamnese.iud = data.iud
    anamnese.physical_limitation = data.physical_limitation
    anamnese.diabetes = data.diabetes
    anamnese.hypertension = data.hypertension

    anamnese.fc_repouso = data.fc_repouso
    anamnese.fc_max = data.fc_max
    anamnese.l1 = data.l1
    anamnese.l2 = data.l2

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
    student.personal_goal = data.q26.capitalize()

    if data.q27 is not None:
        anamnese.q27 = data.q27.capitalize()
    else:
        anamnese.q27 = data.q27

    if anamnese.save():
        student.save()
        return JSONResponse({
            "error": False,
            "msg": f"{person.name}'s Anamnese successfully created."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "msg": f"An error occurred while creating {person.name}'s Anamnese."
        }, 422)


@anamnese_router.get('/{person_id}')
async def get_anamnese(person_id):
    anamnese = Anamnese.find(person_id)
    if anamnese:
        return anamnese.serialize()
    else:
        return JSONResponse({
            "error": True,
            "msg": f"Anamnese not found."
        }, 404)


@anamnese_router.get("/overview/{person_id}")
async def get_overview_information(person_id):
    anamnese = Anamnese.select(
        'q1',
        'q2',
        'q4',
        'q21',
        'q20',
        'diabetes',
        'hypertension',
        'q22',
        'fc_max',
        'fc_repouso',
        'l1',
        'l2'
    ).where('person_id', person_id).first()

    if anamnese:
        return anamnese.serialize()
    else:
        return JSONResponse({
            "error": True,
            "msg": f"Anamnese not found."
        }, 404)
