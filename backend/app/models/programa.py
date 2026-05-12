from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class Programa(Base):
    """Modelo de Programa académico."""

    __tablename__ = "programas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)
    activo = Column(Boolean, default=True)

    cursos = relationship("Curso", back_populates="programa")
