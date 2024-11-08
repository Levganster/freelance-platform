APP_VERSION = '0.1'
APP_TITLE = 'Freelance'
DESCRIPTION = 'Freelance API'

DEBUG = True

DOCS_URL = "/docs"
REDOC_URL = "/redoc"

ALLOW_ORIGINS = ["*"]
ALLOW_METHODS = ["*"]
ALLOW_HEADERS = ["*"]
ALLOW_CREDENTIALS = True

ASYNC_DATABASE_URL ='postgresql+asyncpg://postgres:postgres@localhost:5432/freelance'
SYNC_DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/freelance'

JWT_SECRET_KEY = "your_secret_key"
