from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.routers.auth import get_current_user
from app.schemas.curso import CursoCreate, CursoUpdate, CursoResponse
from app.services.curso_service import CursoService

router = APIRouter(prefix="/cursos", tags=["cursos"])


@router.get("/", response_model=list[CursoResponse])
async def listar_cursos(skip: int = 0, limit: int = 100, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = CursoService(db)
    return await service.listar_cursos(skip=skip, limit=limit)


@router.get("/{curso_id}", response_model=CursoResponse)
async def obtener_curso(curso_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = CursoService(db)
    curso = await service.obtener_curso(curso_id)
    if not curso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Curso con ID {curso_id} no encontrado")
    return curso


@router.post("/", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
async def crear_curso(curso_data: CursoCreate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = CursoService(db)
        return await service.crear_curso(curso_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{curso_id}", response_model=CursoResponse)
async def actualizar_curso(curso_id: int, curso_data: CursoUpdate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = CursoService(db)
        return await service.actualizar_curso(curso_id, curso_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_curso(curso_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = CursoService(db)
        await service.eliminar_curso(curso_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
