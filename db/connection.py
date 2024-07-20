from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config import PATH_TO_DB_FILE

engine = create_engine(fr"sqlite:///{PATH_TO_DB_FILE.absolute()}", echo=False)
async_engine = create_async_engine(fr"sqlite+aiosqlite:///{PATH_TO_DB_FILE.absolute()}", echo=False)

async_db_session = async_sessionmaker(async_engine)()
