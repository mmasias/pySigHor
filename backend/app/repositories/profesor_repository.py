from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.profesor import Profesor


class ProfesorRepository:
    """Repositorio de Profesor."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Profesor]:
        return self.db.query(Profesor).offset(skip).limit(limit).all()

    def get_by_id(self, profesor_id: int) -> Optional[Profesor]:
        return self.db.query(Profesor).filter(Profesor.id == profesor_id).first()

    def get_by_correo(self, correo: str) -> Optional[Profesor]:
        return self.db.query(Profesor).filter(Profesor.correo == correo).first()

    def create(self, profesor_data: dict) -> Profesor:
        db_profesor = Profesor(**profesor_data)
        self.db.add(db_profesor)
        self.db.commit()
        self.db.refresh(db_profesor)
        return db_profesor

    def update(self, profesor: Profesor, profesor_data: dict) -> Profesor:
        for field, value in profesor_data.items():
            if value is not None:
                setattr(profesor, field, value)
        self.db.commit()
        self.db.refresh(profesor)
        return profesor

    def delete(self, profesor: Profesor) -> None:
        self.db.delete(profesor)
        self.db.commit()
