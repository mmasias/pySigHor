# pySigHor > abrirAulas > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirAulas/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirAulas/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/abrirAulas/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/abrirAulas/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2025-11-19
- **Autor**: Gemini

## Propósito
Detallar el flujo de datos para recuperar y mostrar la lista de aulas registradas en el sistema.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/abrirAulas/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Componente `AulaList` que consume la API.
*   **API**: Endpoint `GET /aulas` protegido (requiere token).
*   **AulaService**: Orquestador que llama al repositorio.
*   **AulaRepository**: Ejecuta la consulta SQL `SELECT`.

## Decisiones de diseño
*   Endpoint protegido con `Bearer Token`.
*   Retorno de lista JSON de objetos `AulaResponse` (Pydantic Schema).
*   Separación de DTOs (Schemas) de Modelos de BD (SQLAlchemy).
