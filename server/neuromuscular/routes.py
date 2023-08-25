# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .model import Neuromuscular
from .schema import NewNeuromuscular
from ..person.model import Person


peso_router = APIRouter(prefix='/neurmuscular')

# Create a new Neuromuscular for a specific student using his id


@peso_router.post('/{student_id}')
async def new_neuromuscular(student_id, data: NewNeuromuscular):
    student = Person.find(student_id)
    if not student:
        return JSONResponse("Student not found", 404)

    neuromuscular = Neuromuscular()
    neuromuscular.id_pessoa = student.id_pessoa

    neuromuscular.pl_bench_press = data.pl_bench_press
    neuromuscular.pl_direct_thread = data.pl_direct_thread
    neuromuscular.pl_pull_front = data.pl_pull_front
    neuromuscular.pl_leg_press = data.pl_leg_press
    neuromuscular.pl_knee_extension = data.pl_knee_extension
    neuromuscular.pl_knee_bending = data.pl_knee_bending

    neuromuscular.reps_bench_press = data.reps_bench_press
    neuromuscular.reps_direct_thread = data.reps_direct_thread
    neuromuscular.reps_pull_front = data.reps_pull_front
    neuromuscular.reps_leg_press = data.reps_leg_press
    neuromuscular.reps_knee_extension = data.reps_knee_extension
    neuromuscular.reps_knee_bending = data.reps_knee_bending

    neuromuscular.rm_bench_press = data.rm_bench_press
    neuromuscular.rm_direct_thread = data.rm_direct_thread
    neuromuscular.rm_pull_front = data.rm_pull_front
    neuromuscular.rm_leg_press = data.rm_leg_press
    neuromuscular.rm_knee_extension = data.rm_knee_extension
    neuromuscular.rm_knee_bending = data.rm_knee_bending

    neuromuscular.pontos_bench_press = data.pontos_bench_press
    neuromuscular.pontos_direct_thread = data.pontos_direct_thread
    neuromuscular.pontos_pull_front = data.pontos_pull_front
    neuromuscular.pontos_leg_press = data.pontos_leg_press
    neuromuscular.pontos_knee_extension = data.pontos_knee_extension
    neuromuscular.pontos_knee_bending = data.pontos_knee_bending

    neuromuscular.total_pontos = data.total_pontos

    neuromuscular.created_at = data.created_at
    neuromuscular.save()

    return f"Neuromuscular de {student.nm_pessoa} cadastrado com sucesso!"
