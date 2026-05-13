from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.routers.auth import get_current_user
from app.schemas.recurso import RecursoCreate, RecursoUpdate, RecursoResponse
from app.services.recurso_service import RecursoService

router = APIRouter(prefix="/recursos", tags=["recursos"])


@router.get("/", response_model=list[RecursoResponse])
async def listar_recursos(skip: int = 0, limit: int = 100, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = RecursoService(db)
    return await service.listar_recursos(skip=skip, limit=limit)


@router.get("/{recurso_id}", response_model=RecursoResponse)
async def obtener_recurso(recurso_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = RecursoService(db)
    recurso = await service.obtener_recurso(recurso_id)
    if not recurso:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Recurso con ID {recurso_id} no encontrado")
    return recurso


@router.post("/", response_model=RecursoResponse, status_code=status.HTTP_201_CREATED)
async def crear_recurso(recurso_data: RecursoCreate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = RecursoService(db)
        return await service.crear_recurso(recurso_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{recurso_id}", response_model=RecursoResponse)
async def actualizar_recurso(recurso_id: int, recurso_data: RecursoUpdate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = RecursoService(db)
        return await service.actualizar_recurso(recurso_id, recurso_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{recurso_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_recurso(recurso_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = RecursoService(db)
        await service.eliminar_recurso(recurso_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
