from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.programa import ProgramaCreate, ProgramaUpdate, ProgramaResponse
from app.services.programa_service import ProgramaService

router = APIRouter(prefix="/programas", tags=["programas"])


@router.get("/", response_model=list[ProgramaResponse])
def listar_programas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = ProgramaService(db)
    return service.listar_programas(skip=skip, limit=limit)


@router.get("/{programa_id}", response_model=ProgramaResponse)
def obtener_programa(programa_id: int, db: Session = Depends(get_db)):
    service = ProgramaService(db)
    programa = service.obtener_programa(programa_id)
    if not programa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Programa con ID {programa_id} no encontrado")
    return programa


@router.post("/", response_model=ProgramaResponse, status_code=status.HTTP_201_CREATED)
def crear_programa(programa_data: ProgramaCreate, db: Session = Depends(get_db)):
    try:
        service = ProgramaService(db)
        return service.crear_programa(programa_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{programa_id}", response_model=ProgramaResponse)
def actualizar_programa(programa_id: int, programa_data: ProgramaUpdate, db: Session = Depends(get_db)):
    try:
        service = ProgramaService(db)
        return service.actualizar_programa(programa_id, programa_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{programa_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_programa(programa_id: int, db: Session = Depends(get_db)):
    try:
        service = ProgramaService(db)
        service.eliminar_programa(programa_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
