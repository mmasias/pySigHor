from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.edificio import Edificio


class EdificioRepository:
    """Repositorio de Edificio."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Edificio]:
        return self.db.query(Edificio).offset(skip).limit(limit).all()

    def get_by_id(self, edificio_id: int) -> Optional[Edificio]:
        return self.db.query(Edificio).filter(Edificio.id == edificio_id).first()

    def get_by_nombre(self, nombre: str) -> Optional[Edificio]:
        return self.db.query(Edificio).filter(Edificio.nombre == nombre).first()

    def create(self, edificio_data: dict) -> Edificio:
        db_edificio = Edificio(**edificio_data)
        self.db.add(db_edificio)
        self.db.commit()
        self.db.refresh(db_edificio)
        return db_edificio

    def update(self, edificio: Edificio, edificio_data: dict) -> Edificio:
        for field, value in edificio_data.items():
            if value is not None:
                setattr(edificio, field, value)
        self.db.commit()
        self.db.refresh(edificio)
        return edificio

    def delete(self, edificio: Edificio) -> None:
        self.db.delete(edificio)
        self.db.commit()
