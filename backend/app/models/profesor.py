from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base
from app.models.profesor_curso import profesor_cursos


class Profesor(Base):
    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=True, unique=True)
    telefono = Column(String(20), nullable=True)
    observaciones = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    preferencias = relationship(
        "ProfesorRecurso",
        back_populates="profesor",
        order_by="ProfesorRecurso.prioridad",
        lazy="selectin",
    )

    cursos_asignados = relationship("Curso", secondary=profesor_cursos, lazy="selectin")
