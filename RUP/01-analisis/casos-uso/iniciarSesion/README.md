# pySigHor > iniciarSesion > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/iniciarSesion/README.md)|**Análisis**|[Diseño](/RUP/02-diseño/casos-uso/iniciarSesion/README.md)|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Análisis
- **Versión**: 1.0
- **Fecha**: 2025-07-05
- **Autor**: Equipo de desarrollo

## propósito

Análisis del caso de uso `iniciarSesion()` mediante diagrama de colaboración MVC, identificando clases de análisis y sus interacciones conceptuales para realizar el caso de uso.

## diagrama de colaboración

<div align=center>

|![Análisis iniciarSesion()](/images/RUP/01-analisis/casos-uso/iniciarSesion/iniciarSesion-analisis.svg)|
|-|
|**Disciplina**: Análisis RUP<br>**Enfoque**: Diagramas de colaboración MVC|

</div>

## clases de análisis identificadas

### clases model (naranja #F2AC4E)
|Clase|Responsabilidad|Trazabilidad|
|-|-|-|
|**Usuario**|Entidad del dominio que representa usuario del sistema|Modelo del dominio|
|**Sesion**|Entidad que representa estado de autenticación activa|Concepto del caso de uso|
|**UsuarioRepository**|Concepto puro de acceso a datos de usuarios|Análisis puro|

### clases view (azul #629EF9)
|Clase|Responsabilidad|Derivación|
|-|-|-|
|**LoginView**|Ventana principal de interacción para autenticación|Wireframe SALT|

### clases controller (verde #b5bd68)
|Clase|Responsabilidad|Caso de uso|
|-|-|-|
|**IniciarSesionController**|Control y coordinación completa del caso de uso|iniciarSesion()|

### colaboraciones (verde claro #CDEBA5)
|Colaboración|Propósito|Invocación|
|-|-|-|
|**:Sistema Disponible**|Transición al estado disponible del sistema|Tras autenticación exitosa|

## mensajes de colaboración

### flujo principal
|Origen|Destino|Mensaje|Intención|
|-|-|-|-|
|**UsuarioNoRegistrado**|**LoginView**|`iniciarSesion(usuario, contraseña)`|Solicitar acceso al sistema|
|**LoginView**|**IniciarSesionController**|`autenticar(usuario, contraseña)`|Delegar proceso de autenticación|
|**IniciarSesionController**|**UsuarioRepository**|`validarCredenciales(usuario, contraseña)`|Verificar credenciales contra repositorio|
|**IniciarSesionController**|**Sesion**|`crearSesion(usuario)`|Establecer sesión activa|
|**LoginView**|**Sesion**|`getSesion()`|Obtener sesión para siguiente caso|
|**LoginView**|**:Sistema Disponible**|`sistemaDisponible(administrador)`|Transición a sistema disponible|

## enlaces de dependencia
- **LoginView** conoce a **IniciarSesionController** (delegación)
- **LoginView** conoce a **Sesion** (acceso a resultado)
- **LoginView** conoce a **:Sistema Disponible** (transición de estado)
- **IniciarSesionController** conoce a **UsuarioRepository** (validación)
- **IniciarSesionController** conoce a **Sesion** (creación estado)
- **IniciarSesionController** conoce a **Usuario** (manipulación entidad)
- **UsuarioRepository** conoce a **Usuario** (gestión entidad)

## trazabilidad con artefactos previos

### con especificación detallada
- **Estados internos** → **Clases de análisis**
- **Choice point** → **UsuarioRepository.validarCredenciales()**
- **Transformación actor** → **UsuarioNoRegistrado → Administrador**

### con wireframe
- **Diálogo de login** → **LoginView**
- **Campos usuario/contraseña** → **Atributos de LoginView**
- **Estados de error** → **Manejo en IniciarSesionController**

### con modelo del dominio
- **Usuario** (entidad) → **Usuario** (clase de análisis)
- **Relaciones dominio** → **Enlaces colaboración**

## principios de análisis aplicados

### patrón mvc
- **Un controlador por caso de uso**: IniciarSesionController
- **Vista derivada de prototipo**: LoginView desde wireframe SALT
- **Modelo del dominio**: Usuario con trazabilidad directa

### diagramas de colaboración
- **Foco en enlaces**: dependencias conceptuales, no secuencia temporal
- **Mensajes de intención**: qué se quiere lograr, no cómo implementar
- **Trazabilidad**: cada clase identificada participa en la colaboración

### análisis puro
- **Sin tecnología**: UsuarioRepository es concepto, no implementación
- **Sin detalles de UI**: LoginView es interfaz conceptual
- **Sin implementación**: mensajes expresan intención de negocio

## características del análisis

### responsabilidades identificadas
- **LoginView**: Capturar credenciales y coordinar flujo de autenticación
- **IniciarSesionController**: Orquestar lógica completa del caso de uso
- **UsuarioRepository**: Proveer acceso conceptual a datos de usuarios
- **Usuario**: Representar entidad de dominio en el análisis
- **Sesion**: Mantener estado de autenticación activa

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

- [Especificación detallada](../../00-casos-uso/02-detalle/iniciarSesion/README.md)
- [Modelo del dominio](../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)
- [conversation-log.md](../../../../conversation-log.md) - Metodología de análisis RUP