from pydantic import BaseModel, Field
from typing import Optional


class ProgramaBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None
    activo: bool = True


class ProgramaCreate(ProgramaBase):
    pass


class ProgramaUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = None
    activo: Optional[bool] = None


class ProgramaResponse(ProgramaBase):
    id: int

    class Config:
        orm_mode = True
