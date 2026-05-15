# pySigHor > editarRecurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarRecurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarRecurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/editarRecurso/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/recursos.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/recursos.py) · [services/recurso_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/recurso_service.py) · [repositories/recurso_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/recurso_repository.py) · [models/recurso.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/recurso.py)
- **Frontend:** [pages/RecursosPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/RecursosPage.tsx)



#### Secciones:

**Descripción**: 
Este caso de uso permite actualizar un recurso existente.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/recursos.py`

**Implementación (snippets)**:
```python
@router.put("/{recurso_id}", response_model=RecursosResponse)
def editar_recurso(recurso_id: int, nuevo_recurso: RecursosCreate, db: Session = Depends(get_db)):
    # Lógica de actualización
    return recurso
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/RecursosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X PUT "http://localhost:8000/api/v1/recursos/1" -H "Content-Type: application/json" -d '{"nombre": "Nombre Editado"}'
```
