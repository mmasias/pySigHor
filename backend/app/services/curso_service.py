from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.curso import Curso
from app.schemas.curso import CursoCreate, CursoUpdate
from app.repositories.curso_repository import CursoRepository


class CursoService:
    """Servicio de lógica de negocio de Curso."""

    def __init__(self, db: AsyncSession):
        self.repo = CursoRepository(db)

    async def listar_cursos(self, skip: int = 0, limit: int = 100) -> List[Curso]:
        return await self.repo.get_all(skip=skip, limit=limit)

    async def obtener_curso(self, curso_id: int) -> Curso | None:
        return await self.repo.get_by_id(curso_id)

    async def crear_curso(self, curso_data: CursoCreate) -> Curso:
        existente = await self.repo.get_by_nombre(curso_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un curso con el nombre '{curso_data.nombre}'")
        return await self.repo.create(curso_data.dict())

    async def actualizar_curso(self, curso_id: int, curso_data: CursoUpdate) -> Curso:
        curso = await self.repo.get_by_id(curso_id)
        if not curso:
            raise ValueError(f"Curso con ID {curso_id} no encontrado")
        if curso_data.nombre and curso_data.nombre != curso.nombre:
            existente = await self.repo.get_by_nombre(curso_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un curso con el nombre '{curso_data.nombre}'")
        return await self.repo.update(curso, curso_data.dict(exclude_unset=True))

    async def eliminar_curso(self, curso_id: int) -> None:
        curso = await self.repo.get_by_id(curso_id)
        if not curso:
            raise ValueError(f"Curso con ID {curso_id} no encontrado")
        await self.repo.delete(curso)
