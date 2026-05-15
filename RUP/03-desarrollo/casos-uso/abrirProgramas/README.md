# pySigHor > abrirProgramas > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirProgramas/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirProgramas/README.md)|[Diseño](/RUP/02-diseño/casos-uso/abrirProgramas/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/programas.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/programas.py) · [services/programa_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/programa_service.py) · [repositories/programa_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/programa_repository.py) · [models/programa.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/programa.py)
- **Frontend:** [pages/ProgramasPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/ProgramasPage.tsx)



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
