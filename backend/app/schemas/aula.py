from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

from app.schemas.recurso import RecursoBase, RecursoResponse


class AulaBase(BaseModel):

    codigo: str = Field(..., min_length=1, max_length=20)
    nombre: str = Field(..., min_length=1, max_length=50)


class AulaCreate(AulaBase):

    id_edificio: Optional[int] = None


class AulaUpdate(BaseModel):

    codigo: Optional[str] = Field(None, min_length=1, max_length=20)
    nombre: Optional[str] = Field(None, min_length=1, max_length=50)
    capacidad: Optional[int] = Field(None, ge=0, le=255)
    tipo: Optional[str] = Field(None, max_length=50)
    observaciones: Optional[str] = None
    especial: Optional[bool] = None
    bloqueada: Optional[bool] = None
    id_edificio: Optional[int] = None
    ids_recursos: Optional[list[int]] = None


class AulaResponse(AulaBase):

    id: int
    capacidad: int
    tipo: Optional[str] = None
    observaciones: Optional[str] = None
    especial: bool = False
    bloqueada: bool = False
    id_edificio: Optional[int] = None
    recursos: list[RecursoResponse] = []

    model_config = ConfigDict(from_attributes=True)
