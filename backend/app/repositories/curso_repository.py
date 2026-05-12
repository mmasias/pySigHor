from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.curso import Curso


class CursoRepository:
    """Repositorio de Curso."""

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Curso]:
        return self.db.query(Curso).offset(skip).limit(limit).all()

    def get_by_id(self, curso_id: int) -> Optional[Curso]:
        return self.db.query(Curso).filter(Curso.id == curso_id).first()

    def get_by_nombre(self, nombre: str) -> Optional[Curso]:
        return self.db.query(Curso).filter(Curso.nombre == nombre).first()

    def get_by_programa(self, programa_id: int) -> List[Curso]:
        return self.db.query(Curso).filter(Curso.id_programa == programa_id).all()

    def create(self, curso_data: dict) -> Curso:
        db_curso = Curso(**curso_data)
        self.db.add(db_curso)
        self.db.commit()
        self.db.refresh(db_curso)
        return db_curso

    def update(self, curso: Curso, curso_data: dict) -> Curso:
        for field, value in curso_data.items():
            if value is not None:
                setattr(curso, field, value)
        self.db.commit()
        self.db.refresh(curso)
        return curso

    def delete(self, curso: Curso) -> None:
        self.db.delete(curso)
        self.db.commit()
