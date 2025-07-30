# pySigHor > completeManagement > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/completeManagement/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Análisis
- **Versión**: 1.0
- **Fecha**: 2025-07-09
- **Autor**: Equipo de desarrollo

## propósito

Análisis del caso de uso `completeManagement()` mediante diagrama de colaboración MVC, identificando clases de análisis y sus interacciones conceptuales para realizar el caso de uso.

### rol metodológico del caso de uso

`completeManagement()` es el **caso de uso de convergencia** del sistema SigHor, funcionando como:

- **Hub central de navegación**: Punto de retorno común desde todas las funcionalidades específicas
- **Coordinador de capacidades**: Presenta al usuario todas las opciones disponibles según sus permisos
- **Mantenedor de contexto**: Preserva la sesión activa mientras permite acceso a cualquier funcionalidad

**Invocación**: Este caso de uso es invocado por:
1. **`startSession()`** - Al establecer sesión exitosa inicialmente
2. **Todos los casos de uso de gestión** - Al completar operaciones CRUD (`openPrograms()`, `openCourses()`, etc.)
3. **Casos de uso de proceso** - Al finalizar procesos específicos (`generateSchedule()`, `viewSchedule()`, etc.)

**Resultado**: Mantiene al sistema en estado `SISTEMA_DISPONIBLE`, permitiendo solicitar cualquier funcionalidad del diagrama de contexto.

## diagrama de colaboración

<div align=center>

|![Análisis completeManagement()](/images/RUP/01-analisis/casos-uso/completeManagement/completeManagement-analysis.svg)|
|-|
|**Disciplina**: Análisis RUP<br>**Enfoque**: Diagramas de colaboración MVC|

</div>

## clases de análisis identificadas

### clases model (naranja #F2AC4E)
|Clase|Responsabilidad|Trazabilidad|
|-|-|-|
|**Sesion**|Entidad que mantiene estado de autenticación activa|Concepto del caso de uso|
|**OpcionesMenu**|Entidad que representa opciones disponibles para el usuario|Análisis puro|
|**PermisosRepository**|Concepto puro de acceso a permisos y opciones de usuario|Análisis puro|

### clases view (azul #629EF9)
|Clase|Responsabilidad|Derivación|
|-|-|-|
|**GestionView**|Ventana principal de navegación del sistema|Wireframe SALT|

### clases controller (verde #b5bd68)
|Clase|Responsabilidad|Caso de uso|
|-|-|-|
|**completeManagementController**|Control y coordinación completa del caso de uso|completeManagement()|

### colaboraciones (verde claro #CDEBA5)
|Colaboración|Propósito|Invocación|
|-|-|-|
|**:Collaboration AbrirProgramas**|Permite solicitar apertura de gestión de programas|Según selección|
|**:Collaboration AbrirCursos**|Permite solicitar apertura de gestión de cursos|Según selección|
|**:Collaboration AbrirProfesores**|Permite solicitar apertura de gestión de profesores|Según selección|
|**:Collaboration AbrirEdificios**|Permite solicitar apertura de gestión de edificios|Según selección|
|**:Collaboration AbrirAulas**|Permite solicitar apertura de gestión de aulas|Según selección|
|**:Collaboration AbrirRecursos**|Permite solicitar apertura de gestión de recursos|Según selección|
|**:Collaboration AsignarProfesor**|Permite solicitar asignación de profesores|Según selección|
|**:Collaboration GenerarHorario**|Permite solicitar generación de horarios|Según selección|
|**:Collaboration ConsultarHorario**|Permite solicitar consulta de horarios|Según selección|
|**:Collaboration CerrarSesion**|Permite solicitar cierre de sesión|Según selección|

## mensajes de colaboración

### flujo principal
|Origen|Destino|Mensaje|Intención|
|-|-|-|-|
|**:Sistema Disponible**|**GestionView**|`disponibilizarSistema()`|Resultado de iniciarSesion() invoca completeManagement()|
|**GestionView**|**completeManagementController**|`habilitarOpciones(administrador)`|Delegar habilitación de opciones|
|**completeManagementController**|**Sesion**|`getUsuario()`|Obtener información del usuario autenticado|
|**completeManagementController**|**PermisosRepository**|`obtenerOpciones(usuario)`|Obtener opciones disponibles para el usuario|
|**completeManagementController**|**OpcionesMenu**|`crearOpciones(opciones)`|Crear estructura de opciones|
|**GestionView**|**OpcionesMenu**|`getOpciones()`|Obtener opciones para presentar|
|**GestionView**|**:Collaboration [Según selección]**|`abrirX() / asignarX() / generarX() / etc.`|Invocar colaboración según opción seleccionada|

## enlaces de dependencia
- **GestionView** conoce a **completeManagementController** (delegación)
- **GestionView** conoce a **OpcionesMenu** (acceso a opciones)
- **GestionView** conoce a **Sesion** (acceso a estado)
- **GestionView** conoce a **todas las colaboraciones** (invocación según selección)
- **completeManagementController** conoce a **PermisosRepository** (obtención opciones)
- **completeManagementController** conoce a **OpcionesMenu** (creación estructura)
- **completeManagementController** conoce a **Sesion** (acceso a usuario)
- **PermisosRepository** conoce a **OpcionesMenu** (gestión opciones)

## trazabilidad con artefactos previos

### con especificación detallada
- **Estados internos** → **Clases de análisis**
- **PresentandoMenu** → **GestionView.presentarOpciones()**
- **EsperandoSeleccion** → **GestionView.seleccionarOpcion()**
- **Opciones del menú** → **OpcionesMenu**

### con wireframe
- **Menú principal** → **GestionView**
- **Categorías de opciones** → **OpcionesMenu.organizarPorCategoria()**
- **Botones de selección** → **GestionView.seleccionarOpcion()**

### con modelo del dominio
- **Usuario** (entidad) → **Sesion.getUsuario()**
- **Permisos** (concepto) → **PermisosRepository**

## principios de análisis aplicados

### patrón mvc
- **Un controlador por caso de uso**: completeManagementController
- **Vista derivada de prototipo**: GestionView desde wireframe SALT
- **Modelo del dominio**: OpcionesMenu con trazabilidad directa

### diagramas de colaboración
- **Foco en enlaces**: dependencias conceptuales, no secuencia temporal
- **Mensajes de intención**: qué se quiere lograr, no cómo implementar
- **Trazabilidad**: cada clase identificada participa en la colaboración

### análisis puro
- **Sin tecnología**: PermisosRepository es concepto, no implementación
- **Sin detalles de UI**: GestionView es interfaz conceptual
- **Sin implementación**: mensajes expresan intención de negocio

## características del análisis

### responsabilidades identificadas
- **GestionView**: Habilitar solicitud de opciones y capturar selección del usuario
- **completeManagementController**: Orquestar lógica completa del caso de uso
- **PermisosRepository**: Proveer acceso conceptual a opciones disponibles
- **OpcionesMenu**: Representar estructura de opciones disponibles
- **Sesion**: Mantener estado de autenticación y información del usuario

### relaciones conceptuales
- **Delegación**: Vista delega lógica de negocio al controlador
- **Acceso**: Controlador accede a repositorio para obtener opciones
- **Creación**: Controlador crea estructura de opciones
- **Coordinación**: Vista coordina invocación de la colaboración según selección del usuario

## naturaleza del diagrama de colaboración

### capacidades vs ejecución
- **Capacidades mostradas**: El diagrama muestra todas las colaboraciones que `GestionView` **puede** invocar
- **Ejecución real**: En una ejecución específica, solo **una** colaboración es invocada según la selección del usuario
- **Análisis conceptual**: Se enfoca en responsabilidades y enlaces, no en flujo secuencial específico
- **Completitud**: Todas las transiciones posibles desde el estado SISTEMA_DISPONIBLE están representadas

## centralidad del caso de uso

### hub de navegación
- **Punto de convergencia**: Todos los casos de uso regresan al estado `SISTEMA_DISPONIBLE` vía `completeManagement()`
- **Punto de divergencia**: Desde aquí se accede a todas las funcionalidades del sistema
- **Multiplicidad de colaboraciones**: Conecta con todos los casos de uso según el patrón metodológico establecido

### gestión de flujo
- **Control de navegación**: Determina qué opciones están disponibles
- **Coordinación de casos**: Invoca la colaboración seleccionada
- **Mantenimiento de estado**: Preserva la sesión entre navegaciones

## conexión con disciplinas rup

### desde requisitos
- **Especificación detallada**: Estados del caso de uso → responsabilidades de clases
- **Prototipo**: Wireframes → diseño conceptual de vistas
- **Casos de uso**: Flujo de conversación → mensajes de colaboración

### hacia diseño
- **Clases conceptuales**: Base para clases de diseño tecnológico
- **Colaboraciones**: Patrones para implementación en frameworks específicos
- **Responsabilidades**: Guía para distribución en arquitectura técnica

**Código fuente:** [colaboracion.puml](colaboracion.puml)

## referencias

- [Especificación detallada](../../00-casos-uso/02-detalle/completeManagement/README.md)
- [Modelo del dominio](../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)
- [conversation-log.md](../../../../conversation-log.md) - Metodología de análisis RUP