from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class ProfesorRecurso(Base):
    __tablename__ = "profesor_recursos"

    profesor_id = Column(Integer, ForeignKey("profesores.id"), primary_key=True)
    recurso_id = Column(Integer, ForeignKey("recursos.id"), primary_key=True)
    prioridad = Column(Integer, nullable=False)

    profesor = relationship("Profesor", back_populates="preferencias")
    recurso = relationship("Recurso")
