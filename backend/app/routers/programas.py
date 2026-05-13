from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.routers.auth import get_current_user
from app.schemas.programa import ProgramaCreate, ProgramaUpdate, ProgramaResponse
from app.services.programa_service import ProgramaService

router = APIRouter(prefix="/programas", tags=["programas"])


@router.get("/", response_model=list[ProgramaResponse])
async def listar_programas(skip: int = 0, limit: int = 100, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = ProgramaService(db)
    return await service.listar_programas(skip=skip, limit=limit)


@router.get("/{programa_id}", response_model=ProgramaResponse)
async def obtener_programa(programa_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = ProgramaService(db)
    programa = await service.obtener_programa(programa_id)
    if not programa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Programa con ID {programa_id} no encontrado")
    return programa


@router.post("/", response_model=ProgramaResponse, status_code=status.HTTP_201_CREATED)
async def crear_programa(programa_data: ProgramaCreate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = ProgramaService(db)
        return await service.crear_programa(programa_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{programa_id}", response_model=ProgramaResponse)
async def actualizar_programa(programa_id: int, programa_data: ProgramaUpdate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = ProgramaService(db)
        return await service.actualizar_programa(programa_id, programa_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{programa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_programa(programa_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = ProgramaService(db)
        await service.eliminar_programa(programa_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
