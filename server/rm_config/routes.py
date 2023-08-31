# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .model import RmConfig


rm_router = APIRouter(prefix='/rm_config')


@rm_router.get('/{gender}')
async def get_rm_config(gender):
    if gender in 'Male' or gender in 'Female':
        rm_config = RmConfig.select('exercise', 'threshold',
                                    'points').where('gender', gender).get()

        return rm_config.serialize()
    else:
        return JSONResponse({
            "error": True,
            "data": "Gender is invalid"
        }, 422)
