from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from .settings import (
    APP_VERSION,
    APP_TITLE,
    DEBUG,
    DESCRIPTION,
    DOCS_URL,
    REDOC_URL,
    ALLOW_METHODS,
    ALLOW_HEADERS,
    ALLOW_CREDENTIALS,
    ALLOW_ORIGINS,
)

app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    debug=DEBUG,
    description=DESCRIPTION,
    docs_url=DOCS_URL,
    redoc_url=REDOC_URL,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)

from core.users.views import router as users_router
from core.auth.views import router as auth_router
from core.projects.views import router as projects_router

routers = [users_router, auth_router, projects_router]
for router in routers:
    app.include_router(router)
