from core.abstract_repository import SQLAlchemyRepository, AbstractRepository
from core.users.models import Users
from core.exceptions import CredentialsException
from fastapi_jwt import JwtAccessBearer
from core.settings import JWT_SECRET_KEY

jwt_bearer = JwtAccessBearer(secret_key=JWT_SECRET_KEY)

class AuthRepository(SQLAlchemyRepository):
    model = Users


class AuthService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def login(self, email: str, passwrod: str):
        if item := await self.repository.read_by_data(email=email, password=passwrod):
            return item, jwt_bearer.create_access_token(subject={"id": item.id, "username": item.username, "role": item.role})
        raise CredentialsException()