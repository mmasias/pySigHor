# pySigHor > asignarProfesorACurso > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/asignarProfesorACurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/asignarProfesorACurso/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/asignarProfesorACurso/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/asignarProfesorACurso/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-11
- **Autor**: Gemini

## Propósito
Especificar el flujo para la gestión de asignaciones entre un Profesor y los Cursos que puede dictar, mediante una interfaz de doble lista con guardado en bloque.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/asignarProfesorACurso/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Componente `AsignacionesProfesor` con doble lista (disponibles / asignados).
*   **API**: `GET /profesores/{id}/cursos`, `GET /cursos`, `PUT /profesores/{id}/cursos`.
*   **AsignacionService**: Valida existencia de cursos y ausencia de duplicados; coordina el reemplazo de asignaciones.
*   **AsignacionRepository**: Reemplaza en bloque las filas de la tabla pivot `asignaciones`.

## Decisiones de diseño
*   Guardado en bloque (`PUT`) en lugar de operaciones individuales: reduce llamadas a la API y simplifica el control de transacciones.
*   El Frontend gestiona el estado intermedio de la selección; la API solo conoce el estado final.
*   `422 Unprocessable Entity` si algún `curso_id` del body no existe en la base de datos.
*   Retorno de `200 OK` con la lista de cursos asignados actualizada tras guardar.
