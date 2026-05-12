from typing import List
from sqlalchemy.orm import Session

from app.models.programa import Programa
from app.schemas.programa import ProgramaCreate, ProgramaUpdate


class ProgramaService:
    """Servicio de lógica de negocio de Programa."""

    def __init__(self, db: Session):
        self.db = db

    def listar_programas(self, skip: int = 0, limit: int = 100) -> List[Programa]:
        from app.repositories.programa_repository import ProgramaRepository
        repo = ProgramaRepository(self.db)
        return repo.get_all(skip=skip, limit=limit)

    def obtener_programa(self, programa_id: int) -> Programa | None:
        from app.repositories.programa_repository import ProgramaRepository
        repo = ProgramaRepository(self.db)
        return repo.get_by_id(programa_id)

    def crear_programa(self, programa_data: ProgramaCreate) -> Programa:
        from app.repositories.programa_repository import ProgramaRepository
        repo = ProgramaRepository(self.db)
        existente = repo.get_by_nombre(programa_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un programa con el nombre '{programa_data.nombre}'")
        return repo.create(programa_data.dict())

    def actualizar_programa(self, programa_id: int, programa_data: ProgramaUpdate) -> Programa:
        from app.repositories.programa_repository import ProgramaRepository
        repo = ProgramaRepository(self.db)
        programa = repo.get_by_id(programa_id)
        if not programa:
            raise ValueError(f"Programa con ID {programa_id} no encontrado")
        if programa_data.nombre and programa_data.nombre != programa.nombre:
            existente = repo.get_by_nombre(programa_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un programa con el nombre '{programa_data.nombre}'")
        return repo.update(programa, programa_data.dict(exclude_unset=True))

    def eliminar_programa(self, programa_id: int) -> None:
        from app.repositories.programa_repository import ProgramaRepository
        repo = ProgramaRepository(self.db)
        programa = repo.get_by_id(programa_id)
        if not programa:
            raise ValueError(f"Programa con ID {programa_id} no encontrado")
        repo.delete(programa)
