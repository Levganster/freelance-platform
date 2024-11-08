from fastapi import APIRouter, status, Depends

from core.auth.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)

from core.auth.dependencies import get_auth_service
from core.auth.service import AuthService
from core.auth.schemas import AuthLoginSchema, AuthLoginResponseSchema


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)

@router.post('/login', response_model=AuthLoginResponseSchema, status_code=status.HTTP_200_OK)
async def login(
    item: AuthLoginSchema,
    service: AuthService = Depends(get_auth_service),
):
    item, token = await service.login(item.email, item.password)
    return {"username": item.username, "token": token}