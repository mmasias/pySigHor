# Fase de diseño

## Propósito
Esta fase tiene como objetivo definir la arquitectura del sistema, la selección tecnológica y el diseño detallado de los componentes para guiar la implementación de la variante CLI Standalone.

## Stack tecnológico seleccionado

Para la modernización de **pySigHor**, se ha seleccionado una arquitectura de **CLI (Command Line Interface) Standalone** que implementa su propia capa de servicios y acceso a datos, priorizando la portabilidad total y la independencia de servicios externos.

### CLI: Python + Click
- **Framework**: Click (creación de comandos y prompts).
- **Ventajas**: Interfaz textual portable, distribución simple (binario único), sin dependencias de red.
- **Rol**: Interfaz de línea de comandos para interactuar con el sistema SigHor.

### Lógica de Negocio: Python (Services + Repositories)
- **ORM**: SQLAlchemy (acceso a base de datos).
- **Ventajas**: Arquitectura monolítica, ejecución offline, control total de la lógica.
- **Rol**: Implementación directa de Services, Repositories y Models.

### Base de Datos: SQLite
- **Motor**: SQLite (fichero local).
- **ORM**: SQLAlchemy.
- **Ventajas**: Cero configuración, portabilidad total, sin servidor de base de datos.
- **Ubicación**: `~/.sighor/sighor.db`

## Artefactos de diseño general

### Arquitectura del sistema

Vista de alto nivel de los contenedores y su interacción.

<div align=center>

|![Diagrama de Arquitectura](/images/RUP/02-diseño/arquitectura.svg)
|:-:
|[Código PlantUML](arquitectura.puml)

</div>

### Diagrama de clases de diseño

Modelado de los comandos CLI, servicios, repositorios y modelos de dominio.

<div align=center>

|![Diagrama de Clases](/images/RUP/02-diseño/clases-diseño.svg)
|:-:
|[Código PlantUML](clases-diseño.puml)

</div>

### Configuración y estructura del proyecto

Definición de la estructura de directorios, configuraciones iniciales y decisiones técnicas para materializar la arquitectura en código ejecutable.

[Documento completo](configuracion-proyecto.md)

**Contenido**:
- Estructura de directorios (CLI application)
- Configuraciones iniciales (dependencias, variables de entorno)
- Implementaciones de referencia (Commands, Services, Repositories)
- Gestión de tokens y formateo de salida
- Empaquetado con PyInstaller

## Diseño de casos de uso

El diseño detallado de cada caso de uso (diagramas de secuencia) se encuentra organizado en carpetas específicas:

- [Iniciar Sesión](casos-uso/iniciarSesion/README.md)
- [Abrir Aulas (Listar)](casos-uso/abrirAulas/README.md)
- [Crear Aula](casos-uso/crearAula/README.md)
- [Editar Aula](casos-uso/editarAula/README.md)
- [Eliminar Aula](casos-uso/eliminarAula/README.md)
