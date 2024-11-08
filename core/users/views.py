from fastapi import APIRouter, status, Depends

from core.users.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)

from core.users.dependencies import get_users_service
from core.users.service import UsersService
from core.users.schemas import UsersCreateSchema, UsersGetSchema, UsersUpdateSchema
from core.auth.utils import admin_required

router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)

@router.get('/{id}', dependencies=[Depends(admin_required)], response_model=UsersGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    id: int,
    service: UsersService = Depends(get_users_service),
):
    item = await service.get_by_id(id)
    return item


@router.post('/', response_model=UsersGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    item: UsersCreateSchema,
    service: UsersService = Depends(get_users_service),
):
    new_item = await service.create(item)
    return new_item


@router.put('/{id}', dependencies=[Depends(admin_required)], response_model=UsersGetSchema, status_code=status.HTTP_200_OK)
async def update_one(
    id: int,
    new_item: UsersUpdateSchema,
    service: UsersService = Depends(get_users_service),
):
    new_item = await service.update(id, new_item)
    return new_item


@router.delete('/{id}', dependencies=[Depends(admin_required)], status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: UsersService = Depends(get_users_service),
):
    await service.delete(id)


@router.get('/', dependencies=[Depends(admin_required)], response_model=list[UsersGetSchema], status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: UsersService = Depends(get_users_service),
):
    items = await service.get_all(limit=limit, offset=offset)
    return items

@router.post('/verify/{id}', status_code=status.HTTP_200_OK)
async def verify_user(
    id: int,
    service: UsersService = Depends(get_users_service),
):
    await service.verify(id)
    return {"message": "User verified"}
