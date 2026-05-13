# pySigHor > eliminarEdificio > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarEdificio/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarEdificio/README.md)|[Diseño](/RUP/02-diseño/casos-uso/eliminarEdificio/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/edificios.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/EdificiosPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso se encarga de eliminar un edificio.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/edificios.py`

**Implementación (snippets)**:
```python
@router.delete("/edificios/{id}", response_model=dict, summary="Elimina un edificio")
async def eliminar_edificio(id: int):
    existing_edificio = await EdificioModel.get_or_none(id=id)
    if not existing_edificio:
        raise HTTPException(status_code=404, detail="Edificio no encontrado")
    await existing_edificio.delete()
    return {"message": "Edificio eliminado con éxito"}
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/EdificiosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X DELETE "http://localhost:8000/api/v1/edificios/1"
```
