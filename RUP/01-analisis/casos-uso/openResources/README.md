# pySigHor > openResources > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/openResources/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-17
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `openResources()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para cumplir con los requisitos especificados.

## diagrama de colaboración

<div align=center>

|![Análisis: openResources()](/images/RUP/01-analisis/casos-uso/openResources/openResources-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### ListarRecursosView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de apertura de recursos
- Interactuar con el controlador para obtener la lista de recursos
- Presentar la lista de recursos al administrador
- Capturar criterios de filtrado del administrador
- Manejar la navegación de regreso al sistema

**Colaboraciones**:
- **Entrada**: Recibe `openResources()` desde `:Sistema Disponible`
- **Control**: Se comunica con `RecursosController`
- **Salida**: Retorna control a `:Sistema Disponible`

### clases de control

#### RecursosController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la obtención de la lista completa de recursos
- Manejar la lógica de filtrado por criterios de búsqueda
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `ListarRecursosView`
- **Repositorio**: Delega operaciones de datos a `RecursoRepository`

### clases de entidad (entity)

#### RecursoRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de recursos
- Proporcionar método para obtener todos los recursos
- Implementar búsqueda por criterios específicos
- Mantener la consistencia de los datos de recursos

**Colaboraciones**:
- **Control**: Responde a `RecursosController`
- **Entidad**: Gestiona instancias de `Recurso`

#### Recurso
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información de un recurso individual
- Encapsular atributos: ID, nombre, descripción
- Mantener la integridad de los datos del recurso

**Colaboraciones**:
- **Repositorio**: Es gestionado por `RecursoRepository`

## flujo de colaboración

### secuencia de operaciones

1. **Inicio**: `:Sistema Disponible` → `ListarRecursosView.openResources()`
2. **Listado inicial**: `ListarRecursosView` → `RecursosController.listarRecursos()`
3. **Acceso a datos**: `RecursosController` → `RecursoRepository.obtenerTodos()`
4. **Filtrado (opcional)**: `ListarRecursosView` → `RecursosController.filtrarRecursos(criterio)`
5. **Búsqueda**: `RecursosController` → `RecursoRepository.buscarPorCriterio(criterio)`
6. **Finalización**: `ListarRecursosView` → `:Sistema Disponible.sistemaDisponible(administrador)`

### patrón de colaboración establecido

Este análisis sigue el **patrón metodológico universal** establecido para el proyecto:
- **Entrada estándar**: Desde `:Sistema Disponible`
- **Análisis MVC completo**: Vista, Control y Entidad claramente separados
- **Salida estándar**: Regreso a `:Sistema Disponible` con `sistemaDisponible(administrador)`

## correspondencia con requisitos

### mapeado con especificación detallada

|Requisito del caso de uso|Clase responsable|Método/Colaboración|
|-|-|-|
|Presentar lista de recursos|`ListarRecursosView`|Coordina con `RecursosController.listarRecursos()`|
|Permitir filtrado de lista|`ListarRecursosView`|Invoca `RecursosController.filtrarRecursos(criterio)`|
|ID, nombre, descripción|`Recurso`|Encapsula atributos del recurso|
|Acceso a datos de recursos|`RecursoRepository`|`obtenerTodos()`, `buscarPorCriterio()`|

### operaciones CRUD preparadas

Aunque no implementadas en este caso de uso, el análisis prepara la base para:
- **Crear**: `RecursosController` puede extender funcionalidad
- **Editar**: `RecursoRepository` ya tiene acceso a `Recurso`
- **Eliminar**: Patrón establece la base para futuras operaciones

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

- **Origen**: Caso de uso detallado `openResources()`
- **Destino**: Base para diseño arquitectónico
- **Conexión**: Diagrama de contexto → Análisis de colaboración

## patrones aplicados

### repository pattern
`RecursoRepository` abstrae el acceso a datos, permitiendo diferentes implementaciones sin afectar el controlador.

### mvc pattern
Separación clara entre presentación (`ListarRecursosView`), lógica de aplicación (`RecursosController`) y datos (`Recurso`, `RecursoRepository`).

### sistema de estados
Mantiene coherencia con el diagrama de contexto del administrador, respetando las transiciones de estado establecidas.

## referencias

- [Especificación detallada: openResources()](../../../00-casos-uso/02-detalle/openResources/README.md)
- [Diagrama de contexto - Administrador](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Patrón metodológico universal](../../../../conversation-log.md) - Marco de análisis establecido