from typing import List
from sqlalchemy.orm import Session

from app.models.profesor import Profesor
from app.schemas.profesor import ProfesorCreate, ProfesorUpdate


class ProfesorService:
    """Servicio de lógica de negocio de Profesor."""

    def __init__(self, db: Session):
        self.db = db

    def listar_profesores(self, skip: int = 0, limit: int = 100) -> List[Profesor]:
        from app.repositories.profesor_repository import ProfesorRepository
        repo = ProfesorRepository(self.db)
        return repo.get_all(skip=skip, limit=limit)

    def obtener_profesor(self, profesor_id: int) -> Profesor | None:
        from app.repositories.profesor_repository import ProfesorRepository
        repo = ProfesorRepository(self.db)
        return repo.get_by_id(profesor_id)

    def crear_profesor(self, profesor_data: ProfesorCreate) -> Profesor:
        from app.repositories.profesor_repository import ProfesorRepository
        repo = ProfesorRepository(self.db)
        if profesor_data.correo:
            existente = repo.get_by_correo(profesor_data.correo)
            if existente:
                raise ValueError(f"Ya existe un profesor con el correo '{profesor_data.correo}'")
        return repo.create(profesor_data.dict())

    def actualizar_profesor(self, profesor_id: int, profesor_data: ProfesorUpdate) -> Profesor:
        from app.repositories.profesor_repository import ProfesorRepository
        repo = ProfesorRepository(self.db)
        profesor = repo.get_by_id(profesor_id)
        if not profesor:
            raise ValueError(f"Profesor con ID {profesor_id} no encontrado")
        if profesor_data.correo and profesor_data.correo != profesor.correo:
            existente = repo.get_by_correo(profesor_data.correo)
            if existente:
                raise ValueError(f"Ya existe un profesor con el correo '{profesor_data.correo}'")
        return repo.update(profesor, profesor_data.dict(exclude_unset=True))

    def eliminar_profesor(self, profesor_id: int) -> None:
        from app.repositories.profesor_repository import ProfesorRepository
        repo = ProfesorRepository(self.db)
        profesor = repo.get_by_id(profesor_id)
        if not profesor:
            raise ValueError(f"Profesor con ID {profesor_id} no encontrado")
        repo.delete(profesor)
