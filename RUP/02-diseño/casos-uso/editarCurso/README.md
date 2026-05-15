# pySigHor > editarCurso > Diseño

> |[🏠️](/RUP/README.md)|[📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarCurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarCurso/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/editarCurso/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/editarCurso/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Ollama

## Propósito
Especificar el flujo para la modificación de los datos de una entidad Curso existente.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/editarCurso/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Formulario `CursoForm` (modo edición, datos precargados).
*   **API**: Endpoint `PUT /cursos/{id}`.
*   **CursoService**: Orquesta la búsqueda y actualización.
*   **CursoRepository**: `SELECT` + `UPDATE` en base de datos.

## Decisiones de diseño
*   Uso de `CursoUpdate` schema (campos opcionales).
*   Verificación de existencia antes de actualizar (404 si no existe).
*   Retorno de código HTTP `200 OK` con el objeto actualizado.
