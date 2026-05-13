# pySigHor > abrirCursos > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirCursos/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirCursos/README.md)|[Diseño](/RUP/02-diseño/casos-uso/abrirCursos/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/cursos.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/CursosPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite listar los cursos disponibles.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/cursos.py`
- **Endpoint:** `GET /api/v1/cursos`

**Implementación (snippets)**:
```python
@router.get("/cursos", response_model=list[Curso])
def read_cursos(db: Session = Depends(get_db)):
    cursos = db.query(Curso).all()
    return cursos
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/CursosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X GET "http://localhost:8000/api/v1/cursos"
```
