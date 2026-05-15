# pySigHor > crearEdificio > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearEdificio/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearEdificio/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-03-07
- **Autor**: Claude Code

## Propósito

Especificar el flujo para la creación rápida de un nuevo edificio con filosofía C→U: datos mínimos en creación, transferencia automática a edición completa.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/crearEdificio/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **Frontend**: Formulario `EdificioForm` (modo creación, campos mínimos).
- **API**: Endpoint `POST /edificios`.
- **EdificioService**: Lógica de creación rápida.
- **EdificioRepository**: `INSERT` en base de datos.

## Decisiones de diseño

- Uso de `EdificioCreate` schema: solo `nombre` obligatorio.
- Retorno de código HTTP `201 Created` con el objeto creado (incluye ID generado).
- Tras el `201`, el frontend redirige automáticamente al formulario de edición del edificio recién creado (`<<include>> editarEdificio`).
- Esta es la implementación de la filosofía **C→U** (Create→Update): la creación solo inserta el registro mínimo; la edición completa los datos restantes.
