from sqlalchemy import Column, Integer, String, Boolean

from app.core.database import Base


class Usuario(Base):
    """Modelo de Usuario."""

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True, index=True)
    hashed_password = Column(String(100), nullable=False)
    activo = Column(Boolean, default=True)
