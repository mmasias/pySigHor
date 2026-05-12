from sqlalchemy import Column, Integer, String, Text

from app.core.database import Base


class Recurso(Base):
    """Modelo de Recurso (proyector, laboratorio, etc.)."""

    __tablename__ = "recursos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)
