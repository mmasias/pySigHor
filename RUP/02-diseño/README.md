# Fase de diseño

## Propósito
Esta fase tiene como objetivo definir la arquitectura del sistema, la selección tecnológica y el diseño detallado de los componentes para guiar la implementación.

## Stack tecnológico seleccionado

Para la modernización de **pySigHor**, se ha seleccionado una arquitectura de **Single Page Application (SPA)** con API REST, priorizando la separación de responsabilidades y el valor didáctico.

### Backend: Python + FastAPI
*   **Framework**: FastAPI.
*   **Ventajas**: Alto rendimiento (Asgi), validación de datos automática (Pydantic), documentación interactiva (Swagger UI) y tipado estático fuerte.
*   **Rol**: Exponer la lógica de negocio y acceso a datos a través de una API RESTful.

### Frontend: React + TypeScript
*   **Framework**: React (con Vite como bundler).
*   **Lenguaje**: TypeScript para mayor robustez y mantenibilidad.
*   **Estilos**: CSS Modules o Tailwind (a definir en implementación).
*   **Rol**: Interfaz de usuario interactiva y gestión del estado de la aplicación.

### Base de Datos: SQLite
*   **Motor**: SQLite (fichero local).
*   **ORM**: SQLAlchemy (async).
*   **Ventajas**: Cero configuración, ideal para desarrollo y prototipado rápido, fácilmente migrable a PostgreSQL.

## Artefactos de diseño general

### Arquitectura del sistema

Vista de alto nivel de los contenedores y su interacción.

<div align=center>

|![Diagrama de Arquitectura](/images/RUP/02-diseño/arquitectura.svg)
|:-:
|[Código PlantUML](arquitectura.puml)

</div>

### Diagrama de clases de diseño (dominio y datos)

Modelado de las entidades principales, esquemas de API (Pydantic) y modelos de persistencia.

<div align=center>

|![Diagrama de Clases](/images/RUP/02-diseño/clases-diseño.svg)
|:-:
|[Código PlantUML](clases-diseño.puml)

</div>

### Configuración y estructura del proyecto

Definición de la estructura de directorios, configuraciones iniciales y decisiones técnicas para materializar la arquitectura en código ejecutable.

[Documento completo](configuracion-proyecto.md)

**Contenido**:
*   Estructura de directorios (Backend y Frontend)
*   Configuraciones iniciales (dependencias, variables de entorno)
*   Esquema de base de datos
*   Mapeo entre artefactos de diseño y código
*   Comandos de desarrollo

## Diseño de casos de uso

El diseño detallado de cada caso de uso (diagramas de secuencia) se encuentra organizado en carpetas específicas:

### Sesión

*   [Iniciar Sesión](casos-uso/iniciarSesion/README.md)
*   [Cerrar Sesión](casos-uso/cerrarSesion/README.md)
*   [Completar Gestión](casos-uso/completarGestion/README.md)
*   [Consultar Horario](casos-uso/consultarHorario/README.md)

### Aulas

*   [Abrir Aulas](casos-uso/abrirAulas/README.md)
*   [Crear Aula](casos-uso/crearAula/README.md)
*   [Editar Aula](casos-uso/editarAula/README.md)
*   [Eliminar Aula](casos-uso/eliminarAula/README.md)

### Edificios

*   [Abrir Edificios](casos-uso/abrirEdificios/README.md)
*   [Crear Edificio](casos-uso/crearEdificio/README.md)
*   [Editar Edificio](casos-uso/editarEdificio/README.md)
*   [Eliminar Edificio](casos-uso/eliminarEdificio/README.md)

### Profesores

*   [Abrir Profesores](casos-uso/abrirProfesores/README.md)
*   [Crear Profesor](casos-uso/crearProfesor/README.md)
*   [Editar Profesor](casos-uso/editarProfesor/README.md)
*   [Eliminar Profesor](casos-uso/eliminarProfesor/README.md)

### Programas

*   [Abrir Programas](casos-uso/abrirProgramas/README.md)
*   [Crear Programa](casos-uso/crearPrograma/README.md)
*   [Editar Programa](casos-uso/editarPrograma/README.md)
*   [Eliminar Programa](casos-uso/eliminarPrograma/README.md)

### Cursos

*   [Abrir Cursos](casos-uso/abrirCursos/README.md)
*   [Crear Curso](casos-uso/crearCurso/README.md)
*   [Editar Curso](casos-uso/editarCurso/README.md)
*   [Eliminar Curso](casos-uso/eliminarCurso/README.md)

### Recursos

*   [Abrir Recursos](casos-uso/abrirRecursos/README.md)
*   [Crear Recurso](casos-uso/crearRecurso/README.md)
*   [Editar Recurso](casos-uso/editarRecurso/README.md)
*   [Eliminar Recurso](casos-uso/eliminarRecurso/README.md)
