from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.routers.auth import get_current_user
from app.schemas.profesor import ProfesorCreate, ProfesorUpdate, ProfesorResponse
from app.schemas.preferencia import PreferenciaResponse, PreferenciaUpdate
from app.services.preferencia_service import PreferenciaService
from app.services.profesor_service import ProfesorService

router = APIRouter(prefix="/profesores", tags=["profesores"])


@router.get("", response_model=list[ProfesorResponse])
async def listar_profesores(skip: int = 0, limit: int = 100, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = ProfesorService(db)
    return await service.listar_profesores(skip=skip, limit=limit)


@router.get("/{profesor_id}", response_model=ProfesorResponse)
async def obtener_profesor(profesor_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = ProfesorService(db)
    profesor = await service.obtener_profesor(profesor_id)
    if not profesor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Profesor con ID {profesor_id} no encontrado")
    return profesor


@router.post("", response_model=ProfesorResponse, status_code=status.HTTP_201_CREATED)
async def crear_profesor(profesor_data: ProfesorCreate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = ProfesorService(db)
        return await service.crear_profesor(profesor_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{profesor_id}", response_model=ProfesorResponse)
async def actualizar_profesor(profesor_id: int, profesor_data: ProfesorUpdate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = ProfesorService(db)
        return await service.actualizar_profesor(profesor_id, profesor_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{profesor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_profesor(profesor_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = ProfesorService(db)
        await service.eliminar_profesor(profesor_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{profesor_id}/preferencias", response_model=list[PreferenciaResponse])
async def obtener_preferencias(profesor_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = PreferenciaService(db)
        return await service.obtener_preferencias(profesor_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.put("/{profesor_id}/preferencias", response_model=list[PreferenciaResponse])
async def actualizar_preferencias(profesor_id: int, data: PreferenciaUpdate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = PreferenciaService(db)
        return await service.actualizar_preferencias(profesor_id, data.recurso_ids)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
