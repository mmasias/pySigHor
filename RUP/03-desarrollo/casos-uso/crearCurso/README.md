# pySigHor > crearCurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearCurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearCurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/crearCurso/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/cursos.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/CursosPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite crear un nuevo curso.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/cursos.py`
- **Schema (Curso)**: 
  - `nombre`: string (1-100)
  - `descripcion`: string opcional
  - `creditos`: int opcional (>=0)
  - `horas`: int opcional (>=0)
  - `id_programa`: int opcional

**Implementación (snippets)**:
```python
@router.post("/cursos", response_model=Curso)
def create_curso(curso: dict, db: Session = Depends(get_db)):
    # Validaciones y creación
    new_curso = Curso(**curso)
    db.add(new_curso)
    db.commit()
    return new_curso
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/CursosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X POST "http://localhost:8000/api/v1/cursos" -H "Content-Type: application/json" -d '{"nombre": "Curso X", "creditos": 4}'
```
