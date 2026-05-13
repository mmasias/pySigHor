# pySigHor > crearProfesor > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearProfesor/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearProfesor/README.md)|[Diseño](/RUP/02-diseño/casos-uso/crearProfesor/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/profesores.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/ProfesoresPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite crear un nuevo profesor.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/profesores.py`
- **Schema (Profesor)**: 
  - `nombres`: string (1-100)
  - `apellidos`: string (1-100)
  - `correo`: string opcional (max 150)
  - `telefono`: string opcional (max 20)
  - `observaciones`: string opcional
  - *NOTA: No se incluye el campo 'nombre'.*

**Implementación (snippets)**:
```python
@router.post("/profesores", response_model=ProfesorResponse)
async def crear_profesor(profesor: ProfesorRequest):
    # Lógica de creación
    pass
```

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/ProfesoresPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X POST "http://localhost:8000/api/v1/profesores" -H "Content-Type: application/json" -d '{"nombres": "Juan", "apellidos": "Perez"}'
```
