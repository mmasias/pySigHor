# pySigHor Backend

Sistema Generador de Horarios - Backend FastAPI

## Instalación

```bash
# Instalar Poetry si no lo tienes
curl -sSL https://install.python-poetry.org | python3 -

# Instalar dependencias
poetry install

# Copiar archivo de variables de entorno
cp .env.example .env
```

## Desarrollo

```bash
# Levantar servidor de desarrollo
poetry run uvicorn app.main:app --reload --port 8000

# API Documentation disponible en:
# http://localhost:8000/docs (Swagger UI)
# http://localhost:8000/redoc (ReDoc)
```

## Tests

```bash
# Ejecutar tests
poetry run pytest

# Con coverage
poetry run pytest --cov=app --cov-report=html
```

## Estructura

```
app/
├── core/              # Configuración
├── models/            # SQLAlchemy models
├── schemas/           # Pydantic schemas
├── repositories/      # Repositorios
├── services/          # Lógica de negocio
└── routers/           # Endpoints API
```
