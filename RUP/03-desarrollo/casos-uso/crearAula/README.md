# pySigHor > crearAula > Desarrollo

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearAula/README.md)|[Diseño](/RUP/02-diseño/casos-uso/crearAula/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/aulas.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/aulas.py) · [services/aula_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/aula_service.py) · [repositories/aula_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/aula_repository.py) · [models/aula.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/aula.py)
- **Frontend:** [pages/AulasPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/AulasPage.tsx)



## Descripción

Creación de una nueva aula en el sistema. Valida que no exista un aula con el mismo nombre y que los datos cumplan con las restricciones definidas.

## Estado

✅ **Completado** - Iteración 1

## Backend

### Endpoint

#### POST `/api/v1/aulas/`
Crea una nueva aula.

**Request:**
```http
Authorization: Bearer <token>
Content-Type: application/json

{
  "nombre": "Aula 101",
  "capacidad": 30,
  "especial": false,
  "bloqueada": false,
  "id_edificio": null
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "nombre": "Aula 101",
  "capacidad": 30,
  "especial": false,
  "bloqueada": false,
  "id_edificio": null
}
```

**Response (400 Bad Request):**
```json
{
  "detail": "Ya existe un aula con el nombre 'Aula 101'"
}
```

### Validaciones

**AulaCreate Schema (`backend/app/schemas/aula.py`):**
- `nombre`: string, 1-50 caracteres, requerido
- `capacidad`: integer, 0-255, requerido
- `especial`: boolean, default false
- `bloqueada`: boolean, default false
- `id_edificio`: integer o null, opcional

### Implementación

**Capa de Router:**
```python
@router.post("/", response_model=AulaResponse)
def crear_aula(aula_data: AulaCreate, db: Session = Depends(get_db)):
    return service.crear_aula(aula_data)
```

**Capa de Servicio:**
```python
def crear_aula(self, aula_data: AulaCreate) -> Aula:
    # Validar nombre único
    existente = repo.get_by_nombre(aula_data.nombre)
    if existente:
        raise ValueError(f"Ya existe un aula con el nombre '{aula_data.nombre}'")

    # Crear aula
    return repo.create(aula_data.dict())
```

**Capa de Repositorio:**
```python
def create(self, aula_data: dict) -> Aula:
    db_aula = Aula(**aula_data)
    self.db.add(db_aula)
    self.db.commit()
    self.db.refresh(db_aula)
    return db_aula
```

---

## Frontend

### Implementación

#### Diálogo de Creación (`AulasPage.tsx`)

**Componente Dialog:**
```tsx
<Dialog open={openDialog} onClose={handleCloseDialog}>
  <DialogTitle>Crear Nueva Aula</DialogTitle>
  <DialogContent>
    <TextField
      label="Nombre"
      value={nombre}
      onChange={(e) => setNombre(e.target.value)}
      required
    />
    <TextField
      label="Capacidad"
      type="number"
      value={capacidad}
      onChange={(e) => setCapacidad(parseInt(e.target.value))}
      inputProps={{ min: 0, max: 255 }}
    />
    <FormControlLabel
      control={<Checkbox checked={especial} onChange={(e) => setEspecial(e.target.checked)} />}
      label="Es especial"
    />
    <FormControlLabel
      control={<Checkbox checked={bloqueada} onChange={(e) => setBloqueada(e.target.checked)} />}
      label="Bloqueada"
    />
  </DialogContent>
  <DialogActions>
    <Button onClick={handleCloseDialog}>Cancelar</Button>
    <Button onClick={handleCreate} variant="contained">Crear</Button>
  </DialogActions>
</Dialog>
```

**Manejo de creación:**
```typescript
const handleCreate = async () => {
  try {
    const newAula: AulaCreate = {
      nombre,
      capacidad,
      especial,
      bloqueada,
      id_edificio: null
    };

    await aulaService.crearAula(newAula);
    await loadAulas();  // Recargar lista
    handleCloseDialog();
    setSuccessMessage('Aula creada exitosamente');
  } catch (error) {
    setErrorMessage('Error al crear aula');
  }
};
```

#### API Service
```typescript
crearAula: async (aula: AulaCreate): Promise<Aula> => {
  const response = await apiClient.post('/aulas', aula);
  return response.data;
}
```

---

## Flujo de datos

1. Usuario hace clic en "Crear Nueva Aula"
2. Dialog se abre con campos vacíos
3. Usuario completa formulario:
   - Nombre (requerido, 1-50 chars)
   - Capacidad (requerido, 0-255)
   - Especial (opcional, checkbox)
   - Bloqueada (opcional, checkbox)
4. Usuario hace clic en "Crear"
5. `handleCreate` valida datos
6. `aulaService.crearAula()` hace POST con datos
7. Backend valida nombre único
8. Si válido, crea aula y retorna datos con ID
9. Frontend recarga lista de aulas
10. Dialog se cierra
11. Alert muestra "Aula creada exitosamente"

---

## Notas de implementación

### Backend
- **Nombre único**: Validado en servicio antes de insertar en BD
- **Transacción**: SQLAlchemy maneja commit automáticamente
- **Response code**: 201 Created para creación exitosa
- **Pydantic 1.x**: Usa `.dict()` en lugar de `.model_dump()`

### Frontend
- **Form validation**: Material-UI TextField con `required`
- **Input type**: Capacidad usa `type="number"` con min/max
- **Reset state**: Después de crear, formulario se limpia
- **Auto-refresh**: Lista se recarga automáticamente tras crear

---

## Testing

### Backend
```bash
# Crear aula válida
curl -X POST 'http://localhost:8000/api/v1/aulas/' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
    "nombre": "Aula 205",
    "capacidad": 45,
    "especial": true,
    "bloqueada": false
  }'

# Intentar crear duplicado (debe retornar 400)
curl -X POST 'http://localhost:8000/api/v1/aulas/' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{
    "nombre": "Aula 205",
    "capacidad": 30
  }'
```

### Frontend
1. Ir a http://localhost:5173/aulas
2. Hacer clic en "Crear Nueva Aula"
3. Llenar formulario con datos válidos
4. Hacer clic en "Crear"
5. Verificar que aparece en tabla
6. Intentar crear duplicado
7. Verificar mensaje de error

---

## Casos de prueba

- ✅ Crear aula con todos los campos válidos
- ✅ Crear aula con campos mínimos (nombre + capacidad)
- ✅ Crear aula con nombre duplicado retorna 400
- ✅ Validación de capacidad (0-255)
- ✅ Validación de nombre (1-50 caracteres)
- ✅ Valores por defecto (especial=false, bloqueada=false)

---

## Relacionados

- **abrirAulas** - GET `/api/v1/aulas/` (listar después de crear)
- **editarAula** - PATCH `/api/v1/aulas/{id}` (modificar)
- **eliminarAula** - DELETE `/api/v1/aulas/{id}` (borrar)
