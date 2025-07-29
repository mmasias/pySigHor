# Translation Mapping Table - Spanish to English

This document provides the complete mapping of identifiers from Spanish to English for the pySigHor RUP project.

## Domain Entities

| Spanish | English | Notes |
|---------|---------|-------|
| Profesor | Teacher | Academic instructor |
| Curso | Course | Academic course/subject |
| Aula | Classroom | Physical classroom space |
| Edificio | Building | Campus building |
| Programa | Program | Academic program/curriculum |
| Recurso | Resource | Classroom resource/equipment |
| BloqueHorario | TimeBlock | Predefined time pattern |
| Horario | Schedule | Generated timetable |

## Actors

| Spanish | English | Notes |
|---------|---------|-------|
| Administrador de Horarios | Schedule Administrator | System administrator role |
| Consultor de Horarios | Schedule Consultant | Read-only role |

## Use Cases (Method Names)

### Basic CRUD Operations
| Spanish | English | Notes |
|---------|---------|-------|
| abrirProgramas() | openPrograms() | |
| crearPrograma() | createProgram() | |
| editarPrograma() | editProgram() | |
| eliminarPrograma() | deleteProgram() | |
| abrirCursos() | openCourses() | |
| crearCurso() | createCourse() | |
| editarCurso() | editCourse() | |
| eliminarCurso() | deleteCourse() | |
| abrirProfesores() | openTeachers() | |
| crearProfesor() | createTeacher() | |
| editarProfesor() | editTeacher() | |
| eliminarProfesor() | deleteTeacher() | |
| abrirEdificios() | openBuildings() | |
| crearEdificio() | createBuilding() | |
| editarEdificio() | editBuilding() | |
| eliminarEdificio() | deleteBuilding() | |
| abrirAulas() | openClassrooms() | |
| crearAula() | createClassroom() | |
| editarAula() | editClassroom() | |
| eliminarAula() | deleteClassroom() | |
| abrirRecursos() | openResources() | |
| crearRecurso() | createResource() | |
| editarRecurso() | editResource() | |
| eliminarRecurso() | deleteResource() | |

### Specialized Operations
| Spanish | English | Notes |
|---------|---------|-------|
| configurarPreferenciasProfesor() | configureTeacherPreferences() | |
| asignarProfesorACurso() | assignTeacherToCourse() | |
| generarHorario() | generateSchedule() | |
| consultarHorario() | viewSchedule() | |
| iniciarSesion() | login() | |
| cerrarSesion() | logout() | |
| completarGestion() | completeManagement() | |

## System States

| Spanish | English | Notes |
|---------|---------|-------|
| SESION_CERRADA | SESSION_CLOSED | |
| SISTEMA_DISPONIBLE | SYSTEM_AVAILABLE | |
| PROGRAMAS_ABIERTO | PROGRAMS_OPEN | |
| PROGRAMA_ABIERTO | PROGRAM_OPEN | |
| CURSOS_ABIERTO | COURSES_OPEN | |
| CURSO_ABIERTO | COURSE_OPEN | |
| PROFESORES_ABIERTO | TEACHERS_OPEN | |
| PROFESOR_ABIERTO | TEACHER_OPEN | |
| PROFESOR_PREFERENCIAS_ABIERTO | TEACHER_PREFERENCES_OPEN | |
| PROFESOR_ASIGNATURAS_ABIERTO | TEACHER_ASSIGNMENTS_OPEN | |
| EDIFICIOS_ABIERTO | BUILDINGS_OPEN | |
| EDIFICIO_ABIERTO | BUILDING_OPEN | |
| AULAS_ABIERTO | CLASSROOMS_OPEN | |
| AULA_ABIERTA | CLASSROOM_OPEN | |
| RECURSOS_ABIERTO | RESOURCES_OPEN | |
| RECURSO_ABIERTO | RESOURCE_OPEN | |
| HORARIO_GENERADO | SCHEDULE_GENERATED | |
| HORARIO_ABIERTO | SCHEDULE_OPEN | |

## Analysis Classes

### View Classes
| Spanish | English | Notes |
|---------|---------|-------|
| AbrirProgramasView | OpenProgramsView | |
| AbrirCursosView | OpenCoursesView | |
| AbrirProfesoresView | OpenTeachersView | |
| AbrirEdificiosView | OpenBuildingsView | |
| AbrirAulasView | OpenClassroomsView | |
| AbrirRecursosView | OpenResourcesView | |
| CrearProgramaView | CreateProgramView | |
| CrearCursoView | CreateCourseView | |
| CrearProfesorView | CreateTeacherView | |
| CrearEdificioView | CreateBuildingView | |
| CrearAulaView | CreateClassroomView | |
| CrearRecursoView | CreateResourceView | |
| EditarProgramaView | EditProgramView | |
| EditarCursoView | EditCourseView | |
| EditarProfesorView | EditTeacherView | |
| EditarEdificioView | EditBuildingView | |
| EditarAulaView | EditClassroomView | |
| EditarRecursoView | EditResourceView | |
| ConfigurarPreferenciasView | ConfigurePreferencesView | |
| AsignarProfesorView | AssignTeacherView | |
| GenerarHorarioView | GenerateScheduleView | |
| ConsultarHorarioView | ViewScheduleView | |
| IniciarSesionView | LoginView | |

### Controller Classes
| Spanish | English | Notes |
|---------|---------|-------|
| ProgramasController | ProgramsController | |
| CursosController | CoursesController | |
| ProfesoresController | TeachersController | |
| EdificiosController | BuildingsController | |
| AulasController | ClassroomsController | |
| RecursosController | ResourcesController | |
| HorarioController | ScheduleController | |
| SesionController | SessionController | |

### Repository Classes
| Spanish | English | Notes |
|---------|---------|-------|
| ProgramaRepository | ProgramRepository | |
| CursoRepository | CourseRepository | |
| ProfesorRepository | TeacherRepository | |
| EdificioRepository | BuildingRepository | |
| AulaRepository | ClassroomRepository | |
| RecursoRepository | ResourceRepository | |
| HorarioRepository | ScheduleRepository | |

## Entity Classes (Analysis)
| Spanish | English | Notes |
|---------|---------|-------|
| Programa | Program | |
| Curso | Course | |
| Profesor | Teacher | |
| Edificio | Building | |
| Aula | Classroom | |
| Recurso | Resource | |
| Horario | Schedule | |

## Method Names in Classes

### Repository Methods
| Spanish | English | Notes |
|---------|---------|-------|
| obtenerTodos() | getAll() | |
| obtenerPorId() | getById() | |
| buscarPorCriterio() | findByCriteria() | |
| guardar() | save() | |
| eliminar() | delete() | |
| actualizar() | update() | |

### Controller Methods
| Spanish | English | Notes |
|---------|---------|-------|
| listarProgramas() | listPrograms() | |
| listarCursos() | listCourses() | |
| listarProfesores() | listTeachers() | |
| listarEdificios() | listBuildings() | |
| listarAulas() | listClassrooms() | |
| listarRecursos() | listResources() | |
| filtrarCursos() | filterCourses() | |
| filtrarProfesores() | filterTeachers() | |
| validarDatos() | validateData() | |
| procesarFormulario() | processForm() | |

## Relationships and Associations

| Spanish | English | Notes |
|---------|---------|-------|
| imparte | teaches | Teacher-Course relationship |
| ofrece | offers | Classroom-Resource relationship |
| prefiere | prefers | Teacher-Resource relationship |

## System Name

| Spanish | English | Notes |
|---------|---------|-------|
| SigHor | ScheduleGen | Could also be "TimetableGen" |

## Package Names

| Spanish | English | Notes |
|---------|---------|-------|
| CampusUniversitario | UniversityCampus | |

## Notes

- **Consistency Rule**: Each Spanish term must always map to the same English term across all artifacts
- **Naming Conventions**: 
  - Classes use PascalCase (e.g., `TeacherController`)
  - Methods use camelCase (e.g., `createCourse()`)
  - Constants use UPPER_SNAKE_CASE (e.g., `COURSES_OPEN`)
- **Domain Context**: All translations maintain the academic/university domain semantics