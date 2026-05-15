# pySigHor > crearEdificio > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearEdificio/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearEdificio/README.md)|[Diseño](/RUP/02-diseño/casos-uso/crearEdificio/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/edificios.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/edificios.py) · [services/edificio_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/edificio_service.py) · [repositories/edificio_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/edificio_repository.py) · [models/edificio.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/edificio.py)
- **Frontend:** [pages/EdificiosPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/EdificiosPage.tsx)


Crea un nuevo edificio validando unicidad de nombre. El servicio lanza `ValueError` si el nombre ya existe; el router lo convierte en 400.

## Backend

```python
@router.post("", response_model=EdificioResponse, status_code=status.HTTP_201_CREATED)
async def crear_edificio(edificio_data: EdificioCreate,
                         current_user: str = Depends(get_current_user),
                         db: AsyncSession = Depends(get_db)):
    try:
        service = EdificioService(db)
        return await service.crear_edificio(edificio_data)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
```

```python
# EdificioService.crear_edificio
async def crear_edificio(self, edificio_data: EdificioCreate) -> Edificio:
    existente = await self.repo.get_by_nombre(edificio_data.nombre)
    if existente:
        raise ValueError(f"Ya existe un edificio con el nombre '{edificio_data.nombre}'")
    return await self.repo.create(edificio_data.dict())
```

**Endpoint:** `POST /api/v1/edificios`  
**Schema:** `{ "nombre": string, "direccion": string|null }`

```bash
curl -X POST "http://localhost:8000/api/v1/edificios" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Edificio A", "direccion": "Av. Principal 123"}'
```

## Frontend

`EdificiosPage.tsx` abre un dialog de creación. Al confirmar llama a `edificioService.create(data)` y recarga la lista.
