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

### Casos de uso identificados & avance

<!-- 
Emojis para fases futuras:
- 🏗️ Diseño: Arquitectura/estructura
- 💻 Desarrollo: Programación/implementación  
- 🧪 Pruebas: Testing/validación
-->

<div align=center>

|Caso de uso|[Detalle](/RUP/00-casos-uso/02-detalle/README.md)|Prototipo|[Análisis](/RUP/01-analisis/casos-uso/README.md)|Diseño|Desarrollo|Pruebas|Comentario|
|-|:-:|:-:|:-:|:-:|:-:|:-:|-|
|**startSession()**                   |[📋](/RUP/00-casos-uso/02-detalle/startSession/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/startSession/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/startSession/README.md)|⚪|⚪|⚪|*Punto de entrada al sistema*
|**completeManagement()**             |[📋](/RUP/00-casos-uso/02-detalle/completeManagement/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/completeManagement/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/completeManagement/README.md)|⚪|⚪|⚪|*Hub de convergencia del sistema*
|**openPrograms()**                   |[📋](/RUP/00-casos-uso/02-detalle/openPrograms/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/openPrograms/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/openPrograms/README.md)|⚪|⚪|⚪|*Patrón de apertura de entidades*
|**openCourses()**                    |[📋](/RUP/00-casos-uso/02-detalle/openCourses/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/openCourses/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/openCourses/README.md)|⚪|⚪|⚪|
|**openTeachers()**                   |[📋](/RUP/00-casos-uso/02-detalle/openTeachers/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/openTeachers/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/openTeachers/README.md)|⚪|⚪|⚪|
|**openBuildings()**                  |[📋](/RUP/00-casos-uso/02-detalle/openBuildings/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/openBuildings/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/openBuildings/README.md)|⚪|⚪|⚪|
|**openClassrooms()**                 |[📋](/RUP/00-casos-uso/02-detalle/openClassrooms/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/openClassrooms/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/openClassrooms/README.md)|⚪|⚪|⚪|
|**openResources()**                  |[📋](/RUP/00-casos-uso/02-detalle/openResources/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/openResources/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/openResources/README.md)|⚪|⚪|⚪|
|**createProgram()**                  |[📋](/RUP/00-casos-uso/02-detalle/createProgram/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/createProgram/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/createProgram/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U*
|**editProgram()**                    |[📋](/RUP/00-casos-uso/02-detalle/editProgram/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editProgram/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editProgram/README.md)|⚪|⚪|⚪|*Aplicando filosofía C→U*
|**deleteProgram()**                  |[📋](/RUP/00-casos-uso/02-detalle/deleteProgram/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/deleteProgram/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/deleteProgram/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación*
|**createCourse()**                   |[📋](/RUP/00-casos-uso/02-detalle/createCourse/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/createCourse/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/createCourse/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U completa*
|**editCourse()**                     |[📋](/RUP/00-casos-uso/02-detalle/editCourse/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editCourse/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editCourse/README.md)|⚪|⚪|⚪|*"El gordo" con edición continua completa*
|**deleteCourse()**                   |[📋](/RUP/00-casos-uso/02-detalle/deleteCourse/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/deleteCourse/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/deleteCourse/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación completa*
|**createTeacher()**                  |[📋](/RUP/00-casos-uso/02-detalle/createTeacher/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/createTeacher/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/createTeacher/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U - CORREGIDO*
|**editTeacher()**                    |[📋](/RUP/00-casos-uso/02-detalle/editTeacher/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editTeacher/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editTeacher/README.md)|⚪|⚪|⚪|*"El gordo" con edición continua - CORREGIDO*
|**deleteTeacher()**                  |[📋](/RUP/00-casos-uso/02-detalle/deleteTeacher/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/deleteTeacher/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/deleteTeacher/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación - CORREGIDO*
|**configureTeacherPreferences()**    |[📋](/RUP/00-casos-uso/02-detalle/configureTeacherPreferences/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/configureTeacherPreferences/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/configureTeacherPreferences/README.md)|⚪|⚪|⚪|*Configuración específica de recursos*
|**createBuilding()**                 |[📋](/RUP/00-casos-uso/02-detalle/createBuilding/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/createBuilding/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/createBuilding/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U*
|**editBuilding()**                   |[📋](/RUP/00-casos-uso/02-detalle/editBuilding/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editBuilding/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editBuilding/README.md)|⚪|⚪|⚪|*"El gordo" con edición continua*
|**deleteBuilding()**                 |[📋](/RUP/00-casos-uso/02-detalle/deleteBuilding/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/deleteBuilding/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/deleteBuilding/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación*
|**createClassroom()**                |[📋](/RUP/00-casos-uso/02-detalle/createClassroom/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/createClassroom/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/createClassroom/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U*
|**editClassroom()**                  |[📋](/RUP/00-casos-uso/02-detalle/editClassroom/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editClassroom/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editClassroom/README.md)|⚪|⚪|⚪|*"El gordo" con edición continua*
|**deleteClassroom()**                |[📋](/RUP/00-casos-uso/02-detalle/deleteClassroom/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/deleteClassroom/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/deleteClassroom/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación*
|**createResource()**                 |[📋](/RUP/00-casos-uso/02-detalle/createResource/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/createResource/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/createResource/README.md)|⚪|⚪|⚪|*"El delgado" filosofía C→U*
|**editResource()**                   |[📋](/RUP/00-casos-uso/02-detalle/editResource/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/editResource/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/editResource/README.md)|⚪|⚪|⚪|*"El gordo" con edición continua*
|**deleteResource()**                 |[📋](/RUP/00-casos-uso/02-detalle/deleteResource/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/deleteResource/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/deleteResource/README.md)|⚪|⚪|⚪|*Eliminación segura con confirmación*
|**assignTeacherToCourse()**          |[📋](/RUP/00-casos-uso/02-detalle/assignTeacherToCourse/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/assignTeacherToCourse/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/assignTeacherToCourse/README.md)|⚪|⚪|⚪|*Gestión de asignaciones profesor-curso*
|**generateSchedule()**               |[📋](/RUP/00-casos-uso/02-detalle/generateSchedule/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/generateSchedule/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/generateSchedule/README.md)|⚪|⚪|⚪|*Proceso algorítmico de 4 fases*
|**viewSchedule()**                   |[📋](/RUP/00-casos-uso/02-detalle/viewSchedule/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/viewSchedule/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/viewSchedule/README.md)|⚪|⚪|⚪|*Visualización simple del horario académico*
|**closeSession()**                   |[📋](/RUP/00-casos-uso/02-detalle/closeSession/README.md#diagrama-de-especificación)|[🎨](/RUP/00-casos-uso/02-detalle/closeSession/README.md#wireframes)|[🔍](/RUP/01-analisis/casos-uso/closeSession/README.md)|⚪|⚪|⚪|*Validación de estado de sesión*

</div>

