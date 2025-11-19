<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](/README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](/RUP/README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](/RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](/RUP/00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](/RUP/01-analisis/casos-uso/README.md)
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](/RUP/README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](/extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](/conversation-log.md)

</div>

# pySigHor - Sistema generador de horarios

En 1998, en la asignatura de TPD (Taller de procesamiento de datos) de Ing. Industrial y de Sistemas de la Universidad de Piura, impartida por el prof. Roberto Castro, aplicamos lo que habíamos aprendido en [Investigación de Operaciones](https://es.wikipedia.org/wiki/Programaci%C3%B3n_lineal) para desarrollar SIGHOR, un [algoritmo](l'Algoritmo.md) que derivó en un sistema generador de horarios. ¡Una joyita en Visual Basic 3!

<div align=center>

## El proyecto

|[Proceso(s)](/RUP/README.md)|[Proceso(s)<br><sub>*vPragmática*</sub>](/RUP-pragmatico/README.md)|[Estado actual](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Reflexiones...](/extraDocs/README.md)|
|-|-|-|-|
|Aplicación de la metodología RUP para la reingeniería del sistema, con énfasis en pureza metodológica y trazabilidad sistemática.|Versión "ligera" de los procesos.|Propuesta de artefacto dinámico de seguimiento|Artículos de reflexión a partir de la dinámica de trabajo
|||<sub>enProgreso: [RamaDiseño](https://raw.githubusercontent.com/mmasias/pySigHor/faseDise%C3%B1o-Iteracion001/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)</sub>

</div>

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
├── extraFiles/                      # Archivos de licencias y configuración legacy
├── drafts-temp/                     # Borradores y archivos temporales
├── src/                             # Código fuente original de Visual Basic 3.0
├── conversation-log.md              # Registro completo de conversaciones del proyecto
├── *.md                             # Archivos de documentación y análisis
└── README.md                        # Resumen del proyecto
```

## La aplicación

<div align=center>

|![](/images/F8zDugwX0AArV7H.jpeg)|![](/images/F8zDzlZXQAAe-o8.jpeg)|![](/images/F8zDw0CWEAADw8U.jpeg)|![](/images/F8zD4afXAAIsnGn.jpeg)|![](/images/F8zD2blXAAArega.jpeg)
|:-:|:-:|:-:|:-:|:-:|
|Definición de aulas|Definición de asignaturas (cursos)|Definición de profesores|Pantalla principal|Horario generado|

</div>

## Hitos metodológicos que guían el trabajo (y se esperan alcanzar)

|Pureza conceptual|Patrón metodológico|Documentación metodológica
|-|-|-|
|**Casos de uso atómicos** identificados y organizados|**Conexión sistemática** entre casos de uso mediante colaboraciones|**Artículos técnicos** documentando lecciones aprendidas y decisiones metodológicas
|**Nomenclatura tecnológicamente agnóstica** aplicada sistemáticamente  |**Marco escalable** para análisis futuro de casos de uso restantes|**Trazabilidad completa** en conversation-log con todas las conversaciones registradas
|**Diagramas de contexto** libres de sesgo tecnológico||**Patrones reutilizables** establecidos para proyectos RUP similares
|**Trazabilidad completa** desde requisitos hasta análisis de colaboración||

