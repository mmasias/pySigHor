# pySigHor > eliminarAula > Desarrollo

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarAula/README.md)|[Diseño](/RUP/02-diseño/casos-uso/eliminarAula/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/aulas.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/aulas.py) · [services/aula_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/aula_service.py) · [repositories/aula_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/aula_repository.py) · [models/aula.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/aula.py)
- **Frontend:** [pages/AulasPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/AulasPage.tsx)



## Descripción

Eliminación de un aula existente del sistema. Elimina físicamente el registro de la base de datos.

## Estado

✅ **Completado** - Iteración 1

## Backend

### Endpoint

#### DELETE `/api/v1/aulas/{id}`
Elimina un aula existente.

**Request:**
```http
Authorization: Bearer <token>
```

**Response (204 No Content):**
```http
Status: 204 No Content
```

**Response (404 Not Found):**
```json
{
  "detail": "Aula con ID 999 no encontrada"
}
```

### Implementación

**Capa de Router:**
```python
@router.delete("/{aula_id}")
def eliminar_aula(aula_id: int, db: Session = Depends(get_db)):
    service.eliminar_aula(aula_id)
    return Response(status_code=204)
```

**Capa de Servicio:**
```python
def eliminar_aula(self, aula_id: int) -> None:
    # Obtener aula existente
    aula = repo.get_by_id(aula_id)
    if not aula:
        raise ValueError(f"Aula con ID {aula_id} no encontrada")

    # Eliminar
    repo.delete(aula)
```

**Capa de Repositorio:**
```python
def delete(self, aula: Aula) -> None:
    self.db.delete(aula)
    self.db.commit()
```

---

## Frontend

### Implementación

#### Botón de eliminar en tabla (`AulasPage.tsx`)

**Icono de eliminar:**
```tsx
<IconButton onClick={() => handleDeleteClick(aula)}>
  <DeleteIcon />
</IconButton>
```

#### Diálogo de confirmación

**Estado de confirmación:**
```typescript
const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
const [aulaToDelete, setAulaToDelete] = useState<Aula | null>(null);
```

**Manejo de clic en eliminar:**
```typescript
const handleDeleteClick = (aula: Aula) => {
  setAulaToDelete(aula);
  setDeleteDialogOpen(true);
};
```

**Diálogo de confirmación:**
```tsx
<Dialog open={deleteDialogOpen} onClose={() => setDeleteDialogOpen(false)}>
  <DialogTitle>Confirmar Eliminación</DialogTitle>
  <DialogContent>
    <DialogContentText>
      ¿Estás seguro de que deseas eliminar el aula "{aulaToDelete?.nombre}"?
      Esta acción no se puede deshacer.
    </DialogContentText>
  </DialogContent>
  <DialogActions>
    <Button onClick={() => setDeleteDialogOpen(false)}>Cancelar</Button>
    <Button onClick={handleDelete} color="error" variant="contained">
      Eliminar
    </Button>
  </DialogActions>
</Dialog>
```

**Manejo de eliminación:**
```typescript
const handleDelete = async () => {
  if (!aulaToDelete) return;

  try {
    await aulaService.eliminarAula(aulaToDelete.id);
    await loadAulas();  // Recargar lista
    setDeleteDialogOpen(false);
    setSuccessMessage('Aula eliminada exitosamente');
  } catch (error) {
    setErrorMessage('Error al eliminar aula');
  }
};
```

#### API Service
```typescript
eliminarAula: async (id: number): Promise<void> => {
  await apiClient.delete(`/aulas/${id}`);
}
```

---

## Flujo de datos

1. Usuario hace clic en icono de eliminar (🗑️) en tabla
2. `handleDeleteClick` guarda aula en estado y abre diálogo de confirmación
3. Dialog muestra: "¿Estás seguro de eliminar 'Aula 101'?"
4. Usuario puede:
   - Hacer clic en "Cancelar" → Dialog se cierra sin eliminar
   - Hacer clic en "Eliminar" → Procede con eliminación
5. `handleDelete` llama a `aulaService.eliminarAula()`
6. Service hace DELETE a `/aulas/{id}`
7. Backend valida que aula existe
8. Si existe, elimina registro de BD
9. Backend retorna 204 No Content
10. Frontend recarga lista de aulas
11. Dialog de confirmación se cierra
12. Alert muestra "Aula eliminada exitosamente"

---

## Notas de implementación

### Backend
- **204 No Content**: Código HTTP estándar para DELETE exitoso sin cuerpo
- **Eliminación física**: `db.delete()` elimina permanentemente (no soft delete)
- **Validación previa**: Verifica existencia antes de eliminar
- **Transacción**: SQLAlchemy hace commit automático

### Frontend
- **Confirmación obligatoria**: No elimina directamente, siempre pide confirmación
- **Dialog modal**: Evita eliminaciones accidentales
- **Mensaje descriptivo**: Muestra nombre del aula a eliminar
- **Botón rojo**: `color="error"` para acción destructiva
- **No rollback**: No hay función de "deshacer" después de eliminar

---

## Seguridad

### Validaciones
- ✅ **Autenticación requerida**: Token válido obligatorio
- ✅ **Verificación de existencia**: 404 si ID no existe
- ⚠️ **Sin autorización granular**: Cualquier usuario autenticado puede eliminar
- ⚠️ **Sin verificación de dependencias**: No verifica si el aula está en uso

### Mejoras futuras
- [ ] Verificar si el aula tiene horarios asignados
- [ ] Implementar soft delete (marcar como eliminado)
- [ ] Agregar autorización por roles
- [ ] Implementar "papelera de reciclaje"

---

## Testing

### Backend
```bash
# Eliminar aula existente
curl -X DELETE 'http://localhost:8000/api/v1/aulas/1' \
  -H 'Authorization: Bearer <token>'

# Intentar eliminar aula inexistente (debe retornar 404)
curl -X DELETE 'http://localhost:8000/api/v1/aulas/9999' \
  -H 'Authorization: Bearer <token>'

# Verificar que se eliminó (GET debe retornar 404)
curl -X GET 'http://localhost:8000/api/v1/aulas/1' \
  -H 'Authorization: Bearer <token>'
```

### Frontend
1. Ir a http://localhost:5173/aulas
2. Hacer clic en icono 🗑️ de un aula
3. Verificar que aparece diálogo de confirmación
4. Verificar que muestra nombre del aula
5. Hacer clic en "Cancelar"
6. Verificar que aula NO se eliminó
7. Hacer clic en 🗑️ nuevamente
8. Hacer clic en "Eliminar"
9. Verificar que aula desaparece de tabla
10. Verificar mensaje de éxito

---

## Casos de prueba

- ✅ Eliminar aula existente (retorna 204)
- ✅ Eliminar aula inexistente (retorna 404)
- ✅ Eliminar sin autenticación (retorna 401)
- ✅ Cancelar confirmación (no elimina)
- ✅ Confirmar eliminación (elimina correctamente)
- ✅ Lista actualizada después de eliminar

---

## Relacionados

- **abrirAulas** - GET `/api/v1/aulas/` (ver que desapareció de lista)
- **crearAula** - POST `/api/v1/aulas/` (crear nuevo si se arrepintió)
- **editarAula** - PATCH `/api/v1/aulas/{id}` (modificar en lugar de eliminar)

---

## Notas importantes

⚠️ **ADVERTENCIA**: Esta es una eliminación permanente. Los datos no pueden recuperarse después de eliminar.

📋 **RECOMENDACIÓN**: En producción, considerar:
1. Soft delete (campo `eliminado_en`)
2. Período de retención antes de eliminar permanentemente
3. Backup de datos antes de eliminación
4. Auditoría de eliminaciones (quién eliminó, cuándo)
