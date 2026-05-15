# pySigHor > asignarProfesorACurso > Desarrollo  
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/asignarProfesorACurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/asignarProfesorACurso/README.md)|[Diseño](/RUP/02-diseño/casos-uso/asignarProfesorACurso/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Backend:** [routers/profesores.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/routers/profesores.py) · [services/asignacion_service.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/services/asignacion_service.py) · [repositories/asignacion_repository.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/repositories/asignacion_repository.py) · [models/profesor_curso.py](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/backend/app/models/profesor_curso.py)
- **Frontend:** [pages/ProfesoresPage.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/pages/ProfesoresPage.tsx)



## Modelo de datos

Tabla `profesor_cursos` — many-to-many simple (sin columnas extra), implementada como `Table` de asociación SQLAlchemy al estilo de `aula_recursos`. Un profesor puede impartir varios cursos; un curso puede ser impartido por varios profesores.

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/profesores/{id}/cursos` | Lista de cursos asignados al profesor |
| PUT | `/profesores/{id}/cursos` | Reemplaza todas las asignaciones del profesor |

Payload PUT:
```json
{ "curso_ids": [1, 3, 7] }
```

## UX frontend

Dialog accesible desde el botón SchoolIcon en la tabla de profesores. Muestra dos listas: "Disponibles" (izquierda) y "Asignados" (derecha). El usuario selecciona cursos en cualquier lista (selección múltiple por clic) y usa los botones "Asignar >>" / "<< Desasignar" para moverlos. Guardar reemplaza todas las asignaciones via PUT.
