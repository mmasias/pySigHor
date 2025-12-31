# Comparativa de arquitecturas CLI

<div align=right>

|||||||
|-|-|-|-|-|-|
|[🏠️](../README.md)|[Artículo](README.md)|[Contexto](contexto.md)|[Evidencia](evidencia.md)|**Comparativa**|[Reuso](reusacion-vs-reimplementacion.md)|

</div>

## Dos arquitecturas, un solo análisis

Este documento compara en detalle las dos arquitecturas CLI propuestas para validar la independencia tecnológica de RUP. Ambas implementan los mismos casos de uso del análisis, pero con decisiones arquitectónicas radicalmente diferentes.

**Tesis central:** El análisis MVC permanece inalterado independientemente de la arquitectura elegida.

## Comparativa de alto nivel

<div align=center>

|Arquitectura 1<br>CLI como cliente HTTP|Arquitectura 2<br>CLI monolítico standalone|
|-|-|
|![Arquitectura CLI HTTP](../../images/extraDocs/016-validacion-cli/arquitectura-cli-http.svg)|![Arquitectura CLI Standalone](../../images/extraDocs/016-validacion-cli/arquitectura-cli-standalone.svg)|
|[Ver diagrama PlantUML](arquitectura-cli-http.puml)|[Ver diagrama PlantUML](arquitectura-cli-standalone.puml)|
|**Reusa** backend completo de FastAPI|**Reimplementa** toda la pila (vista + controlador + modelo)|
|**Agrega** solo vista CLI|**Sin dependencias** de servidor HTTP|
|**Depende** de servidor HTTP corriendo|**Standalone** - ejecutable sin servicios externos|
|**Comparte** controlador y modelo con React/Angular|**Portabilidad** máxima|

</div>

## Comparativa técnica detallada

### Dependencias y configuración

<div align=center>

|Aspecto|CLI HTTP|CLI Standalone|
|-|-|-|
|**Dependencias Python**|`click`, `requests`|`click`, `sqlalchemy`, `psycopg2-binary`|
|**Servidor requerido**|FastAPI (http://localhost:8000)|Ninguno|
|**Variables de entorno**|`API_BASE_URL`|`DATABASE_URL`|
|**Configuración de DB**|No requiere (la tiene FastAPI)|Requiere connection string completo|
|**Portabilidad**|Baja (depende de servidor)|Alta (solo requiere DB)|

</div>

**Ejemplo de configuración:**

**CLI HTTP (`config.py`):**

```python
API_BASE_URL = os.getenv('API_BASE_URL', 'http://localhost:8000/api')
```

**CLI Standalone (`database.py`):**

```python
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:pass@localhost:5432/pysighor')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
```

### Estructura de código

<div align=center>

|Componente|CLI HTTP|CLI Standalone|
|-|-|-|
|**Vista**|`commands/*.py` (Click)|`commands/*.py` (Click)|
|**API Client**|`api_client/client.py`|No existe|
|**Controlador**|Reusa FastAPI|`services/*.py` (implementación propia)|
|**Modelo (Repository)**|Reusa FastAPI|`repositories/*.py` (implementación propia)|
|**Modelo (Models)**|Reusa FastAPI|`models/*.py` (SQLAlchemy)|
|**Utils**|`config.py`, `formatters.py`|`config.py`, `database.py`, `formatters.py`|

</div>

### Líneas de código por componente

<div align=center>

|Componente|CLI HTTP|CLI Standalone|Diferencia|
|-|-|-|-|
|**Vista (commands)**|~200 LOC|~250 LOC|+25% (más lógica de orquestación)|
|**API Client**|~100 LOC|0 LOC|-|
|**Services**|0 LOC (reusa)|~400 LOC|+400 LOC|
|**Repositories**|0 LOC (reusa)|~300 LOC|+300 LOC|
|**Models**|0 LOC (reusa)|~200 LOC|+200 LOC|
|**Utils**|~50 LOC|~100 LOC|+50 LOC|
|**TOTAL**|**~350 LOC**|**~1,250 LOC**|**+257%**|

</div>

**Punto clave:** CLI standalone requiere **3.5x más código**, pero es **completamente independiente** del stack web.

## Comparativa de implementación: Caso `iniciarSesion()`

### CLI HTTP: Delegación a API

<details><summary><b>Archivo:</b> commands/auth.py</summary>

```python
import click
from api_client.client import APIClient
from utils.config import save_token

@click.command()
def login():
    """Iniciar sesión (consume API FastAPI)"""
    username = click.prompt('Usuario')
    password = click.prompt('Contraseña', hide_input=True)

    # Delegación completa a API existente
    client = APIClient()
    response = client.post('/login', json={
        'username': username,
        'password': password
    })

    if response.status_code == 200:
        data = response.json()
        save_token(data['token'])
        click.echo('✓ Sesión iniciada')
    else:
        click.echo('✗ Credenciales inválidas', err=True)
```

</details>

#### Responsabilidades

- Vista: Interacción CLI con usuario
- Controlador: **Reusado de FastAPI** (AuthService)
- Modelo: **Reusado de FastAPI** (UserRepository)

**Tiempo de implementación:** ~30 minutos

### CLI Standalone: Implementación completa

<details><summary><b>Archivo:</b> commands/auth.py</summary>

```python
import click
from services.auth_service import AuthenticationService
from repositories.user_repository import UserRepository
from repositories.session_repository import SessionRepository
from utils.database import get_db_session
from utils.config import save_token

@click.command()
def login():
    """Iniciar sesión (standalone)"""
    username = click.prompt('Usuario')
    password = click.prompt('Contraseña', hide_input=True)

    # Orquestación completa de pila propia
    db = get_db_session()
    user_repo = UserRepository(db)
    session_repo = SessionRepository(db)
    auth_service = AuthenticationService(user_repo, session_repo)

    try:
        session = auth_service.authenticate(username, password)

        if session:
            save_token(session.token)
            click.echo('✓ Sesión iniciada')
        else:
            click.echo('✗ Credenciales inválidas', err=True)
    finally:
        db.close()
```

</details>

<details><summary><b>Archivo:</b> services/auth_service.py</summary>

```python
from typing import Optional
from models.session import Session

class AuthenticationService:
    """Controlador: Lógica de autenticación"""

    def __init__(self, user_repo, session_repo):
        self.user_repo = user_repo
        self.session_repo = session_repo

    def authenticate(self, username: str, password: str) -> Optional[Session]:
        """Implementa lógica de análisis MVC"""
        if not self._validate_format(username, password):
            return None

        user = self.user_repo.find_by_username(username)

        if not user or not user.verify_password(password):
            return None

        return self.session_repo.create(user.id)

    def _validate_format(self, username: str, password: str) -> bool:
        return bool(username and password and len(username) >= 3)
```

</details>

<details><summary><b>Archivo:</b> repositories/user_repository.py</summary>

```python
from typing import Optional
from sqlalchemy.orm import Session
from models.user import User

class UserRepository:
    """Modelo: Acceso a datos de usuarios"""

    def __init__(self, db: Session):
        self.db = db

    def find_by_username(self, username: str) -> Optional[User]:
        return self.db.query(User).filter(User.username == username).first()
```

</details>

<details><summary><b>Archivo:</b> models/user.py</summary>

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import bcrypt

Base = declarative_base()

class User(Base):
    """Modelo: Modelo de usuario"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    nombre = Column(String(100))

    def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password_hash.encode('utf-8')
        )
```

</details>

#### Responsabilidades

- Vista: Interacción CLI con usuario
- Controlador: **Implementado desde cero** (AuthenticationService)
- Modelo: **Implementado desde cero** (UserRepository, User model)

**Tiempo de implementación:** ~1.5 horas

**Análisis afectado:** **NINGUNO** - Las responsabilidades del análisis MVC se mantienen idénticas.

## Comparativa de esfuerzo por caso de uso

### Caso: `iniciarSesion()`

<div align=center>

|Aspecto|CLI HTTP|CLI Standalone|
|-|-|-|
|**Archivos nuevos**|1 (command)|5 (command + service + 2 repos + model)|
|**LOC vista**|~25|~35|
|**LOC controlador**|0 (reusa)|~80|
|**LOC modelo**|0 (reusa)|~120|
|**Total LOC**|~25|~235|
|**Tiempo**|30 min|1.5h|
|**Complejidad**|Baja|Media|

</div>

### Caso: `abrirAulas()`

<div align=center>

|Aspecto|CLI HTTP|CLI Standalone|
|-|-|-|
|**Archivos nuevos**|1 (command)|4 (command + service + repo + model)|
|**LOC vista**|~40 (tabla)|~50|
|**LOC controlador**|0 (reusa)|~60|
|**LOC modelo**|0 (reusa)|~100|
|**Total LOC**|~40|~210|
|**Tiempo**|30 min|1.5h|
|**Complejidad**|Baja|Media|

</div>

### Caso: `crearAula()`

<div align=center>

|Aspecto|CLI HTTP|CLI Standalone|
|-|-|-|
|**Archivos nuevos**|1 (command)|2 (command + método en service/repo)|
|**LOC vista**|~30|~40|
|**LOC controlador**|0 (reusa)|~40|
|**LOC modelo**|0 (reusa)|~50|
|**Total LOC**|~30|~130|
|**Tiempo**|30 min|1h|
|**Complejidad**|Baja|Media|

</div>

### Caso: `editarAula()`

<div align=center>

|Aspecto|CLI HTTP|CLI Standalone|
|-|-|-|
|**Archivos nuevos**|1 (command)|2 (command + método en service/repo)|
|**LOC vista**|~35 (prompt valores actuales)|~50|
|**LOC controlador**|0 (reusa)|~60|
|**LOC modelo**|0 (reusa)|~70|
|**Total LOC**|~35|~180|
|**Tiempo**|30 min|2h|
|**Complejidad**|Media|Media-Alta|

</div>

### Caso: `eliminarAula()`

<div align=center>

|Aspecto|CLI HTTP|CLI Standalone|
|-|-|-|
|**Archivos nuevos**|1 (command)|2 (command + método en service/repo)|
|**LOC vista**|~25 (confirmación)|~30|
|**LOC controlador**|0 (reusa)|~30|
|**LOC modelo**|0 (reusa)|~40|
|**Total LOC**|~25|~100|
|**Tiempo**|30 min|1h|
|**Complejidad**|Baja|Media|

</div>

### Totales

<div align=center>

|Métrica|CLI HTTP|CLI Standalone|Factor|
|-|-:|-:|-:|
|**Archivos nuevos**|5|15|3x|
|**Total LOC**|~155|~855|5.5x|
|**Tiempo total**|~2.5h|~7.5h|3x|
|**Complejidad promedio**|Baja|Media|-|
|**Análisis modificado**|No|No|-|

</div>

## Compromisos

<table>
<tr><th>CLI como cliente HTTP</th><th>CLI monolítico standalone</th></tr>
<tr><td valign=top>

**Ventajas:**

- **Reuso máxima** - Todo el backend ya existe
- **Velocidad de desarrollo** - 3x más rápido
- **Consistencia** - Misma lógica que React/Angular
- **Mantenimiento centralizado** - Bug fixes en FastAPI benefician a CLI
- **Simplicidad** - Solo implementa boundary CLI

</td><td valign=top>

**Ventajas:**

- **Independencia total** - No requiere servidor HTTP
- **Portabilidad** - Distribuible como ejecutable único
- **Performance** - Sin latencia de red
- **Robustez** - Menos puntos de falla
- **Funciona sin conexión** - Opera sin conectividad a API

</td></tr>
<tr><td valign=top>

**Desventajas:**

- **Dependencia de servidor** - Requiere FastAPI corriendo
- **Latencia de red** - Cada comando hace llamada HTTP
- **Punto de falla adicional** - Si FastAPI cae, CLI no funciona
- **Complejidad de despliegue** - Usuario debe configurar servidor
- **No portable** - No se puede distribuir como ejecutable único

</td><td valign=top>

**Desventajas:**

- **Reimplementación** - 3x más esfuerzo de desarrollo
- **Duplicación de lógica** - Services y repositories duplicados
- **Mantenimiento doble** - Bug fixes deben aplicarse dos veces
- **Riesgo de divergencia** - Lógica puede inconsistirse con backend
- **Mayor complejidad** - Gestión de DB, migraciones, etc.

</td></tr>
<tr><td valign=top>

**Escenario ideal:**

- Desarrollo interno donde FastAPI ya está corriendo
- Herramienta de administración para equipo técnico
- Scripts de automatización que consumen API existente

</td><td valign=top>

**Escenario ideal:**

- Herramienta de línea de comandos para usuarios finales
- Distribución a equipos sin infraestructura de servidores
- Scripts batch que no pueden depender de servicios externos
- Situaciones donde portabilidad es crítica

</td></tr>
</table>

## Tabla de decisión arquitectónica

<div align=center>

|Criterio|CLI HTTP|CLI Standalone|
|-|-|-|
|**Tiempo de desarrollo**|⭐⭐⭐⭐⭐ (muy rápido)|⭐⭐ (lento)|
|**Reuso de código**|⭐⭐⭐⭐⭐ (100%)|⭐ (0%)|
|**Portabilidad**|⭐ (baja)|⭐⭐⭐⭐⭐ (alta)|
|**Independencia**|⭐ (depende de servidor)|⭐⭐⭐⭐⭐ (standalone)|
|**Performance**|⭐⭐⭐ (latencia HTTP)|⭐⭐⭐⭐⭐ (directo)|
|**Mantenibilidad**|⭐⭐⭐⭐⭐ (centralizado)|⭐⭐ (duplicado)|
|**Complejidad inicial**|⭐⭐⭐⭐⭐ (simple)|⭐⭐ (complejo)|
|**Complejidad de despliegue**|⭐⭐ (servidor requerido)|⭐⭐⭐⭐ (solo DB)|

</div>

## La lección metodológica

### Lo que CAMBIA

<div align=center>

|Aspecto|Entre arquitecturas|
|-|-|
|**Archivos creados**|5 vs 15 archivos|
|**Líneas de código**|155 vs 855 LOC|
|**Tiempo de desarrollo**|2.5h vs 7.5h|
|**Dependencias**|HTTP vs ORM|
|**Complejidad técnica**|Baja vs Media|

</div>

### Lo que NO CAMBIA

<div align=center>

|Artefacto de análisis|Estado|
|-|-|
|**Especificaciones detalladas**|Sin modificación|
|**Diagramas de colaboración MVC**|Sin modificación|
|**Responsabilidades vista/controlador/modelo**|Sin modificación|
|**Diagramas de secuencia de análisis**|Sin modificación|
|**Wireframes SALT**|Sin modificación|

</div>

**Conclusión metodológica:**

> La decisión arquitectónica entre CLI HTTP y CLI standalone es **ortogonal al análisis**. El análisis MVC captura las responsabilidades del sistema, no las decisiones de implementación. Estas decisiones se toman en la fase de diseño basándose en criterios como:
>
> - Tiempo disponible
> - Reuso deseada
> - Requisitos de portabilidad
> - Infraestructura disponible
> - Escenario de despliegue
>
> **RUP cumple su promesa:** Un análisis riguroso soporta múltiples implementaciones sin modificaciones.

## Recomendación de implementación

### Para validación experimental (Artículo 016)

**Implementar AMBAS arquitecturas:**

1. **Fase 1 - CLI HTTP** (~2.5h)
   - Validar reuso máxima
   - Demostrar velocidad de desarrollo
   - Mostrar consistencia con backend existente

2. **Fase 2 - CLI Standalone** (~8h)
   - Validar independencia total
   - Demostrar portabilidad
   - Mostrar que análisis soporta reimplementación completa

**Valor didáctico:**

- Dos arquitecturas radicalmente diferentes
- Mismo análisis MVC sin modificación
- Validación definitiva de independencia tecnológica

### Para producción real

**Criterios de elección:**

<div align=center>

|Elegir CLI HTTP si|Elegir CLI Standalone si|
|-|-|
|Backend FastAPI ya está desplegado y disponible|Usuario objetivo es no técnico sin infraestructura de servidores
|Usuario objetivo es técnico con acceso a servidores|Prioridad es portabilidad y distribución simple
|Prioridad es velocidad de desarrollo y mantenimiento centralizado|Requiere funcionamiento offline o sin dependencias externas
|No requiere distribución offline|Disponibilidad de tiempo para reimplementación

</div>

## Conclusión

Esta comparativa demuestra que:

1. **Dos arquitecturas radicalmente diferentes** (HTTP vs monolítico)
2. **Implementan el mismo análisis** sin modificaciones
3. **Con compromisos medibles** en esfuerzo, portabilidad y mantenimiento
4. **Validando que RUP cumple su promesa** de independencia tecnológica

El análisis MVC es **verdaderamente independiente** de decisiones arquitectónicas. Las responsabilidades vista/controlador/modelo se mantienen, solo cambia **cómo** se implementan técnicamente.

## Referencias

- [Artículo principal](README.md)
- [Contexto del experimento](contexto.md)
- [Evidencia de implementación](evidencia.md)
- [Análisis de reuso vs reimplementación](reusacion-vs-reimplementacion.md)
