from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.aula import Aula


class AulaRepository:
    """Repositorio de Aula."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Aula]:
        """Obtener todas las aulas con paginación."""
        return self.db.query(Aula).offset(skip).limit(limit).all()

    def get_by_id(self, aula_id: int) -> Optional[Aula]:
        """Obtener aula por ID."""
        return self.db.query(Aula).filter(Aula.id == aula_id).first()

    def get_by_nombre(self, nombre: str) -> Optional[Aula]:
        """Obtener aula por nombre."""
        return self.db.query(Aula).filter(Aula.nombre == nombre).first()

    def create(self, aula_data: dict) -> Aula:
        """Crear nueva aula."""
        db_aula = Aula(**aula_data)
        self.db.add(db_aula)
        self.db.commit()
        self.db.refresh(db_aula)
        return db_aula

    def update(self, aula: Aula, aula_data: dict) -> Aula:
        """Actualizar aula existente."""
        for field, value in aula_data.items():
            if value is not None:
                setattr(aula, field, value)

        self.db.commit()
        self.db.refresh(aula)
        return aula

    def delete(self, aula: Aula) -> None:
        """Eliminar aula."""
        self.db.delete(aula)
        self.db.commit()
