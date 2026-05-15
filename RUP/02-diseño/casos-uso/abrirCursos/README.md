# pySigHor > abrirCursos > Diseño

> |[🏠️](/RUP/README.md)|[📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirCursos/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirCursos/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/abrirCursos/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/abrirCursos/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Ollama

## Propósito
Detallar el flujo de datos para recuperar y mostrar la lista de cursos registrados en el sistema.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/abrirCursos/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Componente `CursoList` que consume la API.
*   **API**: Endpoint `GET /cursos` protegido (requiere token).
*   **CursoService**: Orquestador que llama al repositorio.
*   **CursoRepository**: Ejecuta la consulta SQL `SELECT`.

## Decisiones de diseño
*   Endpoint protegido con `Bearer Token`.
*   Retorno de lista JSON de objetos `CursoResponse` (Pydantic Schema).
*   Separación de DTOs (Schemas) de Modelos de BD (SQLAlchemy).
