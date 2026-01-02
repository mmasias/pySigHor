# pySigHor > eliminarAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar la interacción entre los componentes del sistema CLI Standalone para eliminar una aula, incluyendo confirmación interactiva o automática mediante flag.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/eliminarAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (AulaCommand)**: Recibe ID, solicita confirmación, ejecuta eliminación.
- **TokenManager**: Verifica autenticación mediante token almacenado.
- **AulaService**: Lógica de negocio para eliminar aula.
- **AulaRepository**: Abstracción para eliminación de datos.
- **Base de Datos (SQLite)**: Persistencia local de aulas.

## Decisiones de diseño

- Confirmación interactiva por defecto mediante `click.confirm`.
- Flag `--confirm` para bypass de confirmación (scripts automatizados).
- Eliminación física (hard delete) sin papelera de reciclaje.
- Verificación de existencia antes de intentar eliminar.
- Retorno booleano indicando éxito o fallo de la operación.
- Constraints de integridad referencial manejados por SQLite.
