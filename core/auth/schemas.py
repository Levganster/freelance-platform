from pydantic import BaseModel

class AuthLoginSchema(BaseModel):
    email: str
    password: str

class AuthLoginResponseSchema(BaseModel):
    username: str
    token: str
