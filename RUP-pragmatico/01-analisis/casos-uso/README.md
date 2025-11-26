# Análisis de Casos de Uso - vPragmática

<div align=center>

**Versión simplificada y orientada a la práctica de la documentación RUP**  
*Enfocada en artefactos clave para comprensión rápida y eficiente*

|||||
|-|-|-|-|
|[Inicio](../../README.md)|[Modelo del dominio](../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)|[Casos de uso](../../00-casos-uso/02-detalle/README.md)|**Análisis**|

</div>

## Casos de uso analizados

### Gestión del sistema
- [iniciarSesion](./iniciarSesion/README.md) - Análisis de autenticación de usuarios
- [cerrarSesion](./cerrarSesion/README.md) - Análisis de cierre de sesión
- [completarGestion](./completarGestion/README.md) - Análisis del hub de convergencia del sistema

### Apertura de entidades
- [abrirProgramas](./abrirProgramas/README.md) - Análisis de gestión de programas académicos
- [abrirCursos](./abrirCursos/README.md) - Análisis de gestión de cursos
- [abrirProfesores](./abrirProfesores/README.md) - Análisis de gestión de profesores
- [abrirEdificios](./abrirEdificios/README.md) - Análisis de gestión de edificios
- [abrirAulas](./abrirAulas/README.md) - Análisis de gestión de aulas
- [abrirRecursos](./abrirRecursos/README.md) - Análisis de gestión de recursos

### Análisis de los *CRUD*s

|Programas|Cursos|Aulas|Edificios|Profesores|Recursos|
|-|-|-|-|-|-|
|[crearPrograma()](./crearPrograma/README.md)|[crearCurso()](./crearCurso/README.md)|[crearAula()](./crearAula/README.md)|[crearEdificio()](./crearEdificio/README.md)|[crearProfesor()](./crearProfesor/README.md)|[crearRecurso()](./crearRecurso/README.md)|
|[editarPrograma()](./editarPrograma/README.md)|[editarCurso()](./editarCurso/README.md)|[editarAula()](./editarAula/README.md)|[editarEdificio()](./editarEdificio/README.md)|[editarProfesor()](./editarProfesor/README.md)|[editarRecurso()](./editarRecurso/README.md)|
|[eliminarPrograma()](./eliminarPrograma/README.md)|[eliminarCurso()](./eliminarCurso/README.md)|[eliminarAula()](./eliminarAula/README.md)|[eliminarEdificio()](./eliminarEdificio/README.md)|[eliminarProfesor()](./eliminarProfesor/README.md)|[eliminarRecurso()](./eliminarRecurso/README.md)|

### Operaciones de Horarios
- [consultarHorario](./consultarHorario/README.md) - Análisis de consulta de horarios
- [generarHorario](./generarHorario/README.md) - Análisis de generación de horarios
