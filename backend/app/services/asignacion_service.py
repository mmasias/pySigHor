from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.curso import Curso
from app.repositories.asignacion_repository import AsignacionRepository
from app.repositories.profesor_repository import ProfesorRepository


class AsignacionService:

    def __init__(self, db: AsyncSession):
        self.db = db
        self.profesor_repo = ProfesorRepository(db)
        self.asignacion_repo = AsignacionRepository(db)

    async def obtener_asignaciones(self, profesor_id: int) -> List[Curso]:
        profesor = await self.profesor_repo.get_by_id(profesor_id)
        if not profesor:
            raise ValueError(f"Profesor con ID {profesor_id} no encontrado")
        return await self.asignacion_repo.get_cursos_asignados(profesor_id)

    async def actualizar_asignaciones(self, profesor_id: int, curso_ids: List[int]) -> List[Curso]:
        profesor = await self.profesor_repo.get_by_id(profesor_id)
        if not profesor:
            raise ValueError(f"Profesor con ID {profesor_id} no encontrado")

        if curso_ids:
            result = await self.db.execute(select(Curso).where(Curso.id.in_(curso_ids)))
            found = result.scalars().all()
            if len(found) != len(curso_ids):
                found_ids = {c.id for c in found}
                missing = [cid for cid in curso_ids if cid not in found_ids]
                raise ValueError(f"Cursos no encontrados: {missing}")

        return await self.asignacion_repo.replace_all(profesor_id, curso_ids)
