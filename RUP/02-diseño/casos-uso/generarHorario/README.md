# pySigHor > generarHorario > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/generarHorario/README.md)|[Análisis](/RUP/01-analisis/casos-uso/generarHorario/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/generarHorario/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/generarHorario/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-11
- **Autor**: Gemini

## Propósito
Especificar el flujo para la generación del horario académico mediante el algoritmo de 4 fases, incluyendo validación de datos previos, confirmación de reemplazo y persistencia automática del resultado.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/generarHorario/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Componente `GenerarHorario` con botón de generación, feedback de validación y diálogo de confirmación de reemplazo.
*   **API**: `GET /horario/preflight`, `POST /horario/generar`.
*   **HorarioService**: Valida datos mínimos del sistema; carga datos maestros completos; coordina la invocación de `HorarioGenerator`.
*   **HorarioGenerator**: Encapsula el algoritmo de 4 fases (`PrepararH`, `GeneraPreHorario`, `GeneraHorario`, `IngresoHE/HV`); persiste el resultado vía `HorarioRepository`.
*   **HorarioRepository**: Carga conteos y datos maestros; reemplaza el horario en BD (`DELETE` + `INSERT`).

## Decisiones de diseño
*   `GET /horario/preflight` separa la comprobación de condiciones de la ejecución: permite dar feedback claro al usuario antes de comprometer recursos de cómputo.
*   El Frontend controla la lógica de confirmación (datos insuficientes -> error; horario existente -> diálogo); la API no gestiona estados de sesión intermedios.
*   `HorarioGenerator` encapsula las 4 fases como unidad indivisible: el Service lo trata como un servicio de alto nivel (`generar(datos)`) sin conocer detalles internos del algoritmo.
*   Persistencia delegada al Generator: el propio Generator llama a `HorarioRepository` para guardar, lo que garantiza que solo un horario válido y completo se persiste.
*   `201 Created` con `HorarioGeneradoResponse` (resumen estadístico: cursos asignados, conflictos resueltos, aulas utilizadas) — no devuelve el horario completo para no saturar la respuesta.
