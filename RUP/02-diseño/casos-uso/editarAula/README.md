# pySigHor > editarAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (Spring Boot + Angular)
- **Fecha**: 2025-12-29
- **Autor**: Manuel Masías + Claude Sonnet 4.5

## Propósito
Detallar el proceso de actualización de una aula existente, incluyendo validación de existencia y manejo de errores.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/editarAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend (Angular)**: Formulario reactivo `AulaFormComponent` en modo edición.
*   **AulaController**: Endpoint REST `PUT /api/aulas/{id}` protegido.
*   **AulaService**: Lógica de actualización con validación de existencia.
*   **AulaRepository**: Interface Spring Data JPA para persistencia.

## Decisiones de diseño
*   Verificación previa de existencia del ID (lanza `EntityNotFoundException` → 404).
*   Uso de `AulaUpdateDTO` con validaciones Bean Validation.
*   Implementación de **PUT completo** (todos los campos obligatorios).
*   JPA `save()` realiza merge automático de entidad existente.
*   Manejo de excepciones con `@ControllerAdvice` para respuestas consistentes.
*   Respuesta 200 OK con entidad actualizada completa.
