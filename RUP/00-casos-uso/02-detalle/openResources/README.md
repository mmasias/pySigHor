# pySigHor > openResources > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-uso/openResources/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-17
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `openResources()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la gestión de recursos.

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|openResources()|
|**Actor primario**|Administrador|
|**Objetivo**|Presentar lista de recursos con capacidad de filtrado y navegación a operaciones CRUD|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Usuario autenticado como Administrador en estado SISTEMA_DISPONIBLE|
|**Postcondición exitosa**|Lista de recursos mostrada, usuario puede filtrar, crear, editar, eliminar o volver al sistema|
|**Postcondición de fallo**|N/A - caso de uso sin condiciones de fallo|

## diagrama de especificación

<div align=center>

|![Caso de uso: openResources()](/images/RUP/00-casos-uso/02-detalle/openResources/openResources.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo
**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: gestión de recursos
<div align=center>

|![Wireframe: Gestión de recursos](/images/RUP/00-casos-uso/02-detalle/openResources/openResources-wireframe.svg)|
|-|
|**Estado**: MostrandoLista / FiltrandoLista|

</div>

**Correspondencia con especificación:**
- Sistema "presenta lista de recursos"
- Actor "visualiza recursos disponibles"
- Sistema "permite filtrar lista"
- Actor "puede seleccionar opciones de gestión"

### validaciones del wireframe
- ¿La tabla muestra claramente ID, nombre y descripción?
- ¿Es intuitivo el campo de búsqueda?
- ¿Los botones de acción están bien posicionados?
- ¿Falta información que el wireframe revela?

**Código fuente:** [prototipo.puml](prototipo.puml)

## conversación detallada

### flujo principal (único)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**Administrador**|solicita listar recursos||
||**Sistema**|presenta lista de recursos|• ID, nombre, descripción de cada recurso<br>• Permite solicitar filtrar lista<br>• Permite solicitar crear recurso nuevo<br>• Permite solicitar eliminar recurso<br>• Permite solicitar editar recurso|
|**Administrador**|solicita filtrar lista||(opcional)|
||**Sistema**|presenta lista filtrada|• Misma información con criterio aplicado|
|**Administrador**|solicita una de las opciones||

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**MostrandoLista**|Estado donde se muestra la lista completa de recursos|Sistema debe presentar todos los recursos sin filtro|
|**FiltrandoLista**|Estado donde se aplica criterio de búsqueda|Sistema debe filtrar y mostrar solo recursos que coincidan|

## funcionalidad unificada: listar = filtrar = buscar

### concepto clave
- **openResources()** es un caso de uso que abarca:
  - **Listar** (sin criterio) → muestra todos los recursos
  - **Filtrar/Buscar** (con criterio) → muestra recursos que coinciden

### criterios de filtrado
- **Campo de búsqueda** aplica filtro a:
  - ID del recurso
  - Nombre del recurso
  - Descripción del recurso

## opciones de navegación

### operaciones CRUD
- **Solicitar crear recurso** → Navegar a `crearRecurso()`
- **Solicitar editar recurso** → Navegar a `editarRecurso()`
- **Solicitar eliminar recurso** → Navegar a `eliminarRecurso()`

### navegación del sistema
- **Solicitar salir** → Navegar a `completeManagement()`

## conexión con diagrama de contexto

Este caso de uso corresponde a la transición:
- **SISTEMA_DISPONIBLE** → `openResources()` → **RECURSOS_ABIERTO**

Y las transiciones de salida:
- **RECURSOS_ABIERTO** → `crearRecurso()` → **RECURSO_ABIERTO**
- **RECURSOS_ABIERTO** → `editarRecurso()` → **RECURSO_ABIERTO**
- **RECURSOS_ABIERTO** → `eliminarRecurso()` → **RECURSOS_ABIERTO**
- **RECURSOS_ABIERTO** → `completeManagement()` → **SISTEMA_DISPONIBLE**

## vocabulario utilizado

### actor (Administrador)
- **solicita**: expresa la intención de realizar una acción
- **visualiza**: observa y comprende la información presentada
- **selecciona**: elige una opción específica o recurso

### sistema
- **presenta**: muestra de forma organizada los recursos y opciones
- **permite**: habilita funcionalidades de filtrado y navegación

## características metodológicas

### separación de responsabilidades
- **Actor**: Solo navega, filtra y selecciona opciones
- **Sistema**: Solo presenta datos, no procesa lógica de negocio

### ausencia de detalles de implementación
- No especifica tecnología de interfaz
- No incluye detalles de presentación específica
- No menciona estructura de datos o almacenamiento

### conversación atómica
- El caso de uso representa una conversación completa
- Tiene objetivo claro: gestionar recursos
- Termina con selección de acción específica

### rol del actor
- **Entrada**: Administrador (desde sistema disponible)
- **Salida**: Administrador (con conocimiento de recursos disponibles)
- **Estado**: Permanece como Administrador durante toda la conversación

### patrón de gestión de datos maestros
- **Punto de entrada**: Hub para todas las operaciones CRUD de recursos
- **Funcionalidad unificada**: Listar + filtrar en un solo caso de uso
- **Navegación consistente**: Sigue el patrón establecido del sistema

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [completeManagement()](../completeManagement/README.md) - Caso de uso previo
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada