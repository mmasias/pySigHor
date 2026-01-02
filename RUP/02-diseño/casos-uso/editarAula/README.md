# pySigHor > editarAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar la interacción entre los componentes del sistema CLI Standalone para modificar una aula existente, mostrando valores actuales como defaults en prompts interactivos.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/editarAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (AulaCommand)**: Recibe ID, carga datos actuales, solicita nuevos valores.
- **TokenManager**: Verifica autenticación mediante token almacenado.
- **AulaService**: Lógica de negocio para obtener, validar y actualizar aula.
- **AulaRepository**: Abstracción para acceso y actualización de datos.
- **Base de Datos (SQLite)**: Persistencia local de aulas.

## Decisiones de diseño

- Consulta previa para obtener datos actuales del aula.
- Prompts de Click con valores actuales como `default`.
- Usuario puede mantener valores presionando Enter sin modificar.
- Validación completa en capa de servicio antes de persistir.
- Actualización in-place del objeto ORM seguido de commit.
- Manejo de aula no encontrada con mensaje de error explícito.
