# pySigHor > configurarPreferenciasProfesor > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/README.md)|[Análisis](/RUP/01-analisis/casos-uso/configurarPreferenciasProfesor/README.md)|[Diseño](/RUP/02-diseño/casos-uso/configurarPreferenciasProfesor/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/profesores.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/profesores.py) · [services/preferencia_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/preferencia_service.py) · [repositories/preferencia_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/preferencia_repository.py) · [models/profesor_recurso.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/profesor_recurso.py)
- **Frontend:** [pages/ProfesoresPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/ProfesoresPage.tsx)



## Modelo de datos

Tabla `profesor_recursos` — many-to-many con columna `prioridad` (Integer). A diferencia de `aula_recursos`, requiere clase ORM mapeada (`ProfesorRecurso`) para exponer la columna extra al algoritmo de generación de horarios.

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/profesores/{id}/preferencias` | Lista de recursos ordenados por prioridad |
| PUT | `/profesores/{id}/preferencias` | Reemplaza todas las preferencias del profesor |

Payload PUT:
```json
{ "recurso_ids": [3, 1, 5, 2] }
```
El orden del array determina la prioridad (índice 0 = prioridad 1).

## UX frontend

Dialog accesible desde el botón "Preferencias" en la tabla de profesores. Muestra la lista completa de recursos con su orden de prioridad actual. Botones ↑ / ↓ por fila para reordenar. Guardar reemplaza todas las preferencias via PUT.

Si el profesor no tiene preferencias previas, el sistema inicializa la lista con todos los recursos disponibles en orden por id.
