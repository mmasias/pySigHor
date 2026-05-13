from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.profesor import Profesor


class ProfesorRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Profesor]:
        result = await self.db.execute(select(Profesor).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_by_id(self, profesor_id: int) -> Optional[Profesor]:
        result = await self.db.execute(select(Profesor).filter(Profesor.id == profesor_id))
        return result.scalar_one_or_none()

    async def get_by_correo(self, correo: str) -> Optional[Profesor]:
        result = await self.db.execute(select(Profesor).filter(Profesor.correo == correo))
        return result.scalar_one_or_none()

    async def create(self, profesor_data: dict) -> Profesor:
        db_profesor = Profesor(**profesor_data)
        self.db.add(db_profesor)
        await self.db.commit()
        await self.db.refresh(db_profesor)
        return db_profesor

    async def update(self, profesor: Profesor, profesor_data: dict) -> Profesor:
        for field, value in profesor_data.items():
            if value is not None:
                setattr(profesor, field, value)
        await self.db.commit()
        await self.db.refresh(profesor)
        return profesor

    async def delete(self, profesor: Profesor) -> None:
        await self.db.delete(profesor)
        await self.db.commit()
