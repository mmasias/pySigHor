from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.profesor import ProfesorCreate, ProfesorUpdate, ProfesorResponse
from app.services.profesor_service import ProfesorService

router = APIRouter(prefix="/profesores", tags=["profesores"])


@router.get("/", response_model=list[ProfesorResponse])
def listar_profesores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = ProfesorService(db)
    return service.listar_profesores(skip=skip, limit=limit)


@router.get("/{profesor_id}", response_model=ProfesorResponse)
def obtener_profesor(profesor_id: int, db: Session = Depends(get_db)):
    service = ProfesorService(db)
    profesor = service.obtener_profesor(profesor_id)
    if not profesor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Profesor con ID {profesor_id} no encontrado")
    return profesor


@router.post("/", response_model=ProfesorResponse, status_code=status.HTTP_201_CREATED)
def crear_profesor(profesor_data: ProfesorCreate, db: Session = Depends(get_db)):
    try:
        service = ProfesorService(db)
        return service.crear_profesor(profesor_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{profesor_id}", response_model=ProfesorResponse)
def actualizar_profesor(profesor_id: int, profesor_data: ProfesorUpdate, db: Session = Depends(get_db)):
    try:
        service = ProfesorService(db)
        return service.actualizar_profesor(profesor_id, profesor_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{profesor_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_profesor(profesor_id: int, db: Session = Depends(get_db)):
    try:
        service = ProfesorService(db)
        service.eliminar_profesor(profesor_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
