"""${message}

Revision ID: 001
Revises:
Create Date: 2026-05-13
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=50), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("rol", sa.String(length=20), server_default="admin"),
        sa.Column("activo", sa.Boolean(), server_default="1"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_usuarios_username"), "usuarios", ["username"], unique=True)
    op.create_index(op.f("ix_usuarios_id"), "usuarios", ["id"], unique=False)

    op.create_table(
        "edificios",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=50), nullable=False),
        sa.Column("direccion", sa.String(length=100), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_edificios_id"), "edificios", ["id"], unique=False)
    op.create_unique_constraint("uq_edificios_nombre", "edificios", ["nombre"])

    op.create_table(
        "programas",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=100), nullable=False),
        sa.Column("descripcion", sa.Text(), nullable=True),
        sa.Column("activo", sa.Boolean(), server_default="1"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_programas_id"), "programas", ["id"], unique=False)
    op.create_unique_constraint("uq_programas_nombre", "programas", ["nombre"])

    op.create_table(
        "aulas",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=50), nullable=False),
        sa.Column("capacidad", sa.Integer(), nullable=False),
        sa.Column("especial", sa.Boolean(), server_default="0"),
        sa.Column("bloqueada", sa.Boolean(), server_default="0"),
        sa.Column("id_edificio", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["id_edificio"], ["edificios.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_aulas_id"), "aulas", ["id"], unique=False)
    op.create_index(op.f("ix_aulas_nombre"), "aulas", ["nombre"], unique=True)

    op.create_table(
        "cursos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=100), nullable=False),
        sa.Column("descripcion", sa.Text(), nullable=True),
        sa.Column("creditos", sa.Integer(), nullable=True),
        sa.Column("horas", sa.Integer(), nullable=True),
        sa.Column("id_programa", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["id_programa"], ["programas.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_cursos_id"), "cursos", ["id"], unique=False)
    op.create_unique_constraint("uq_cursos_nombre", "cursos", ["nombre"])

    op.create_table(
        "profesores",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombres", sa.String(length=100), nullable=False),
        sa.Column("apellidos", sa.String(length=100), nullable=False),
        sa.Column("correo", sa.String(length=150), nullable=True),
        sa.Column("telefono", sa.String(length=20), nullable=True),
        sa.Column("observaciones", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_profesores_id"), "profesores", ["id"], unique=False)
    op.create_unique_constraint("uq_profesores_correo", "profesores", ["correo"])

    op.create_table(
        "recursos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nombre", sa.String(length=100), nullable=False),
        sa.Column("descripcion", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_recursos_id"), "recursos", ["id"], unique=False)
    op.create_unique_constraint("uq_recursos_nombre", "recursos", ["nombre"])


def downgrade() -> None:
    op.drop_table("recursos")
    op.drop_table("profesores")
    op.drop_table("cursos")
    op.drop_table("aulas")
    op.drop_table("programas")
    op.drop_table("edificios")
    op.drop_table("usuarios")
