from sqlalchemy.exc import IntegrityError

from core.abstract_repository import SQLAlchemyRepository, AbstractRepository
from core.users.models import Users
from core.exceptions import ConflictException, NotFoundException, CredentialsException
from core.users.schemas import UsersCreateSchema

class UsersRepository(SQLAlchemyRepository):
    model = Users


class UsersService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def create(self, item: UsersCreateSchema):
        item_dict = item.model_dump()
        try:
            return await self.repository.create(item_dict)
        except IntegrityError:
            raise ConflictException()

    async def get_all(self, limit: int, offset: int):
        if items := await self.repository.read_all(limit, offset):
            return items
        raise NotFoundException()

    async def get_by_id(self, id: int):
        if item := await self.repository.read_by_id(id):
            return item
        raise NotFoundException()

    async def update(self, id: int, item: UsersCreateSchema):
        item_dict = item.model_dump()
    
        if upd_item := await self.repository.update_by_id(id, item_dict):
            return upd_item
        raise NotFoundException()

    async def delete(self, id: int):
        if item := await self.repository.delete_by_id(id):
            return item
        raise NotFoundException()
    
    async def login(self, email: str, passwrod: str):
        if item := await self.repository.read_by_data(email=email, password=passwrod):
            return {"email": item.email, "password": item.password}
        raise CredentialsException()
    
    async def verify(self, id: int):
        if item := await self.repository.update_by_id(id, {"is_verified": True}):
            return item
        raise NotFoundException()