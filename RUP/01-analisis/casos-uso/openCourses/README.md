# pySigHor > abrirCursos > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirCursos/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|


## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-16
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `abrirCursos()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para cumplir con los requisitos especificados.

## diagrama de colaboración

<div align=center>

|![Análisis: abrirCursos()](/images/RUP/01-analisis/casos-uso/abrirCursos/abrirCursos-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### AbrirCursosView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de apertura de cursos académicos
- Interactuar con el controlador para obtener la lista de cursos
- Presentar la lista de cursos al administrador
- Capturar criterios de filtrado del administrador
- Manejar la navegación de regreso al sistema y a operaciones CRUD

**Colaboraciones**:
- **Entrada**: Recibe `abrirCursos()` desde `:Sistema Disponible`
- **Control**: Se comunica con `CursosController`
- **Salida**: Navega a `:Sistema Disponible` o colaboraciones CRUD

### clases de control

#### CursosController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la obtención de la lista completa de cursos académicos
- Manejar la lógica de filtrado por criterios de búsqueda
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `AbrirCursosView`
- **Repositorio**: Delega operaciones de datos a `CursoRepository`

### clases de entidad (entity)

#### CursoRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de cursos académicos
- Proporcionar método para obtener todos los cursos
- Implementar búsqueda por criterios específicos
- Mantener la consistencia de los datos de cursos

**Colaboraciones**:
- **Control**: Responde a `CursosController`
- **Entidad**: Gestiona instancias de `Curso`

#### Curso
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información de un curso académico individual
- Encapsular atributos: código, nombre, descripción
- Mantener la integridad de los datos del curso

**Colaboraciones**:
- **Repositorio**: Es gestionado por `CursoRepository`

## flujo de colaboración

### secuencia de operaciones

1. **Inicio**: `:Sistema Disponible` → `AbrirCursosView.abrirCursos()`
2. **Listado inicial**: `AbrirCursosView` → `CursosController.listarCursos()`
3. **Acceso a datos**: `CursosController` → `CursoRepository.obtenerTodos()`
4. **Filtrado (opcional)**: `AbrirCursosView` → `CursosController.filtrarCursos(criterio)`
5. **Búsqueda**: `CursosController` → `CursoRepository.buscarPorCriterio(criterio)`
6. **Navegación**: `AbrirCursosView` → Opciones disponibles

### opciones de navegación disponibles

- **completarGestion()** → `:Sistema Disponible`
- **crearCurso()** → `:Collaboration CrearCurso`
- **editarCurso()** → `:Collaboration EditarCurso`
- **eliminarCurso()** → `:Collaboration EliminarCurso`

## correspondencia con requisitos

### mapeado con especificación detallada

|Requisito del caso de uso|Clase responsable|Método/Colaboración|
|-|-|-|
|Presentar lista de cursos|`AbrirCursosView`|Coordina con `CursosController.listarCursos()`|
|Permitir filtrado de lista|`AbrirCursosView`|Invoca `CursosController.filtrarCursos(criterio)`|
|Código, nombre, descripción|`Curso`|Encapsula atributos del curso académico|
|Acceso a datos de cursos|`CursoRepository`|`obtenerTodos()`, `buscarPorCriterio()`|

### patrón de colaboración establecido

Este análisis sigue el **patrón metodológico universal** establecido para el proyecto:
- **Entrada estándar**: Desde `:Sistema Disponible`
- **Análisis MVC completo**: Vista, Control y Entidad claramente separados
- **Salidas múltiples**: `completarGestion()` + navegación CRUD mediante flechas discontinuas

## características del análisis

### separación de responsabilidades MVC

- **Vista**: Solo presentación e interacción con usuario
- **Control**: Solo coordinación y lógica de aplicación  
- **Entidad**: Solo datos y reglas de negocio

### agnóstico tecnológicamente

- No especifica tecnología de interfaz de usuario
- No asume implementación específica de base de datos
- Mantiene independencia de frameworks

### trazabilidad completa

- **Origen**: Caso de uso detallado `abrirCursos()`
- **Destino**: Base para diseño arquitectónico
- **Conexión**: Diagrama de contexto → Análisis de colaboración

## patrones aplicados

### repository pattern
`CursoRepository` abstrae el acceso a datos, permitiendo diferentes implementaciones sin afectar el controlador.

### mvc pattern
Separación clara entre presentación (`AbrirCursosView`), lógica de aplicación (`CursosController`) y datos (`Curso`, `CursoRepository`).

### navigation pattern
Flechas discontinuas indican opciones de navegación disponibles para el usuario, manteniendo flexibilidad en el flujo.

## referencias

- [Especificación detallada: abrirCursos()](../../../00-casos-uso/02-detalle/abrirCursos/README.md)
- [Diagrama de contexto - Administrador](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Patrón metodológico universal](../../../../conversation-log.md) - Marco de análisis establecido