# pySigHor > crearCurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearCurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearCurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/crearCurso/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/cursos.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/cursos.py) · [services/curso_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/curso_service.py) · [repositories/curso_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/curso_repository.py) · [models/curso.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/curso.py)
- **Frontend:** [pages/CursosPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/CursosPage.tsx)



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
