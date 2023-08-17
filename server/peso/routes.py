# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models import Peso
from .schemas import NewPeso
from ..person.models import Person


peso_router = APIRouter(prefix='/peso')

# Create a new Peso for a specific student using his id


@peso_router.post('/{student_id}')
async def new_peso(student_id, data: NewPeso):
    student = Person.find(student_id)
    if not student:
        return JSONResponse("Student not found", 404)

    peso = Peso()
    peso.id_pessoa = student.id_pessoa
    peso.peso = data.peso
    peso.dt_data = data.dt_data
    peso.save()

    return f"Peso de {student.nm_pessoa} cadastrado com sucesso!"
