# pySigHor > crearPrograma > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearPrograma/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearPrograma/README.md)|[Diseño](/RUP/02-diseño/casos-uso/crearPrograma/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/programas.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/ProgramasPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite crear un nuevo programa.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/programas.py`
- **Schema (Programa)**: 
  - `nombre`: string (1-100), único
  - `descripcion`: string opcional
  - `activo`: bool (default True)

**Implementación (snippets)**:
```python
@router.post('/', response_model=Programa)
def create_programa_endpoint(programa: ProgramaCreate, db: Session = Depends(get_db)):
    # Validaciones y creación
    return create_programa(db, programa)
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/ProgramasPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X POST "http://localhost:8000/api/v1/programas/" -H "Content-Type: application/json" -d '{"nombre": "Programa Nuevo", "descripcion": "Desc"}'
```
