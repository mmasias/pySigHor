from pydantic import BaseModel, Field
from typing import Optional


class AulaBase(BaseModel):
    """Schema base de Aula."""

    nombre: str = Field(..., min_length=1, max_length=50)
    capacidad: int = Field(..., ge=0, le=255)
    especial: bool = False
    bloqueada: bool = False
    id_edificio: Optional[int] = None


class AulaCreate(AulaBase):
    """Schema para crear Aula."""
    pass


class AulaUpdate(BaseModel):
    """Schema para actualizar Aula (campos opcionales)."""

    nombre: Optional[str] = Field(None, min_length=1, max_length=50)
    capacidad: Optional[int] = Field(None, ge=0, le=255)
    especial: Optional[bool] = None
    bloqueada: Optional[bool] = None
    id_edificio: Optional[int] = None


class AulaResponse(AulaBase):
    """Schema para respuesta de Aula."""

    id: int

    class Config:
        orm_mode = True
