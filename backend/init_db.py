from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.database import Base
from app.models import Aula, Edificio, Usuario, Programa, Curso, Profesor, Recurso
from app.core.config import settings
from app.core.security import get_password_hash

# Crear engine temporal
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

# Crear tablas
Base.metadata.create_all(bind=engine)

# Seed: usuario admin (idempotente)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()
try:
    admin = db.query(Usuario).filter(Usuario.username == "admin").first()
    if not admin:
        db.add(Usuario(
            username="admin",
            hashed_password=get_password_hash("admin"),
            activo=True,
        ))
        db.commit()
        print("✅ Usuario admin creado")
    else:
        print("ℹ️  Usuario admin ya existe")
finally:
    db.close()

print("✅ Base de datos creada exitosamente")
print(f"✅ Tablas creadas: {list(Base.metadata.tables.keys())}")
