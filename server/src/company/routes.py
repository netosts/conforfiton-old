# pylint: skip-file
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .model import Company
from .schema import NewCompany

company_router = APIRouter(prefix='/company')


@company_router.post('/')
async def new_company(data: NewCompany):
    company = Company()
    company.brand_name = data.brand_name
    company.business_name = data.business_name
    # company.cnpj = data.cnpj
    # company.exempt_sr = data.exempt_sr
    # company.state_registration = data.state_registration
    # company.uf = data.uf
    # company.email = data.email
    # company.phone_number = data.phone_number

    if company.save():
        return JSONResponse({
            "error": False,
            "data": f"{company.brand_name} was successfully registered."
        }, 200)
    else:
        return JSONResponse({
            "error": True,
            "data": f"Something went wrong and {company.brand_name} could not be registered."
        }, 422)
