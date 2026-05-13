# pySigHor > eliminarRecurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarRecurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarRecurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/eliminarRecurso/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/recursos.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/RecursosPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite eliminar un recurso.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/recursos.py`

**Implementación (snippets)**:
```python
@router.delete("/{recurso_id}")
def eliminar_recurso(recurso_id: int, db: Session = Depends(get_db)):
    # Lógica de eliminación
    return {"message": "Recurso eliminado"}
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/RecursosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X DELETE "http://localhost:8000/api/v1/recursos/1"
```
