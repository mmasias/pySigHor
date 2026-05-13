# pySigHor > editarPrograma > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarPrograma/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarPrograma/README.md)|[Diseño](/RUP/02-diseño/casos-uso/editarPrograma/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/programas.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/ProgramasPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite actualizar un programa existente.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/programas.py`

**Implementación (snippets)**:
```python
@router.patch('/{id}', response_model=Programa)
def update_programa_endpoint(id: int, programa: ProgramaUpdate, db: Session = Depends(get_db)):
    return update_programa(db, id, programa)
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/ProgramasPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X PATCH "http://localhost:8000/api/v1/programas/1" -H "Content-Type: application/json" -d '{"nombre": "Nombre Actualizado"}'
```
