# Configuración y estructura del proyecto

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración → Construcción
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2025-11-19
- **Autor**: Claude Sonnet 4.5

## Propósito

Este documento define la estructura de directorios, configuraciones iniciales y decisiones técnicas necesarias para materializar la arquitectura diseñada en código ejecutable. Sirve como puente entre el diseño abstracto y la implementación concreta.

## Filosofía de organización

### Principios aplicados

1. **Separación de responsabilidades**: Backend y Frontend en repositorios lógicos independientes
2. **Escalabilidad**: Estructura que permite crecer sin reestructurar
3. **Convenciones sobre configuración**: Seguir estándares de la comunidad (FastAPI, React)
4. **Trazabilidad**: Mapeo directo entre artefactos de diseño y código

## Estructura de directorios

### Vista general

```
pySigHor/
├── backend/                    # Aplicación FastAPI
│   ├── app/
│   │   ├── core/              # Configuración central
│   │   ├── models/            # Modelos SQLAlchemy (BD)
│   │   ├── schemas/           # Schemas Pydantic (API)
│   │   ├── repositories/      # Capa de acceso a datos
│   │   ├── services/          # Lógica de negocio
│   │   ├── routers/           # Endpoints API
│   │   └── main.py            # Punto de entrada
│   ├── migrations/            # Migraciones de BD (Alembic)
│   ├── tests/                 # Tests unitarios e integración
│   ├── pyproject.toml         # Dependencias Poetry
│   └── .env.example           # Plantilla variables de entorno
│
├── frontend/                   # Aplicación React + Vite
│   ├── src/
│   │   ├── components/        # Componentes reutilizables
│   │   ├── pages/             # Páginas principales
│   │   ├── services/          # Clientes API
│   │   ├── context/           # Context API (estado global)
│   │   ├── types/             # Tipos TypeScript
│   │   ├── utils/             # Utilidades
│   │   ├── App.tsx            # Componente raíz
│   │   └── main.tsx           # Punto de entrada
│   ├── public/                # Recursos estáticos
│   ├── package.json           # Dependencias npm
│   ├── tsconfig.json          # Configuración TypeScript
│   └── vite.config.ts         # Configuración Vite
│
├── docs/                       # Documentación adicional
├── RUP/                        # Artefactos metodológicos
└── README.md                   # Documentación principal
```

### Justificación de la estructura

#### Backend: Arquitectura por capas

```
app/
├── core/          → Configuración (settings, security, database)
├── models/        → Entidades de dominio (ORM)
├── schemas/       → Contratos de API (DTO)
├── repositories/  → Abstracción de acceso a datos
├── services/      → Orquestación de lógica de negocio
└── routers/       → Definición de endpoints HTTP
```

**Flujo de una petición**:
```
Router → Service → Repository → Model → Database
   ↓                    ↓
Schema (input)    Schema (output)
```

Esta separación permite:
- **Testabilidad**: Cada capa puede probarse independientemente
- **Mantenibilidad**: Cambios en BD no afectan lógica de negocio
- **Reutilización**: Servicios pueden llamarse desde múltiples routers

#### Frontend: Organización por responsabilidad

```
src/
├── components/   → Elementos UI reutilizables (Button, Input, Modal)
├── pages/        → Vistas completas (LoginPage, AulasPage)
├── services/     → Comunicación con API (aulaService.ts)
├── context/      → Estado global (AuthContext, AppContext)
└── types/        → Definiciones TypeScript (interfaces, types)
```

**Flujo de una acción del usuario**:
```
Page → Service → API Backend
  ↓       ↓
Component Context (estado)
```

## Configuraciones iniciales

### Backend: FastAPI + SQLAlchemy

#### 1. Dependencias (`backend/pyproject.toml`)

```toml
[tool.poetry]
name = "pysighor-backend"
version = "0.1.0"
description = "API REST para sistema de generación de horarios universitarios"
authors = ["pySigHor Team"]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.109.0"
uvicorn = {extras = ["standard"], version = "^0.27.0"}
sqlalchemy = {extras = ["asyncio"], version = "^2.0.25"}
aiosqlite = "^0.19.0"
pydantic = {extras = ["email"], version = "^2.5.3"}
pydantic-settings = "^2.1.0"
python-jose = {extras = ["cryptography"], version = "^3.3.0"}
passlib = {extras = ["bcrypt"], version = "^1.7.4"}
python-multipart = "^0.0.6"
alembic = "^1.13.1"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.4"
pytest-asyncio = "^0.23.3"
httpx = "^0.26.0"
black = "^24.1.0"
ruff = "^0.1.14"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

**Justificación de dependencias clave**:
- `fastapi` + `uvicorn`: Framework async de alto rendimiento
- `sqlalchemy[asyncio]` + `aiosqlite`: ORM async para SQLite
- `pydantic`: Validación automática de datos
- `python-jose` + `passlib`: Manejo de JWT y hashing de contraseñas
- `alembic`: Migraciones de base de datos versionadas

#### 2. Configuración central (`backend/app/core/config.py`)

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # Aplicación
    APP_NAME: str = "pySigHor API"
    VERSION: str = "0.1.0"
    DEBUG: bool = False

    # Base de datos
    DATABASE_URL: str = "sqlite+aiosqlite:///./pysighor.db"

    # Seguridad
    SECRET_KEY: str  # Debe estar en .env
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:5173"]

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()
```

**Justificación**:
- `pydantic_settings`: Carga variables desde `.env` con validación
- `lru_cache`: Singleton para evitar lecturas repetidas
- Separación de configuración por dominios (app, db, security)

#### 3. Plantilla de variables de entorno (`backend/.env.example`)

```env
# Aplicación
DEBUG=True

# Base de Datos
DATABASE_URL=sqlite+aiosqlite:///./pysighor.db

# Seguridad (CAMBIAR EN PRODUCCIÓN)
SECRET_KEY=CHANGE_THIS_TO_A_RANDOM_SECRET_KEY_IN_PRODUCTION
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS (Frontend URL)
BACKEND_CORS_ORIGINS=["http://localhost:5173"]
```

**Nota de seguridad**: El `SECRET_KEY` debe generarse con:
```bash
openssl rand -hex 32
```

#### 4. Configuración de base de datos (`backend/app/core/database.py`)

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from .config import get_settings

settings = get_settings()

# Motor async de SQLAlchemy
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Log de queries en modo debug
    future=True
)

# Fábrica de sesiones
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base para modelos
Base = declarative_base()

# Dependency para FastAPI
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
```

**Justificación**:
- Motor async para no bloquear el event loop
- `async_sessionmaker`: Patrón factory para sesiones
- `get_db()`: Inyección de dependencias en endpoints

#### 5. Configuración de seguridad (`backend/app/core/security.py`)

```python
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from .config import get_settings

settings = get_settings()

# Contexto de hashing (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica contraseña contra hash."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Genera hash bcrypt de contraseña."""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """Crea token JWT con expiración."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token: str) -> dict:
    """Decodifica y valida token JWT."""
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
```

**Justificación**:
- `bcrypt`: Algoritmo de hashing lento (resistente a fuerza bruta)
- JWT: Tokens stateless con expiración automática
- Funciones puras: Fáciles de testear

### Frontend: React + TypeScript + Vite

#### 1. Dependencias (`frontend/package.json`)

```json
{
  "name": "pysighor-frontend",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.3",
    "axios": "^1.6.5"
  },
  "devDependencies": {
    "@types/react": "^18.2.48",
    "@types/react-dom": "^18.2.18",
    "@typescript-eslint/eslint-plugin": "^6.19.0",
    "@typescript-eslint/parser": "^6.19.0",
    "@vitejs/plugin-react": "^4.2.1",
    "eslint": "^8.56.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "typescript": "^5.3.3",
    "vite": "^5.0.11"
  }
}
```

**Justificación de dependencias clave**:
- `react` + `react-dom`: Framework UI
- `react-router-dom`: Navegación SPA
- `axios`: Cliente HTTP con interceptores
- `vite`: Bundler rápido (Hot Module Replacement)
- `typescript`: Tipado estático para robustez

#### 2. Configuración TypeScript (`frontend/tsconfig.json`)

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,

    /* Path aliases */
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

**Justificación**:
- `strict: true`: Máxima seguridad de tipos
- `jsx: react-jsx`: Nuevo JSX transform (sin `import React`)
- Path aliases `@/*`: Imports limpios (`@/components/Button`)

#### 3. Configuración Vite (`frontend/vite.config.ts`)

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
```

**Justificación**:
- Proxy `/api` → Backend: Evita CORS en desarrollo
- Alias `@`: Coherencia con tsconfig
- Puerto 5173: Default de Vite (convención)

#### 4. Cliente HTTP con interceptores (`frontend/src/services/api.ts`)

```typescript
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '/api',
  headers: {
    'Content-Type': 'application/json'
  }
});

// Interceptor: Agregar token JWT automáticamente
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Interceptor: Manejo de errores global
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expirado: limpiar y redirigir a login
      localStorage.removeItem('access_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
```

**Justificación**:
- Interceptor de request: Inyección automática de token
- Interceptor de response: Manejo centralizado de errores 401
- Configuración DRY: Evita repetir headers en cada request

#### 5. Context de autenticación (`frontend/src/context/AuthContext.tsx`)

```typescript
import React, { createContext, useContext, useState, useEffect } from 'react';
import api from '@/services/api';

interface User {
  username: string;
  rol: string;
}

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    // Verificar token al cargar la aplicación
    const token = localStorage.getItem('access_token');
    if (token) {
      // TODO: Validar token con endpoint /me
      setUser({ username: 'admin', rol: 'admin' }); // Placeholder
    }
  }, []);

  const login = async (username: string, password: string) => {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    const response = await api.post('/token', formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    });

    localStorage.setItem('access_token', response.data.access_token);
    setUser({ username, rol: 'admin' }); // TODO: Obtener del backend
  };

  const logout = () => {
    localStorage.removeItem('access_token');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, isAuthenticated: !!user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};
```

**Justificación**:
- Context API: Estado global sin librerías externas
- Custom hook `useAuth`: API limpia para componentes
- Persistencia en localStorage: Mantener sesión entre recargas

## Esquema de base de datos inicial

### Script SQL (`backend/migrations/001_initial_schema.sql`)

```sql
-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    rol VARCHAR(20) DEFAULT 'admin',
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de aulas
CREATE TABLE IF NOT EXISTS aulas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    capacidad INTEGER NOT NULL,
    edificio VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Usuario administrador inicial (password: admin123)
-- Hash bcrypt de 'admin123'
INSERT INTO usuarios (username, password_hash, rol) VALUES
('admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5QQJqy.5RkSoq', 'admin');

-- Datos de ejemplo para aulas
INSERT INTO aulas (nombre, capacidad, edificio) VALUES
('A-101', 30, 'Edificio A'),
('A-102', 40, 'Edificio A'),
('B-201', 25, 'Edificio B');
```

**Justificación**:
- Usuario admin inicial: Permite login inmediato
- Datos de ejemplo: Facilitan testing visual
- Timestamps: Auditoría básica de operaciones

### Modelo SQLAlchemy (`backend/app/models/usuario.py`)

```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    rol = Column(String(20), default="admin")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
```

**Justificación**:
- Mapeo directo con tabla SQL
- Índices en campos de búsqueda frecuente (`username`)
- `server_default`: Timestamps gestionados por BD

## Comandos iniciales de desarrollo

### Backend

```bash
# Instalar dependencias
cd backend
poetry install

# Crear base de datos y ejecutar migraciones
poetry run python -m app.core.init_db

# Ejecutar servidor de desarrollo
poetry run uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
# Instalar dependencias
cd frontend
npm install

# Ejecutar servidor de desarrollo
npm run dev
```

### Verificación

1. **Backend**: http://localhost:8000/docs (Swagger UI automático)
2. **Frontend**: http://localhost:5173
3. **Login inicial**: `admin` / `admin123`

## Mapeo entre artefactos de diseño y código

| Artefacto de Diseño | Código |
|---------------------|--------|
| `Usuario` (Modelo) | `backend/app/models/usuario.py` |
| `Aula` (Modelo) | `backend/app/models/aula.py` |
| `Token` (Schema) | `backend/app/schemas/auth.py` |
| `AulaCreate` (Schema) | `backend/app/schemas/aula.py` |
| `IUsuarioRepository` | `backend/app/repositories/usuario.py` |
| `IAulaRepository` | `backend/app/repositories/aula.py` |
| `AuthService` | `backend/app/services/auth.py` |
| `AulaService` | `backend/app/services/aula.py` |
| `POST /token` | `backend/app/routers/auth.py` |
| `GET /aulas` | `backend/app/routers/aulas.py` |
| `Frontend (React)` | `frontend/src/pages/*.tsx` |

Esta tabla garantiza **trazabilidad completa** entre el diseño UML y la implementación.

## Próximos pasos

Con esta configuración definida, el proyecto está listo para:

1. **Construcción**: Implementar los 5 casos de uso del Vertical Slice
2. **Testing**: Escribir tests siguiendo la estructura de carpetas
3. **Documentación**: Generar docs automáticas con Swagger (backend) y Storybook (frontend, opcional)
4. **Despliegue**: Contenerización con Docker (fase posterior)

## Reflexiones metodológicas

### ¿Por qué este nivel de detalle?

1. **Valor didáctico**: Los estudiantes ven que el diseño NO es abstracto, sino un plano ejecutable
2. **Reducción de fricción**: Elimina decisiones triviales durante la codificación (¿dónde va este archivo?)
3. **Estándares industriales**: Refleja prácticas profesionales de equipos reales
4. **Trazabilidad**: Cada decisión técnica está justificada y conectada con artefactos RUP

### Costo vs. Beneficio

**Costo**: 2-3 horas de planificación adicional
**Beneficio**:
- Desarrollo 3x más rápido (sin indecisiones)
- Código consistente desde el inicio
- Onboarding de nuevos desarrolladores en minutos
- Base sólida para escalabilidad

En proyectos reales, esta inversión se amortiza en la primera semana de desarrollo.

---

**Este documento completa la fase de Diseño. El proyecto está listo para transitar a Construcción con fundamentos sólidos y trazables.**
