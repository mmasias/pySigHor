<div align=right>

|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../01-analisis/casos-uso/README.md)
|-:

</div>

# Dashboard de seguimiento RUP

## Dashboards por stack tecnológico

| Stack | Dashboard |
|-------|-----------|
| FastAPI + React | [![](https://img.shields.io/badge/-Ver_dashboard-lightblue?style=flat)](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) |
| Spring + Angular | [![](https://img.shields.io/badge/-Ver_dashboard-lightblue?style=flat)](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) |
| CLI Python HTTP | [![](https://img.shields.io/badge/-Ver_dashboard-lightblue?style=flat)](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-cli-python-http/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) |
| CLI Python Standalone | [![](https://img.shields.io/badge/-Ver_dashboard-lightblue?style=flat)](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-cli-python-standalone/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) |

## Estado hasta análisis (main)

<div align=center>

|![Dashboard RUP - Diagrama de Contexto](/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|:-:|
|**Dashboard de seguimiento — todos los CdUs en fase de análisis**|
|Código fuente: [diagrama-contexto-administrador.puml](diagrama-contexto-administrador.puml)|

</div>

## Leyenda de estados RUP

| Color | Fase |
|-|-|
| Gris | Identificado |
| Rojo | Requisitado / prototipado |
| Amarillo oscuro | Analizado |
| Verde | Diseñado |
| Celeste | Desarrollado |
| Azul | Probado |
| Negro | Completado |

El análisis es compartido por todos los stacks y vive en `main`. A partir de `02-diseño/`, cada rama de implementación es independiente.
