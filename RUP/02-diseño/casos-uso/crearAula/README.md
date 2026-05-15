# pySigHor > crearAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearAula/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/crearAula/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/crearAula/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2025-11-19
- **Autor**: Gemini

## Propósito
Especificar el flujo para la creación de una nueva entidad Aula, incluyendo validaciones y persistencia.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/crearAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Formulario `AulaForm` (modo creación).
*   **API**: Endpoint `POST /aulas`.
*   **AulaService**: Lógica de creación.
*   **AulaRepository**: `INSERT` en base de datos.

## Decisiones de diseño
*   Uso de `AulaCreate` schema para validación de entrada (tipos, obligatoriedad).
*   Retorno de código HTTP `201 Created` con el objeto creado.
