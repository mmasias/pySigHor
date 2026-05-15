# pySigHor > eliminarRecurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarRecurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarRecurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/eliminarRecurso/README.md)|**Desarrollo**|Pruebas|

> |-|-|-|-|-|-|-|

- **Backend:** [routers/recursos.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/recursos.py) · [services/recurso_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/recurso_service.py) · [repositories/recurso_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/recurso_repository.py) · [models/recurso.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/recurso.py)
- **Frontend:** [pages/RecursosPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/RecursosPage.tsx)



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
