from sqlalchemy import Column, Integer, String, Text

from app.core.database import Base


class Profesor(Base):
    """Modelo de Profesor."""

    __tablename__ = "profesores"

    id = Column(Integer, primary_key=True, index=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150), nullable=True, unique=True)
    telefono = Column(String(20), nullable=True)
    observaciones = Column(Text, nullable=True)
