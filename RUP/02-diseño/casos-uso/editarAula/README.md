# pySigHor > editarAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (CLI HTTP)
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar el flujo para actualizar una aula existente desde la CLI, solicitando el ID y los nuevos datos mediante prompts interactivos.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/editarAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (Click)**: Comando `sighor aulas edit <id>` que solicita nuevos datos mediante prompts.
- **APIClient**: Cliente HTTP que realiza PUT `/aulas/{id}` con token y datos actualizados.
- **API (FastAPI)**: Endpoint `PUT /aulas/{id}` protegido (requiere token) (reutilizado).
- **AulaService**: Valida existencia y orquesta actualización (reutilizado).
- **AulaRepository**: Ejecuta UPDATE en base de datos (reutilizado).

## Decisiones de diseño

- **ID como argumento**: `sighor aulas edit 5` recibe el ID como parámetro posicional.
- **Prompts para nuevos valores**: CLI solicita nombre, capacidad y edificio con valores actuales como default.
- Verificación previa de existencia del ID (404 si no existe).
- CLI como **cliente HTTP puro**: consume mismo endpoint `PUT /aulas/{id}` que interfaz React.
- Uso de schema `AulaUpdate` con campos opcionales (permite actualización parcial).
- **Reuso completo del backend**: AulaService y AulaRepository sin modificaciones.
