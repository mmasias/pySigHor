# pySigHor > abrirProgramas > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirProgramas/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirProgramas/README.md)|[Diseño](/RUP/02-diseño/casos-uso/abrirProgramas/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/programas.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/ProgramasPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite listar todos los programas disponibles.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/programas.py`
- **Endpoint:** `GET /api/v1/programas/`

**Implementación (snippets)**:
```python
@router.get('/', response_model=list[Programa])
def read_programas(db: Session = Depends(get_db)):
    return get_programas(db)
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/ProgramasPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X GET "http://localhost:8000/api/v1/programas/"
```
