# pySigHor > editarCurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarCurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarCurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/editarCurso/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/cursos.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/cursos.py) · [services/curso_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/curso_service.py) · [repositories/curso_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/curso_repository.py) · [models/curso.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/curso.py)
- **Frontend:** [pages/CursosPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/CursosPage.tsx)



#### Secciones:

**Descripción**: 
Este caso de uso permite actualizar un curso existente.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/cursos.py`

**Implementación (snippets)**:
```python
@router.put("/cursos/{curso_id}", response_model=Curso)
def update_curso(curso_id: int, curso_data: dict, db: Session = Depends(get_db)):
    # Lógica de actualización
    return curso
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/CursosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X PUT "http://localhost:8000/api/v1/cursos/1" -H "Content-Type: application/json" -d '{"nombre": "Nombre Actualizado"}'
```
