# pySigHor > abrirEdificios > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirEdificios/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirEdificios/README.md)|[Diseño](/RUP/02-diseño/casos-uso/abrirEdificios/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/edificios.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/edificios.py) · [services/edificio_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/edificio_service.py) · [repositories/edificio_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/edificio_repository.py) · [models/edificio.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/edificio.py)
- **Frontend:** [pages/EdificiosPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/EdificiosPage.tsx)


Lista todos los edificios existentes. El router delega en el servicio, que consulta el repositorio.

## Backend

```python
@router.get("", response_model=list[EdificioResponse])
async def listar_edificios(skip: int = 0, limit: int = 100,
                           current_user: str = Depends(get_current_user),
                           db: AsyncSession = Depends(get_db)):
    service = EdificioService(db)
    return await service.listar_edificios(skip=skip, limit=limit)
```

```python
# EdificioRepository.get_all
async def get_all(self, skip: int = 0, limit: int = 100) -> List[Edificio]:
    result = await self.db.execute(select(Edificio).offset(skip).limit(limit))
    return result.scalars().all()
```

**Endpoint:** `GET /api/v1/edificios`

```bash
curl -X GET "http://localhost:8000/api/v1/edificios" \
  -H "Authorization: Bearer <token>"
```

## Frontend

`EdificiosPage.tsx` llama a `edificioService.getAll()` al montar el componente y renderiza la lista en una tabla MUI.
