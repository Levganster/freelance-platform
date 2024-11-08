"""
FastAPI dependencies for the app users
"""

from core.users.service import UsersRepository, UsersService 

# TODO: define your dependencies here
def get_users_service():
    return UsersService(UsersRepository)