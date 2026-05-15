# pySigHor > abrirAulas > Desarrollo

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirAulas/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirAulas/README.md)|[Diseño](/RUP/02-diseño/casos-uso/abrirAulas/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/aulas.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/aulas.py) · [services/aula_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/aula_service.py) · [repositories/aula_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/aula_repository.py) · [models/aula.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/aula.py)
- **Frontend:** [pages/AulasPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/AulasPage.tsx)



## Descripción

Listado de todas las aulas del sistema con soporte para paginación. Permite visualizar todas las aulas existentes con sus datos completos.

## Estado

✅ **Completado** - Iteración 1

## Backend

### Endpoint

#### GET `/api/v1/aulas/`
Retorna lista paginada de aulas.

**Request:**
```http
Authorization: Bearer <token>
```

**Query Params:**
- `skip` (optional): Número de registros a saltar (default: 0)
- `limit` (optional): Número máximo de registros a retornar (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "nombre": "Aula 101",
    "capacidad": 40,
    "especial": false,
    "bloqueada": false,
    "id_edificio": null
  }
]
```

### Implementación

- **Capa de Router**: `backend/app/routers/aulas.py`
  - Endpoint decorado con `@router.get("/")`
  - Requiere autenticación vía `get_current_user()`
  - Llama a servicio `AulaService.listar_aulas()`

- **Capa de Servicio**: `backend/app/services/aula_service.py`
  - `listar_aulas(skip, limit)` retorna lista de modelos SQLAlchemy

- **Capa de Repositorio**: `backend/app/repositories/aula_repository.py`
  - `get_all(skip, limit)` ejecuta query SQL con paginación

- **Modelo**: `backend/app/models/aula.py`
  - `Aula` - Modelo SQLAlchemy con campos: id, nombre, capacidad, especial, bloqueada, id_edificio

- **Schema**: `backend/app/schemas/aula.py`
  - `AulaResponse` - Schema Pydantic con `orm_mode = True`

---

## Frontend

### Implementación

#### AulasPage (`AulasPage.tsx`)

**Componentes Material-UI:**
- `Table` - Tabla de aulas
- `TableHead` / `TableBody` - Estructura de tabla
- `TableCell` - Celdas de datos
- `IconButton` - Botones de acción (edit, delete)
- `Button` - Botón "Crear Nueva Aula"
- `Dialog` - Modal para crear/editar
- `Alert` - Notificaciones de éxito/error

**Estado React:**
- `aulas: Aula[]` - Lista de aulas
- `loading: boolean` - Estado de carga
- `error: string` - Mensaje de error
- `openDialog: boolean` - Control del modal
- `editingAula: Aula | null` - Aula being edited

**Efecto:**
```typescript
useEffect(() => {
  loadAulas();
}, []);
```

#### API Service (`api.ts`)

```typescript
listarAulas: async (skip = 0, limit = 100): Promise<Aula[]> => {
  const response = await apiClient.get(`/aulas?skip=${skip}&limit=${limit}`);
  return response.data;
}
```

**Autenticación:**
El interceptor de Axios agrega automáticamente `Authorization: Bearer <token>`

---

## Flujo de datos

1. Usuario navega a `/aulas`
2. `ProtectedRoute` verifica autenticación
3. `AulasPage` monta y ejecuta `useEffect`
4. `loadAulas()` llama a `aulaService.listarAulas()`
5. Axios hace GET a `/api/v1/aulas/` con Bearer token
6. Backend valida token y retorna lista de aulas
7. Aulas se muestran en tabla Material-UI

---

## Notas de implementación

### Backend
- **Paginación**: Implementada con `OFFSET` y `LIMIT` de SQL
- **Autenticación**: Todos los endpoints requieren token válido
- **Serialización**: Pydantic `orm_mode = True` convierte modelos SQLAlchemy a JSON

### Frontend
- **Carga inicial**: `useEffect` con array vacío se ejecuta una vez al montar
- **Manejo de errores**: Try-catch con `Alert` de Material-UI
- **Loading state**: Muestra texto "Cargando..." mientras fetchea

---

## Testing

### Backend
```bash
# Listar todas las aulas
curl -X GET 'http://localhost:8000/api/v1/aulas/' \
  -H 'Authorization: Bearer <token>'
```

### Frontend
1. Iniciar sesión
2. Navegar a "/Aulas" en menú (o http://localhost:5173/aulas)
3. Verificar que se muestra tabla con todas las aulas
4. Si no hay aulas, verificar que mensaje es apropiado

---

## Casos de prueba

- ✅ Listar aulas cuando existen registros
- ✅ Listar aulas cuando no hay registros (retorna array vacío)
- ✅ Acceder sin token retorna 401 Unauthorized
- ✅ Acceder con token inválido retorna 401
- ✅ Paginación funciona correctamente (skip, limit)

---

## Relacionados

- **crearAula** - POST `/api/v1/aulas/`
- **editarAula** - PATCH `/api/v1/aulas/{id}`
- **eliminarAula** - DELETE `/api/v1/aulas/{id}`
