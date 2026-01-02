# Configuración y estructura del proyecto - CLI HTTP

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración → Construcción
- **Disciplina**: Diseño
- **Versión**: 1.0 (CLI HTTP)
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Este documento define la estructura de directorios, configuraciones iniciales y decisiones técnicas para implementar una interfaz CLI que consume la API FastAPI existente. La arquitectura prioriza el **reuso máximo** del backend ya implementado.

## Filosofía de organización

### Principios aplicados

1. **Reuso máximo**: Backend FastAPI completo sin modificaciones
2. **Separación CLI/API**: CLI como cliente HTTP independiente
3. **Simplicidad**: Estructura minimalista enfocada en comandos
4. **Portabilidad**: Interfaz textual ejecutable en cualquier terminal

## Estructura de directorios

### Vista general

```
pySigHor/
├── cli/                        # Aplicación CLI (NUEVO)
│   ├── sighor/
│   │   ├── commands/          # Comandos Click
│   │   │   ├── __init__.py
│   │   │   ├── auth.py        # login, logout
│   │   │   └── aulas.py       # list, create, edit, delete
│   │   ├── client/            # Cliente HTTP
│   │   │   ├── __init__.py
│   │   │   ├── api_client.py  # Wrapper de requests
│   │   │   └── token_manager.py  # Gestión de tokens
│   │   ├── utils/             # Utilidades
│   │   │   ├── __init__.py
│   │   │   ├── output.py      # Formateo de salida
│   │   │   └── config.py      # Configuración CLI
│   │   └── main.py            # Punto de entrada CLI
│   ├── tests/                 # Tests CLI
│   ├── pyproject.toml         # Dependencias Poetry
│   └── .env.example           # API_BASE_URL
│
├── backend/                    # Backend FastAPI (REUTILIZADO)
│   └── [Estructura completa heredada de diseño-fastapi-react]
│
├── RUP/                        # Artefactos metodológicos
└── README.md                   # Documentación principal
```

### Justificación de la estructura

#### CLI: Organización por comandos

```
cli/sighor/
├── commands/        → Comandos Click (auth, aulas, etc.)
├── client/          → Cliente HTTP + gestión de tokens
├── utils/           → Formateo de salida, configuración
└── main.py          → Entry point (CLI app)
```

**Flujo de un comando**:
```
Comando Click → APIClient → HTTP Request → Backend FastAPI → Response
                                                    ↓
                                        Services/Repositories/DB
                                                    ↓
Formatear output ← JSON Response ← HTTP Response ←
```

Esta separación permite:

- **Independencia**: CLI desacoplado del backend (solo consume API)
- **Testabilidad**: Comandos pueden probarse con mock de API
- **Mantenibilidad**: Cambios en backend no afectan CLI (API estable)

## Configuraciones iniciales

### Dependencias Python (pyproject.toml)

```toml
[tool.poetry]
name = "pysighor-cli"
version = "0.1.0"
description = "CLI para sistema SigHor"
authors = ["pySigHor Team"]

[tool.poetry.dependencies]
python = "^3.11"
click = "^8.1.7"          # Framework CLI
requests = "^2.31.0"      # Cliente HTTP
rich = "^13.7.0"          # Formateo de salida (tablas, colores)
python-dotenv = "^1.0.0"  # Variables de entorno

[tool.poetry.dev-dependencies]
pytest = "^7.4.3"
pytest-mock = "^3.12.0"
black = "^23.12.1"
ruff = "^0.1.8"

[tool.poetry.scripts]
sighor = "sighor.main:cli"  # Comando global
```

### Variables de entorno (.env)

```bash
# Conexión a API FastAPI
API_BASE_URL=http://localhost:8000/api

# Archivo de almacenamiento de token
TOKEN_FILE=~/.sighor/token

# Timeout de requests (segundos)
API_TIMEOUT=30

# Modo de salida por defecto (table, json)
DEFAULT_OUTPUT_FORMAT=table
```

## Mapeo entre diseño y código

### Diagrama de clases → Código CLI

| Clase de diseño | Archivo | Responsabilidad |
|----------------|---------|-----------------|
| `CLIApp` | `sighor/main.py` | Entry point de comandos Click |
| `AuthCommands` | `sighor/commands/auth.py` | Comandos `login`, `logout` |
| `AulaCommands` | `sighor/commands/aulas.py` | Comandos `list`, `create`, `edit`, `delete` |
| `APIClient` | `sighor/client/api_client.py` | Wrapper de `requests` (GET, POST, PUT, DELETE) |
| `TokenManager` | `sighor/client/token_manager.py` | Guardar/recuperar/eliminar token JWT |
| `OutputFormatter` | `sighor/utils/output.py` | Formatear salida (tabla Rich, JSON) |

### Endpoints consumidos

| Caso de uso | Comando CLI | Endpoint FastAPI | Método |
|-------------|-------------|------------------|--------|
| `iniciarSesion()` | `sighor login` | `/token` | POST |
| `abrirAulas()` | `sighor aulas list` | `/aulas?skip=0&limit=100` | GET |
| `crearAula()` | `sighor aulas create` | `/aulas` | POST |
| `editarAula()` | `sighor aulas edit <id>` | `/aulas/{id}` | PUT |
| `eliminarAula()` | `sighor aulas delete <id>` | `/aulas/{id}` | DELETE |

## Comandos de desarrollo

### Instalación

```bash
# Instalar dependencias
cd cli
poetry install

# Activar entorno virtual
poetry shell
```

### Ejecución local

```bash
# Asegurar que backend FastAPI está corriendo
cd ../backend
poetry run uvicorn app.main:app --reload

# En otra terminal, ejecutar CLI
cd ../cli
poetry run sighor --help
poetry run sighor login
poetry run sighor aulas list
```

### Testing

```bash
# Ejecutar tests CLI (con mock de API)
poetry run pytest

# Ejecutar tests con cobertura
poetry run pytest --cov=sighor
```

### Empaquetado

```bash
# Construir paquete distribuible
poetry build

# Instalar CLI globalmente
pip install dist/pysighor_cli-0.1.0-py3-none-any.whl

# Ejecutar desde cualquier directorio
sighor --help
```

## Dependencias del backend

### Requisito crítico: Backend FastAPI debe estar corriendo

El CLI HTTP depende completamente del backend FastAPI:

```bash
# Terminal 1: Backend
cd backend
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000

# Terminal 2: CLI
cd cli
poetry run sighor login
```

**Ventajas de esta dependencia:**

- Reuso total de lógica de negocio
- Misma base de datos que interfaz React
- Validaciones y seguridad centralizadas

**Desventajas:**

- Requiere dos procesos corriendo
- Sobrecarga de red (HTTP local)
- No funciona offline

Para casos donde el backend no está disponible, ver rama `diseño-cli-python-standalone`.

## Ejemplo de implementación: Comando `login`

```python
# sighor/commands/auth.py
import click
from sighor.client.api_client import APIClient
from sighor.client.token_manager import TokenManager

@click.command()
@click.option('--username', prompt=True, help='Nombre de usuario')
@click.option('--password', prompt=True, hide_input=True, help='Contraseña')
def login(username, password):
    """Iniciar sesión en el sistema SigHor"""

    client = APIClient()
    token_manager = TokenManager()

    try:
        # Consumir endpoint POST /token
        response = client.post('/token',
                              data={'username': username, 'password': password})

        if response.status_code == 200:
            token = response.json()['access_token']
            token_manager.save_token(token)
            click.echo(click.style('✓ Sesión iniciada exitosamente', fg='green'))
        else:
            click.echo(click.style('✗ Credenciales inválidas', fg='red'), err=True)

    except requests.exceptions.ConnectionError:
        click.echo(click.style('✗ Error: Backend FastAPI no disponible', fg='red'), err=True)
        click.echo('Asegúrate de que el servidor esté corriendo en http://localhost:8000')
```

## Ejemplo de implementación: Comando `aulas list`

```python
# sighor/commands/aulas.py
import click
from rich.console import Console
from rich.table import Table
from sighor.client.api_client import APIClient
from sighor.utils.output import format_table

@click.command()
@click.option('--format', type=click.Choice(['table', 'json']), default='table',
              help='Formato de salida')
def list(format):
    """Listar todas las aulas"""

    client = APIClient()

    try:
        # Consumir endpoint GET /aulas
        response = client.get('/aulas', params={'skip': 0, 'limit': 100})

        if response.status_code == 200:
            aulas = response.json()

            if format == 'table':
                console = Console()
                table = Table(title="Aulas registradas")
                table.add_column("ID", justify="right", style="cyan")
                table.add_column("Nombre", style="magenta")
                table.add_column("Capacidad", justify="right", style="green")
                table.add_column("Edificio", style="yellow")

                for aula in aulas:
                    table.add_row(str(aula['id']), aula['nombre'],
                                str(aula['capacidad']), aula['edificio'])

                console.print(table)
            else:
                # Formato JSON
                click.echo(json.dumps(aulas, indent=2))
        else:
            click.echo(click.style('✗ Error al listar aulas', fg='red'), err=True)

    except requests.exceptions.ConnectionError:
        click.echo(click.style('✗ Error: Backend FastAPI no disponible', fg='red'), err=True)
```

## Próximos pasos

1. **Implementación de comandos**: Codificar todos los comandos según diseño
2. **Tests unitarios**: Mockear APIClient para tests independientes
3. **Documentación de usuario**: Manual de uso del CLI
4. **Distribución**: Publicar en PyPI como paquete instalable

## Comparativa con arquitectura CLI Standalone

| Aspecto | CLI HTTP (esta rama) | CLI Standalone |
|---------|---------------------|----------------|
| **Backend** | Reutiliza FastAPI completo | Implementa Services/Repos propios |
| **Dependencias** | Requiere FastAPI corriendo | Solo requiere DB |
| **LOC estimadas** | ~350 líneas | ~1,250 líneas |
| **Tiempo desarrollo** | ~2.5h | ~8h |
| **Ventaja clave** | Reuso máximo | Independencia total |
| **Caso de uso ideal** | Entorno con API disponible | Entorno standalone/offline |

Esta arquitectura CLI HTTP es óptima cuando:

- El backend FastAPI ya está implementado y corriendo
- Se prioriza rapidez de desarrollo (reuso)
- Consistencia con frontend React es crítica
- Sobrecarga HTTP local es aceptable

Para casos donde se requiere CLI standalone (sin servidor HTTP), ver rama `diseño-cli-python-standalone`.
