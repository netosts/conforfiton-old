# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models import Peso
from .schemas import NewPeso
from ..student.models import Student


peso_router = APIRouter(prefix='/peso')

# Create a new Peso for a specific student using his id
@peso_router.post('/{student_id}')
async def new_peso(student_id, data: NewPeso):
    student = Student.find(student_id)
    if not student:
        return JSONResponse("Student not found", 404)
    
    peso = Peso()
    peso.ID_Pessoa = student.ID_Pessoa
    peso.peso = data.peso
    peso.dtData = data.dtData
    peso.save()

    return f"Peso de {student.nmPessoa} cadastrado com sucesso!"