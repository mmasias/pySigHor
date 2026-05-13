from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.usuario import Usuario


class UsuarioRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_username(self, username: str) -> Optional[Usuario]:
        result = await self.db.execute(select(Usuario).filter(Usuario.username == username))
        return result.scalar_one_or_none()

    async def create(self, data: dict) -> Usuario:
        db_usuario = Usuario(**data)
        self.db.add(db_usuario)
        await self.db.commit()
        await self.db.refresh(db_usuario)
        return db_usuario
