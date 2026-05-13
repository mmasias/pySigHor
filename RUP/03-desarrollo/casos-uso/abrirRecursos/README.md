# pySigHor > abrirRecursos > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirRecursos/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirRecursos/README.md)|[Diseño](/RUP/02-diseño/casos-uso/abrirRecursos/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/recursos.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/RecursosPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite visualizar detalles de un recurso.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/recursos.py`
- **Endpoint:** `GET /api/v1/recursos/{recurso_id}`

**Implementación (snippets)**:
```python
@router.get("/{recurso_id}", response_model=RecursosResponse)
def abrir_recurso(recurso_id: int, db: Session = Depends(get_db)):
    recurso = db.query(Recurso).filter(Recurso.id == recurso_id).first()
    return recurso
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/RecursosPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X GET "http://localhost:8000/api/v1/recursos/1"
```
