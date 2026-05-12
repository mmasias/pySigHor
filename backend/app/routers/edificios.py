from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.edificio import EdificioCreate, EdificioUpdate, EdificioResponse
from app.services.edificio_service import EdificioService

router = APIRouter(prefix="/edificios", tags=["edificios"])


@router.get("/", response_model=list[EdificioResponse])
def listar_edificios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = EdificioService(db)
    return service.listar_edificios(skip=skip, limit=limit)


@router.get("/{edificio_id}", response_model=EdificioResponse)
def obtener_edificio(edificio_id: int, db: Session = Depends(get_db)):
    service = EdificioService(db)
    edificio = service.obtener_edificio(edificio_id)
    if not edificio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Edificio con ID {edificio_id} no encontrado")
    return edificio


@router.post("/", response_model=EdificioResponse, status_code=status.HTTP_201_CREATED)
def crear_edificio(edificio_data: EdificioCreate, db: Session = Depends(get_db)):
    try:
        service = EdificioService(db)
        return service.crear_edificio(edificio_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{edificio_id}", response_model=EdificioResponse)
def actualizar_edificio(edificio_id: int, edificio_data: EdificioUpdate, db: Session = Depends(get_db)):
    try:
        service = EdificioService(db)
        return service.actualizar_edificio(edificio_id, edificio_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{edificio_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_edificio(edificio_id: int, db: Session = Depends(get_db)):
    try:
        service = EdificioService(db)
        service.eliminar_edificio(edificio_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
