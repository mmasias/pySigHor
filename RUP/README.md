<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](01-analisis/casos-uso/README.md)
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../conversation-log.md)

</div>

# Reingeniería usando RUP

Esto a modo de mapa inicial, luego lo refinamos. También hay una [propuesta de dashboard de seguimiento](99-seguimiento/README.md). y el [seguimiento de toda la interacción](../conversation-log.md).

## Disciplinas RUP

- [00 - Modelo del dominio](/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md#diagrama)

- [01 - Actores y casos de uso](/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso.md#diagrama)

  - [Diagrama de contexto (actor administrador)](/RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md#diagrama)

- [02 - Diseño](/RUP/02-diseño/README.md)

### Casos de uso identificados & avance

<!-- 
Emojis para fases futuras:
- 🏗️ Diseño: Arquitectura/estructura
- 💻 Desarrollo: Programación/implementación  
- 🧪 Pruebas: Testing/validación
-->

<div align=center>

|Caso de uso|[Detalle](/RUP/00-casos-uso/02-detalle/README.md)|Prototipo|[Análisis](/RUP/01-analisis/casos-uso/README.md)|[Diseño](/RUP/02-diseño/README.md)|Desarrollo|Pruebas|Comentario|
|-|:-:|:-:|:-:|:-:|:-:|:-:|-|
|**iniciarSesion()** |[📋](/RUP/00-casos-uso/02-detalle/iniciarSesion/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/iniciarSesion/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/iniciarSesion/README.md)|[🏗️](/RUP/02-diseño/casos-uso/iniciarSesion/README.md)|[💻](/RUP/03-desarrollo/casos-uso/iniciarSesion/README.md)|⚪|*Punto de entrada al sistema*
|***completarGestion()***   |[📋](/RUP/00-casos-uso/02-detalle/completarGestion/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/completarGestion/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/completarGestion/README.md)|⚪|⚪|⚪|*Hub de convergencia del sistema*
|**abrirProgramas()**|[📋](/RUP/00-casos-uso/02-detalle/abrirProgramas/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/abrirProgramas/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/abrirProgramas/README.md)|⚪|⚪|⚪|*Patrón de apertura de entidades*
|**abrirCursos()**|[📋](/RUP/00-casos-uso/02-detalle/abrirCursos/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/abrirCursos/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/abrirCursos/README.md)|⚪|⚪|⚪|
|**abrirProfesores()**|[📋](/RUP/00-casos-uso/02-detalle/abrirProfesores/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/abrirProfesores/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/abrirProfesores/README.md)|⚪|⚪|⚪|
|**abrirEdificios()**|[📋](/RUP/00-casos-uso/02-detalle/abrirEdificios/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/abrirEdificios/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/abrirEdificios/README.md)|[🏗️](/RUP/02-diseño/casos-uso/abrirEdificios/README.md)|⚪|⚪|
|**abrirAulas()**|[📋](/RUP/00-casos-uso/02-detalle/abrirAulas/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/abrirAulas/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/abrirAulas/README.md)|[🏗️](/RUP/02-diseño/casos-uso/abrirAulas/README.md)|[💻](/RUP/03-desarrollo/casos-uso/abrirAulas/README.md)|⚪|⚪|
|**abrirRecursos()**|[📋](/RUP/00-casos-uso/02-detalle/abrirRecursos/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/abrirRecursos/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/abrirRecursos/README.md)|⚪|⚪|⚪|
|**crearPrograma()**|[📋](/RUP/00-casos-uso/02-detalle/crearPrograma/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/crearPrograma/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/crearPrograma/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U*
|**editarPrograma()**|[📋](/RUP/00-casos-uso/02-detalle/editarPrograma/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editarPrograma/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editarPrograma/README.md)|⚪|⚪|⚪|*Aplicando filosofía C→U*
|**eliminarPrograma()**|[📋](/RUP/00-casos-uso/02-detalle/eliminarPrograma/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/eliminarPrograma/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/eliminarPrograma/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación*
|**crearCurso()**|[📋](/RUP/00-casos-uso/02-detalle/crearCurso/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/crearCurso/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/crearCurso/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U completa*
|**editarCurso()**|[📋](/RUP/00-casos-uso/02-detalle/editarCurso/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editarCurso/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editarCurso/README.md)|⚪|⚪|⚪|*"El gordo" con edición continua completa*
|**eliminarCurso()**|[📋](/RUP/00-casos-uso/02-detalle/eliminarCurso/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/eliminarCurso/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/eliminarCurso/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación completa*
|**crearProfesor()**|[📋](/RUP/00-casos-uso/02-detalle/crearProfesor/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/crearProfesor/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/crearProfesor/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U - CORREGIDO*
|**editarProfesor()**|[📋](/RUP/00-casos-uso/02-detalle/editarProfesor/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editarProfesor/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editarProfesor/README.md)|⚪|⚪|⚪|*"El gordo" con edición continua - CORREGIDO*
|**eliminarProfesor()**|[📋](/RUP/00-casos-uso/02-detalle/eliminarProfesor/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/eliminarProfesor/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/eliminarProfesor/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación - CORREGIDO*
|**configurarPreferenciasProfesor()**|[📋](/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/configurarPreferenciasProfesor/README.md)|⚪|⚪|⚪|*Configuración específica de recursos*
|**crearEdificio()**|[📋](/RUP/00-casos-uso/02-detalle/crearEdificio/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/crearEdificio/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/crearEdificio/README.md)|[🏗️](/RUP/02-diseño/casos-uso/crearEdificio/README.md)|⚪|⚪|*"El delgado" filosofía C→U*
|**editarEdificio()**|[📋](/RUP/00-casos-uso/02-detalle/editarEdificio/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editarEdificio/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editarEdificio/README.md)|[🏗️](/RUP/02-diseño/casos-uso/editarEdificio/README.md)|⚪|⚪|*"El gordo" con edición continua*
|**eliminarEdificio()**|[📋](/RUP/00-casos-uso/02-detalle/eliminarEdificio/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/eliminarEdificio/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/eliminarEdificio/README.md)|[🏗️](/RUP/02-diseño/casos-uso/eliminarEdificio/README.md)|⚪|⚪|*Eliminación segura con confirmación*
|**crearAula()**|[📋](/RUP/00-casos-uso/02-detalle/crearAula/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/crearAula/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/crearAula/README.md)|[🏗️](/RUP/02-diseño/casos-uso/crearAula/README.md)|[💻](/RUP/03-desarrollo/casos-uso/crearAula/README.md)|⚪|⚪|*"El delgado" filosofía C→U*
|**editarAula()**|[📋](/RUP/00-casos-uso/02-detalle/editarAula/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editarAula/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editarAula/README.md)|[🏗️](/RUP/02-diseño/casos-uso/editarAula/README.md)|[💻](/RUP/03-desarrollo/casos-uso/editarAula/README.md)|⚪|⚪|*"El gordo" con edición continua*
|**eliminarAula()**|[📋](/RUP/00-casos-uso/02-detalle/eliminarAula/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/eliminarAula/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/eliminarAula/README.md)|[🏗️](/RUP/02-diseño/casos-uso/eliminarAula/README.md)|[💻](/RUP/03-desarrollo/casos-uso/eliminarAula/README.md)|⚪|⚪|*Eliminación segura con confirmación*
|**crearRecurso()**|[📋](/RUP/00-casos-uso/02-detalle/crearRecurso/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/crearRecurso/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/crearRecurso/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U*
|**editarRecurso()**|[📋](/RUP/00-casos-uso/02-detalle/editarRecurso/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editarRecurso/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editarRecurso/README.md)|⚪|⚪|⚪|*"El gordo" con edición continua*
|**eliminarRecurso()**|[📋](/RUP/00-casos-uso/02-detalle/eliminarRecurso/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/eliminarRecurso/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/eliminarRecurso/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación*
|**asignarProfesorACurso()**|[📋](/RUP/00-casos-uso/02-detalle/asignarProfesorACurso/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/asignarProfesorACurso/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/asignarProfesorACurso/README.md)|⚪|⚪|⚪|*Gestión de asignaciones profesor-curso*
|**generarHorario()**|[📋](/RUP/00-casos-uso/02-detalle/generarHorario/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/generarHorario/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/generarHorario/README.md)|⚪|⚪|⚪|*Proceso algorítmico de 4 fases*
|**consultarHorario()**|[📋](/RUP/00-casos-uso/02-detalle/consultarHorario/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/consultarHorario/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/consultarHorario/README.md)|⚪|⚪|⚪|*Visualización simple del horario académico*
|**cerrarSesion()**|[📋](/RUP/00-casos-uso/02-detalle/cerrarSesion/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/cerrarSesion/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/cerrarSesion/README.md)|⚪|⚪|⚪|*Validación de estado de sesión*

</div>

