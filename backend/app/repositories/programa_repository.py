from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.programa import Programa


class ProgramaRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Programa]:
        result = await self.db.execute(select(Programa).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_by_id(self, programa_id: int) -> Optional[Programa]:
        result = await self.db.execute(select(Programa).filter(Programa.id == programa_id))
        return result.scalar_one_or_none()

    async def get_by_nombre(self, nombre: str) -> Optional[Programa]:
        result = await self.db.execute(select(Programa).filter(Programa.nombre == nombre))
        return result.scalar_one_or_none()

    async def create(self, programa_data: dict) -> Programa:
        db_programa = Programa(**programa_data)
        self.db.add(db_programa)
        await self.db.commit()
        await self.db.refresh(db_programa)
        return db_programa

    async def update(self, programa: Programa, programa_data: dict) -> Programa:
        for field, value in programa_data.items():
            if value is not None:
                setattr(programa, field, value)
        await self.db.commit()
        await self.db.refresh(programa)
        return programa

    async def delete(self, programa: Programa) -> None:
        await self.db.delete(programa)
        await self.db.commit()
