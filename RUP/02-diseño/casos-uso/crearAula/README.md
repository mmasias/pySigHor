# pySigHor > crearAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (CLI HTTP)
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar el flujo para crear una nueva aula desde la CLI mediante prompts interactivos, enviando los datos al backend FastAPI para validación y persistencia.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/crearAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (Click)**: Comando `sighor aulas create` que solicita datos mediante prompts.
- **APIClient**: Cliente HTTP que realiza POST `/aulas` con token y datos del aula.
- **API (FastAPI)**: Endpoint `POST /aulas` protegido (requiere token) (reutilizado).
- **AulaService**: Valida y orquesta la creación (reutilizado).
- **AulaRepository**: Ejecuta INSERT en base de datos (reutilizado).

## Decisiones de diseño

- **Prompts interactivos**: CLI solicita nombre, capacidad y edificio mediante `click.prompt()`.
- CLI como **cliente HTTP puro**: consume mismo endpoint `POST /aulas` que interfaz React.
- **Validaciones en backend**: Pydantic valida tipos y restricciones (capacidad > 0, etc.) con schema `AulaCreate`.
- Respuesta exitosa (201 Created) muestra mensaje de confirmación con ID del aula creada.
- **Reuso completo del backend**: AulaService y AulaRepository sin modificaciones.
