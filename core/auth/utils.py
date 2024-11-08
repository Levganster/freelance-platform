from fastapi import Depends
from fastapi_jwt import JwtAuthorizationCredentials
from core.auth.service import jwt_bearer
from core.exceptions import ForbiddenException

async def admin_required(credentials: JwtAuthorizationCredentials = Depends(jwt_bearer)):
    if credentials.subject.get("role") != "admin":
        raise ForbiddenException()
    return credentials

async def is_verified(credentials: JwtAuthorizationCredentials = Depends(jwt_bearer)):
    if credentials.subject.get("is_verified") != True:
        raise ForbiddenException()
    return credentials
