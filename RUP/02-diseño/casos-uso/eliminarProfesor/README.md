# pySigHor > eliminarProfesor > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarProfesor/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarProfesor/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/eliminarProfesor/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/eliminarProfesor/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Ollama

## Propósito
Especificar el flujo para la eliminación segura de una entidad Profesor, con confirmación previa del usuario.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/eliminarProfesor/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Componente de lista con diálogo de confirmación.
*   **API**: Endpoint `DELETE /profesores/{id}`.
*   **ProfesorService**: Verifica existencia y coordina la eliminación.
*   **ProfesorRepository**: `DELETE` en base de datos.

## Decisiones de diseño
*   Confirmación obligatoria en el frontend antes de enviar la petición.
*   Retorno de código HTTP `204 No Content` tras eliminación exitosa.
*   El servicio verifica que el profesor existe antes de eliminar (404 si no existe).
