# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models import Person
from .schemas import NewPerson


person_router = APIRouter(prefix='/person')

@person_router.post('/')  # Create a new person
async def new_person(data: NewPerson):
    # Look for CPF duplicate
    cpf = Person.where('cpfCnpj', data.cpfCnpj).count()
    if cpf > 0:
        error_message = {
            "error": "Duplicate CPF",
            "message": "The provided CPF is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)
    
    # Look for RG of specified UF duplicate
    if data.rg != None and data.ufRG != None:
        rg = Person.where('rg', data.rg).where('ufRG', data.ufRG).count()
        if rg > 0:
            error_message = {
                "error": "Duplicate RG in specified UF",
                "message": "The provided RG and UF are already registered in the database."
            }
            return JSONResponse(content=error_message, status_code=409)
        
    # Email duplicate validation
    email = Person.where('dsEmail', data.dsEmail).count()
    if email > 0:
        error_message = {
            "error": "Duplicate Email",
            "message": "The provided Email is already registered in the database."
        }
        return JSONResponse(content=error_message, status_code=409)

    person = Person()
    person.nmPessoa = data.nmPessoa
    person.ser = data.ser
    person.tipoPessoa = data.tipoPessoa
    person.cpfCnpj = data.cpfCnpj
    person.rg = data.rg
    person.ufRG = data.ufRG
    person.empPersonal = data.empPersonal
    person.dtNascimento = data.dtNascimento
    person.dsObs = data.dsObs
    person.dsEmail = data.dsEmail
    person.telefone = data.telefone
    person.save()

    return f"{person.nmPessoa} foi cadastrado(a) com sucesso!"


@person_router.delete('/{ID_Pessoa}')
async def delete_person(ID_Pessoa):
    person = Person.find(ID_Pessoa)
    personName = person.nmPessoa
    person.delete()

    return f"{personName} foi deletado(a) com sucesso!"