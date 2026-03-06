<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../01-analisis/casos-uso/README.md)
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../conversation-log.md)

</div>

# Dashboard de seguimiento RUP

Este dashboard visual muestra el progreso del proyecto de modernización de SigHor utilizando la metodología RUP (Rational Unified Process).

## Diagrama de contexto con seguimiento

<div align=center>

|![Dashboard RUP - Diagrama de Contexto](/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|:-:|
|**Dashboard de seguimiento del proyecto pySigHor**|
|Código fuente: [diagrama-contexto-administrador.puml](diagrama-contexto-administrador.puml)|

</div>

## Leyenda de estados RUP

|Color|Fase|Descripción|
|-|-|-|
|🔘 **Gris**|Identificado|Caso de uso identificado pero no iniciado|
|🔴 **Rojo**|Detalle/prototipado|Especificación detallada y prototipado|
|🟫 **Amarillo oscuro**|Análisis|Análisis MVC y colaboraciones|
|🟢 **Verde**|Diseño|Diseño arquitectónico y detallado|
|🔵 **Celeste**|Desarrollo|Implementación del código|
|🔵 **Azul**|Pruebas|Testing y validación|
|⚫ **Negro**|Completado|Caso de uso completamente terminado|

## Navegación del diagrama

Cada transición puede incluir hasta 4 enlaces según la fase alcanzada:
- **[nombreCasoUso()]** - Especificación detallada (requisitos + prototipo)
- **[A]** - Análisis MVC
- **[D]** - Diseño técnico (diagramas de secuencia)
- **[dev]** - Desarrollo (implementación)

## Progreso actual

### Casos de uso en fase de desarrollo (🔵 Celeste) — Iteración 1

- **iniciarSesion()** — autenticación JWT, backend + frontend
- **abrirAulas()** — GET /aulas, listado completo
- **crearAula()** — POST /aulas, filosofía C→U
- **editarAula()** — PATCH /aulas/{id}
- **eliminarAula()** — DELETE /aulas/{id}

### Casos de uso en fase de diseño (🟢 Verde) — Iteración 2

- **abrirEdificios()** — diagrama de secuencia listo
- **crearEdificio()** — diagrama de secuencia listo (C→U, datos mínimos)
- **editarEdificio()** — diagrama de secuencia listo
- **eliminarEdificio()** — diagrama de secuencia listo (verificación de aulas dependientes → 409)

### Casos de uso en fase de análisis (🟫 Amarillo oscuro)

Todos los demás (~22 CdUs): Programas, Cursos, Profesores, Recursos, Horarios, y transversales (completarGestion, cerrarSesion, asignarProfesorACurso, generarHorario, consultarHorario).

## Estadísticas del proyecto

| Fase | CdUs | % |
|---|:-:|:-:|
| 🔵 Desarrollo (Iteración 1) | 5 | ~16% |
| 🟢 Diseño (Iteración 2) | 4 | ~13% |
| 🟫 Análisis | ~22 | ~71% |
| **Total** | **~31** | |

## Próximos pasos

### Completado
- ✅ Fase de análisis: todos los CdUs
- ✅ Diseño técnico + implementación: Iteración 1 (Aulas + autenticación)
- ✅ Diseño técnico: Iteración 2 (Edificios)

### En curso
- Acción 1: Migrar autenticación de hardcodeado a BD real (prerrequisito de Iteración 2)
- Acción 2: Implementar Iteración 2 — Edificios CRUD + tests Pytest

## Metodología

Este dashboard se actualiza automáticamente conforme se completan las fases RUP para cada caso de uso:

1. **Identificado** → **Detalle/prototipado** → **Análisis** → **Diseño** → **Desarrollo** → **Pruebas** → **Completado**

El diagrama utiliza colores y estilos de línea específicos para mostrar visualmente el estado de cada transición entre estados del sistema.

## Referencias

- [Diagrama de contexto RUP puro](../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Documentación de casos de uso](../00-casos-uso/02-detalle/README.md)
- [Análisis de casos de uso](../01-analisis/casos-uso/README.md)
- [Conversation log](../../conversation-log.md)
