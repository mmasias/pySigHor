from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.recurso import Recurso
from app.repositories.preferencia_repository import PreferenciaRepository
from app.repositories.profesor_repository import ProfesorRepository
from app.schemas.preferencia import PreferenciaResponse


class PreferenciaService:

    def __init__(self, db: AsyncSession):
        self.db = db
        self.profesor_repo = ProfesorRepository(db)
        self.preferencia_repo = PreferenciaRepository(db)

    async def obtener_preferencias(self, profesor_id: int) -> List[PreferenciaResponse]:
        profesor = await self.profesor_repo.get_by_id(profesor_id)
        if not profesor:
            raise ValueError(f"Profesor con ID {profesor_id} no encontrado")

        prefs = await self.preferencia_repo.get_by_profesor(profesor_id)
        if prefs:
            return [
                PreferenciaResponse(
                    recurso_id=p.recurso_id,
                    nombre_recurso=p.recurso.nombre,
                    prioridad=p.prioridad,
                )
                for p in prefs
            ]

        result = await self.db.execute(select(Recurso).order_by(Recurso.id))
        recursos = result.scalars().all()
        return [
            PreferenciaResponse(
                recurso_id=r.id,
                nombre_recurso=r.nombre,
                prioridad=idx,
            )
            for idx, r in enumerate(recursos, start=1)
        ]

    async def actualizar_preferencias(
        self, profesor_id: int, recurso_ids: List[int]
    ) -> List[PreferenciaResponse]:
        profesor = await self.profesor_repo.get_by_id(profesor_id)
        if not profesor:
            raise ValueError(f"Profesor con ID {profesor_id} no encontrado")

        result = await self.db.execute(select(Recurso).where(Recurso.id.in_(recurso_ids)))
        found = result.scalars().all()
        if len(found) != len(recurso_ids):
            found_ids = {r.id for r in found}
            missing = [rid for rid in recurso_ids if rid not in found_ids]
            raise ValueError(f"Recursos no encontrados: {missing}")

        prefs = await self.preferencia_repo.replace_all(profesor_id, recurso_ids)
        return [
            PreferenciaResponse(
                recurso_id=p.recurso_id,
                nombre_recurso=p.recurso.nombre,
                prioridad=p.prioridad,
            )
            for p in prefs
        ]
