# pySigHor > editarRecurso > Diseño

> |[🏠️](/RUP/README.md)|[📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarRecurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarRecurso/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/editarRecurso/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/editarRecurso/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Ollama

## Propósito
Especificar el flujo para la modificación de los datos de una entidad Recurso existente.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/editarRecurso/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Formulario `RecursoForm` (modo edición, datos precargados).
*   **API**: Endpoint `PUT /recursos/{id}`.
*   **RecursoService**: Orquesta la búsqueda y actualización.
*   **RecursoRepository**: `SELECT` + `UPDATE` en base de datos.

## Decisiones de diseño
*   Uso de `RecursoUpdate` schema (campos opcionales).
*   Verificación de existencia antes de actualizar (404 si no existe).
*   Retorno de código HTTP `200 OK` con el objeto actualizado.
