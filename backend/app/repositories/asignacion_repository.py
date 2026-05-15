from typing import List

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.curso import Curso
from app.models.profesor_curso import profesor_cursos


class AsignacionRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_cursos_asignados(self, profesor_id: int) -> List[Curso]:
        result = await self.db.execute(
            select(Curso)
            .join(profesor_cursos, Curso.id == profesor_cursos.c.curso_id)
            .where(profesor_cursos.c.profesor_id == profesor_id)
            .order_by(Curso.nombre)
        )
        return result.scalars().all()

    async def replace_all(self, profesor_id: int, curso_ids: List[int]) -> List[Curso]:
        await self.db.execute(
            delete(profesor_cursos).where(profesor_cursos.c.profesor_id == profesor_id)
        )
        for curso_id in curso_ids:
            await self.db.execute(
                profesor_cursos.insert().values(profesor_id=profesor_id, curso_id=curso_id)
            )
        await self.db.commit()
        return await self.get_cursos_asignados(profesor_id)
