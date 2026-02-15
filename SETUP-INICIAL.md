# pySigHor - Iteración 1: Setup Inicial

## ✅ Completo

Este README guía el setup inicial del proyecto pySigHor.

## Estructura Creada

```
pySigHor/
├── backend/                    ✅ Backend FastAPI
│   ├── app/
│   │   ├── core/              ✅ Configuración central
│   │   ├── models/            ✅ Modelos SQLAlchemy
│   │   ├── schemas/           ✅ Schemas Pydantic
│   │   ├── repositories/      ✅ Repositorios
│   │   ├── services/          ✅ Servicios de lógica de negocio
│   │   └── routers/           ✅ Endpoints API
│   ├── pyproject.toml         ✅ Dependencias Poetry
│   ├── .env.example           ✅ Plantilla variables entorno
│   └── init_db.py             ✅ Script inicialización BD
│
└── frontend/                   ✅ Frontend React + Vite
    ├── src/
    │   ├── pages/             ✅ Páginas (Login, Aulas)
    │   ├── services/          ✅ Cliente API
    │   ├── context/           ✅ Contexto de autenticación
    │   ├── types/             ✅ Tipos TypeScript
    │   └── App.tsx            ✅ Componente raíz
    ├── package.json           ✅ Dependencias npm
    └── vite.config.ts         ✅ Configuración Vite
```

## Pasos Siguientes

### 1. Backend (FastAPI)

```bash
cd backend

# Ejecutar script de configuración automática
./setup.sh

# Levantar servidor
poetry run uvicorn app.main:app --reload --port 8000
```

**Verificar**:
- Swagger UI: http://localhost:8000/docs
- Health check: http://localhost:8000/health
- API docs: http://localhost:8000/redoc

### 2. Frontend (React + Vite)

```bash
cd frontend

# Ejecutar script de configuración automática
./setup.sh

# Levantar servidor
npm run dev
```

**Verificar**:
- Frontend: http://localhost:5173
- Login: usuario `admin` / contraseña `admin`
- CRUD Aulas completo

## Archivos Clave

### Backend

- `app/core/config.py` - Configuración central
- `app/core/security.py` - JWT y password hashing
- `app/models/aula.py` - Modelo de Aula
- `app/schemas/aula.py` - Schemas Pydantic
- `app/repositories/aula_repository.py` - Repositorio de Aula
- `app/services/aula_service.py` - Lógica de negocio
- `app/routers/aulas.py` - Endpoints CRUD de Aulas
- `app/routers/auth.py` - Endpoint de autenticación
- `app/main.py` - Punto de entrada FastAPI

### Frontend

- `src/types/index.ts` - Tipos TypeScript
- `src/services/api.ts` - Cliente API con axios
- `src/context/AuthContext.tsx` - Contexto de autenticación
- `src/pages/LoginPage.tsx` - Página de login
- `src/pages/AulasPage.tsx` - CRUD de Aulas
- `src/App.tsx` - App principal con rutas

## Validaciones Implementadas

### Backend
- ✅ Autenticación JWT con Bearer Token
- ✅ Validación de capacidad (0-255)
- ✅ Validación de nombre único
- ✅ PATCH para actualización parcial
- ✅ Protección de endpoints con token

### Frontend
- ✅ Login funcional con Material-UI
- ✅ Gestión de token en localStorage
- ✅ CRUD completo de Aulas
- ✅ Formularios con validaciones
- ✅ Confirmación en eliminación
- ✅ Manejo de errores con Alert

## Notas

- **Usuario hardcodeado**: Usuario `admin` con contraseña `admin` para pruebas
- **Base de datos**: SQLite para desarrollo (fácil migración a PostgreSQL)
- **UI Framework**: Material-UI v5
- **State Management**: React Context API
- **Routing**: React Router v6

---

**Estado**: Listo para Bloque 1 (Setup Inicial)
Fecha: 15 de febrero de 2026
Iteración 1: Auth + CRUD Aulas
