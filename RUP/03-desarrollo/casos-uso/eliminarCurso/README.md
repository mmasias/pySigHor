# pySigHor > eliminarCurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarCurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarCurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/eliminarCurso/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/cursos.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/cursos.py) · [services/curso_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/curso_service.py) · [repositories/curso_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/curso_repository.py) · [models/curso.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/curso.py)
- **Frontend:** [pages/CursosPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/CursosPage.tsx)



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
