from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.recurso import RecursoCreate, RecursoUpdate, RecursoResponse
from app.services.recurso_service import RecursoService

router = APIRouter(prefix="/recursos", tags=["recursos"])


@router.get("/", response_model=list[RecursoResponse])
def listar_recursos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = RecursoService(db)
    return service.listar_recursos(skip=skip, limit=limit)


@router.get("/{recurso_id}", response_model=RecursoResponse)
def obtener_recurso(recurso_id: int, db: Session = Depends(get_db)):
    service = RecursoService(db)
    recurso = service.obtener_recurso(recurso_id)
    if not recurso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Recurso con ID {recurso_id} no encontrado")
    return recurso


@router.post("/", response_model=RecursoResponse, status_code=status.HTTP_201_CREATED)
def crear_recurso(recurso_data: RecursoCreate, db: Session = Depends(get_db)):
    try:
        service = RecursoService(db)
        return service.crear_recurso(recurso_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{recurso_id}", response_model=RecursoResponse)
def actualizar_recurso(recurso_id: int, recurso_data: RecursoUpdate, db: Session = Depends(get_db)):
    try:
        service = RecursoService(db)
        return service.actualizar_recurso(recurso_id, recurso_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{recurso_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_recurso(recurso_id: int, db: Session = Depends(get_db)):
    try:
        service = RecursoService(db)
        service.eliminar_recurso(recurso_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
