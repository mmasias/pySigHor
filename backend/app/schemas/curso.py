from pydantic import BaseModel, Field
from typing import Optional


class CursoBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None
    creditos: Optional[int] = Field(None, ge=0)
    horas: Optional[int] = Field(None, ge=0)
    id_programa: Optional[int] = None


class CursoCreate(CursoBase):
    pass


class CursoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = None
    creditos: Optional[int] = Field(None, ge=0)
    horas: Optional[int] = Field(None, ge=0)
    id_programa: Optional[int] = None


class CursoResponse(CursoBase):
    id: int

    class Config:
        orm_mode = True
