# Auditoría formal: Diseño vs Implementación

## Información de la auditoría

- **Fecha**: 2026-05-13
- **Rama auditada**: `diseño-fastapi-react`
- **Commit auditado**: `40af49d` (tag: `pre-auditoria-diseno-codigo`)
- **Artefacto de diseño de referencia**: `RUP/02-diseño/configuracion-proyecto.md`
- **Auditor**: opencode (GLM-5.1)

## Criterios de severidad

| Severidad | Criterio |
|---|---|
| **CRITICA** | Impide funcionamiento correcto o compromete seguridad |
| **ALTA** | Divergencia arquitectónica significativa vs diseño |
| **MEDIA** | Bug funcional o gap de UX que afecta un caso de uso |
| **BAJA** | Code smell, nomenclatura o detalle cosmético |

## Desviaciones identificadas

### D01 - Motor sincrónico en lugar de asincrónico | CRITICA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `DATABASE_URL: str = "sqlite+aiosqlite:///./pysighor.db"` + `create_async_engine` + `AsyncSession` + `async_sessionmaker` (configuracion-proyecto.md, líneas ~180-210) |
| **Código real** | `backend/app/core/database.py`: `sqlite:///./pySigHor.db` + `create_engine` + `Session` + `sessionmaker` (sincrónico) |
| **Impacto** | Toda la cadena Router->Service->Repository opera en modo bloqueante. Se pierde el beneficio async de FastAPI. |
| **Estado** | [PENDIENTE] |

### D02 - Pydantic v1 en lugar de v2 | CRITICA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `pydantic = {extras = ["email"], version = "^2.5.3"}` + `pydantic-settings = "^2.1.0"` (configuracion-proyecto.md, líneas ~113-130) |
| **Código real** | `backend/pyproject.toml`: `pydantic = "^1.10.13"`, sin `pydantic-settings`. `core/config.py`: `from pydantic import BaseSettings` (v1) |
| **Impacto** | API de configuración diferente, `orm_mode` vs `from_attributes`, sin separación de paquetes |
| **Estado** | [PENDIENTE] |

### D03 - SECRET_KEY con valor por defecto inseguro | CRITICA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `SECRET_KEY: str` sin default (falla si no está en `.env`) (configuracion-proyecto.md, línea ~172) |
| **Código real** | `backend/app/core/config.py:12`: `SECRET_KEY: str = "your-secret-key-here-change-in-production"` |
| **Impacto** | En producción sin `.env`, el sistema corre con secreto conocido y predecible |
| **Estado** | [PENDIENTE] |

### D04 - CORS hardcodeado en lugar de configurable | ALTA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173"]` en Settings (configuracion-proyecto.md, línea ~174) |
| **Código real** | `backend/app/main.py:16`: `allow_origins=["http://localhost:5173"]` hardcodeado |
| **Impacto** | No se puede cambiar sin modificar código fuente |
| **Estado** | [PENDIENTE] |

### D05 - Endpoints CRUD sin protección de autenticación | CRITICA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | Diseño de `abrirAulas` (RUP/02-diseño/casos-uso/abrirAulas/README.md): "Todos los endpoints requieren token valido" |
| **Código real** | `backend/app/routers/aulas.py` (y los otros 5 routers CRUD): ningún endpoint usa `Depends(oauth2_scheme)` ni `Depends(get_current_user)` |
| **Impacto** | Los 30+ endpoints CRUD son públicamente accesibles sin autenticación |
| **Estado** | [PENDIENTE] |

### D06 - Modelo Usuario sin campo `rol` | ALTA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | SQL: `rol VARCHAR(20) DEFAULT 'admin'` + Modelo: `rol = Column(String(20), default="admin")` (configuracion-proyecto.md, líneas ~310-330) |
| **Código real** | `backend/app/models/usuario.py`: solo tiene `id, username, hashed_password, activo` |
| **Impacto** | El frontend referencia `user.rol` pero nunca llega del backend. No hay control de acceso basado en roles. |
| **Estado** | [PENDIENTE] |

### D07 - Modelos sin timestamps | ALTA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | SQL: `created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP`, `updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP` (configuracion-proyecto.md, líneas ~310-320) |
| **Código real** | Ningún modelo tiene campos de timestamp |
| **Impacto** | Sin auditoría de cuándo se crearon o modificaron los registros |
| **Estado** | [PENDIENTE] |

### D08 - Sin infraestructura Alembic | ALTA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `alembic = "^1.13.1"` como dependencia + directorio `migrations/` (configuracion-proyecto.md, líneas ~120, ~85) |
| **Código real** | `alembic` está en `pyproject.toml` como dependencia pero no existe `alembic.ini`, `migrations/env.py`, ni versiones |
| **Impacto** | Sin migraciones versionadas. Cambios de schema requieren recrear la BD manualmente. |
| **Estado** | [PENDIENTE] |

### D09 - Sin tests | ALTA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | Directorio `tests/` con `pytest`, `pytest-asyncio`, `httpx` (configuracion-proyecto.md, línea ~42, líneas ~135-140) |
| **Código real** | No existe directorio `tests/`. Las dependencias están declaradas pero sin usar. |
| **Impacto** | No hay disciplina de Pruebas RUP. Cero cobertura. |
| **Estado** | [PENDIENTE] |

### D10 - Import `Optional` faltante en security.py | CRITICA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | N/A (bug de código, no desviación de diseño) |
| **Código real** | `backend/app/core/security.py:21`: `def create_access_token(data: dict, expires_delta: Optional[timedelta] = None)` usa `Optional` sin importarlo de `typing` |
| **Impacto** | `NameError` en runtime si se invoca con `expires_delta` explícito |
| **Estado** | [PENDIENTE] |

### D11 - Frontend sin navegación | ALTA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | Diagrama de contexto define `completarGestion()` como estado central de navegación. `frontend/src/components/` con componentes reutilizables |
| **Código real** | No existe `components/` ni `utils/`. No hay sidebar, navbar ni menú. Solo se navega editando la URL. |
| **Impacto** | La aplicación es inutilizable sin conocimiento de las rutas |
| **Estado** | [PENDIENTE] |

### D12 - Formularios sin selectores de FK | MEDIA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | Modelo Aula tiene `id_edificio` (FK a Edificio). Modelo Curso tiene `id_programa` (FK a Programa). |
| **Código real** | `frontend/src/pages/AulasPage.tsx`: define `id_edificio` en `formData` pero el diálogo no tiene dropdown de Edificio. `CursosPage.tsx`: mismo problema con Programa. |
| **Impacto** | Relaciones modeladas pero invisibles al usuario |
| **Estado** | [PENDIENTE] |

### D13 - Theme MUI con API incorrecta | MEDIA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | N/A (bug de código) |
| **Código real** | `frontend/src/App.tsx:14-18`: `createTheme({ colorScheme: { mode: 'light' } })` - no es API válida de MUI v5. Correcto: `palette: { mode: 'light' }` |
| **Impacto** | Configuración de theme silenciosamente ignorada |
| **Estado** | [PENDIENTE] |

### D14 - Sin interceptor 401 en frontend | MEDIA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `frontend/src/services/api.ts` con interceptor response: `if (error.response?.status === 401) { localStorage.removeItem('access_token'); window.location.href = '/login'; }` (configuracion-proyecto.md, líneas ~410-430) |
| **Código real** | `frontend/src/services/api.ts`: solo existe interceptor de request (inyectar token). No hay interceptor de response. |
| **Impacto** | Token expirado produce errores en cada llamada sin redirigir al login |
| **Estado** | [PENDIENTE] |

### D15 - Token no verificado al cargar aplicación | MEDIA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `AuthContext.tsx` con `useEffect` que valida token contra endpoint `/me` (configuracion-proyecto.md, líneas ~460-480) |
| **Código real** | `frontend/src/context/AuthContext.tsx:18-24`: lee token de localStorage y confía en él sin llamar `authService.verifyToken()` |
| **Impacto** | Token revocado o expirado se acepta hasta que una llamada API falle |
| **Estado** | [PENDIENTE] |

### D16 - Imports `EmailStr` sin usar | BAJA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | N/A (bug de código) |
| **Código real** | `backend/app/schemas/profesor.py:1` y `backend/app/schemas/auth.py:1` importan `EmailStr` pero no lo usan |
| **Impacto** | Import muerto, posible error si falta dependencia `email-validator` |
| **Estado** | [PENDIENTE] |

### D17 - Imports diferidos en services | BAJA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | N/A (code smell) |
| **Código real** | Todos los `services/*.py` importan e instancian su repository dentro de cada método en lugar de en `__init__` |
| **Impacto** | Overhead innecesario por llamada, patrón no idiomático |
| **Estado** | [PENDIENTE] |

### D18 - Sin directorio `components/` | MEDIA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `frontend/src/components/` con elementos UI reutilizables (configuracion-proyecto.md, línea ~88) |
| **Código real** | Directorio no existe. Las 6 páginas CRUD son copia-pega monolíticas. |
| **Impacto** | Cambio de patrón requiere editar 6 archivos idénticos |
| **Estado** | [PENDIENTE] |

### D19 - Sin directorio `utils/` | BAJA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `frontend/src/utils/` (configuracion-proyecto.md, línea ~91) |
| **Código real** | Directorio no existe |
| **Impacto** | Sin utilidades compartidas |
| **Estado** | [PENDIENTE] |

### D20 - Sin directorio `public/` | BAJA

| Aspecto | Detalle |
|---|---|
| **Diseño especifica** | `frontend/public/` para recursos estáticos (configuracion-proyecto.md, línea ~94) |
| **Código real** | Directorio no existe |
| **Impacto** | Sin ubicación para assets estáticos (favicon, etc.) |
| **Estado** | [PENDIENTE] |

## Resumen estadístico

| Severidad | Cantidad |
|---|---|
| CRITICA | 4 (D01, D02, D03, D05) + 1 bug (D10) |
| ALTA | 5 (D04, D06, D07, D08, D09) + 1 gap (D11) |
| MEDIA | 4 (D12, D13, D14, D15) + 1 gap (D18) |
| BAJA | 3 (D16, D17, D19) + 1 gap (D20) |
| **Total** | **20** |
