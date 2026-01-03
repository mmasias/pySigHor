<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](/README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](/RUP/README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](/RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](/RUP/00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](/RUP/01-analisis/casos-uso/README.md)
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](/RUP/README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](/extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](/conversation-log.md)

</div>

# pySigHor - Sistema generador de horarios

## La aplicación

En 1998, en la asignatura de TPD (Taller de procesamiento de datos) de Ing. Industrial y de Sistemas de la Universidad de Piura, impartida por el prof. Roberto Castro, aplicamos lo que habíamos aprendido en [Investigación de Operaciones](https://es.wikipedia.org/wiki/Programaci%C3%B3n_lineal) para desarrollar SIGHOR, un [algoritmo](l'Algoritmo.md) que derivó en un sistema generador de horarios. ¡Una joyita en Visual Basic 3!

<div align=center>

|![](/images/F8zDugwX0AArV7H.jpeg)|![](/images/F8zDzlZXQAAe-o8.jpeg)|![](/images/F8zDw0CWEAADw8U.jpeg)|![](/images/F8zD4afXAAIsnGn.jpeg)|![](/images/F8zD2blXAAArega.jpeg)
|:-:|:-:|:-:|:-:|:-:|
|Definición de aulas|Definición de asignaturas (cursos)|Definición de profesores|Pantalla principal|Horario generado|

</div>

## El proyecto

|||
|-|-|
[Proceso(s)](/RUP/README.md)|Aplicación de la metodología RUP para la reingeniería del sistema, con énfasis en **independencia tecnológica** y trazabilidad sistemática.
[Estado actual](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|Dashboard visual de progreso con 32 casos de uso analizados y dashboard(s) por stack para hacer seguimiento del diseño.
[Reflexiones...](/extraDocs/README.md)|Artículos documentando decisiones metodológicas y validaciones experimentales

### Experimento de independencia tecnológica RUP

> **Hipótesis:** Un análisis RUP completo puede soportar múltiples implementaciones tecnológicas sin modificaciones.
> <div align=center>
>
> |Rama|Stack|CdU|Dashboard|Estado|
> |-|-|-:|:-:|-|
> |- [***main***](https://github.com/mmasias/pySigHor/tree/main)|<sup>Análisis puro (agnóstico)|32/32|[Ver](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|Completado|
> |- [***diseño-fastapi-react***](https://github.com/mmasias/pySigHor/tree/diseño-fastapi-react/RUP/02-diseño/)|<sup>FastAPI + React|5/32|[Ver](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|En diseño...|
> |- [***diseño-spring-angular***](https://github.com/mmasias/pySigHor/tree/diseño-spring-angular/RUP/02-diseño/)|<sup>Spring + Angular|5/32|[Ver](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|En diseño...|
> |- [***diseño-cli-python-http***](https://github.com/mmasias/pySigHor/tree/diseño-cli-python-http/RUP/02-diseño/)|<sup>CLI con reuso|5/32|[Ver](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-cli-python-http/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|En diseño...|
> |- [***diseño-cli-python-standalone***](https://github.com/mmasias/pySigHor/tree/diseño-cli-python-standalone/RUP/02-diseño/)|<sup>CLI standalone|5/32|[Ver](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-cli-python-standalone/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|En diseño...|
>
> </div>
>
> **Caminos evolutivos probados:**
>
> - Web GUI tradicional (FastAPI/React, Spring/Angular)
> - CLI standalone (arquitectura monolítica)
> - CLI con reuso de infraestructura (consume API existente)
>
> **Resultado:** 0 modificaciones al análisis tras 4 caminos evolutivos diferentes ([Artículo 015](/extraDocs/015-dashboards-multistack-validacion-experimental/))

## Hitos

|Conceptuales|Validaciones|Documentación
|-|-|-|
|**32 casos de uso** con análisis MVC completo|**Independencia tecnológica validada** con 4 caminos evolutivos (Web GUI, CLI standalone, CLI con reuso)|**Artículos técnicos** documentando decisiones y validaciones ([extraDocs](/extraDocs/README.md))
|**Nomenclatura MVC** aplicada sistemáticamente|**0 modificaciones al análisis** tras 4 caminos evolutivos de implementación|**Trazabilidad completa** en 51+ conversaciones documentadas ([conversation-log](/conversation-log.md))
|**Diagramas de contexto** libres de sesgo tecnológico|**Dashboard visual** para seguimiento de progreso|**Colaboración humano-IA** documentada éticamente ([Artículo 005](/extraDocs/005-etiquetado-etico-colaboracion-humano-ia/))
|**Wireframes SALT** como abstracciones de interacción|**Validación multi-paradigma** (GUI web → CLI terminal)|**Proceso completamente documentado** para replicación y estudio

## Estructura del repositorio

```text
pySigHor/
├── RUP/                             # Estructura del proyecto RUP
│   ├── 00-casos-uso/                # Casos de uso (requisitos)
│   ├── 01-analisis/                 # Análisis
│   ├── 02-diseño/                   # Diseño
│   └── 99-seguimiento/              # Dashboard y seguimiento
├── extraDocs/                       # Documentación adicional y análisis
├── images/                          # Capturas de pantalla y assets de documentación
│   ├── RUP/                         # Imágenes generadas de diagramas RUP
│   └── extraDocs/                   # Imágenes de documentación adicional
├── drafts-temp/                     # Borradores y archivos temporales
├── src/                             # Código fuente original de Visual Basic 3.0
│   └── extraFiles/                  # Archivos de licencias y configuración legacy
├── conversation-log.md              # Registro completo de conversaciones del proyecto
├── *.md                             # Archivos de documentación y análisis
└── README.md                        # Resumen del proyecto
```


<div align=right>

---

<sub>*In memoriam L.F.M.*</sub>

</div>
