# pySigHor > crearCurso > Diseño

> |[🏠️](/RUP/README.md)|[📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearCurso/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearCurso/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/crearCurso/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/crearCurso/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Ollama

## Propósito
Especificar el flujo para la creación de una nueva entidad Curso, incluyendo validaciones y persistencia.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/crearCurso/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Formulario `CursoForm` (modo creación).
*   **API**: Endpoint `POST /cursos`.
*   **CursoService**: Lógica de creación.
*   **CursoRepository**: `INSERT` en base de datos.

## Decisiones de diseño
*   Uso de `CursoCreate` schema para validación de entrada (tipos, obligatoriedad).
*   Retorno de código HTTP `201 Created` con el objeto creado.
