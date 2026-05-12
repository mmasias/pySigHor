from typing import List
from sqlalchemy.orm import Session

from app.models.edificio import Edificio
from app.schemas.edificio import EdificioCreate, EdificioUpdate


class EdificioService:
    """Servicio de lógica de negocio de Edificio."""

    def __init__(self, db: Session):
        self.db = db

    def listar_edificios(self, skip: int = 0, limit: int = 100) -> List[Edificio]:
        from app.repositories.edificio_repository import EdificioRepository
        repo = EdificioRepository(self.db)
        return repo.get_all(skip=skip, limit=limit)

    def obtener_edificio(self, edificio_id: int) -> Edificio | None:
        from app.repositories.edificio_repository import EdificioRepository
        repo = EdificioRepository(self.db)
        return repo.get_by_id(edificio_id)

    def crear_edificio(self, edificio_data: EdificioCreate) -> Edificio:
        from app.repositories.edificio_repository import EdificioRepository
        repo = EdificioRepository(self.db)
        existente = repo.get_by_nombre(edificio_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un edificio con el nombre '{edificio_data.nombre}'")
        return repo.create(edificio_data.dict())

    def actualizar_edificio(self, edificio_id: int, edificio_data: EdificioUpdate) -> Edificio:
        from app.repositories.edificio_repository import EdificioRepository
        repo = EdificioRepository(self.db)
        edificio = repo.get_by_id(edificio_id)
        if not edificio:
            raise ValueError(f"Edificio con ID {edificio_id} no encontrado")
        if edificio_data.nombre and edificio_data.nombre != edificio.nombre:
            existente = repo.get_by_nombre(edificio_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un edificio con el nombre '{edificio_data.nombre}'")
        return repo.update(edificio, edificio_data.dict(exclude_unset=True))

    def eliminar_edificio(self, edificio_id: int) -> None:
        from app.repositories.edificio_repository import EdificioRepository
        repo = EdificioRepository(self.db)
        edificio = repo.get_by_id(edificio_id)
        if not edificio:
            raise ValueError(f"Edificio con ID {edificio_id} no encontrado")
        repo.delete(edificio)
