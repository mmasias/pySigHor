from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.recurso import Recurso


class RecursoRepository:
    """Repositorio de Recurso."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Recurso]:
        return self.db.query(Recurso).offset(skip).limit(limit).all()

    def get_by_id(self, recurso_id: int) -> Optional[Recurso]:
        return self.db.query(Recurso).filter(Recurso.id == recurso_id).first()

    def get_by_nombre(self, nombre: str) -> Optional[Recurso]:
        return self.db.query(Recurso).filter(Recurso.nombre == nombre).first()

    def create(self, recurso_data: dict) -> Recurso:
        db_recurso = Recurso(**recurso_data)
        self.db.add(db_recurso)
        self.db.commit()
        self.db.refresh(db_recurso)
        return db_recurso

    def update(self, recurso: Recurso, recurso_data: dict) -> Recurso:
        for field, value in recurso_data.items():
            if value is not None:
                setattr(recurso, field, value)
        self.db.commit()
        self.db.refresh(recurso)
        return recurso

    def delete(self, recurso: Recurso) -> None:
        self.db.delete(recurso)
        self.db.commit()
