# pySigHor > eliminarPrograma > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarPrograma/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarPrograma/README.md)|[Diseño](/RUP/02-diseño/casos-uso/eliminarPrograma/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/programas.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/ProgramasPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite eliminar un programa.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/programas.py`

**Implementación (snippets)**:
```python
@router.delete('/{id}', response_model=dict)
def delete_programa_endpoint(id: int, db: Session = Depends(get_db)):
    return delete_programa(db, id)
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/ProgramasPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X DELETE "http://localhost:8000/api/v1/programas/1"
```
