# pySigHor > eliminarAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (CLI HTTP)
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar el flujo para eliminar un aula existente desde la CLI, con confirmación explícita mediante flag o prompt interactivo.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/eliminarAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (Click)**: Comando `sighor aulas delete <id>` con flag opcional `--confirm`.
- **APIClient**: Cliente HTTP que realiza DELETE `/aulas/{id}` con token de autorización.
- **API (FastAPI)**: Endpoint `DELETE /aulas/{id}` protegido (requiere token) (reutilizado).
- **AulaService**: Valida existencia y orquesta eliminación (reutilizado).
- **AulaRepository**: Ejecuta DELETE en base de datos (reutilizado).

## Decisiones de diseño

- **Confirmación requerida**: Sin flag `--confirm`, CLI solicita confirmación interactiva (y/n).
- **ID como argumento**: `sighor aulas delete 5` recibe el ID como parámetro posicional.
- CLI como **cliente HTTP puro**: consume mismo endpoint `DELETE /aulas/{id}` que interfaz React.
- Retorno de `204 No Content` al éxito (sin cuerpo de respuesta).
- Manejo de integridad referencial: Si aula tiene horarios asignados, backend retorna error y CLI lo muestra.
- **Reuso completo del backend**: AulaService y AulaRepository sin modificaciones.
