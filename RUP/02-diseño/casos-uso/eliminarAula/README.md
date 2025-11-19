# Diseño del caso de uso: eliminarAula

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Propósito
Especificar el flujo para la eliminación física de un registro de aula.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/eliminarAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Botón de eliminación con confirmación.
*   **API**: Endpoint `DELETE /aulas/{id}`.
*   **AulaService**: Lógica de eliminación.
*   **AulaRepository**: `DELETE` en base de datos.

## Decisiones de diseño
*   Retorno de `204 No Content` al éxito.
*   Manejo de integridad referencial (si el aula tiene horarios asignados, la BD podría lanzar error, el Service debe capturarlo).
