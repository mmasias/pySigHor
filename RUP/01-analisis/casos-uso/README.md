<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../../00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](README.md)
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../conversation-log.md)

</div>

# Análisis de Casos de Uso

Esta carpeta contiene el análisis MVC (Model-View-Controller) de cada caso de uso especificado, incluyendo diagramas de colaboración y secuencia.

## Casos de uso analizados

### Gestión del sistema
- [startSession](startSession/README.md) - Autenticación con clases de análisis MVC
- [endSession](endSession/README.md) - Cierre de sesión con validación de estado
- [completeManagement](completeManagement/README.md) - Hub de convergencia con coordinación de colaboraciones

### Apertura de entidades
- [openPrograms](openPrograms/README.md) - Gestión de vista de listado de programas
- [openCourses](openCourses/README.md) - Gestión de vista de listado de cursos
- [openTeachers](openTeachers/README.md) - Gestión de vista de listado de profesores
- [openBuildings](openBuildings/README.md) - Gestión de vista de listado de edificios
- [openClassrooms](openClassrooms/README.md) - Gestión de vista de listado de aulas
- [openResources](openResources/README.md) - Gestión de vista de listado de recursos

### CRUD de Programas
- [createProgram](createProgram/README.md) - Análisis de creación con filosofía C→U
- [editProgram](editProgram/README.md) - Análisis de edición continua "el gordo"
- [deleteProgram](deleteProgram/README.md) - Análisis de eliminación segura

### CRUD de Cursos (Completo)
- [createCourse](createCourse/README.md) - Análisis completo con colaboración y secuencia
- [editCourse](editCourse/README.md) - Análisis completo con colaboración y secuencia
- [deleteCourse](deleteCourse/README.md) - Análisis de eliminación segura de cursos

### CRUD de Profesores
- [createTeacher](createTeacher/README.md) - Análisis de creación con filosofía C→U
- [editTeacher](editTeacher/README.md) - Análisis de edición continua "el gordo"
- [deleteTeacher](deleteTeacher/README.md) - Análisis de eliminación segura
- [configureTeacherPreferences](configureTeacherPreferences/README.md) - Análisis de configuración específica
- [assignTeacherToCourse](assignTeacherToCourse/README.md) - Análisis de gestión de asignaciones profesor-curso

### CRUD de Edificios
- [createBuilding](createBuilding/README.md) - Análisis de creación con relación a aulas
- [editBuilding](editBuilding/README.md) - Análisis de edición con impacto en aulas
- [deleteBuilding](deleteBuilding/README.md) - Análisis de eliminación con validación de dependencias

### CRUD de Aulas
- [createClassroom](createClassroom/README.md) - Análisis de creación con asignación de edificio y recursos
- [editClassroom](editClassroom/README.md) - Análisis de edición con gestión de recursos y capacidad
- [deleteClassroom](deleteClassroom/README.md) - Análisis de eliminación con validación de horarios

### CRUD de Recursos
- [createResource](createResource/README.md) - Análisis de creación de recursos para aulas
- [editResource](editResource/README.md) - Análisis de edición con impacto en preferencias
- [deleteResource](deleteResource/README.md) - Análisis de eliminación con validación de asignaciones

### Gestión de Horarios
- [generateSchedule](generateSchedule/README.md) - Análisis del algoritmo de optimización
- [viewSchedule](viewSchedule/README.md) - Análisis de consulta y filtrado de horarios

## Estructura de análisis

Cada carpeta de análisis contiene:

- **README.md** - Análisis MVC completo del caso de uso
- **colaboracion.puml** - Diagrama de colaboración entre clases de análisis
- **secuencia.puml** - Diagrama de secuencia (para casos complejos)

## Clases de análisis aplicadas

### Boundary (Vista)
- Clases de interfaz que manejan la interacción con el actor
- Responsables de presentar datos y capturar solicitudes

### Control (Controlador)
- Clases que coordinan la lógica del caso de uso
- Orquestan las colaboraciones entre boundary y entity

### Entity (Entidad)
- Clases que representan conceptos del dominio
- Repositories y entidades de negocio

## Metodología de análisis

- **Patrón MVC** aplicado sistemáticamente
- **Colaboraciones explícitas** entre clases de análisis
- **Secuencias detalladas** para casos de uso complejos (CRUD completo)
- **Trazabilidad** desde especificación hasta análisis
- **Nomenclatura consistente** con las leyes del proyecto