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

- [iniciarSesion](./iniciarSesion/README.md)
- [cerrarSesion](./cerrarSesion/README.md)
- [completarGestion](./completarGestion/README.md) - Hub de convergencia del sistema

### Apertura de entidades (a.k.a. "*gestión*")

- [abrirProgramas](./abrirProgramas/README.md) - Gestión de programas académicos
- [abrirCursos](./abrirCursos/README.md) - Gestión de cursos
- [abrirProfesores](./abrirProfesores/README.md) - Gestión de profesores
- [abrirEdificios](./abrirEdificios/README.md) - Gestión de edificios
- [abrirAulas](./abrirAulas/README.md) - Gestión de aulas
- [abrirRecursos](./abrirRecursos/README.md) - Gestión de recursos

### Los *CRUD*s

|Programas|Cursos|Aulas|Edificios|Profesores|Recursos|
|-|-|-|-|-|-|
|[crearPrograma()](./crearPrograma/README.md)|[crearCurso()](./crearCurso/README.md)|[crearAula()](./crearAula/README.md)|[crearEdificio()](./crearEdificio/README.md)|[crearProfesor()](./crearProfesor/README.md)|[crearRecurso()](./crearRecurso/README.md)|
|[editarPrograma()](./editarPrograma/README.md)|[editarCurso()](./editarCurso/README.md)|[editarAula()](./editarAula/README.md)|[editarEdificio()](./editarEdificio/README.md)|[editarProfesor()](./editarProfesor/README.md)|[editarRecurso()](./editarRecurso/README.md)|
|[eliminarPrograma()](./eliminarPrograma/README.md)|[eliminarCurso()](./eliminarCurso/README.md)|[eliminarAula()](./eliminarAula/README.md)|[eliminarEdificio()](./eliminarEdificio/README.md)|[eliminarProfesor()](./eliminarProfesor/README.md)|[eliminarRecurso()](./eliminarRecurso/README.md)|

### Operaciones de Horarios
- [consultarHorario](./consultarHorario/README.md) - Consulta de horarios
- [generarHorario](./generarHorario/README.md) - Generación de horarios
