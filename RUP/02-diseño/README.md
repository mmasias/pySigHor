# Fase de diseño

## Propósito
Esta fase tiene como objetivo definir la arquitectura del sistema, la selección tecnológica y el diseño detallado de los componentes para guiar la implementación.

## Stack tecnológico seleccionado

Para la modernización de **pySigHor**, se ha seleccionado una arquitectura de **Single Page Application (SPA)** con API REST, priorizando la separación de responsabilidades y el valor didáctico.

### Backend: Java + Spring Boot
*   **Framework**: Spring Boot 3.x.
*   **Ventajas**: Ecosistema maduro, inyección de dependencias robusta, Spring Security para autenticación/autorización, Spring Data JPA para persistencia, documentación extensa.
*   **Rol**: Exponer la lógica de negocio y acceso a datos a través de una API RESTful.

### Frontend: Angular + TypeScript
*   **Framework**: Angular 17+ (standalone components).
*   **Lenguaje**: TypeScript nativo (opinionado y fuertemente tipado).
*   **Estilos**: Angular Material o Bootstrap (a definir en implementación).
*   **Rol**: Interfaz de usuario interactiva y gestión del estado de la aplicación con servicios y RxJS.

### Base de Datos: H2
*   **Motor**: H2 Database (en memoria o fichero local).
*   **ORM**: Spring Data JPA con Hibernate.
*   **Ventajas**: Cero configuración, ideal para desarrollo y prototipado rápido, fácilmente migrable a PostgreSQL o MySQL.

## Artefactos de diseño general

### Arquitectura del sistema

Vista de alto nivel de los contenedores y su interacción.

<div align=center>

|![Diagrama de Arquitectura](/images/RUP/02-diseño/arquitectura.svg)
|:-:
|[Código PlantUML](arquitectura.puml)

</div>

### Diagrama de clases de diseño (dominio y datos)

Modelado de las entidades principales, DTOs, repositorios Spring Data y configuración de Spring Security.

<div align=center>

|![Diagrama de Clases](/images/RUP/02-diseño/clases-diseño.svg)
|:-:
|[Código PlantUML](clases-diseño.puml)

</div>

### Configuración y estructura del proyecto

Definición de la estructura de directorios, configuraciones iniciales y decisiones técnicas para materializar la arquitectura en código ejecutable.

[Documento completo](configuracion-proyecto.md)

**Contenido**:
*   Estructura de directorios (Backend Maven y Frontend Angular CLI)
*   Configuraciones iniciales (dependencias, application.properties)
*   Esquema de base de datos
*   Mapeo entre artefactos de diseño y código
*   Comandos de desarrollo

## Diseño de casos de uso

El diseño detallado de cada caso de uso (diagramas de secuencia) se encuentra organizado en carpetas específicas:

*   [Iniciar Sesión](casos-uso/iniciarSesion/README.md)
*   [Abrir Aulas (Listar)](casos-uso/abrirAulas/README.md)
*   [Crear Aula](casos-uso/crearAula/README.md)
*   [Editar Aula](casos-uso/editarAula/README.md)
*   [Eliminar Aula](casos-uso/eliminarAula/README.md)
