# pySigHor > openPrograms > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/openPrograms/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-16
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `openPrograms()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para cumplir con los requisitos especificados.

## diagrama de colaboración

<div align=center>

|![Análisis: openPrograms()](/images/RUP/01-analisis/casos-uso/openPrograms/openPrograms-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### openProgramsView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de apertura de programas académicos
- Interactuar con el controlador para obtener la lista de programas
- Presentar la lista de programas al administrador
- Capturar criterios de filtrado del administrador
- Manejar la navegación de regreso al sistema y a operaciones CRUD

**Colaboraciones**:
- **Entrada**: Recibe `openPrograms()` desde `:Sistema Disponible`
- **Control**: Se comunica con `ProgramasController`
- **Salida**: Navega a `:Sistema Disponible` o colaboraciones CRUD

### clases de control

#### ProgramasController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la obtención de la lista completa de programas académicos
- Manejar la lógica de filtrado por criterios de búsqueda
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `openProgramsView`
- **Repositorio**: Delega operaciones de datos a `ProgramaRepository`

### clases de entidad (entity)

#### ProgramaRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de programas académicos
- Proporcionar método para obtener todos los programas
- Implementar búsqueda por criterios específicos
- Mantener la consistencia de los datos de programas

**Colaboraciones**:
- **Control**: Responde a `ProgramasController`
- **Entidad**: Gestiona instancias de `Programa`

#### Programa
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información de un programa académico individual
- Encapsular atributos: código, nombre, descripción
- Mantener la integridad de los datos del programa

**Colaboraciones**:
- **Repositorio**: Es gestionado por `ProgramaRepository`

## flujo de colaboración

### secuencia de operaciones

1. **Inicio**: `:Sistema Disponible` → `openProgramsView.openPrograms()`
2. **Listado inicial**: `openProgramsView` → `ProgramasController.listarProgramas()`
3. **Acceso a datos**: `ProgramasController` → `ProgramaRepository.obtenerTodos()`
4. **Filtrado (opcional)**: `openProgramsView` → `ProgramasController.filtrarProgramas(criterio)`
5. **Búsqueda**: `ProgramasController` → `ProgramaRepository.buscarPorCriterio(criterio)`
6. **Navegación**: `openProgramsView` → Opciones disponibles

### opciones de navegación disponibles

- **completarGestion()** → `:Sistema Disponible`
- **crearPrograma()** → `:Collaboration CrearPrograma`
- **editarPrograma()** → `:Collaboration EditarPrograma`
- **eliminarPrograma()** → `:Collaboration EliminarPrograma`

## correspondencia con requisitos

### mapeado con especificación detallada

|Requisito del caso de uso|Clase responsable|Método/Colaboración|
|-|-|-|
|Presentar lista de programas|`openProgramsView`|Coordina con `ProgramasController.listarProgramas()`|
|Permitir filtrado de lista|`openProgramsView`|Invoca `ProgramasController.filtrarProgramas(criterio)`|
|Código, nombre, descripción|`Programa`|Encapsula atributos del programa académico|
|Acceso a datos de programas|`ProgramaRepository`|`obtenerTodos()`, `buscarPorCriterio()`|

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

- **Origen**: Caso de uso detallado `openPrograms()`
- **Destino**: Base para diseño arquitectónico
- **Conexión**: Diagrama de contexto → Análisis de colaboración

## patrones aplicados

### repository pattern
`ProgramaRepository` abstrae el acceso a datos, permitiendo diferentes implementaciones sin afectar el controlador.

### mvc pattern
Separación clara entre presentación (`openProgramsView`), lógica de aplicación (`ProgramasController`) y datos (`Programa`, `ProgramaRepository`).

### navigation pattern
Flechas discontinuas indican opciones de navegación disponibles para el usuario, manteniendo flexibilidad en el flujo.

## referencias

- [Especificación detallada: openPrograms()](../../../00-casos-uso/02-detalle/openPrograms/README.md)
- [Diagrama de contexto - Administrador](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Patrón metodológico universal](../../../../conversation-log.md) - Marco de análisis establecido