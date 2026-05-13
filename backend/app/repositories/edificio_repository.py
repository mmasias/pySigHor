from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.edificio import Edificio


class EdificioRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Edificio]:
        result = await self.db.execute(select(Edificio).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_by_id(self, edificio_id: int) -> Optional[Edificio]:
        result = await self.db.execute(select(Edificio).filter(Edificio.id == edificio_id))
        return result.scalar_one_or_none()

    async def get_by_nombre(self, nombre: str) -> Optional[Edificio]:
        result = await self.db.execute(select(Edificio).filter(Edificio.nombre == nombre))
        return result.scalar_one_or_none()

    async def create(self, edificio_data: dict) -> Edificio:
        db_edificio = Edificio(**edificio_data)
        self.db.add(db_edificio)
        await self.db.commit()
        await self.db.refresh(db_edificio)
        return db_edificio

    async def update(self, edificio: Edificio, edificio_data: dict) -> Edificio:
        for field, value in edificio_data.items():
            if value is not None:
                setattr(edificio, field, value)
        await self.db.commit()
        await self.db.refresh(edificio)
        return edificio

    async def delete(self, edificio: Edificio) -> None:
        await self.db.delete(edificio)
        await self.db.commit()
