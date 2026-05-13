from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.profesor import Profesor
from app.schemas.profesor import ProfesorCreate, ProfesorUpdate
from app.repositories.profesor_repository import ProfesorRepository


class ProfesorService:
    """Servicio de lógica de negocio de Profesor."""

    def __init__(self, db: AsyncSession):
        self.repo = ProfesorRepository(db)

    async def listar_profesores(self, skip: int = 0, limit: int = 100) -> List[Profesor]:
        return await self.repo.get_all(skip=skip, limit=limit)

    async def obtener_profesor(self, profesor_id: int) -> Profesor | None:
        return await self.repo.get_by_id(profesor_id)

    async def crear_profesor(self, profesor_data: ProfesorCreate) -> Profesor:
        if profesor_data.correo:
            existente = await self.repo.get_by_correo(profesor_data.correo)
            if existente:
                raise ValueError(f"Ya existe un profesor con el correo '{profesor_data.correo}'")
        return await self.repo.create(profesor_data.dict())

    async def actualizar_profesor(self, profesor_id: int, profesor_data: ProfesorUpdate) -> Profesor:
        profesor = await self.repo.get_by_id(profesor_id)
        if not profesor:
            raise ValueError(f"Profesor con ID {profesor_id} no encontrado")
        if profesor_data.correo and profesor_data.correo != profesor.correo:
            existente = await self.repo.get_by_correo(profesor_data.correo)
            if existente:
                raise ValueError(f"Ya existe un profesor con el correo '{profesor_data.correo}'")
        return await self.repo.update(profesor, profesor_data.dict(exclude_unset=True))

    async def eliminar_profesor(self, profesor_id: int) -> None:
        profesor = await self.repo.get_by_id(profesor_id)
        if not profesor:
            raise ValueError(f"Profesor con ID {profesor_id} no encontrado")
        await self.repo.delete(profesor)
