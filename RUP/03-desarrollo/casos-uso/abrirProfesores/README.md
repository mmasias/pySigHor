# pySigHor > abrirProfesores > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirProfesores/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirProfesores/README.md)|[Diseño](/RUP/02-diseño/casos-uso/abrirProfesores/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/profesores.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/profesores.py) · [services/profesor_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/profesor_service.py) · [repositories/profesor_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/profesor_repository.py) · [models/profesor.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/profesor.py)
- **Frontend:** [pages/ProfesoresPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/ProfesoresPage.tsx)



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
