from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.curso import CursoCreate, CursoUpdate, CursoResponse
from app.services.curso_service import CursoService

router = APIRouter(prefix="/cursos", tags=["cursos"])


@router.get("/", response_model=list[CursoResponse])
def listar_cursos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    service = CursoService(db)
    return service.listar_cursos(skip=skip, limit=limit)


@router.get("/{curso_id}", response_model=CursoResponse)
def obtener_curso(curso_id: int, db: Session = Depends(get_db)):
    service = CursoService(db)
    curso = service.obtener_curso(curso_id)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Curso con ID {curso_id} no encontrado")
    return curso


@router.post("/", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def crear_curso(curso_data: CursoCreate, db: Session = Depends(get_db)):
    try:
        service = CursoService(db)
        return service.crear_curso(curso_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{curso_id}", response_model=CursoResponse)
def actualizar_curso(curso_id: int, curso_data: CursoUpdate, db: Session = Depends(get_db)):
    try:
        service = CursoService(db)
        return service.actualizar_curso(curso_id, curso_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_curso(curso_id: int, db: Session = Depends(get_db)):
    try:
        service = CursoService(db)
        service.eliminar_curso(curso_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
