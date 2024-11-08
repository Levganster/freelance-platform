from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from core.settings import ASYNC_DATABASE_URL


class Base(DeclarativeBase):
    __table_args__ = {
        'extend_existing': True
    }


engine = create_async_engine(ASYNC_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)