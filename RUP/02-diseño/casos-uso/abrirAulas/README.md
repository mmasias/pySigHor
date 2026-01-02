# pySigHor > abrirAulas > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirAulas/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirAulas/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (CLI HTTP)
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar el flujo de datos para recuperar y mostrar la lista de aulas registradas en el sistema desde la interfaz CLI, formateando la salida como tabla ASCII o JSON.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/abrirAulas/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (Click)**: Comando `sighor aulas list` que consume la API y formatea salida.
- **APIClient**: Cliente HTTP que realiza GET `/aulas` con token de autorización.
- **API (FastAPI)**: Endpoint `GET /aulas` protegido (requiere token) (reutilizado).
- **AulaService**: Orquestador que llama al repositorio (reutilizado).
- **AulaRepository**: Ejecuta la consulta SQL `SELECT` (reutilizado).
- **OutputFormatter**: Formatea datos como tabla Rich o JSON (específico de CLI).

## Decisiones de diseño

- Endpoint protegido con `Bearer Token` (token obtenido de `token_manager`).
- CLI como **cliente HTTP puro**: consume mismo endpoint `GET /aulas` que interfaz React.
- **Formateo de salida flexible**: tabla ASCII (Rich) por defecto, JSON con flag `--format json`.
- Retorno de lista JSON de objetos `AulaResponse` (Pydantic Schema heredado).
- **Reuso completo del backend**: AulaService y AulaRepository sin modificaciones.
