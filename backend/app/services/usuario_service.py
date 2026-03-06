from typing import Optional
from sqlalchemy.orm import Session

from app.models.usuario import Usuario


class UsuarioService:
    """Servicio de lógica de negocio de Usuario."""

    def __init__(self, db: Session):
        self.db = db

    def autenticar(self, username: str, password: str) -> Optional[Usuario]:
        """Autenticar usuario. Retorna el usuario si es válido, None si falla."""
        from app.repositories.usuario_repository import UsuarioRepository
        from app.core.security import verify_password

        repo = UsuarioRepository(self.db)
        usuario = repo.get_by_username(username)

        if not usuario:
            return None
        if not verify_password(password, usuario.hashed_password):
            return None
        if not usuario.activo:
            return None

        return usuario
