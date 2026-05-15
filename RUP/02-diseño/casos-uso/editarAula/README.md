# pySigHor > editarAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarAula/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/editarAula/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/editarAula/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2025-11-19
- **Autor**: Gemini

## Propósito
Detallar el proceso de actualización de una aula existente.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/editarAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Formulario `AulaForm` (modo edición, precargado).
*   **API**: Endpoint `PUT /aulas/{id}`.
*   **AulaService**: Lógica de actualización.
*   **AulaRepository**: `UPDATE` en base de datos.

## Decisiones de diseño
*   Verificación previa de existencia del ID (404 si no existe).
*   Uso de `AulaUpdate` schema (campos opcionales si se desea PATCH, obligatorios si es PUT completo).
