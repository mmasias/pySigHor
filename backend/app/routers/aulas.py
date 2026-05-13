from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.routers.auth import get_current_user
from app.schemas.aula import AulaCreate, AulaUpdate, AulaResponse
from app.services.aula_service import AulaService

router = APIRouter(prefix="/aulas", tags=["aulas"])


@router.get("", response_model=list[AulaResponse])
async def listar_aulas(
    skip: int = 0,
    limit: int = 100,
    current_user: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Listar todas las aulas con paginación."""
    service = AulaService(db)
    aulas = await service.listar_aulas(skip=skip, limit=limit)
    return aulas


@router.get("/{aula_id}", response_model=AulaResponse)
async def obtener_aula(
    aula_id: int,
    current_user: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Obtener un aula por ID."""
    service = AulaService(db)
    aula = await service.obtener_aula(aula_id)
    if not aula:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aula con ID {aula_id} no encontrada",
        )
    return aula


@router.post("", response_model=AulaResponse, status_code=status.HTTP_201_CREATED)
async def crear_aula(
    aula_data: AulaCreate,
    current_user: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Crear nueva aula."""
    try:
        service = AulaService(db)
        aula = await service.crear_aula(aula_data)
        return aula
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.patch("/{aula_id}", response_model=AulaResponse)
async def actualizar_aula(
    aula_id: int,
    aula_data: AulaUpdate,
    current_user: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Actualizar aula existente (merge parcial)."""
    try:
        service = AulaService(db)
        aula = await service.actualizar_aula(aula_id, aula_data)
        return aula
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete("/{aula_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_aula(
    aula_id: int,
    current_user: str = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Eliminar aula existente."""
    try:
        service = AulaService(db)
        await service.eliminar_aula(aula_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )
