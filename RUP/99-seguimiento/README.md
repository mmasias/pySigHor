<div align=right>

|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../01-analisis/casos-uso/README.md)
|-:

</div>

# Dashboard de seguimiento RUP

El dashboard de seguimiento muestra el progreso de implementación por stack tecnológico. Cada rama de implementación mantiene su propio dashboard, reflejando el estado de desarrollo específico de esa tecnología.

## Dashboards por stack

| Stack | Dashboard |
|-------|-----------|
| FastAPI + React | [![](https://img.shields.io/badge/-Ver_dashboard-lightblue?style=flat)](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) |
| Spring + Angular | [![](https://img.shields.io/badge/-Ver_dashboard-lightblue?style=flat)](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) |
| CLI Python HTTP | [![](https://img.shields.io/badge/-Ver_dashboard-lightblue?style=flat)](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-cli-python-http/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) |
| CLI Python Standalone | [![](https://img.shields.io/badge/-Ver_dashboard-lightblue?style=flat)](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-cli-python-standalone/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) |

## Leyenda de estados RUP

| Color | Fase |
|-|-|
| 🔘 Gris | Identificado |
| 🔴 Rojo | Detalle / prototipado |
| 🟫 Amarillo oscuro | Analizado |
| 🟢 Verde | Diseñado |
| 🔵 Celeste | Desarrollado |
| 🔵 Azul | Probado |
| ⚫ Negro | Completado |

## Nota metodológica

El dashboard es tecnológicamente específico: el diseño y el desarrollo dependen del stack elegido. El análisis (hasta `01-analisis/`) es compartido por todos los stacks y vive en `main`. A partir de `02-diseño/`, cada rama de implementación es independiente.
