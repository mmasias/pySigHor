# pySigHor > eliminarCurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarCurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarCurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/eliminarCurso/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/cursos.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/CursosPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite eliminar un curso.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/cursos.py`

**Implementación (snippets)**:
```python
@router.delete("/cursos/{curso_id}", response_model=dict)
def delete_curso(curso_id: int, db: Session = Depends(get_db)):
    # Lógica de eliminación
    return {"message": "Curso eliminado correctamente"}
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/CursosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X DELETE "http://localhost:8000/api/v1/cursos/1"
```
