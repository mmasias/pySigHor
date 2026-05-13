# pySigHor > abrirProfesores > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirProfesores/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirProfesores/README.md)|[Diseño](/RUP/02-diseño/casos-uso/abrirProfesores/README.md)|**Desarrollo**|Pruebas|

- **Estado:** ✅ **Completado** - Iteración 2
- **Backend:** router en `backend/app/routers/profesores.py`, rama `diseño-fastapi-react`
- **Frontend:** `frontend/src/pages/ProfesoresPage.tsx`, service en `api.ts`, types en `types/index.ts`

#### Secciones:

**Descripción**: 
Este caso de uso permite listar los profesores registrados.

**Estado**: Completado

**Backend (Archivo, Endpoint con request/response JSON)**:
- **Archivo:** `backend/app/routers/profesores.py`
- **Endpoint:** `GET /api/v1/profesores`

**Frontend (Archivo, Implementación)**:
- **Archivo:** `frontend/src/pages/ProfesoresPage.tsx`

**Testing (curl + pasos frontend)**:
```bash
curl -X GET "http://localhost:8000/api/v1/profesores"
```
