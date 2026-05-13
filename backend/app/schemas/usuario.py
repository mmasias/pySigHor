from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class UsuarioBase(BaseModel):

    username: str = Field(..., min_length=1, max_length=50)


class UsuarioCreate(UsuarioBase):

    password: str = Field(..., min_length=1)


class UsuarioResponse(UsuarioBase):

    id: int
    activo: bool
    rol: str

    model_config = ConfigDict(from_attributes=True)
