# Casos de Uso - vPragmática

<div align=center>

**Versión simplificada y orientada a la práctica de la documentación RUP**  
*Enfocada en artefactos clave para comprensión rápida y eficiente*

|||||
|-|-|-|-|
|[Inicio](../../README.md)|[Modelo del dominio](../00-modelo-del-dominio/modelo-dominio.md)|**Casos de uso**|[Análisis](../../01-analisis/casos-uso/README.md)|

</div>

## Actores y casos de uso identificados

<div align=center>

||||
|:-:|:-:|:-:|
|![Actores y Casos de Uso](/images/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-001.svg)|![Actores y Casos de Uso](/images/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-002.svg)|![Actores y Casos de Uso](/images/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-003.svg)
|Código fuente:[actores-casos-uso-001.puml](actores-casos-uso-001.puml)|Código fuente: [actores-casos-uso-002.puml](actores-casos-uso-002.puml)|Código fuente: [actores-casos-uso-003.puml](actores-casos-uso-003.puml)

</div>

## Diagrama de contexto

<div align=center>

![](/images/RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.svg)

</div>

## Detalle de los casos de uso

### Gestión del sistema
- [iniciarSesion](./iniciarSesion/README.md) - Autenticación de usuarios
- [cerrarSesion](./cerrarSesion/README.md) - Cierre de sesión
- [completarGestion](./completarGestion/README.md) - Hub de convergencia del sistema

### Apertura de entidades
- [abrirProgramas](./abrirProgramas/README.md) - Gestión de programas académicos
- [abrirCursos](./abrirCursos/README.md) - Gestión de cursos
- [abrirProfesores](./abrirProfesores/README.md) - Gestión de profesores
- [abrirEdificios](./abrirEdificios/README.md) - Gestión de edificios
- [abrirAulas](./abrirAulas/README.md) - Gestión de aulas
- [abrirRecursos](./abrirRecursos/README.md) - Gestión de recursos

### CRUD de Programas
- [crearPrograma](./crearPrograma/README.md) - Creación de programas académicos
- [editarPrograma](./editarPrograma/README.md) - Edición de programas académicos
- [eliminarPrograma](./eliminarPrograma/README.md) - Eliminación de programas académicos

### CRUD de Cursos
- [crearCurso](./crearCurso/README.md) - Creación de cursos académicos
- [editarCurso](./editarCurso/README.md) - Edición de cursos académicos
- [eliminarCurso](./eliminarCurso/README.md) - Eliminación de cursos académicos

### CRUD de Aulas
- [crearAula](./crearAula/README.md) - Creación de aulas
- [editarAula](./editarAula/README.md) - Edición de aulas
- [eliminarAula](./eliminarAula/README.md) - Eliminación de aulas

### CRUD de Edificios
- [crearEdificio](./crearEdificio/README.md) - Creación de edificios
- [editarEdificio](./editarEdificio/README.md) - Edición de edificios
- [eliminarEdificio](./eliminarEdificio/README.md) - Eliminación de edificios

### CRUD de Profesores
- [crearProfesor](./crearProfesor/README.md) - Creación de profesores
- [editarProfesor](./editarProfesor/README.md) - Edición de profesores
- [eliminarProfesor](./eliminarProfesor/README.md) - Eliminación de profesores

### CRUD de Recursos
- [crearRecurso](./crearRecurso/README.md) - Creación de recursos
- [editarRecurso](./editarRecurso/README.md) - Edición de recursos
- [eliminarRecurso](./eliminarRecurso/README.md) - Eliminación de recursos

### Operaciones de Horarios
- [consultarHorario](./consultarHorario/README.md) - Consulta de horarios
- [generarHorario](./generarHorario/README.md) - Generación de horarios
