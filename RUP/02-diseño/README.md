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

![Diagrama de Arquitectura](/images/RUP/02-diseño/arquitectura.svg)

[Código PlantUML](arquitectura.puml)

### Diagrama de clases de diseño (dominio y datos)

Modelado de las entidades principales, esquemas de API (Pydantic) y modelos de persistencia.

![Diagrama de Clases](/images/RUP/02-diseño/clases-diseño.svg)

[Código PlantUML](clases-diseño.puml)

## Diseño de casos de uso

El diseño detallado de cada caso de uso (diagramas de secuencia) se encuentra organizado en carpetas específicas:

*   [Iniciar Sesión](casos-uso/iniciarSesion/README.md)
*   [Abrir Aulas (Listar)](casos-uso/abrirAulas/README.md)
*   [Crear Aula](casos-uso/crearAula/README.md)
*   [Editar Aula](casos-uso/editarAula/README.md)
*   [Eliminar Aula](casos-uso/eliminarAula/README.md)
