# pySigHor > eliminarPrograma > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarPrograma/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarPrograma/README.md)|[Diseño](/RUP/02-diseño/casos-uso/eliminarPrograma/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/programas.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/programas.py) · [services/programa_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/programa_service.py) · [repositories/programa_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/programa_repository.py) · [models/programa.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/programa.py)
- **Frontend:** [pages/ProgramasPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/ProgramasPage.tsx)



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
