# pySigHor > abrirAulas > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirAulas/README.md)|**Análisis**|[Diseño](/RUP/02-diseño/casos-uso/abrirAulas/README.md)|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-17
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `abrirAulas()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para cumplir con los requisitos especificados.

## diagrama de colaboración

<div align=center>

|![Análisis: abrirAulas()](/images/RUP/01-analisis/casos-uso/abrirAulas/abrirAulas-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### ListarAulasView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de apertura de aulas
- Interactuar con el controlador para obtener la lista de aulas
- Presentar la lista de aulas al administrador
- Capturar criterios de filtrado del administrador
- Manejar la navegación de regreso al sistema

**Colaboraciones**:
- **Entrada**: Recibe `abrirAulas()` desde `:Sistema Disponible`
- **Control**: Se comunica con `AulasController`
- **Salida**: Retorna control a `:Sistema Disponible`

### clases de control

#### AulasController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la obtención de la lista completa de aulas
- Manejar la lógica de filtrado por criterios de búsqueda
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `ListarAulasView`
- **Repositorio**: Delega operaciones de datos a `AulaRepository`

### clases de entidad (entity)

#### AulaRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de aulas
- Proporcionar método para obtener todas las aulas
- Implementar búsqueda por criterios específicos
- Mantener la consistencia de los datos de aulas

**Colaboraciones**:
- **Control**: Responde a `AulasController`
- **Entidad**: Gestiona instancias de `Aula`

#### Aula
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información de un aula individual
- Encapsular atributos: ID, nombre, capacidad, edificio
- Mantener la integridad de los datos del aula

**Colaboraciones**:
- **Repositorio**: Es gestionado por `AulaRepository`

## flujo de colaboración

### secuencia de operaciones

1. **Inicio**: `:Sistema Disponible` → `ListarAulasView.abrirAulas()`
2. **Listado inicial**: `ListarAulasView` → `AulasController.listarAulas()`
3. **Acceso a datos**: `AulasController` → `AulaRepository.obtenerTodos()`
4. **Filtrado (opcional)**: `ListarAulasView` → `AulasController.filtrarAulas(criterio)`
5. **Búsqueda**: `AulasController` → `AulaRepository.buscarPorCriterio(criterio)`
6. **Finalización**: `ListarAulasView` → `:Sistema Disponible.sistemaDisponible(administrador)`

### patrón de colaboración establecido

Este análisis sigue el **patrón metodológico universal** establecido para el proyecto:
- **Entrada estándar**: Desde `:Sistema Disponible`
- **Análisis MVC completo**: Vista, Control y Entidad claramente separados
- **Salida estándar**: Regreso a `:Sistema Disponible` con `sistemaDisponible(administrador)`

## correspondencia con requisitos

### mapeado con especificación detallada

|Requisito del caso de uso|Clase responsable|Método/Colaboración|
|-|-|-|
|Presentar lista de aulas|`ListarAulasView`|Coordina con `AulasController.listarAulas()`|
|Permitir filtrado de lista|`ListarAulasView`|Invoca `AulasController.filtrarAulas(criterio)`|
|ID, nombre, capacidad, edificio|`Aula`|Encapsula atributos del aula|
|Acceso a datos de aulas|`AulaRepository`|`obtenerTodos()`, `buscarPorCriterio()`|

### operaciones CRUD preparadas

Aunque no implementadas en este caso de uso, el análisis prepara la base para:
- **Crear**: `AulasController` puede extender funcionalidad
- **Editar**: `AulaRepository` ya tiene acceso a `Aula`
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

- **Origen**: Caso de uso detallado `abrirAulas()`
- **Destino**: Base para diseño arquitectónico
- **Conexión**: Diagrama de contexto → Análisis de colaboración

## patrones aplicados

### repository pattern
`AulaRepository` abstrae el acceso a datos, permitiendo diferentes implementaciones sin afectar el controlador.

### mvc pattern
Separación clara entre presentación (`ListarAulasView`), lógica de aplicación (`AulasController`) y datos (`Aula`, `AulaRepository`).

### sistema de estados
Mantiene coherencia con el diagrama de contexto del administrador, respetando las transiciones de estado establecidas.

## referencias

- [Especificación detallada: abrirAulas()](../../../00-casos-uso/02-detalle/abrirAulas/README.md)
- [Diagrama de contexto - Administrador](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Patrón metodológico universal](../../../../conversation-log.md) - Marco de análisis establecido