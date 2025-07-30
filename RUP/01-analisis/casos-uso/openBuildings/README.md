# pySigHor > abrirEdificios > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirEdificios/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-17
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `abrirEdificios()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para cumplir con los requisitos especificados.

## diagrama de colaboración

<div align=center>

|![Análisis: abrirEdificios()](/images/RUP/01-analisis/casos-uso/abrirEdificios/abrirEdificios-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### ListarEdificiosView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de apertura de edificios
- Interactuar con el controlador para obtener la lista de edificios
- Presentar la lista de edificios al administrador
- Capturar criterios de filtrado del administrador
- Manejar la navegación de regreso al sistema

**Colaboraciones**:
- **Entrada**: Recibe `abrirEdificios()` desde `:Sistema Disponible`
- **Control**: Se comunica con `EdificiosController`
- **Salida**: Retorna control a `:Sistema Disponible`

### clases de control

#### EdificiosController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la obtención de la lista completa de edificios
- Manejar la lógica de filtrado por criterios de búsqueda
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `ListarEdificiosView`
- **Repositorio**: Delega operaciones de datos a `EdificioRepository`

### clases de entidad (entity)

#### EdificioRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de edificios
- Proporcionar método para obtener todos los edificios
- Implementar búsqueda por criterios específicos
- Mantener la consistencia de los datos de edificios

**Colaboraciones**:
- **Control**: Responde a `EdificiosController`
- **Entidad**: Gestiona instancias de `Edificio`

#### Edificio
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información de un edificio individual
- Encapsular atributos: ID, nombre
- Mantener la integridad de los datos del edificio

**Colaboraciones**:
- **Repositorio**: Es gestionado por `EdificioRepository`

## flujo de colaboración

### secuencia de operaciones

1. **Inicio**: `:Sistema Disponible` → `ListarEdificiosView.abrirEdificios()`
2. **Listado inicial**: `ListarEdificiosView` → `EdificiosController.listarEdificios()`
3. **Acceso a datos**: `EdificiosController` → `EdificioRepository.obtenerTodos()`
4. **Filtrado (opcional)**: `ListarEdificiosView` → `EdificiosController.filtrarEdificios(criterio)`
5. **Búsqueda**: `EdificiosController` → `EdificioRepository.buscarPorCriterio(criterio)`
6. **Finalización**: `ListarEdificiosView` → `:Sistema Disponible.sistemaDisponible(administrador)`

### patrón de colaboración establecido

Este análisis sigue el **patrón metodológico universal** establecido para el proyecto:
- **Entrada estándar**: Desde `:Sistema Disponible`
- **Análisis MVC completo**: Vista, Control y Entidad claramente separados
- **Salida estándar**: Regreso a `:Sistema Disponible` con `sistemaDisponible(administrador)`

## correspondencia con requisitos

### mapeado con especificación detallada

|Requisito del caso de uso|Clase responsable|Método/Colaboración|
|-|-|-|
|Presentar lista de edificios|`ListarEdificiosView`|Coordina con `EdificiosController.listarEdificios()`|
|Permitir filtrado de lista|`ListarEdificiosView`|Invoca `EdificiosController.filtrarEdificios(criterio)`|
|ID, nombre del edificio|`Edificio`|Encapsula atributos del edificio|
|Acceso a datos de edificios|`EdificioRepository`|`obtenerTodos()`, `buscarPorCriterio()`|

### operaciones CRUD preparadas

Aunque no implementadas en este caso de uso, el análisis prepara la base para:
- **Crear**: `EdificiosController` puede extender funcionalidad
- **Editar**: `EdificioRepository` ya tiene acceso a `Edificio`
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

- **Origen**: Caso de uso detallado `abrirEdificios()`
- **Destino**: Base para diseño arquitectónico
- **Conexión**: Diagrama de contexto → Análisis de colaboración

## patrones aplicados

### repository pattern
`EdificioRepository` abstrae el acceso a datos, permitiendo diferentes implementaciones sin afectar el controlador.

### mvc pattern
Separación clara entre presentación (`ListarEdificiosView`), lógica de aplicación (`EdificiosController`) y datos (`Edificio`, `EdificioRepository`).

### sistema de estados
Mantiene coherencia con el diagrama de contexto del administrador, respetando las transiciones de estado establecidas.

## referencias

- [Especificación detallada: abrirEdificios()](../../../00-casos-uso/02-detalle/abrirEdificios/README.md)
- [Diagrama de contexto - Administrador](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Patrón metodológico universal](../../../../conversation-log.md) - Marco de análisis establecido