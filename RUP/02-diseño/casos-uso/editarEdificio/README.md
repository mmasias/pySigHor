# pySigHor > editarEdificio > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarEdificio/README.md)|[Análisis](/RUP/01-analisis/casos-uso/editarEdificio/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-03-07
- **Autor**: Claude Code

## Propósito

Detallar el proceso de actualización de un edificio existente, incluyendo la verificación previa de existencia.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/editarEdificio/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **Frontend**: Formulario `EdificioForm` (modo edición, datos precargados).
- **API**: Endpoint `PATCH /edificios/{id}`.
- **EdificioService**: Lógica de actualización.
- **EdificioRepository**: `UPDATE` en base de datos.

## Decisiones de diseño

- Verificación previa de existencia del ID: `404 Not Found` si el edificio no existe.
- Uso de `EdificioUpdate` schema con campos opcionales (PATCH semántico).
- Este caso de uso es el destino de la transferencia automática desde `crearEdificio()` (filosofía C→U).
- Patrón idéntico a `editarAula`: mismo flujo, distinta entidad.
