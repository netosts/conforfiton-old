# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models import RmConfig


rm_router = APIRouter(prefix='/rm_config')

@rm_router.get('/{sexo}')
async def get_rm_config(sexo):
    rm = RmConfig.select('exercicio', 'threshold', 'pontos').where('sexo', sexo).get()

    return rm.serialize()
