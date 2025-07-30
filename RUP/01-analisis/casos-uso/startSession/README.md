# pySigHor > startSession > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/startSession/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Análisis
- **Versión**: 1.0
- **Fecha**: 2025-07-05
- **Autor**: Equipo de desarrollo

## propósito

Análisis del caso de uso `startSession()` mediante diagrama de colaboración MVC, identificando clases de análisis y sus interacciones conceptuales para realizar el caso de uso.

## diagrama de colaboración

<div align=center>

|![Análisis startSession()](/images/RUP/01-analisis/casos-uso/startSession/startSession-analysis.svg)|
|-|
|**Disciplina**: Análisis RUP<br>**Enfoque**: Diagramas de colaboración MVC|

</div>

## clases de análisis identificadas

### clases model (naranja #F2AC4E)
|Clase|Responsabilidad|Trazabilidad|
|-|-|-|
|**User**|Entidad del dominio que representa usuario del sistema|Modelo del dominio|
|**Session**|Entidad que representa estado de autenticación activa|Concepto del caso de uso|
|**UserRepository**|Concepto puro de acceso a datos de usuarios|Análisis puro|

### clases view (azul #629EF9)
|Clase|Responsabilidad|Derivación|
|-|-|-|
|**LoginView**|Ventana principal de interacción para autenticación|Wireframe SALT|

### clases controller (verde #b5bd68)
|Clase|Responsabilidad|Caso de uso|
|-|-|-|
|**StartSessionController**|Control y coordinación completa del caso de uso|startSession()|

### colaboraciones (verde claro #CDEBA5)
|Colaboración|Propósito|Invocación|
|-|-|-|
|**:System Available**|Transición al estado disponible del sistema|Tras autenticación exitosa|

## mensajes de colaboración

### flujo principal
|Origen|Destino|Mensaje|Intención|
|-|-|-|-|
|**UnregisteredUser**|**LoginView**|`startSession(username, password)`|Solicitar acceso al sistema|
|**LoginView**|**StartSessionController**|`authenticate(username, password)`|Delegar proceso de autenticación|
|**StartSessionController**|**UserRepository**|`validateCredentials(username, password)`|Verificar credenciales contra repositorio|
|**StartSessionController**|**Session**|`createSession(user)`|Establecer sesión activa|
|**LoginView**|**Session**|`getSession()`|Obtener sesión para siguiente caso|
|**LoginView**|**:System Available**|`systemAvailable(administrator)`|Transición a sistema disponible|

## enlaces de dependencia
- **LoginView** conoce a **StartSessionController** (delegación)
- **LoginView** conoce a **Session** (acceso a resultado)
- **LoginView** conoce a **:System Available** (transición de estado)
- **StartSessionController** conoce a **UserRepository** (validación)
- **StartSessionController** conoce a **Session** (creación estado)
- **StartSessionController** conoce a **User** (manipulación entidad)
- **UserRepository** conoce a **User** (gestión entidad)

## trazabilidad con artefactos previos

### con especificación detallada
- **Estados internos** → **Clases de análisis**
- **Choice point** → **UserRepository.validateCredentials()**
- **Transformación actor** → **UnregisteredUser → Administrator**

### con wireframe
- **Diálogo de login** → **LoginView**
- **Campos usuario/contraseña** → **Atributos de LoginView**
- **Estados de error** → **Manejo en StartSessionController**

### con modelo del dominio
- **User** (entidad) → **User** (clase de análisis)
- **Relaciones dominio** → **Enlaces colaboración**

## principios de análisis aplicados

### patrón mvc
- **Un controlador por caso de uso**: StartSessionController
- **Vista derivada de prototipo**: LoginView desde wireframe SALT
- **Modelo del dominio**: User con trazabilidad directa

### diagramas de colaboración
- **Foco en enlaces**: dependencias conceptuales, no secuencia temporal
- **Mensajes de intención**: qué se quiere lograr, no cómo implementar
- **Trazabilidad**: cada clase identificada participa en la colaboración

### análisis puro
- **Sin tecnología**: UserRepository es concepto, no implementación
- **Sin detalles de UI**: LoginView es interfaz conceptual
- **Sin implementación**: mensajes expresan intención de negocio

## características del análisis

### responsabilidades identificadas
- **LoginView**: Capturar credenciales y coordinar flujo de autenticación
- **StartSessionController**: Orquestar lógica completa del caso de uso
- **UserRepository**: Proveer acceso conceptual a datos de usuarios
- **User**: Representar entidad de dominio en el análisis
- **Session**: Mantener estado de autenticación activa

### relaciones conceptuales
- **Delegación**: Vista delega lógica de negocio al controlador
- **Acceso**: Controlador accede a repositorio para validación
- **Creación**: Controlador crea sesión tras validación exitosa
- **Transición**: Vista coordina transición al estado SISTEMA_DISPONIBLE

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

- [Especificación detallada](../../00-casos-uso/02-detalle/startSession/README.md)
- [Modelo del dominio](../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)
- [conversation-log.md](../../../../conversation-log.md) - Metodología de análisis RUP