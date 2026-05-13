from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Aula(Base):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True, index=True)
    capacidad = Column(Integer, nullable=False)
    especial = Column(Boolean, default=False)
    bloqueada = Column(Boolean, default=False)
    id_edificio = Column(Integer, ForeignKey("edificios.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    edificio = relationship("Edificio", back_populates="aulas")
