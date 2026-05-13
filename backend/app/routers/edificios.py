from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.routers.auth import get_current_user
from app.schemas.edificio import EdificioCreate, EdificioUpdate, EdificioResponse
from app.services.edificio_service import EdificioService

router = APIRouter(prefix="/edificios", tags=["edificios"])


@router.get("/", response_model=list[EdificioResponse])
async def listar_edificios(skip: int = 0, limit: int = 100, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = EdificioService(db)
    return await service.listar_edificios(skip=skip, limit=limit)


@router.get("/{edificio_id}", response_model=EdificioResponse)
async def obtener_edificio(edificio_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    service = EdificioService(db)
    edificio = await service.obtener_edificio(edificio_id)
    if not edificio:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Edificio con ID {edificio_id} no encontrado")
    return edificio


@router.post("/", response_model=EdificioResponse, status_code=status.HTTP_201_CREATED)
async def crear_edificio(edificio_data: EdificioCreate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = EdificioService(db)
        return await service.crear_edificio(edificio_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch("/{edificio_id}", response_model=EdificioResponse)
async def actualizar_edificio(edificio_id: int, edificio_data: EdificioUpdate, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = EdificioService(db)
        return await service.actualizar_edificio(edificio_id, edificio_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete("/{edificio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def eliminar_edificio(edificio_id: int, current_user: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    try:
        service = EdificioService(db)
        await service.eliminar_edificio(edificio_id)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
