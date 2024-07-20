from abc import ABC, abstractmethod

from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError

import config
from config import logger
from db.connection import async_db_session


class AbstractRepository(ABC):
    @abstractmethod
    async def fetch_all(self) -> list:
        raise NotImplemented

    @abstractmethod
    def get_by_id(self, id: int):
        raise NotImplemented

    @abstractmethod
    async def create_one(self, **kwargs):
        raise NotImplemented

    @abstractmethod
    async def update_by_id(self, id: int, **kwargs):
        raise NotImplemented

    @abstractmethod
    async def delete_by_id(self, id: int):
        raise NotImplemented


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def fetch_all(self) -> list["SQLAlchemyRepository.model"]:
        async with async_db_session as session:
            stmt = select(self.model)
            result = await session.execute(stmt)
            result = result.scalars().all()

        return result

    async def get_by_id(self, id: int) -> "SQLAlchemyRepository.model":
        async with async_db_session as session:
            stmt = select(self.model).where(self.model.id == id)

            try:
                result = await session.execute(stmt)
                result = result.scalars().first()
            except (SQLAlchemyError, Exception) as exc:
                logger.exception(f"An error occurred while getting {self.model} object. {id=}")

        return result

    async def create_one(self, **kwargs) -> "SQLAlchemyRepository.model":
        async with async_db_session as session:
            new_object = self.model(**kwargs)

            try:
                session.add(new_object)
                await session.commit()
                await session.flush()
            except (SQLAlchemyError, Exception) as exc:
                logger.exception(f"An error occurred while creating {self.model} object. {kwargs=}")

            return new_object

    async def update_by_id(self, id: int, **kwargs) -> "SQLAlchemyRepository.model":
        async with async_db_session as session:
            stmt = update(self.model).where(self.model.id == id).returning(self.model)
            stmt = stmt.values(**kwargs)

            try:
                result = await session.execute(stmt)
                result = result.scalars().first()
                await session.commit()
            except (SQLAlchemyError, Exception) as exc:
                logger.exception(f"An error occurred while updating {self.model} object. {id=}, {kwargs=}")

            if not result:
                raise Exception("Object not found")

            return result

    async def delete_by_id(self, id: int) -> None:
        async with async_db_session as session:
            stmt = delete(self.model).where(self.model.id == id)

            try:
                await session.execute(stmt)
                await session.commit()
            except (SQLAlchemyError, Exception) as exc:
                logger.exception(f"An error occurred while deleting {self.model} object. {id=}")
