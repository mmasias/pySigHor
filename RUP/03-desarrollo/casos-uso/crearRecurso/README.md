# pySigHor > crearRecurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearRecurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearRecurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/crearRecurso/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/recursos.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/recursos.py) · [services/recurso_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/recurso_service.py) · [repositories/recurso_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/recurso_repository.py) · [models/recurso.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/recurso.py)
- **Frontend:** [pages/RecursosPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/RecursosPage.tsx)



#### Secciones:

**Descripción**: 
Este caso de uso permite crear un nuevo recurso.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/recursos.py`
- **Schema (Recurso)**: 
  - `nombre`: string (1-100)
  - `descripcion`: string opcional

**Implementación (snippets)**:
```python
@router.post("/", response_model=RecursosResponse)
def crear_recurso(nuevo_recurso: RecursosCreate, db: Session = Depends(get_db)):
    recurso = Recurso(**nuevo_recurso.dict())
    db.add(recurso)
    db.commit()
    return recurso
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/RecursosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X POST "http://localhost:8000/api/v1/recursos" -H "Content-Type: application/json" -d '{"nombre": "Recurso 1", "descripcion": "Desc"}'
```
