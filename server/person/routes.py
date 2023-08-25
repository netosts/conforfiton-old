# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .model import Person
from ..student.model import Student
from ..personal.model import Personal
from .schema import NewPerson


person_router = APIRouter(prefix='/person')


@person_router.post('/{role}')
async def new_person(role, data: NewPerson):
    # Look for CPF duplicate
    cpf = Person.where('cpf', data).count()
    if cpf > 0:
        error_message = {
            "error": "Duplicate CPF",
            "message": "The provided CPF is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)

    # Look for RG of specified UF duplicate
    if data.rg != None and data.uf_rg != None:
        rg = Person.where('rg', data.rg).where('uf_rg', data.uf_rg).count()
        if rg > 0:
            error_message = {
                "error": "Duplicate RG in specified UF",
                "message": "The provided RG and UF are already registered in the database."
            }
            return JSONResponse(content=error_message, status_code=409)

    # Email duplicate validation
    email = Person.where('ds_email', data.ds_email).count()
    if email > 0:
        error_message = {
            "error": "Duplicate Email",
            "message": "The provided Email is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)

    person = Person()
    person.nm_pessoa = data.nm_pessoa
    person.ser = data.ser
    person.tipo_pessoa = data.tipo_pessoa
    person.cpf_cnpj = data.cpf_cnpj
    person.rg = data.rg
    person.uf_rg = data.uf_rg
    person.emp_personal = data.emp_personal
    person.dt_nascimento = data.dt_nascimento
    person.ds_obs = data.ds_obs
    person.ds_email = data.ds_email
    person.telefone = data.telefone
    person.save()

    return f"{person.nm_pessoa} foi cadastrado(a) com sucesso!"


@person_router.delete('/{id_pessoa}')
async def delete_person(id_pessoa):
    person = Person.find(id_pessoa)
    personName = person.nm_pessoa
    person.delete()

    return f"{personName} foi deletado(a) com sucesso!"
