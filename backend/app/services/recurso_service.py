from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.recurso import Recurso
from app.schemas.recurso import RecursoCreate, RecursoUpdate
from app.repositories.recurso_repository import RecursoRepository


class RecursoService:
    """Servicio de lógica de negocio de Recurso."""

    def __init__(self, db: AsyncSession):
        self.repo = RecursoRepository(db)

    async def listar_recursos(self, skip: int = 0, limit: int = 100) -> List[Recurso]:
        return await self.repo.get_all(skip=skip, limit=limit)

    async def obtener_recurso(self, recurso_id: int) -> Recurso | None:
        return await self.repo.get_by_id(recurso_id)

    async def crear_recurso(self, recurso_data: RecursoCreate) -> Recurso:
        existente = await self.repo.get_by_nombre(recurso_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un recurso con el nombre '{recurso_data.nombre}'")
        return await self.repo.create(recurso_data.dict())

    async def actualizar_recurso(self, recurso_id: int, recurso_data: RecursoUpdate) -> Recurso:
        recurso = await self.repo.get_by_id(recurso_id)
        if not recurso:
            raise ValueError(f"Recurso con ID {recurso_id} no encontrado")
        if recurso_data.nombre and recurso_data.nombre != recurso.nombre:
            existente = await self.repo.get_by_nombre(recurso_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un recurso con el nombre '{recurso_data.nombre}'")
        return await self.repo.update(recurso, recurso_data.dict(exclude_unset=True))

    async def eliminar_recurso(self, recurso_id: int) -> None:
        recurso = await self.repo.get_by_id(recurso_id)
        if not recurso:
            raise ValueError(f"Recurso con ID {recurso_id} no encontrado")
        await self.repo.delete(recurso)
