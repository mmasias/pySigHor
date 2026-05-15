# pySigHor > eliminarEdificio > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarEdificio/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarEdificio/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-03-07
- **Autor**: Claude Code

## Propósito

Especificar el flujo para la eliminación segura de un edificio, incluyendo confirmación del usuario y verificación de integridad referencial con las aulas asociadas.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/eliminarEdificio/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **Frontend**: Botón de eliminación con diálogo de confirmación.
- **API**: Endpoint `DELETE /edificios/{id}`.
- **EdificioService**: Lógica de eliminación con verificación de dependencias.
- **EdificioRepository**: `DELETE` en base de datos.

## Decisiones de diseño

- Retorno de `204 No Content` al eliminar correctamente.
- **Verificación de integridad referencial en la capa de servicio** (no delegada a la BD): el `EdificioService` consulta si existen aulas asociadas al edificio antes de proceder.
- Si el edificio tiene aulas asociadas: `409 Conflict` con mensaje descriptivo. El frontend muestra el error al usuario.
- Si no tiene aulas: se procede con el `DELETE`.
- Esta decisión de diseño es la diferencia principal respecto a `eliminarAula`: los edificios tienen dependientes (aulas), las aulas no tienen dependientes directos en la Iteración 1.
