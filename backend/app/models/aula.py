from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Aula(Base):
    """Modelo de Aula."""

    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True, index=True)
    capacidad = Column(Integer, nullable=False)
    especial = Column(Boolean, default=False)
    bloqueada = Column(Boolean, default=False)
    id_edificio = Column(Integer, ForeignKey("edificios.id"), nullable=True)

    # Relación con edificio
    edificio = relationship("Edificio", back_populates="aulas")
