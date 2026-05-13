from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


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


class AulaResponse(AulaBase):

    id: int

    model_config = ConfigDict(from_attributes=True)
