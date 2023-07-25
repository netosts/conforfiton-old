# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models import Cardio
from .schemas import NewCardio
from ..student.models import Student


cardio_router = APIRouter(prefix='/cardio')

# Create a new fqCardio for a specific student using his id
@cardio_router.post('/{student_id}')
async def new_cardio(student_id, data: NewCardio):
    student = Student.find(student_id)
    if not student:
        return JSONResponse("Student not found", 404)

    cardio = Cardio()
    cardio.ID_Pessoa = student.ID_Pessoa
    cardio.bpmRepouso = data.bpmRepouso
    cardio.bpmMaximo = data.bpmMaximo
    cardio.dtData = data.dtData
    cardio.save()

    return f"Frequência cardíaca de {student.nmPessoa} cadastrada com sucesso!"