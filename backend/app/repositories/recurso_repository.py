from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.recurso import Recurso


class RecursoRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Recurso]:
        result = await self.db.execute(select(Recurso).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_by_id(self, recurso_id: int) -> Optional[Recurso]:
        result = await self.db.execute(select(Recurso).filter(Recurso.id == recurso_id))
        return result.scalar_one_or_none()

    async def get_by_nombre(self, nombre: str) -> Optional[Recurso]:
        result = await self.db.execute(select(Recurso).filter(Recurso.nombre == nombre))
        return result.scalar_one_or_none()

    async def create(self, recurso_data: dict) -> Recurso:
        db_recurso = Recurso(**recurso_data)
        self.db.add(db_recurso)
        await self.db.commit()
        await self.db.refresh(db_recurso)
        return db_recurso

    async def update(self, recurso: Recurso, recurso_data: dict) -> Recurso:
        for field, value in recurso_data.items():
            if value is not None:
                setattr(recurso, field, value)
        await self.db.commit()
        await self.db.refresh(recurso)
        return recurso

    async def delete(self, recurso: Recurso) -> None:
        await self.db.delete(recurso)
        await self.db.commit()
