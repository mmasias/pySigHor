from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Text, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base

aula_recursos = Table(
    "aula_recursos",
    Base.metadata,
    Column("aula_id", Integer, ForeignKey("aulas.id"), primary_key=True),
    Column("recurso_id", Integer, ForeignKey("recursos.id"), primary_key=True),
)


class Aula(Base):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20), nullable=False, unique=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True, index=True)
    capacidad = Column(Integer, nullable=False, default=0)
    tipo = Column(String(50), nullable=True)
    observaciones = Column(Text, nullable=True)
    especial = Column(Boolean, default=False)
    bloqueada = Column(Boolean, default=False)
    id_edificio = Column(Integer, ForeignKey("edificios.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    edificio = relationship("Edificio", back_populates="aulas")
    recursos = relationship("Recurso", secondary=aula_recursos, lazy="selectin")
