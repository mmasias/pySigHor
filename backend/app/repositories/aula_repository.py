from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.aula import Aula
from app.models.recurso import Recurso


class AulaRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Aula]:
        result = await self.db.execute(
            select(Aula).options(selectinload(Aula.recursos)).offset(skip).limit(limit)
        )
        return result.scalars().all()

    async def get_by_id(self, aula_id: int) -> Optional[Aula]:
        result = await self.db.execute(
            select(Aula).options(selectinload(Aula.recursos)).filter(Aula.id == aula_id)
        )
        return result.scalar_one_or_none()

    async def get_by_nombre(self, nombre: str) -> Optional[Aula]:
        result = await self.db.execute(select(Aula).filter(Aula.nombre == nombre))
        return result.scalar_one_or_none()

    async def create(self, aula_data: dict) -> Aula:
        db_aula = Aula(**aula_data)
        self.db.add(db_aula)
        await self.db.commit()
        await self.db.refresh(db_aula)
        return db_aula

    async def update(self, aula: Aula, aula_data: dict) -> Aula:
        for field, value in aula_data.items():
            if value is not None:
                setattr(aula, field, value)
        await self.db.commit()
        await self.db.refresh(aula)
        return aula

    async def set_recursos(self, aula: Aula, ids_recursos: List[int]) -> Aula:
        result = await self.db.execute(
            select(Recurso).where(Recurso.id.in_(ids_recursos))
        )
        recursos = result.scalars().all()
        aula.recursos = list(recursos)
        await self.db.commit()
        await self.db.refresh(aula)
        return aula

    async def delete(self, aula: Aula) -> None:
        await self.db.delete(aula)
        await self.db.commit()
