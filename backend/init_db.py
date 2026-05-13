import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.core.database import Base, engine
from app.models import Aula, Curso, Edificio, Programa, Profesor, Recurso, Usuario
from app.core.security import get_password_hash


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as db:
        from sqlalchemy import select

        result = await db.execute(select(Usuario).where(Usuario.username == "admin"))
        admin = result.scalar_one_or_none()
        if not admin:
            db.add(
                Usuario(
                    username="admin",
                    hashed_password=get_password_hash("admin"),
                    activo=True,
                )
            )
            await db.commit()
            print("Usuario admin creado")
        else:
            print("Usuario admin ya existe")

    print(f"Base de datos creada exitosamente")
    print(f"Tablas creadas: {list(Base.metadata.tables.keys())}")


if __name__ == "__main__":
    asyncio.run(init_db())
