from typing import List
from sqlalchemy.orm import Session

from app.models.recurso import Recurso
from app.schemas.recurso import RecursoCreate, RecursoUpdate


class RecursoService:
    """Servicio de lógica de negocio de Recurso."""

    def __init__(self, db: Session):
        self.db = db

    def listar_recursos(self, skip: int = 0, limit: int = 100) -> List[Recurso]:
        from app.repositories.recurso_repository import RecursoRepository
        repo = RecursoRepository(self.db)
        return repo.get_all(skip=skip, limit=limit)

    def obtener_recurso(self, recurso_id: int) -> Recurso | None:
        from app.repositories.recurso_repository import RecursoRepository
        repo = RecursoRepository(self.db)
        return repo.get_by_id(recurso_id)

    def crear_recurso(self, recurso_data: RecursoCreate) -> Recurso:
        from app.repositories.recurso_repository import RecursoRepository
        repo = RecursoRepository(self.db)
        existente = repo.get_by_nombre(recurso_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un recurso con el nombre '{recurso_data.nombre}'")
        return repo.create(recurso_data.dict())

    def actualizar_recurso(self, recurso_id: int, recurso_data: RecursoUpdate) -> Recurso:
        from app.repositories.recurso_repository import RecursoRepository
        repo = RecursoRepository(self.db)
        recurso = repo.get_by_id(recurso_id)
        if not recurso:
            raise ValueError(f"Recurso con ID {recurso_id} no encontrado")
        if recurso_data.nombre and recurso_data.nombre != recurso.nombre:
            existente = repo.get_by_nombre(recurso_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un recurso con el nombre '{recurso_data.nombre}'")
        return repo.update(recurso, recurso_data.dict(exclude_unset=True))

    def eliminar_recurso(self, recurso_id: int) -> None:
        from app.repositories.recurso_repository import RecursoRepository
        repo = RecursoRepository(self.db)
        recurso = repo.get_by_id(recurso_id)
        if not recurso:
            raise ValueError(f"Recurso con ID {recurso_id} no encontrado")
        repo.delete(recurso)
