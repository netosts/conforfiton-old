# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models import Anamnese
from .schemas import NewAnamnese
from ..student.models import Student


anamnese_router = APIRouter(prefix='/anamnese')

@anamnese_router.post('/{id_pessoa}')
async def new_anamnese(id_pessoa, data: NewAnamnese):
    student = Student.find(id_pessoa)
    if not student:
        return JSONResponse("Student not fonund", 404)
    
    return data
