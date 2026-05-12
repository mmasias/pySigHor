from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Curso(Base):
    """Modelo de Curso académico."""

    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)
    creditos = Column(Integer, nullable=True)
    horas = Column(Integer, nullable=True)
    id_programa = Column(Integer, ForeignKey("programas.id"), nullable=True)

    programa = relationship("Programa", back_populates="cursos")
