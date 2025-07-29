<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../../01-analisis/casos-uso/README.md)
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../conversation-log.md)

</div>

# Detalle y Prototipo de Casos de Uso

Esta carpeta contiene la especificación detallada y prototipado de cada caso de uso identificado en el sistema SigHor.

## Casos de uso especificados

### Gestión del sistema
- [startSession](startSession/) - Autenticación de usuarios
- [closeSession](closeSession/) - Cierre de sesión
- [completeManagement](completeManagement/) - Hub de convergencia del sistema

### Apertura de entidades
- [openPrograms](openPrograms/) - Gestión de programas académicos
- [openCourses](openCourses/) - Gestión de cursos
- [openTeachers](openTeachers/) - Gestión de profesores
- [openBuildings](openBuildings/) - Gestión de edificios
- [openClassrooms](openClassrooms/) - Gestión de aulas
- [openResources](openResources/) - Gestión de recursos

### CRUD de Programas
- [createProgram](createProgram/) - Creación de programas académicos
- [editProgram](editProgram/) - Edición de programas académicos
- [deleteProgram](deleteProgram/) - Eliminación de programas académicos

### CRUD de Cursos
- [createCourse](createCourse/) - Creación de cursos académicos
- [editCourse](editCourse/) - Edición de cursos académicos
- [deleteCourse](deleteCourse/) - Eliminación de cursos académicos

### CRUD de Profesores
- [createTeacher](createTeacher/) - Creación de profesores
- [editTeacher](editTeacher/) - Edición de profesores
- [deleteTeacher](deleteTeacher/) - Eliminación de profesores
- [configureTeacherPreferences](configureTeacherPreferences/) - Configuración de preferencias de recursos
- [assignTeacherToCourse](assignTeacherToCourse/) - Gestión de asignaciones profesor-curso

### CRUD de Edificios
- [createBuilding](createBuilding/) - Creación de edificios
- [editBuilding](editBuilding/) - Edición de edificios
- [deleteBuilding](deleteBuilding/) - Eliminación de edificios

### CRUD de Aulas
- [createClassroom](createClassroom/) - Creación de aulas
- [editClassroom](editClassroom/) - Edición de aulas
- [deleteClassroom](deleteClassroom/) - Eliminación de aulas

### CRUD de Recursos
- [createResource](createResource/) - Creación de recursos
- [editResource](editResource/) - Edición de recursos
- [deleteResource](deleteResource/) - Eliminación de recursos

### Gestión de Horarios
- [generateSchedule](generateSchedule/) - Generación automática de horarios
- [viewSchedule](viewSchedule/) - Consulta de horarios generados

## Estructura de cada caso de uso

Cada carpeta de caso de uso contiene:

- **README.md** - Especificación completa del caso de uso
- **especificacion.puml** - Diagrama de especificación en PlantUML
- **prototipo.puml** - Wireframes de prototipado en Salt

## Metodología aplicada

- **Filosofía C→U** - Casos de creación vinculados automáticamente con edición
- **Patrones "el delgado" y "el gordo"** - Creación mínima vs edición completa
- **Leyes del proyecto** - Vocabulario restringido y diseño sin implementación
- **Tecnología agnóstica** - Especificaciones independientes de la implementación