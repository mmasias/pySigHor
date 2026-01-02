# pySigHor > crearAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar la interacción entre los componentes del sistema CLI Standalone para crear una nueva aula mediante prompts interactivos, validar los datos y persistirlos en la base de datos local.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/crearAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (AulaCommand)**: Solicita datos mediante prompts interactivos.
- **TokenManager**: Verifica autenticación mediante token almacenado.
- **AulaService**: Lógica de negocio para validar y crear aula.
- **AulaRepository**: Abstracción para persistencia de datos.
- **Base de Datos (SQLite)**: Persistencia local de aulas.

## Decisiones de diseño

- Uso de prompts interactivos de Click para captura de datos.
- Validación en capa de servicio (campos requeridos, tipos, restricciones).
- Constraint de unicidad en nombre de aula manejado por SQLite.
- ID autogenerado por la base de datos (autoincrement).
- Validación de tipo entero para capacidad directamente en prompt de Click.
- Respuesta incluye ID del aula creada para referencia inmediata.
