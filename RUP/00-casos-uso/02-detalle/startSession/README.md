# pySigHor > startSession > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-uso/startSession/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-05
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `startSession()` mediante diagrama de estado, mostrando la conversación completa entre el UsuarioNoRegistrado y el Sistema para el proceso de autenticación.

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|startSession()|
|**Actor primario**|UsuarioNoRegistrado|
|**Objetivo**|Autenticar credenciales del usuario para permitir acceso al sistema|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Usuario no está autenticado en el sistema|
|**Postcondición exitosa**|UsuarioNoRegistrado se convierte en Administrador, sistema disponible para funcionalidades|
|**Postcondición de fallo**|Usuario no autenticado, sistema permanece en estado inicial|

## diagrama de especificación

<div align=center>

|![Caso de uso: startSession()](/images/RUP/00-casos-uso/02-detalle/startSession/startSession.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo
**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: diálogo de inicio de sesión
<div align=center>

|![Wireframe: Inicio de sesión](/images/RUP/00-casos-uso/02-detalle/startSession/startSession-wireframe.svg)|
|-|
|**Estado**: SolicitandoAcceso → ProporcionandoCredenciales|

</div>

**Correspondencia con especificación:**
- Actor "solicita acceder al sistema"
- Sistema "permite introducir usuario y contraseña"

#### pantalla 2: credenciales inválidas
<div align=center>

|![Wireframe: Error de credenciales](/images/RUP/00-casos-uso/02-detalle/startSession/startSession-invalid-credentials-wireframe.svg)|
|-|
|**Estado**: Choice point → regreso a SolicitandoAcceso|

</div>

**Correspondencia con especificación:**
- Choice point evalúa: "usuario:contraseña no válida"
- Sistema presenta mismo diálogo + mensaje de error

### validaciones del wireframe
- ¿El diálogo refleja correctamente la conversación actor-sistema?
- ¿Es clara la diferencia entre estado normal y estado de error?
- ¿La terminología "SigHor" es familiar para usuarios finales?
- ¿Faltan elementos en la especificación que el wireframe revela?

**Código fuente:** [prototipo.puml](prototipo.puml)

## conversación detallada

### flujo principal (éxito)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**UsuarioNoRegistrado**|solicita acceder al sistema||
||**Sistema**|permite introducir|• usuario<br>• contraseña|
|**UsuarioNoRegistrado**|introduce|• usuario<br>• contraseña|
|||usuario:contraseña válida|

### flujo alternativo (error)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**UsuarioNoRegistrado**|solicita acceder al sistema||
||**Sistema**|permite introducir|• usuario<br>• contraseña|
|**UsuarioNoRegistrado**|introduce|• usuario<br>• contraseña|
|||usuario:contraseña no válida|

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**SolicitandoAcceso**|Estado inicial donde se requiere autenticación|Sistema debe permitir introducir credenciales|
|**ProporcionandoCredenciales**|Usuario está introduciendo credenciales|Sistema recibe entrada de datos|
|**Punto de decisión**|Evaluación de credenciales introducidas|Sistema determina validez|

## validaciones del sistema

|Validación|Criterio|Resultado|
|-|-|-|
|**Credenciales válidas**|usuario:contraseña válida|Se cambia de rol de UsuarioNoRegistrado a Administrador|
|||Continuar con completeManagement()|
|**Credenciales inválidas**|usuario:contraseña no válida|Regresar a SolicitandoAcceso|

## conexión con diagrama de contexto

Este caso de uso corresponde a la transición:
- **SESION_CERRADA** → `startSession()` → **SISTEMA_DISPONIBLE**

La especificación detalla la transición desde **SESION_CERRADA** hacia **SISTEMA_DISPONIBLE** del diagrama de contexto del Administrador de Horarios.

## vocabulario utilizado

### actor (UsuarioNoRegistrado)
- **solicita**: inicia conversación pidiendo algo al sistema
- **introduce**: proporciona información requerida por el sistema

### sistema
- **permite**: habilita funcionalidad para el actor

## características metodológicas

### separación de responsabilidades
- **Actor**: Solo inicia conversación e introduce datos
- **Sistema**: Solo permite acciones, no se especifican validaciones explícitas

### ausencia de detalles de implementación
- No especifica tecnología de autenticación
- No incluye detalles de interfaz específica
- No menciona base de datos o repositorios específicos

### conversación atómica
- El caso de uso representa una conversación completa
- Tiene objetivo claro: autenticar usuario
- Termina en estado definido: éxito o fallo

### transformación del actor
- **Entrada**: UsuarioNoRegistrado (sin permisos en el sistema)
- **Salida**: Administrador (con acceso completo a funcionalidades)
- **Mecanismo**: Autenticación exitosa produce cambio de rol
- **Representación**: `UsuarioNoRegistrado → Administrador` en transición de salida

### trazabilidad con contexto
- Estados internos corresponden a flujo del diagrama de contexto
- Transición de salida conecta con siguiente caso de uso (mostrarMenu)
- Cambio de actor permite acceso a todos los casos de uso del Administrador

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada