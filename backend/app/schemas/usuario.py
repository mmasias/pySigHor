from pydantic import BaseModel, Field


class UsuarioBase(BaseModel):
    """Schema base de Usuario."""

    username: str = Field(..., min_length=1, max_length=50)


class UsuarioCreate(UsuarioBase):
    """Schema para crear Usuario (con contraseña en plano)."""

    password: str = Field(..., min_length=1)


class UsuarioResponse(UsuarioBase):
    """Schema para respuesta de Usuario (sin hashed_password)."""

    id: int
    activo: bool

    class Config:
        orm_mode = True
