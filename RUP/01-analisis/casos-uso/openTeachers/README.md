# pySigHor > abrirProfesores > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirProfesores/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-16
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `abrirProfesores()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para cumplir con los requisitos especificados.

## diagrama de colaboración

<div align=center>

|![Análisis: abrirProfesores()](/images/RUP/01-analisis/casos-uso/abrirProfesores/abrirProfesores-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### ListarProfesoresView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de apertura de profesores
- Interactuar con el controlador para obtener la lista de profesores
- Presentar la lista de profesores al administrador
- Capturar criterios de filtrado del administrador
- Manejar la navegación de regreso al sistema

**Colaboraciones**:
- **Entrada**: Recibe `abrirProfesores()` desde `:Sistema Disponible`
- **Control**: Se comunica con `ProfesoresController`
- **Salida**: Retorna control a `:Sistema Disponible`

### clases de control

#### ProfesoresController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la obtención de la lista completa de profesores
- Manejar la lógica de filtrado por criterios de búsqueda
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `ListarProfesoresView`
- **Repositorio**: Delega operaciones de datos a `ProfesorRepository`

### clases de entidad (entity)

#### ProfesorRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de profesores
- Proporcionar método para obtener todos los profesores
- Implementar búsqueda por criterios específicos
- Mantener la consistencia de los datos de profesores

**Colaboraciones**:
- **Control**: Responde a `ProfesoresController`
- **Entidad**: Gestiona instancias de `Profesor`

#### Profesor
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información de un profesor individual
- Encapsular atributos: código, nombre, apellidos
- Mantener la integridad de los datos del profesor

**Colaboraciones**:
- **Repositorio**: Es gestionado por `ProfesorRepository`

## flujo de colaboración

### secuencia de operaciones

1. **Inicio**: `:Sistema Disponible` → `ListarProfesoresView.abrirProfesores()`
2. **Listado inicial**: `ListarProfesoresView` → `ProfesoresController.listarProfesores()`
3. **Acceso a datos**: `ProfesoresController` → `ProfesorRepository.obtenerTodos()`
4. **Filtrado (opcional)**: `ListarProfesoresView` → `ProfesoresController.filtrarProfesores(criterio)`
5. **Búsqueda**: `ProfesoresController` → `ProfesorRepository.buscarPorCriterio(criterio)`
6. **Finalización**: `ListarProfesoresView` → `:Sistema Disponible.sistemaDisponible(administrador)`

### patrón de colaboración establecido

Este análisis sigue el **patrón metodológico universal** establecido para el proyecto:
- **Entrada estándar**: Desde `:Sistema Disponible`
- **Análisis MVC completo**: Vista, Control y Entidad claramente separados
- **Salida estándar**: Regreso a `:Sistema Disponible` con `sistemaDisponible(administrador)`

## correspondencia con requisitos

### mapeado con especificación detallada

|Requisito del caso de uso|Clase responsable|Método/Colaboración|
|-|-|-|
|Presentar lista de profesores|`ListarProfesoresView`|Coordina con `ProfesoresController.listarProfesores()`|
|Permitir filtrado de lista|`ListarProfesoresView`|Invoca `ProfesoresController.filtrarProfesores(criterio)`|
|Código, nombre, apellidos|`Profesor`|Encapsula atributos del profesor|
|Acceso a datos de profesores|`ProfesorRepository`|`obtenerTodos()`, `buscarPorCriterio()`|

### operaciones CRUD preparadas

Aunque no implementadas en este caso de uso, el análisis prepara la base para:
- **Crear**: `ProfesoresController` puede extender funcionalidad
- **Editar**: `ProfesorRepository` ya tiene acceso a `Profesor`
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

- **Origen**: Caso de uso detallado `abrirProfesores()`
- **Destino**: Base para diseño arquitectónico
- **Conexión**: Diagrama de contexto → Análisis de colaboración

## patrones aplicados

### repository pattern
`ProfesorRepository` abstrae el acceso a datos, permitiendo diferentes implementaciones sin afectar el controlador.

### mvc pattern
Separación clara entre presentación (`ListarProfesoresView`), lógica de aplicación (`ProfesoresController`) y datos (`Profesor`, `ProfesorRepository`).

### sistema de estados
Mantiene coherencia con el diagrama de contexto del administrador, respetando las transiciones de estado establecidas.

## referencias

- [Especificación detallada: abrirProfesores()](../../../00-casos-uso/02-detalle/abrirProfesores/README.md)
- [Diagrama de contexto - Administrador](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Patrón metodológico universal](../../../../conversation-log.md) - Marco de análisis establecido