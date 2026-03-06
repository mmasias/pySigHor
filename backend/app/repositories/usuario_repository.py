from typing import Optional
from sqlalchemy.orm import Session

from app.models.usuario import Usuario


class UsuarioRepository:
    """Repositorio de Usuario."""

    def __init__(self, db: Session):
        self.db = db

    def get_by_username(self, username: str) -> Optional[Usuario]:
        """Obtener usuario por username."""
        return self.db.query(Usuario).filter(Usuario.username == username).first()

    def create(self, data: dict) -> Usuario:
        """Crear nuevo usuario."""
        db_usuario = Usuario(**data)
        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
