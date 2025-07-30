<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../../01-analisis/casos-uso/README.md)
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../conversation-log.md)

</div>

# Detalle y Prototipo de Casos de Uso

Esta carpeta contiene la especificación detallada y prototipado de cada caso de uso identificado en el sistema SigHor.

## Casos de uso especificados

### Gestión del sistema
- [startSession](startSession/README.md) - Autenticación de usuarios
- [closeSession](closeSession/README.md) - Cierre de sesión
- [completeManagement](completeManagement/README.md) - Hub de convergencia del sistema

### Apertura de entidades
- [openPrograms](openPrograms/README.md) - Gestión de programas académicos
- [openCourses](openCourses/README.md) - Gestión de cursos
- [openTeachers](openTeachers/README.md) - Gestión de profesores
- [openBuildings](openBuildings/README.md) - Gestión de edificios
- [openClassrooms](openClassrooms/README.md) - Gestión de aulas
- [openResources](openResources/README.md) - Gestión de recursos

### CRUD de Programas
- [createProgram](createProgram/README.md) - Creación de programas académicos
- [editProgram](editProgram/README.md) - Edición de programas académicos
- [deleteProgram](deleteProgram/README.md) - Eliminación de programas académicos

### CRUD de Cursos
- [createCourse](createCourse/README.md) - Creación de cursos académicos
- [editCourse](editCourse/README.md) - Edición de cursos académicos
- [deleteCourse](deleteCourse/README.md) - Eliminación de cursos académicos

### CRUD de Profesores
- [createTeacher](createTeacher/README.md) - Creación de profesores
- [editTeacher](editTeacher/README.md) - Edición de profesores
- [deleteTeacher](deleteTeacher/README.md) - Eliminación de profesores
- [configureTeacherPreferences](configureTeacherPreferences/README.md) - Configuración de preferencias de recursos
- [assignTeacherToCourse](assignTeacherToCourse/README.md) - Gestión de asignaciones profesor-curso

### CRUD de Edificios
- [createBuilding](createBuilding/README.md) - Creación de edificios
- [editBuilding](editBuilding/README.md) - Edición de edificios
- [deleteBuilding](deleteBuilding/README.md) - Eliminación de edificios

### CRUD de Aulas
- [createClassroom](createClassroom/README.md) - Creación de aulas
- [editClassroom](editClassroom/README.md) - Edición de aulas
- [deleteClassroom](deleteClassroom/README.md) - Eliminación de aulas

### CRUD de Recursos
- [createResource](createResource/README.md) - Creación de recursos
- [editResource](editResource/README.md) - Edición de recursos
- [deleteResource](deleteResource/README.md) - Eliminación de recursos

### Gestión de Horarios
- [generateSchedule](generateSchedule/README.md) - Generación automática de horarios
- [viewSchedule](viewSchedule/README.md) - Consulta de horarios generados

## Estructura de cada caso de uso

Cada carpeta de caso de uso contiene:

- **README.md** - Especificación completa del caso de uso
- **especificacion.puml** - Diagrama de especificación en PlantUML
- **prototipo.puml** o **wireframe.pml**- Wireframes de prototipado en Salt

## Metodología aplicada

- **Filosofía C→U** - Casos de creación vinculados automáticamente con edición
- **Patrones "el delgado" y "el gordo"** - Creación mínima vs edición completa
- **Leyes del proyecto** - Vocabulario restringido y diseño sin implementación
- **Tecnología agnóstica** - Especificaciones independientes de la implementación