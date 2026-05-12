from typing import List
from sqlalchemy.orm import Session

from app.models.curso import Curso
from app.schemas.curso import CursoCreate, CursoUpdate


class CursoService:
    """Servicio de lógica de negocio de Curso."""

    def __init__(self, db: Session):
        self.db = db

    def listar_cursos(self, skip: int = 0, limit: int = 100) -> List[Curso]:
        from app.repositories.curso_repository import CursoRepository
        repo = CursoRepository(self.db)
        return repo.get_all(skip=skip, limit=limit)

    def obtener_curso(self, curso_id: int) -> Curso | None:
        from app.repositories.curso_repository import CursoRepository
        repo = CursoRepository(self.db)
        return repo.get_by_id(curso_id)

    def crear_curso(self, curso_data: CursoCreate) -> Curso:
        from app.repositories.curso_repository import CursoRepository
        repo = CursoRepository(self.db)
        existente = repo.get_by_nombre(curso_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un curso con el nombre '{curso_data.nombre}'")
        return repo.create(curso_data.dict())

    def actualizar_curso(self, curso_id: int, curso_data: CursoUpdate) -> Curso:
        from app.repositories.curso_repository import CursoRepository
        repo = CursoRepository(self.db)
        curso = repo.get_by_id(curso_id)
        if not curso:
            raise ValueError(f"Curso con ID {curso_id} no encontrado")
        if curso_data.nombre and curso_data.nombre != curso.nombre:
            existente = repo.get_by_nombre(curso_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un curso con el nombre '{curso_data.nombre}'")
        return repo.update(curso, curso_data.dict(exclude_unset=True))

    def eliminar_curso(self, curso_id: int) -> None:
        from app.repositories.curso_repository import CursoRepository
        repo = CursoRepository(self.db)
        curso = repo.get_by_id(curso_id)
        if not curso:
            raise ValueError(f"Curso con ID {curso_id} no encontrado")
        repo.delete(curso)
