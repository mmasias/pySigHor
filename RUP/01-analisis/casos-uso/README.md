<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../../00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](README.md)
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../conversation-log.md)

</div>

# Análisis de Casos de Uso

Esta carpeta contiene el análisis MVC (Model-View-Controller) de cada caso de uso especificado, incluyendo diagramas de colaboración y secuencia.

## Casos de uso analizados

### Gestión del sistema
- [iniciarSesion](iniciarSesion/) - Autenticación con clases de análisis MVC
- [cerrarSesion](cerrarSesion/) - Cierre de sesión con validación de estado
- [completarGestion](completarGestion/) - Hub de convergencia con coordinación de colaboraciones

### Apertura de entidades
- [abrirProgramas](abrirProgramas/) - Gestión de vista de listado de programas
- [abrirCursos](abrirCursos/) - Gestión de vista de listado de cursos
- [abrirProfesores](abrirProfesores/) - Gestión de vista de listado de profesores
- [abrirEdificios](abrirEdificios/) - Gestión de vista de listado de edificios
- [abrirAulas](abrirAulas/) - Gestión de vista de listado de aulas
- [abrirRecursos](abrirRecursos/) - Gestión de vista de listado de recursos

### CRUD de Programas
- [crearPrograma](crearPrograma/) - Análisis de creación con filosofía C→U
- [editarPrograma](editarPrograma/) - Análisis de edición continua "el gordo"
- [eliminarPrograma](eliminarPrograma/) - Análisis de eliminación segura

### CRUD de Cursos (Completo)
- [crearCurso](crearCurso/) - Análisis completo con colaboración y secuencia
- [editarCurso](editarCurso/) - Análisis completo con colaboración y secuencia
- [eliminarCurso](eliminarCurso/) - Análisis de eliminación segura de cursos

### CRUD de Profesores
- [crearProfesor](crearProfesor/) - Análisis de creación con filosofía C→U
- [editarProfesor](editarProfesor/) - Análisis de edición continua "el gordo"
- [eliminarProfesor](eliminarProfesor/) - Análisis de eliminación segura
- [configurarPreferenciasProfesor](configurarPreferenciasProfesor/) - Análisis de configuración específica
- [asignarProfesorACurso](asignarProfesorACurso/) - Análisis de gestión de asignaciones profesor-curso

### CRUD de Edificios
- [crearEdificio](crearEdificio/) - Análisis de creación con relación a aulas
- [editarEdificio](editarEdificio/) - Análisis de edición con impacto en aulas
- [eliminarEdificio](eliminarEdificio/) - Análisis de eliminación con validación de dependencias

### CRUD de Aulas
- [crearAula](crearAula/) - Análisis de creación con asignación de edificio y recursos
- [editarAula](editarAula/) - Análisis de edición con gestión de recursos y capacidad
- [eliminarAula](eliminarAula/) - Análisis de eliminación con validación de horarios

### CRUD de Recursos
- [crearRecurso](crearRecurso/) - Análisis de creación de recursos para aulas
- [editarRecurso](editarRecurso/) - Análisis de edición con impacto en preferencias
- [eliminarRecurso](eliminarRecurso/) - Análisis de eliminación con validación de asignaciones

### Gestión de Horarios
- [generarHorario](generarHorario/) - Análisis del algoritmo de optimización
- [consultarHorario](consultarHorario/) - Análisis de consulta y filtrado de horarios

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

## Análisis Consolidado

### Consolidación de Métodos
- **[Consolidación de Métodos de Clases](../consolidacion-metodos-clases.md)** - Mapa detallado de interfaces para especificación de componentes
- **[Diagrama de Clases Consolidado](../consolidacion-metodos-clases.puml)** - 73 clases de análisis con métodos completos
- **[Reporte de Inconsistencias](../reporte-inconsistencias.md)** - Análisis de duplicaciones y recomendaciones de refactorización

### Estadísticas del Análisis
- **Total clases consolidadas**: 73 de 31 casos de uso
- **Distribución**: 31 Views, 18 Controllers, 24 Entities
- **Métodos únicos**: 186 con análisis de consistencia
- **Patrones identificados**: CRUD, Repository, Controller, View