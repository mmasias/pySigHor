# pySigHor > editarAula > Desarrollo

<div align=right>

|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../../../../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../../../00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../../../00-casos-uso/02-detalle/editarAula/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../../../01-analisis/casos-uso/editarAula/README.md)|
|-:|
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../../../../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../../../conversation-log.md)|

</div>

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarAula/README.md)|[Diseño](/RUP/02-diseño/casos-uso/editarAula/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

## Descripción

Actualización de un aula existente. Permite modificar algunos o todos los campos del aula, validando que el nuevo nombre no coincida con otro aula existente.

## Estado

✅ **Completado** - Iteración 1

## Backend

### Archivo
- **Ruta**: `backend/app/routers/aulas.py`
- **Rama**: `diseño-fastapi-react`

### Endpoint

#### PATCH `/api/v1/aulas/{id}`
Actualiza un aula existente.

**Request:**
```http
Authorization: Bearer <token>
Content-Type: application/json

{
  "capacidad": 50
}
```

**Response (200 OK):**
```json
{
  "id": 1,
  "nombre": "Aula 101",
  "capacidad": 50,
  "especial": false,
  "bloqueada": false,
  "id_edificio": null
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Aula con ID 999 no encontrada"
}
```

**Response (400 Bad Request):**
```json
{
  "detail": "Ya existe un aula con el nombre 'Aula 102'"
}
```

### Validaciones

**AulaUpdate Schema (`backend/app/schemas/aula.py`):**
- Todos los campos son **opcionales**
- `nombre`: string, 1-50 caracteres (si se proporciona)
- `capacidad`: integer, 0-255 (si se proporciona)
- `especial`: boolean (si se proporciona)
- `bloqueada`: boolean (si se proporciona)
- `id_edificio`: integer o null (si se proporciona)

### Implementación

**Capa de Router:**
```python
@router.patch("/{aula_id}", response_model=AulaResponse)
def actualizar_aula(
    aula_id: int,
    aula_data: AulaUpdate,
    db: Session = Depends(get_db)
):
    return service.actualizar_aula(aula_id, aula_data)
```

**Capa de Servicio:**
```python
def actualizar_aula(self, aula_id: int, aula_data: AulaUpdate) -> Aula:
    # Obtener aula existente
    aula = repo.get_by_id(aula_id)
    if not aula:
        raise ValueError(f"Aula con ID {aula_id} no encontrada")

    # Si se actualiza el nombre, verificar que no exista
    if aula_data.nombre and aula_data.nombre != aula.nombre:
        existente = repo.get_by_nombre(aula_data.nombre)
        if existente:
            raise ValueError(f"Ya existe un aula con el nombre '{aula_data.nombre}'")

    # Actualizar solo campos proporcionados
    return repo.update(aula, aula_data.dict(exclude_unset=True))
```

**Capa de Repositorio:**
```python
def update(self, aula: Aula, aula_data: dict) -> Aula:
    for key, value in aula_data.items():
        setattr(aula, key, value)
    self.db.commit()
    self.db.refresh(aula)
    return aula
```

---

## Frontend

### Archivo
- **Página**: `frontend/src/pages/AulasPage.tsx`
- **Service**: `frontend/src/services/api.ts`
- **Types**: `frontend/src/types/index.ts`
- **Rama**: `diseño-fastapi-react`

### Implementación

#### Diálogo de Edición (`AulasPage.tsx`)

**Botón de editar en tabla:**
```tsx
<IconButton onClick={() => handleEdit(aula)}>
  <EditIcon />
</IconButton>
```

**Carga de datos en formulario:**
```typescript
const handleEdit = (aula: Aula) => {
  setEditingAula(aula);
  setNombre(aula.nombre);
  setCapacidad(aula.capacidad);
  setEspecial(aula.especial);
  setBloqueada(aula.bloqueada);
  setOpenDialog(true);
};
```

**Título condicional del diálogo:**
```tsx
<DialogTitle>
  {editingAula ? 'Editar Aula' : 'Crear Nueva Aula'}
</DialogTitle>
```

**Manejo de actualización:**
```typescript
const handleUpdate = async () => {
  if (!editingAula) return;

  try {
    const updatedAula: AulaUpdate = {
      nombre,
      capacidad,
      especial,
      bloqueada,
      id_edificio: null
    };

    await aulaService.actualizarAula(editingAula.id, updatedAula);
    await loadAulas();  // Recargar lista
    handleCloseDialog();
    setSuccessMessage('Aula actualizada exitosamente');
  } catch (error) {
    setErrorMessage('Error al actualizar aula');
  }
};
```

**Botón de acción condicional:**
```tsx
<Button onClick={editingAula ? handleUpdate : handleCreate} variant="contained">
  {editingAula ? 'Actualizar' : 'Crear'}
</Button>
```

#### API Service
```typescript
actualizarAula: async (id: number, aula: AulaUpdate): Promise<Aula> => {
  const response = await apiClient.patch(`/aulas/${id}`, aula);
  return response.data;
}
```

---

## Flujo de datos

1. Usuario hace clic en icono de editar (✏️) en tabla
2. `handleEdit` carga datos del aula en estado del formulario
3. Dialog se abre con título "Editar Aula"
4. Usuario modifica campos deseados
5. Usuario hace clic en "Actualizar"
6. `handleUpdate` llama a `aulaService.actualizarAula()`
7. Service hace PATCH con solo campos modificados
8. Backend valida:
   - Aula existe
   - Nombre único (si se modifica)
9. Si válido, actualiza aula y retorna datos actualizados
10. Frontend recarga lista de aulas
11. Dialog se cierra
12. Alert muestra "Aula actualizada exitosamente"

---

## Notas de implementación

### Backend
- **PATCH vs PUT**: PATCH permite actualizaciones parciales
- **exclude_unset=True**: Solo actualiza campos proporcionados
- **Validación de nombre**: Solo si el nombre cambia
- **SQLAlchemy UPDATE**: Usa `setattr()` para actualizar campos dinámicamente

### Frontend
- **Mismo formulario**: Reutiliza Dialog para crear y editar
- **Estado editingAula**: null = crear, objeto = editar
- **Carga de datos**: Al abrir edición, formulario se pre-llena
- **Botón condicional**: Cambia texto entre "Crear" y "Actualizar"

---

## Diferencias con crearAula

| Aspecto | crearAula | editarAula |
|---------|-----------|------------|
| Método | POST | PATCH |
| Endpoint | `/aulas/` | `/aulas/{id}` |
| Campos | Todos requeridos | Todos opcionales |
| Validación nombre | Único global | Único (excluyendo self) |
| Código respuesta | 201 Created | 200 OK |

---

## Testing

### Backend
```bash
# Actualizar capacidad
curl -X PATCH 'http://localhost:8000/api/v1/aulas/1' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"capacidad": 60}'

# Actualizar nombre
curl -X PATCH 'http://localhost:8000/api/v1/aulas/1' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"nombre": "Aula 101-A"}'

# Actualizar nombre a uno existente (debe retornar 400)
curl -X PATCH 'http://localhost:8000/api/v1/aulas/1' \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"nombre": "Aula 102"}'
```

### Frontend
1. Ir a http://localhost:5173/aulas
2. Hacer clic en icono ✏️ de un aula
3. Verificar que Dialog se abre con datos precargados
4. Modificar capacidad
5. Hacer clic en "Actualizar"
6. Verificar que tabla muestra valor actualizado
7. Intentar cambiar nombre a uno existente
8. Verificar mensaje de error

---

## Casos de prueba

- ✅ Actualizar un campo (capacidad)
- ✅ Actualizar múltiples campos
- ✅ Actualizar aula inexistente retorna 404
- ✅ Actualizar nombre a uno existente retorna 400
- ✅ Actualizar nombre a su mismo valor (no error)
- ✅ Actualización sin cambios (PATCH vacío)

---

## Relacionados

- **abrirAulas** - GET `/api/v1/aulas/` (ver actualizado en lista)
- **crearAula** - POST `/api/v1/aulas/` (crear nuevo)
- **eliminarAula** - DELETE `/api/v1/aulas/{id}` (borrar)
