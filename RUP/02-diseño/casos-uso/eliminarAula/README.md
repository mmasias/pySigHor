# pySigHor > eliminarAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/eliminarAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (Spring Boot + Angular)
- **Fecha**: 2025-12-29
- **Autor**: Manuel Masías + Claude Sonnet 4.5

## Propósito
Especificar el flujo para la eliminación física de un registro de aula, incluyendo confirmación previa y manejo de errores.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/eliminarAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend (Angular)**: Botón de eliminación con modal de confirmación.
*   **AulaController**: Endpoint REST `DELETE /api/aulas/{id}` protegido.
*   **AulaService**: Lógica de eliminación con validación de existencia.
*   **AulaRepository**: Interface Spring Data JPA para eliminación.

## Decisiones de diseño
*   Confirmación explícita del usuario mediante modal de Angular Material/Bootstrap.
*   Verificación previa de existencia del ID (lanza `EntityNotFoundException` → 404).
*   Retorno de `204 No Content` al éxito (sin body en respuesta).
*   Manejo de integridad referencial: si aula tiene relaciones (horarios asignados), JPA lanza `DataIntegrityViolationException` capturada por `@ControllerAdvice` → 409 Conflict.
*   Respuesta al frontend sin contenido, actualización optimista de la lista.
