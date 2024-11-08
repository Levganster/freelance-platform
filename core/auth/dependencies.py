"""
FastAPI dependencies for the app users
"""

from core.auth.service import AuthRepository, AuthService 

# TODO: define your dependencies here
def get_auth_service():
    return AuthService(AuthRepository)