# pySigHor > editarEdificio > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarEdificio/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarEdificio/README.md)|[Diseño](/RUP/02-diseño/casos-uso/editarEdificio/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/edificios.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/EdificiosPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso se encarga de editar un edificio existente.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/edificios.py`
- **Schema (Edificio)**: 
  - `nombre`: string (1-50)
  - `direccion`: string opcional (max 100)

**Implementación (snippets)**:
```python
@router.patch("/edificios/{id}", response_model=EdificioResponse, summary="Actualiza parcialmente un edificio")
async def actualizar_edificio(id: int, edificio: EdificioRequest):
    existing_edificio = await EdificioModel.get(id)
    if not existing_edificio:
        raise HTTPException(status_code=404, detail="Edificio no encontrado")
    # ... lógica de update ...
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/EdificiosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X PATCH "http://localhost:8000/api/v1/edificios/1" -H "Content-Type: application/json" -d '{"nombre": "Edificio A Modificado"}'
```
