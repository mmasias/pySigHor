from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class EdificioBase(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=50)
    direccion: Optional[str] = Field(None, max_length=100)


class EdificioCreate(EdificioBase):
    pass


class EdificioUpdate(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=50)
    direccion: Optional[str] = Field(None, max_length=100)


class EdificioResponse(EdificioBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
