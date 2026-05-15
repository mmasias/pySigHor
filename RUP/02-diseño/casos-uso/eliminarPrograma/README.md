# pySigHor > eliminarPrograma > Diseño

> |[🏠️](/RUP/README.md)|[📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarPrograma/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarPrograma/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/eliminarPrograma/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/eliminarPrograma/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Ollama

## Propósito
Especificar el flujo para la eliminación segura de una entidad Programa, con confirmación previa del usuario.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/eliminarPrograma/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Componente de lista con diálogo de confirmación.
*   **API**: Endpoint `DELETE /programas/{id}`.
*   **ProgramaService**: Verifica existencia y coordina la eliminación.
*   **ProgramaRepository**: `DELETE` en base de datos.

## Decisiones de diseño
*   Confirmación obligatoria en el frontend antes de enviar la petición.
*   Retorno de código HTTP `204 No Content` tras eliminación exitosa.
*   El servicio verifica que el programa existe antes de eliminar (404 si no existe).
