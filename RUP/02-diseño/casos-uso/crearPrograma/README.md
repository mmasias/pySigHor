# pySigHor > crearPrograma > Diseño

> |[🏠️](/RUP/README.md)|[📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearPrograma/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearPrograma/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/crearPrograma/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/crearPrograma/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Ollama

## Propósito
Especificar el flujo para la creación de una nueva entidad Programa, incluyendo validaciones y persistencia.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/crearPrograma/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Formulario `ProgramaForm` (modo creación).
*   **API**: Endpoint `POST /programas`.
*   **ProgramaService**: Lógica de creación.
*   **ProgramaRepository**: `INSERT` en base de datos.

## Decisiones de diseño
*   Uso de `ProgramaCreate` schema para validación de entrada (tipos, obligatoriedad).
*   Retorno de código HTTP `201 Created` con el objeto creado.
