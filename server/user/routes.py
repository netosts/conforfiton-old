from fastapi import APIRouter


router = APIRouter(prefix='/user')

@router.post('/register')
def user_register():
    pass