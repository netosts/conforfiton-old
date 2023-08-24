# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .models import RmConfig


rm_router = APIRouter(prefix='/rm_config')


@rm_router.get('/{gender}')
async def get_rm_config(gender):
    if gender not in 'Male' or 'Female':
        return JSONResponse({
            "error": True,
            "data": "Gender is invalid"
        }, 422)

    rm = RmConfig.select('exercise', 'threshold',
                         'points').where('gender', gender).get()

    return rm.serialize()
