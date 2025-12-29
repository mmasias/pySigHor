# pySigHor > crearAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (Spring Boot + Angular)
- **Fecha**: 2025-12-29
- **Autor**: Manuel Masías + Claude Sonnet 4.5

## Propósito
Especificar el flujo para la creación de una nueva entidad Aula, incluyendo validaciones, mapeo DTO-Entidad y persistencia.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/crearAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend (Angular)**: Formulario reactivo `AulaFormComponent` con validaciones client-side.
*   **AulaController**: Endpoint REST `POST /api/aulas` protegido.
*   **AulaService**: Lógica de creación y mapeo bidireccional DTO-Entidad.
*   **AulaRepository**: Interface Spring Data JPA para persistencia.

## Decisiones de diseño
*   Uso de `AulaCreateDTO` con validaciones Bean Validation (`@NotNull`, `@Size`, `@Min`).
*   Retorno de código HTTP `201 Created` con Location header apuntando al recurso creado.
*   Mapeo manual DTO-Entidad en capa de servicio (alternativa: MapStruct).
*   Validaciones duplicadas: client-side (UX inmediata) y server-side (seguridad).
