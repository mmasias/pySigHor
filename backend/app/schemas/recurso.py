from pydantic import BaseModel, Field
from typing import Optional


class RecursoBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None


class RecursoCreate(RecursoBase):
    pass


class RecursoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    descripcion: Optional[str] = None


class RecursoResponse(RecursoBase):
    id: int

    class Config:
        orm_mode = True
