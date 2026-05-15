from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

from app.schemas.recurso import RecursoBase


class AulaBase(BaseModel):

    nombre: str = Field(..., min_length=1, max_length=50)
    capacidad: int = Field(..., ge=0, le=255)
    especial: bool = False
    bloqueada: bool = False
    id_edificio: Optional[int] = None


class AulaCreate(AulaBase):
    pass


class AulaUpdate(BaseModel):

    nombre: Optional[str] = Field(None, min_length=1, max_length=50)
    capacidad: Optional[int] = Field(None, ge=0, le=255)
    especial: Optional[bool] = None
    bloqueada: Optional[bool] = None
    id_edificio: Optional[int] = None
    ids_recursos: Optional[list[int]] = None


class AulaResponse(AulaBase):

    id: int
    recursos: list[RecursoBase] = []

    model_config = ConfigDict(from_attributes=True)
