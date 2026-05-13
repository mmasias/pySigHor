from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from app.core.security import verify_password


class UsuarioService:
    """Servicio de lógica de negocio de Usuario."""

    def __init__(self, db: AsyncSession):
        self.repo = UsuarioRepository(db)

    async def autenticar(self, username: str, password: str) -> Optional[Usuario]:
        """Autenticar usuario. Retorna el usuario si es válido, None si falla."""
        usuario = await self.repo.get_by_username(username)

        if not usuario:
            return None
        if not verify_password(password, usuario.hashed_password):
            return None
        if not usuario.activo:
            return None

        return usuario
