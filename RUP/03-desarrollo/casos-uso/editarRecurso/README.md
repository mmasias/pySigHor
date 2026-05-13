# pySigHor > editarRecurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarRecurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarRecurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/editarRecurso/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/recursos.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/RecursosPage.tsx`, service en `api.ts`, types en `types/index.ts`

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
