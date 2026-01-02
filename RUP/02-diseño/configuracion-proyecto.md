# Configuración del Proyecto - CLI Standalone

**Proyecto:** pySigHor - Modernización del Sistema Generador de Horarios
**Fase RUP:** Elaboración
**Artefacto:** Configuración del Proyecto (CLI Standalone)
**Autor:** Equipo de desarrollo
**Fecha:** 2026-01-02

## Introducción

Este documento detalla la configuración técnica necesaria para desarrollar e implementar la variante **CLI Standalone** del sistema pySigHor. Esta arquitectura implementa toda la lógica de negocio y acceso a datos dentro de la propia aplicación CLI, sin dependencias de servicios externos.

## Stack tecnológico

### Lenguaje base

- **Python 3.11+**: Lenguaje de programación principal.

### Frameworks y bibliotecas principales

- **Click 8.1+**: Framework para construcción de interfaces CLI.
- **SQLAlchemy 2.0+**: ORM para acceso a base de datos.
- **PyJWT 2.8+**: Generación y validación de tokens JWT.
- **Passlib 1.7+**: Hash seguro de contraseñas (bcrypt).
- **Rich 13.7+**: Formateo de salida en terminal (tablas ASCII).
- **Python-dotenv 1.0+**: Gestión de variables de entorno.

### Base de datos

- **SQLite 3**: Base de datos embebida local.

### Herramientas de desarrollo

- **Pytest 7.4+**: Framework de pruebas.
- **Black 23.12+**: Formateador de código.
- **Flake8 7.0+**: Linter de código.
- **MyPy 1.8+**: Verificador de tipos estáticos.
- **PyInstaller 6.3+**: Empaquetador de ejecutables.

## Estructura del proyecto

```text
pySigHor-cli-standalone/
├── cli/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── aulas.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── aula_service.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   ├── user_repository.py
│   │   └── aula_repository.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── aula.py
│   └── utils/
│       ├── __init__.py
│       ├── token_manager.py
│       ├── output_formatter.py
│       └── db.py
├── tests/
│   ├── __init__.py
│   ├── test_auth_service.py
│   ├── test_aula_service.py
│   ├── test_user_repository.py
│   └── test_aula_repository.py
├── scripts/
│   ├── init_db.sql
│   └── build.sh
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── pytest.ini
├── .env.example
└── README.md
```

## Configuración de dependencias

### requirements.txt

```txt
click==8.1.7
SQLAlchemy==2.0.25
PyJWT==2.8.0
passlib[bcrypt]==1.7.4
rich==13.7.0
python-dotenv==1.0.0
```

### requirements-dev.txt

```txt
-r requirements.txt
pytest==7.4.4
pytest-cov==4.1.0
black==23.12.1
flake8==7.0.0
mypy==1.8.0
PyInstaller==6.3.0
```

## Configuración de la aplicación

### cli/config.py

```python
"""
Configuración general de la aplicación CLI Standalone.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Directorio de datos de usuario
HOME_DIR = Path.home()
APP_DIR = HOME_DIR / ".sighor"
APP_DIR.mkdir(exist_ok=True)

# Base de datos
DATABASE_PATH = APP_DIR / "sighor.db"
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

# Autenticación
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Token storage
TOKEN_FILE = APP_DIR / "token"

# Output
DEFAULT_OUTPUT_FORMAT = "table"
```

### .env.example

```bash
# Secret key for JWT signing (CHANGE IN PRODUCTION)
SECRET_KEY=your-secret-key-here

# Database (optional, defaults to ~/.sighor/sighor.db)
# DATABASE_URL=sqlite:///path/to/custom/sighor.db

# Token expiration (minutes)
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## Implementación de componentes clave

### 1. Punto de entrada principal (cli/main.py)

```python
"""
Punto de entrada principal de la aplicación CLI Standalone.
"""
import click
from cli.commands.auth import auth_group
from cli.commands.aulas import aulas_group
from cli.utils.db import init_db

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """
    pySigHor - Sistema Generador de Horarios (CLI Standalone)
    """
    # Inicializar base de datos si no existe
    init_db()

cli.add_command(auth_group, name="auth")
cli.add_command(aulas_group, name="aulas")

if __name__ == "__main__":
    cli()
```

### 2. Configuración de base de datos (cli/utils/db.py)

```python
"""
Configuración de SQLAlchemy y gestión de sesiones.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from cli.config import DATABASE_URL, DATABASE_PATH

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Generador de sesiones de base de datos.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """
    Inicializa la base de datos y crea las tablas si no existen.
    """
    if not DATABASE_PATH.exists():
        from cli.models.user import User
        from cli.models.aula import Aula
        Base.metadata.create_all(bind=engine)

        # Crear usuario por defecto
        from cli.services.auth_service import AuthService
        from cli.repositories.user_repository import UserRepository

        db = next(get_db())
        user_repo = UserRepository(db)
        auth_service = AuthService(user_repo)

        # Usuario: admin / admin123
        if not user_repo.find_by_username("admin"):
            from cli.models.user import User
            admin = User(
                username="admin",
                email="admin@sighor.com",
                hashed_password=auth_service.hash_password("admin123")
            )
            db.add(admin)
            db.commit()
```

### 3. Gestión de tokens (cli/utils/token_manager.py)

```python
"""
Gestión de tokens JWT en sistema de archivos.
"""
from pathlib import Path
from cli.config import TOKEN_FILE

class TokenManager:
    """
    Gestiona el almacenamiento y recuperación de tokens JWT.
    """

    @staticmethod
    def save_token(token: str) -> None:
        """
        Guarda el token en el sistema de archivos.
        """
        TOKEN_FILE.write_text(token)

    @staticmethod
    def load_token() -> str:
        """
        Carga el token desde el sistema de archivos.

        Returns:
            str: Token JWT

        Raises:
            FileNotFoundError: Si no existe el token
        """
        if not TOKEN_FILE.exists():
            raise FileNotFoundError("No hay sesión activa. Ejecuta 'sighor auth login' primero.")
        return TOKEN_FILE.read_text().strip()

    @staticmethod
    def delete_token() -> None:
        """
        Elimina el token del sistema de archivos.
        """
        if TOKEN_FILE.exists():
            TOKEN_FILE.unlink()

    @staticmethod
    def token_exists() -> bool:
        """
        Verifica si existe un token guardado.
        """
        return TOKEN_FILE.exists()
```

### 4. Formateo de salida (cli/utils/output_formatter.py)

```python
"""
Formateo de salida para la CLI usando Rich.
"""
import json
from typing import List, Dict, Any
from rich.console import Console
from rich.table import Table

console = Console()

class OutputFormatter:
    """
    Formatea la salida de datos en diferentes formatos.
    """

    @staticmethod
    def format_table(data: List[Dict[str, Any]], columns: List[str]) -> None:
        """
        Formatea datos como tabla ASCII usando Rich.

        Args:
            data: Lista de diccionarios con los datos
            columns: Lista de nombres de columnas a mostrar
        """
        table = Table(show_header=True, header_style="bold cyan")

        for column in columns:
            table.add_column(column.upper())

        for row in data:
            table.add_row(*[str(row.get(col, "")) for col in columns])

        console.print(table)

    @staticmethod
    def format_json(data: Any) -> None:
        """
        Formatea datos como JSON.

        Args:
            data: Datos a formatear
        """
        print(json.dumps(data, indent=2, ensure_ascii=False))
```

### 5. Modelo de Aula (cli/models/aula.py)

```python
"""
Modelo de datos para Aula.
"""
from sqlalchemy import Column, Integer, String
from cli.utils.db import Base

class Aula(Base):
    """
    Modelo de datos para un aula.
    """
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    capacidad = Column(Integer, nullable=False)
    edificio = Column(String(100), nullable=False)

    def to_dict(self):
        """
        Convierte el objeto a diccionario.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "capacidad": self.capacidad,
            "edificio": self.edificio
        }
```

### 6. Repository de Aula (cli/repositories/aula_repository.py)

```python
"""
Repository para acceso a datos de Aula.
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from cli.models.aula import Aula

class AulaRepository:
    """
    Repository para operaciones CRUD sobre Aula.
    """

    def __init__(self, db: Session):
        self.db = db

    def find_all(self) -> List[Aula]:
        """
        Obtiene todas las aulas.
        """
        return self.db.query(Aula).all()

    def find_by_id(self, aula_id: int) -> Optional[Aula]:
        """
        Busca un aula por ID.
        """
        return self.db.query(Aula).filter(Aula.id == aula_id).first()

    def create(self, aula: Aula) -> Aula:
        """
        Crea una nueva aula.
        """
        self.db.add(aula)
        self.db.commit()
        self.db.refresh(aula)
        return aula

    def update(self, aula: Aula) -> Aula:
        """
        Actualiza una aula existente.
        """
        self.db.commit()
        self.db.refresh(aula)
        return aula

    def delete(self, aula_id: int) -> bool:
        """
        Elimina una aula por ID.
        """
        aula = self.find_by_id(aula_id)
        if aula:
            self.db.delete(aula)
            self.db.commit()
            return True
        return False
```

### 7. Service de Aula (cli/services/aula_service.py)

```python
"""
Service con lógica de negocio para Aula.
"""
from typing import List, Optional, Dict, Any
from cli.repositories.aula_repository import AulaRepository
from cli.models.aula import Aula

class AulaService:
    """
    Service con lógica de negocio para gestión de aulas.
    """

    def __init__(self, aula_repository: AulaRepository):
        self.aula_repository = aula_repository

    def get_all(self) -> List[Dict[str, Any]]:
        """
        Obtiene todas las aulas.
        """
        aulas = self.aula_repository.find_all()
        return [aula.to_dict() for aula in aulas]

    def get_by_id(self, aula_id: int) -> Optional[Dict[str, Any]]:
        """
        Obtiene un aula por ID.
        """
        aula = self.aula_repository.find_by_id(aula_id)
        return aula.to_dict() if aula else None

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Crea una nueva aula.
        """
        if not self.validate_aula(data):
            raise ValueError("Datos de aula inválidos")

        aula = Aula(
            nombre=data["nombre"],
            capacidad=data["capacidad"],
            edificio=data["edificio"]
        )
        created = self.aula_repository.create(aula)
        return created.to_dict()

    def update(self, aula_id: int, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Actualiza una aula existente.
        """
        aula = self.aula_repository.find_by_id(aula_id)
        if not aula:
            return None

        if not self.validate_aula(data):
            raise ValueError("Datos de aula inválidos")

        aula.nombre = data["nombre"]
        aula.capacidad = data["capacidad"]
        aula.edificio = data["edificio"]

        updated = self.aula_repository.update(aula)
        return updated.to_dict()

    def delete(self, aula_id: int) -> bool:
        """
        Elimina una aula.
        """
        return self.aula_repository.delete(aula_id)

    def validate_aula(self, data: Dict[str, Any]) -> bool:
        """
        Valida los datos de un aula.
        """
        required = ["nombre", "capacidad", "edificio"]
        if not all(field in data for field in required):
            return False

        if not isinstance(data["capacidad"], int) or data["capacidad"] <= 0:
            return False

        return True
```

### 8. Comando de listado de aulas (cli/commands/aulas.py - fragmento)

```python
"""
Comandos CLI para gestión de aulas.
"""
import click
from cli.services.aula_service import AulaService
from cli.repositories.aula_repository import AulaRepository
from cli.utils.db import get_db
from cli.utils.output_formatter import OutputFormatter
from cli.utils.token_manager import TokenManager

@click.group()
def aulas_group():
    """
    Gestión de aulas.
    """
    pass

@aulas_group.command(name="list")
@click.option("--format", type=click.Choice(["table", "json"]), default="table",
              help="Formato de salida")
def list_aulas(format):
    """
    Lista todas las aulas.
    """
    # Verificar autenticación
    try:
        TokenManager.load_token()
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        return

    # Obtener datos
    db = next(get_db())
    aula_repo = AulaRepository(db)
    aula_service = AulaService(aula_repo)

    aulas = aula_service.get_all()

    # Formatear salida
    if format == "table":
        OutputFormatter.format_table(aulas, ["id", "nombre", "capacidad", "edificio"])
    else:
        OutputFormatter.format_json(aulas)
```

## Empaquetado y distribución

### PyInstaller (scripts/build.sh)

```bash
#!/bin/bash

# Build script para generar ejecutable standalone

echo "Building pySigHor CLI Standalone..."

pyinstaller \
    --onefile \
    --name sighor \
    --add-data "cli:cli" \
    cli/main.py

echo "Build complete. Executable at: dist/sighor"
```

### Uso del ejecutable

```bash
# Después de compilar con PyInstaller
./dist/sighor auth login
./dist/sighor aulas list
./dist/sighor aulas create
```

## Pruebas

### pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts =
    --verbose
    --cov=cli
    --cov-report=html
    --cov-report=term-missing
```

### Ejemplo de prueba (tests/test_aula_service.py)

```python
"""
Pruebas para AulaService.
"""
import pytest
from cli.services.aula_service import AulaService
from cli.repositories.aula_repository import AulaRepository

def test_validate_aula_valid_data():
    """
    Prueba validación con datos correctos.
    """
    service = AulaService(None)
    data = {
        "nombre": "A101",
        "capacidad": 30,
        "edificio": "A"
    }
    assert service.validate_aula(data) is True

def test_validate_aula_missing_field():
    """
    Prueba validación con campo faltante.
    """
    service = AulaService(None)
    data = {
        "nombre": "A101",
        "capacidad": 30
    }
    assert service.validate_aula(data) is False
```

## Comparación: CLI HTTP vs CLI Standalone

|Aspecto|CLI HTTP|CLI Standalone|
|-|-|-|
|Arquitectura|Cliente HTTP|Monolítica|
|Dependencias|FastAPI backend|SQLAlchemy directo|
|LOC estimadas|~350|~1,250|
|Latencia|Red HTTP|Memoria local|
|Portabilidad|Requiere backend|Ejecutable único|
|Complejidad|Baja (reuso)|Media (implementación completa)|
|Despliegue|Cliente + Servidor|Solo ejecutable|
|Base de datos|Compartida (vía API)|Local SQLite|
|Offline|No|Sí|

## Próximos pasos de implementación

1. Implementar AuthService y UserRepository completos.
2. Desarrollar comandos CLI restantes (crear, editar, eliminar).
3. Implementar suite de pruebas completa.
4. Configurar CI/CD para compilación automática de ejecutable.
5. Documentar proceso de instalación y distribución del ejecutable.
6. Crear scripts de inicialización de base de datos con datos de ejemplo.
