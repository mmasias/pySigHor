from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class ProfesorBase(BaseModel):
    nombres: str = Field(..., min_length=1, max_length=100)
    apellidos: str = Field(..., min_length=1, max_length=100)
    correo: Optional[str] = Field(None, max_length=150)
    telefono: Optional[str] = Field(None, max_length=20)
    observaciones: Optional[str] = None


class ProfesorCreate(ProfesorBase):
    pass


class ProfesorUpdate(BaseModel):
    nombres: Optional[str] = Field(None, min_length=1, max_length=100)
    apellidos: Optional[str] = Field(None, min_length=1, max_length=100)
    correo: Optional[str] = Field(None, max_length=150)
    telefono: Optional[str] = Field(None, max_length=20)
    observaciones: Optional[str] = None


class ProfesorResponse(ProfesorBase):
    id: int

    class Config:
        orm_mode = True
