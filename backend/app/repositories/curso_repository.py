from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.curso import Curso


class CursoRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Curso]:
        result = await self.db.execute(select(Curso).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_by_id(self, curso_id: int) -> Optional[Curso]:
        result = await self.db.execute(select(Curso).filter(Curso.id == curso_id))
        return result.scalar_one_or_none()

    async def get_by_nombre(self, nombre: str) -> Optional[Curso]:
        result = await self.db.execute(select(Curso).filter(Curso.nombre == nombre))
        return result.scalar_one_or_none()

    async def get_by_programa(self, programa_id: int) -> List[Curso]:
        result = await self.db.execute(select(Curso).filter(Curso.id_programa == programa_id))
        return result.scalars().all()

    async def create(self, curso_data: dict) -> Curso:
        db_curso = Curso(**curso_data)
        self.db.add(db_curso)
        await self.db.commit()
        await self.db.refresh(db_curso)
        return db_curso

    async def update(self, curso: Curso, curso_data: dict) -> Curso:
        for field, value in curso_data.items():
            if value is not None:
                setattr(curso, field, value)
        await self.db.commit()
        await self.db.refresh(curso)
        return curso

    async def delete(self, curso: Curso) -> None:
        await self.db.delete(curso)
        await self.db.commit()
