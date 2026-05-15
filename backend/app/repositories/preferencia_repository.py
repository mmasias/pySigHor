from typing import List

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.profesor_recurso import ProfesorRecurso


class PreferenciaRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_profesor(self, profesor_id: int) -> List[ProfesorRecurso]:
        result = await self.db.execute(
            select(ProfesorRecurso)
            .filter(ProfesorRecurso.profesor_id == profesor_id)
            .order_by(ProfesorRecurso.prioridad)
        )
        return result.scalars().all()

    async def replace_all(self, profesor_id: int, recurso_ids: List[int]) -> List[ProfesorRecurso]:
        await self.db.execute(
            delete(ProfesorRecurso).where(ProfesorRecurso.profesor_id == profesor_id)
        )
        for idx, recurso_id in enumerate(recurso_ids, start=1):
            self.db.add(
                ProfesorRecurso(profesor_id=profesor_id, recurso_id=recurso_id, prioridad=idx)
            )
        await self.db.commit()
        return await self.get_by_profesor(profesor_id)
