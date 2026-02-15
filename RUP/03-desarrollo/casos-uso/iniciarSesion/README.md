# pySigHor > iniciarSesion > Desarrollo

<div align=right>

|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../../../../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../../../00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../../../00-casos-uso/02-detalle/iniciarSesion/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../../../01-analisis/casos-uso/iniciarSesion/README.md)|
|-:|
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../../../../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../../../conversation-log.md)|

</div>

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/iniciarSesion/README.md)|[Análisis](/RUP/01-analisis/casos-uso/iniciarSesion/README.md)|[Diseño](/RUP/02-diseño/casos-uso/iniciarSesion/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

## Descripción

Autenticación de usuarios mediante JWT (JSON Web Tokens) con OAuth2PasswordBearer. El sistema valida credenciales y genera un token que se utiliza para acceder a los endpoints protegidos.

## Estado

✅ **Completado** - Iteración 1

## Backend

### Archivo
- **Ruta**: `backend/app/routers/auth.py`
- **Rama**: `diseño-fastapi-react`

### Endpoints

#### POST `/api/v1/auth/login`
Autentica usuario y retorna token JWT.

**Request:**
```http
Content-Type: application/x-www-form-urlencoded

username=admin&password=admin
```

**Response:**
```json
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer"
}
```

#### POST `/api/v1/auth/verify-token`
Verifica si un token es válido.

**Request:**
```http
Authorization: Bearer <token>
```

**Response:**
```json
{
  "username": "admin"
}
```

### Implementación

- **Framework**: FastAPI 0.100.1
- **Autenticación**: OAuth2PasswordBearer con JWT
- **Algoritmo**: HS256
- **Expiración**: 30 minutos
- **Password hashing**: Bcrypt 3.2.2 (cost factor 12)
- **Usuario hardcodeado**:
  - Username: `admin`
  - Password: `admin`
  - Hash: `$2b$12$/cpgJO5lA7gtvYHWHxLcgePFZ0HL35bUdnQ2nzYf7dKcWyRVjS7ym`

### Archivos relacionados
- `backend/app/core/security.py` - Funciones de hash y verificación
- `backend/app/core/config.py` - Configuración de JWT
- `backend/app/main.py` - Configuración de CORS y rutas

---

## Frontend

### Archivo
- **Página**: `frontend/src/pages/LoginPage.tsx`
- **Context**: `frontend/src/context/AuthContext.tsx`
- **Service**: `frontend/src/services/api.ts`
- **Rama**: `diseño-fastapi-react`

### Implementación

- **Framework**: React 18 + TypeScript 5
- **UI**: Material-UI v5
- **Router**: React Router v6
- **HTTP Client**: Axios

#### LoginPage (`LoginPage.tsx`)
- Formulario con campos username/password
- Manejo de errores con alertas
- Redirección automática a `/aulas` tras login exitoso

#### AuthContext (`AuthContext.tsx`)
- Context API para gestión de estado de autenticación
- Almacena token y usuario en `localStorage`
- Proporciona funciones `login()`, `logout()`, `isAuthenticated`

#### API Service (`api.ts`)
- Configuración de Axios con interceptor Bearer token
- Función `authService.login()` que envía datos como `application/x-www-form-urlencoded`

### Flujo de autenticación

1. Usuario ingresa credenciales en formulario
2. `LoginPage` llama a `authService.login(username, password)`
3. Service hace POST a `/api/v1/auth/login` con datos form-urlencoded
4. Backend valida y retorna `{ access_token, token_type }`
5. Token se guarda en `localStorage`
6. Context actualiza estado `isAuthenticated = true`
7. Usuario redirigido a `/aulas`
8. Axios interceptor agrega `Authorization: Bearer <token>` a todas las peticiones siguientes

---

## Notas de implementación

### Backend
- **Compatibility Issue**: FastAPI 0.100.1 requiere Pydantic 1.x (no 2.x)
- **Bcrypt**: Versión 3.2.2 requerida para compatibilidad con passlib 1.7.4
- **CORS**: Configurado para permitir `http://localhost:5173`

### Frontend
- **OAuth2 Form**: Requiere `URLSearchParams` (no `FormData`) para compatibility con FastAPI
- **Protected Routes**: Componente `ProtectedRoute` verifica `isAuthenticated` antes de renderizar
- **Token Persistence**: Token guardado en localStorage persiste entre sesiones

---

## Testing

### Backend
```bash
# Login
curl -X POST 'http://localhost:8000/api/v1/auth/login' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=admin&password=admin'

# Verify token
curl -X POST 'http://localhost:8000/api/v1/auth/verify-token' \
  -H 'Authorization: Bearer <token>'
```

### Frontend
1. Abrir http://localhost:5173
2. Ingresar username: `admin`, password: `admin`
3. Verificar redirección a `/aulas`
4. Verificar token en `localStorage` (DevTools → Application → Local Storage)

---

## Próximos pasos

- [ ] Implementar refresh tokens
- [ ] Implementar logout en backend (invalidar token)
- [ ] Agregar "recuerdame" (remember me)
- [ ] Implementar recuperación de contraseña
- [ ] Mover usuarios hardcodeados a base de datos
