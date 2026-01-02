# Fase de diseño

## Propósito

Esta fase tiene como objetivo definir la arquitectura del sistema, la selección tecnológica y el diseño detallado de los componentes para guiar la implementación.

## Stack tecnológico seleccionado

Para la modernización de **pySigHor**, se ha seleccionado una arquitectura de **CLI (Command Line Interface)** que consume una API REST existente, priorizando el reuso máximo del backend y la validación de independencia de paradigma de interfaz.

### CLI: Python + Click + Requests

- **Framework CLI**: Click (creación de comandos y prompts).
- **Cliente HTTP**: Requests (consumo de API FastAPI).
- **Ventajas**: Reuso completo del backend FastAPI, desarrollo rápido, interfaz textual portable.
- **Rol**: Interfaz de línea de comandos para interactuar con el sistema SigHor.

### Backend: Python + FastAPI (Reutilizado)

- **Framework**: FastAPI.
- **Ventajas**: Backend completo ya implementado en rama `diseño-fastapi-react`.
- **Rol**: Exponer la lógica de negocio y acceso a datos a través de una API RESTful.
- **Reuso**: Services, Repositories, Models, configuración de base de datos.

### Base de Datos: SQLite (Heredada)

- **Motor**: SQLite (fichero local).
- **ORM**: SQLAlchemy (async).
- **Ventajas**: Misma base de datos que interfaz React, coherencia total de datos.

## Artefactos de diseño general

### Arquitectura del sistema

Vista de alto nivel de los contenedores y su interacción (CLI como cliente HTTP de FastAPI).

<div align=center>

|![Diagrama de Arquitectura](/images/RUP/02-diseño/arquitectura.svg)
|:-:
|[Código PlantUML](arquitectura.puml)

</div>

### Diagrama de clases de diseño (CLI + Backend reutilizado)

Modelado de comandos CLI, cliente HTTP y mapeo con backend FastAPI existente.

<div align=center>

|![Diagrama de Clases](/images/RUP/02-diseño/clases-diseño.svg)
|:-:
|[Código PlantUML](clases-diseño.puml)

</div>

### Configuración y estructura del proyecto

Definición de la estructura de directorios del CLI, configuraciones iniciales y decisiones técnicas para materializar la arquitectura en código ejecutable.

[Documento completo](configuracion-proyecto.md)

**Contenido**:

- Estructura de directorios CLI
- Dependencias (Click, Requests, Rich)
- Configuración de conexión a API FastAPI
- Gestión de tokens de sesión
- Comandos de desarrollo y ejecución

## Diseño de casos de uso

El diseño detallado de cada caso de uso (diagramas de secuencia CLI → API) se encuentra organizado en carpetas específicas:

- [Iniciar Sesión](casos-uso/iniciarSesion/README.md)
- [Abrir Aulas (Listar)](casos-uso/abrirAulas/README.md)
- [Crear Aula](casos-uso/crearAula/README.md)
- [Editar Aula](casos-uso/editarAula/README.md)
- [Eliminar Aula](casos-uso/eliminarAula/README.md)
