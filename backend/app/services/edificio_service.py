from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.edificio import Edificio
from app.schemas.edificio import EdificioCreate, EdificioUpdate
from app.repositories.edificio_repository import EdificioRepository


class EdificioService:
    """Servicio de lógica de negocio de Edificio."""

    def __init__(self, db: AsyncSession):
        self.repo = EdificioRepository(db)

    async def listar_edificios(self, skip: int = 0, limit: int = 100) -> List[Edificio]:
        return await self.repo.get_all(skip=skip, limit=limit)

    async def obtener_edificio(self, edificio_id: int) -> Edificio | None:
        return await self.repo.get_by_id(edificio_id)

    async def crear_edificio(self, edificio_data: EdificioCreate) -> Edificio:
        existente = await self.repo.get_by_nombre(edificio_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un edificio con el nombre '{edificio_data.nombre}'")
        return await self.repo.create(edificio_data.dict())

    async def actualizar_edificio(self, edificio_id: int, edificio_data: EdificioUpdate) -> Edificio:
        edificio = await self.repo.get_by_id(edificio_id)
        if not edificio:
            raise ValueError(f"Edificio con ID {edificio_id} no encontrado")
        if edificio_data.nombre and edificio_data.nombre != edificio.nombre:
            existente = await self.repo.get_by_nombre(edificio_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un edificio con el nombre '{edificio_data.nombre}'")
        return await self.repo.update(edificio, edificio_data.dict(exclude_unset=True))

    async def eliminar_edificio(self, edificio_id: int) -> None:
        edificio = await self.repo.get_by_id(edificio_id)
        if not edificio:
            raise ValueError(f"Edificio con ID {edificio_id} no encontrado")
        await self.repo.delete(edificio)
