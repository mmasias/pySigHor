from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.programa import Programa
from app.schemas.programa import ProgramaCreate, ProgramaUpdate
from app.repositories.programa_repository import ProgramaRepository


class ProgramaService:
    """Servicio de lógica de negocio de Programa."""

    def __init__(self, db: AsyncSession):
        self.repo = ProgramaRepository(db)

    async def listar_programas(self, skip: int = 0, limit: int = 100) -> List[Programa]:
        return await self.repo.get_all(skip=skip, limit=limit)

    async def obtener_programa(self, programa_id: int) -> Programa | None:
        return await self.repo.get_by_id(programa_id)

    async def crear_programa(self, programa_data: ProgramaCreate) -> Programa:
        existente = await self.repo.get_by_nombre(programa_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un programa con el nombre '{programa_data.nombre}'")
        return await self.repo.create(programa_data.dict())

    async def actualizar_programa(self, programa_id: int, programa_data: ProgramaUpdate) -> Programa:
        programa = await self.repo.get_by_id(programa_id)
        if not programa:
            raise ValueError(f"Programa con ID {programa_id} no encontrado")
        if programa_data.nombre and programa_data.nombre != programa.nombre:
            existente = await self.repo.get_by_nombre(programa_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un programa con el nombre '{programa_data.nombre}'")
        return await self.repo.update(programa, programa_data.dict(exclude_unset=True))

    async def eliminar_programa(self, programa_id: int) -> None:
        programa = await self.repo.get_by_id(programa_id)
        if not programa:
            raise ValueError(f"Programa con ID {programa_id} no encontrado")
        await self.repo.delete(programa)
