from sqlalchemy import Column, ForeignKey, Integer, Table

from app.core.database import Base

profesor_cursos = Table(
    "profesor_cursos",
    Base.metadata,
    Column("profesor_id", Integer, ForeignKey("profesores.id"), primary_key=True),
    Column("curso_id", Integer, ForeignKey("cursos.id"), primary_key=True),
)
