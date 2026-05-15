# pySigHor > abrirEdificios > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirEdificios/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirEdificios/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-03-07
- **Autor**: Claude Code

## Propósito

Detallar el flujo de datos para recuperar y mostrar la lista de edificios registrados en el sistema.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/abrirEdificios/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **Frontend**: Componente `EdificioList` que consume la API.
- **API**: Endpoint `GET /edificios` protegido (requiere token).
- **EdificioService**: Orquestador que llama al repositorio.
- **EdificioRepository**: Ejecuta la consulta SQL `SELECT`.

## Decisiones de diseño

- Endpoint protegido con `Bearer Token`.
- Retorno de lista JSON de objetos `EdificioResponse` (Pydantic Schema).
- Separación de DTOs (Schemas) de Modelos de BD (SQLAlchemy).
- Patrón idéntico a `abrirAulas`: mismo flujo, distinta entidad.
