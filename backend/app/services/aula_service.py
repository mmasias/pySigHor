from typing import List
from sqlalchemy.orm import Session

from app.models.aula import Aula
from app.schemas.aula import AulaCreate, AulaUpdate


class AulaService:
    """Servicio de lógica de negocio de Aula."""

    def __init__(self, db: Session):
        self.db = db

    def listar_aulas(self, skip: int = 0, limit: int = 100) -> List[Aula]:
        """Listar todas las aulas con paginación."""
        from app.repositories.aula_repository import AulaRepository
        repo = AulaRepository(self.db)
        return repo.get_all(skip=skip, limit=limit)

    def obtener_aula(self, aula_id: int) -> Aula | None:
        """Obtener aula por ID."""
        from app.repositories.aula_repository import AulaRepository
        repo = AulaRepository(self.db)
        return repo.get_by_id(aula_id)

    def crear_aula(self, aula_data: AulaCreate) -> Aula:
        """Crear nueva aula con validaciones."""
        from app.repositories.aula_repository import AulaRepository
        repo = AulaRepository(self.db)

        # Validar que no exista aula con mismo nombre
        existente = repo.get_by_nombre(aula_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un aula con el nombre '{aula_data.nombre}'")

        return repo.create(aula_data.dict())

    def actualizar_aula(self, aula_id: int, aula_data: AulaUpdate) -> Aula:
        """Actualizar aula existente."""
        from app.repositories.aula_repository import AulaRepository
        repo = AulaRepository(self.db)

        aula = repo.get_by_id(aula_id)
        if not aula:
            raise ValueError(f"Aula con ID {aula_id} no encontrada")

        # Si se actualiza el nombre, verificar que no exista
        if aula_data.nombre and aula_data.nombre != aula.nombre:
            existente = repo.get_by_nombre(aula_data.nombre)
            if existente:
                raise ValueError(f"Ya existe un aula con el nombre '{aula_data.nombre}'")

        return repo.update(aula, aula_data.dict(exclude_unset=True))

    def eliminar_aula(self, aula_id: int) -> None:
        """Eliminar aula existente."""
        from app.repositories.aula_repository import AulaRepository
        repo = AulaRepository(self.db)

        aula = repo.get_by_id(aula_id)
        if not aula:
            raise ValueError(f"Aula con ID {aula_id} no encontrada")

        repo.delete(aula)
