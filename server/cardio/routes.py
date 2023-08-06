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
    cardio.id_pessoa = student.id_pessoa
    cardio.bpm_repouso = data.bpm_repouso
    cardio.bpm_maximo = data.bpm_maximo
    cardio.dt_data = data.dt_data
    cardio.save()

    return f"Frequência cardíaca de {student.nm_pessoa} cadastrada com sucesso!"