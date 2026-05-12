from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.programa import Programa


class ProgramaRepository:
    """Repositorio de Programa."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Programa]:
        return self.db.query(Programa).offset(skip).limit(limit).all()

    def get_by_id(self, programa_id: int) -> Optional[Programa]:
        return self.db.query(Programa).filter(Programa.id == programa_id).first()

    def get_by_nombre(self, nombre: str) -> Optional[Programa]:
        return self.db.query(Programa).filter(Programa.nombre == nombre).first()

    def create(self, programa_data: dict) -> Programa:
        db_programa = Programa(**programa_data)
        self.db.add(db_programa)
        self.db.commit()
        self.db.refresh(db_programa)
        return db_programa

    def update(self, programa: Programa, programa_data: dict) -> Programa:
        for field, value in programa_data.items():
            if value is not None:
                setattr(programa, field, value)
        self.db.commit()
        self.db.refresh(programa)
        return programa

    def delete(self, programa: Programa) -> None:
        self.db.delete(programa)
        self.db.commit()
