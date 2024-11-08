from pydantic import BaseModel


class UsersBaseSchema(BaseModel):
    id: int


class UsersCreateSchema(BaseModel):
    username: str
    email: str
    password: str


class UsersGetSchema(UsersCreateSchema,UsersBaseSchema):
    role: str

class UsersUpdateSchema(UsersCreateSchema):
    ...
