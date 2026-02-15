from sqlalchemy import create_engine
from app.core.database import Base
from app.models import Aula, Edificio
from app.core.config import settings

# Crear engine temporal
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

# Crear tablas
Base.metadata.create_all(bind=engine)

print("✅ Base de datos creada exitosamente")
print(f"✅ Tablas creadas: {Base.metadata.tables.keys()}")
