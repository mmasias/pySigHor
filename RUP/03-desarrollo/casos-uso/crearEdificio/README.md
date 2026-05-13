# pySigHor > crearEdificio > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearEdificio/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearEdificio/README.md)|[Diseño](/RUP/02-diseño/casos-uso/crearEdificio/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/edificios.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/EdificiosPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso se encarga de crear un nuevo edificio.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/edificios.py`
- **Schema (Edificio)**: 
  - `nombre`: string (1-50)
  - `direccion`: string opcional (max 100)

**Implementación (snippets)**:
```python
@router.post("/edificios", response_model=EdificioResponse, summary="Crea un nuevo edificio")
async def crear_edificio(edificio: EdificioRequest):
    if await EdificioModel.query.where(EdificioModel.nombre == edificio.nombre).gino.first():
        raise HTTPException(status_code=409, detail="Nombre de edificio ya existe")

    new_edificio = await EdificioModel.create(nombre=edificio.nombre, direccion=edificio.direccion)
    return EdificioResponse(**new_edificio.to_dict())
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/EdificiosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X POST "http://localhost:8000/api/v1/edificios" -H "Content-Type: application/json" -d '{"nombre": "Edificio A", "direccion": "Av. Principal 123"}'
```
