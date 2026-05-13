from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.aula import Aula
from app.schemas.aula import AulaCreate, AulaUpdate
from app.repositories.aula_repository import AulaRepository


class AulaService:
    """Servicio de lógica de negocio de Aula."""

    def __init__(self, db: AsyncSession):
        self.repo = AulaRepository(db)

    async def listar_aulas(self, skip: int = 0, limit: int = 100) -> List[Aula]:
        """Listar todas las aulas con paginación."""
        return await self.repo.get_all(skip=skip, limit=limit)

    async def obtener_aula(self, aula_id: int) -> Aula | None:
        """Obtener aula por ID."""
        return await self.repo.get_by_id(aula_id)

    async def crear_aula(self, aula_data: AulaCreate) -> Aula:
        """Crear nueva aula con validaciones."""
        existente = await self.repo.get_by_nombre(aula_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un aula con el nombre '{aula_data.nombre}'")

        return await self.repo.create(aula_data.dict())

    async def actualizar_aula(self, aula_id: int, aula_data: AulaUpdate) -> Aula:
        """Actualizar aula existente."""
        aula = await self.repo.get_by_id(aula_id)
        if not aula:
            raise ValueError(f"Aula con ID {aula_id} no encontrada")

        if aula_data.nombre and aula_data.nombre != aula.nombre:
            existente = await self.repo.get_by_nombre(aula_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un aula con el nombre '{aula_data.nombre}'")

        return await self.repo.update(aula, aula_data.dict(exclude_unset=True))

    async def eliminar_aula(self, aula_id: int) -> None:
        """Eliminar aula existente."""
        aula = await self.repo.get_by_id(aula_id)
        if not aula:
            raise ValueError(f"Aula con ID {aula_id} no encontrada")

        await self.repo.delete(aula)
