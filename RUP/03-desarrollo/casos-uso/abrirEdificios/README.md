# pySigHor > abrirEdificios > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirEdificios/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirEdificios/README.md)|[Diseño](/RUP/02-diseño/casos-uso/abrirEdificios/README.md)|**Desarrollo**|Pruebas|

> |-|-|-|-|-|-|-|

- **Backend:** [routers/edificios.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/edificios.py) · [services/edificio_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/edificio_service.py) · [repositories/edificio_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/edificio_repository.py) · [models/edificio.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/edificio.py)
- **Frontend:** [pages/EdificiosPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/EdificiosPage.tsx)



#### Secciones:

**Descripción**: 
Este caso de uso se encarga de listar todos los edificios existentes en la base de datos.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/edificios.py`
- **Endpoint:**
  ```python
  @router.get("/edificios", response_model=list[EdificioResponse], summary="Obtiene todos los edificios")
  async def obtener_edificios():
      edificios = await EdificioModel.query.gino.all()
      return [EdificioResponse(**edificio.to_dict()) for edificio in edificios]
  ```

**Validaciones**: 
- No hay validaciones adicionales necesarias para este endpoint.

**Implementación (snippets)**:
```python
from fastapi import APIRouter, Depends
from backend.app.models.edificio_model import Edificio as EdificioModel
from backend.app.schemas.edificio_schema import EdificioResponse

router = APIRouter()

@router.get("/edificios", response_model=list[EdificioResponse], summary="Obtiene todos los edificios")
async def obtener_edificios():
    edificios = await EdificioModel.query.gino.all()
    return [EdificioResponse(**edificio.to_dict()) for edificio in edificios]
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/EdificiosPage.tsx`

**Flujo de datos**: 
- **API:** GET /api/v1/edificios

**Testing (curl + pasos frontend)**:
```bash
curl -X GET "http://localhost:8000/api/v1/edificios"
```
- En la interfaz del usuario, se verifica que la lista de edificios sea renderizada correctamente.
