from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Edificio(Base):
    """Modelo de Edificio."""

    __tablename__ = "edificios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True)
    direccion = Column(String(100), nullable=True)

    # Relación con aulas
    aulas = relationship("Aula", back_populates="edificio")
