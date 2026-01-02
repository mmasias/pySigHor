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

Los casos de uso analizados incluyen **2 enlaces** de navegación:
- **[nombreCasoUso]** - Especificación detallada
- **[A]** - Análisis MVC

## Progreso actual

### Casos de uso en fase de análisis (🟫 Amarillo oscuro)

- **iniciarSesion()** - Autenticación de usuarios (especificación + prototipo + análisis)
- **completarGestion()** - Hub de convergencia del sistema (especificación + prototipo + análisis)
- **abrirProgramas()** - Apertura de gestión de programas académicos (especificación + prototipo + análisis)
- **abrirCursos()** - Apertura de gestión de cursos (especificación + prototipo + análisis)
- **abrirProfesores()** - Apertura de gestión de profesores (especificación + prototipo + análisis)
- **abrirEdificios()** - Apertura de gestión de edificios (especificación + prototipo + análisis)
- **abrirAulas()** - Apertura de gestión de aulas (especificación + prototipo + análisis)
- **abrirRecursos()** - Apertura de gestión de recursos (especificación + prototipo + análisis)
- **crearPrograma()** - Creación de programas académicos como "el delgado" C→U (especificación + prototipo + análisis)
- **editarPrograma()** - Edición de programas académicos aplicando filosofía C→U (especificación + prototipo + análisis)
- **eliminarPrograma()** - Eliminación segura de programas con confirmación (especificación + prototipo + análisis)
- **crearCurso()** - Creación de cursos como "el delgado" C→U (especificación + prototipo + análisis + secuencia)
- **editarCurso()** - Edición de cursos como "el gordo" con edición continua (especificación + prototipo + análisis + secuencia)
- **eliminarCurso()** - Eliminación segura de cursos con confirmación (especificación + prototipo + análisis)
- **eliminarProfesor()** - Eliminación segura de profesores con confirmación (especificación + prototipo + análisis) - CORREGIDO
- **editarProfesor()** - Edición de profesores como "el gordo" con edición continua (especificación + prototipo + análisis) - CORREGIDO
- **crearEdificio()** - Creación de edificios como "el delgado" C→U (especificación + prototipo + análisis)
- **editarEdificio()** - Edición de edificios como "el gordo" con edición continua (especificación + prototipo + análisis)
- **eliminarEdificio()** - Eliminación segura de edificios con confirmación (especificación + prototipo + análisis)
- **crearAula()** - Creación de aulas como "el delgado" C→U (especificación + prototipo + análisis)
- **editarAula()** - Edición de aulas como "el gordo" con edición continua (especificación + prototipo + análisis)
- **eliminarAula()** - Eliminación segura de aulas con confirmación (especificación + prototipo + análisis)
- **crearRecurso()** - Creación de recursos como "el delgado" C→U (especificación + prototipo + análisis)
- **editarRecurso()** - Edición de recursos como "el gordo" con edición continua (especificación + prototipo + análisis)
- **eliminarRecurso()** - Eliminación segura de recursos con confirmación (especificación + prototipo + análisis)
- **configurarPreferenciasProfesor()** - Configuración específica de preferencias de recursos (especificación + prototipo + análisis)
- **generarHorario()** - Generación automática de horarios con proceso de 4 fases (especificación + prototipo + análisis)
- **consultarHorario()** - Consulta de horarios generados (especificación + prototipo + análisis)
- **asignarProfesorACurso()** - Gestión de asignaciones profesor-curso (especificación + prototipo + análisis)
- **cerrarSesion()** - Cierre de sesión (especificación + prototipo + análisis)

### Casos de uso identificados únicamente (🔘 Gris)

#### Gestión de datos maestros

(Todos los casos de uso de datos maestros están en análisis o superior)

#### Operaciones CRUD

- **crearRecurso()** / **editarRecurso()** / **eliminarRecurso()**

#### Funcionalidades especiales

#### Sistema

(Todos los casos de uso del sistema están en análisis o superior)

## Estadísticas del proyecto

- **Total de casos de uso**: 32
- **Casos de uso en diseño**: 5 (15.6%) - Validación experimental en 4 stacks tecnológicos
- **Casos de uso en análisis**: 27 (84.4%)
- **Casos de uso identificados**: 0 (0%)
- **Progreso general**: 100% análisis + 15.6% diseño experimental

## Próximos pasos

### Hilos completados en análisis

1. **Hilo Programas completado** - crearPrograma(), editarPrograma(), eliminarPrograma()
2. **Hilo Cursos completado** - crearCurso(), editarCurso(), eliminarCurso()
3. **Hilo Profesores completado** - crearProfesor(), editarProfesor(), eliminarProfesor(), configurarPreferenciasProfesor()
4. **Hilo Edificios completado** - crearEdificio(), editarEdificio(), eliminarEdificio()
5. **Hilo Aulas completado** - crearAula(), editarAula(), eliminarAula()
6. **Hilo Recursos completado** - crearRecurso(), editarRecurso(), eliminarRecurso()
7. **Hilo Horarios completado** - generarHorario(), consultarHorario()
8. **Hilo Sistema completado** - iniciarSesion(), cerrarSesion(), completarGestion()

### Proyecto completado en análisis

- **Todos los hilos funcionales completados**
- **32 casos de uso con especificación detallada**
- **32 casos de uso con análisis MVC completo**
- **Metodología RUP aplicada sistemáticamente**

### Fase de diseño experimental (en progreso)

- **5 casos de uso diseñados** en 4 stacks tecnológicos diferentes:
  - FastAPI + React (frontend/backend)
  - Spring Boot + Angular (frontend/backend)
  - CLI Python + HTTP (cliente/servidor)
  - CLI Python Standalone (monolítico)
- **Objetivo**: Validar independencia tecnológica de RUP
- **Casos diseñados**: iniciarSesion, abrirAulas, crearAula, editarAula, eliminarAula
- **Próximo paso**: Ampliar diseño a más casos de uso según necesidad

## Metodología

Este dashboard se actualiza automáticamente conforme se completan las fases RUP para cada caso de uso:

1. **Identificado** → **Detalle/prototipado** → **Análisis** → **Diseño** → **Desarrollo** → **Pruebas** → **Completado**

El diagrama utiliza colores y estilos de línea específicos para mostrar visualmente el estado de cada transición entre estados del sistema.

## Referencias

- [Diagrama de contexto RUP puro](../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Documentación de casos de uso](../00-casos-uso/02-detalle/README.md)
- [Análisis de casos de uso](../01-analisis/casos-uso/README.md)
- [Conversation log](../../conversation-log.md)
