# pySigHor > abrirEdificios > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-u../openBuildings/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-17
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `abrirEdificios()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la gestión de edificios.

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|abrirEdificios()|
|**Actor primario**|Administrador|
|**Objetivo**|Presentar lista de edificios con capacidad de filtrado y navegación a operaciones CRUD|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Usuario autenticado como Administrador en estado SISTEMA_DISPONIBLE|
|**Postcondición exitosa**|Lista de edificios mostrada, usuario puede filtrar, crear, editar, eliminar o volver al sistema|
|**Postcondición de fallo**|N/A - caso de uso sin condiciones de fallo|

## diagrama de especificación

<div align=center>

|![Caso de uso: abrirEdificios()](/images/RUP/00-casos-uso/02-detalle/abrirEdificios/abrirEdificios.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo
**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: gestión de edificios
<div align=center>

|![Wireframe: Gestión de edificios](/images/RUP/00-casos-uso/02-detalle/abrirEdificios/abrirEdificios-wireframe.svg)|
|-|
|**Estado**: MostrandoLista / FiltrandoLista|

</div>

**Correspondencia con especificación:**
- Sistema "presenta lista de edificios"
- Actor "visualiza edificios disponibles"
- Sistema "permite filtrar lista"
- Actor "puede seleccionar opciones de gestión"

### validaciones del wireframe
- ¿La tabla muestra claramente ID y nombre?
- ¿Es intuitivo el campo de búsqueda?
- ¿Los botones de acción están bien posicionados?
- ¿Falta información que el wireframe revela?

**Código fuente:** [prototipo.puml](prototipo.puml)



## conversación detallada

### flujo principal (único)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**Administrador**|solicita listar edificios||
||**Sistema**|presenta lista de edificios|• ID, nombre de cada edificio<br>• Permite solicitar filtrar lista<br>• Permite solicitar crear edificio nuevo<br>• Permite solicitar eliminar edificio<br>• Permite solicitar editar edificio|
|**Administrador**|solicita filtrar lista||(opcional)|
||**Sistema**|presenta lista filtrada|• Misma información con criterio aplicado|
|**Administrador**|solicita una de las opciones||

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**MostrandoLista**|Estado donde se muestra la lista completa de edificios|Sistema debe presentar todos los edificios sin filtro|
|**FiltrandoLista**|Estado donde se aplica criterio de búsqueda|Sistema debe filtrar y mostrar solo edificios que coincidan|

## funcionalidad unificada: listar = filtrar = buscar

### concepto clave
- **abrirEdificios()** es un caso de uso que abarca:
  - **Listar** (sin criterio) → muestra todos los edificios
  - **Filtrar/Buscar** (con criterio) → muestra edificios que coinciden

### criterios de filtrado
- **Campo de búsqueda** aplica filtro a:
  - ID del edificio
  - Nombre del edificio

## opciones de navegación

### operaciones CRUD
- **Solicitar crear edificio** → Navegar a `crearEdificio()`
- **Solicitar editar edificio** → Navegar a `editarEdificio()`
- **Solicitar eliminar edificio** → Navegar a `eliminarEdificio()`

### navegación del sistema
- **Solicitar salir** → Navegar a `completarGestion()`

## conexión con diagrama de contexto

Este caso de uso corresponde a la transición:
- **SISTEMA_DISPONIBLE** → `abrirEdificios()` → **EDIFICIOS_ABIERTO**

Y las transiciones de salida:
- **EDIFICIOS_ABIERTO** → `crearEdificio()` → **EDIFICIO_ABIERTO**
- **EDIFICIOS_ABIERTO** → `editarEdificio()` → **EDIFICIO_ABIERTO**
- **EDIFICIOS_ABIERTO** → `eliminarEdificio()` → **EDIFICIOS_ABIERTO**
- **EDIFICIOS_ABIERTO** → `completarGestion()` → **SISTEMA_DISPONIBLE**

## vocabulario utilizado

### actor (Administrador)
- **solicita**: expresa la intención de realizar una acción
- **visualiza**: observa y comprende la información presentada
- **selecciona**: elige una opción específica o edificio

### sistema
- **presenta**: muestra de forma organizada los edificios y opciones
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
- Tiene objetivo claro: gestionar edificios
- Termina con selección de acción específica

### rol del actor
- **Entrada**: Administrador (desde sistema disponible)
- **Salida**: Administrador (con conocimiento de edificios disponibles)
- **Estado**: Permanece como Administrador durante toda la conversación

### patrón de gestión de datos maestros
- **Punto de entrada**: Hub para todas las operaciones CRUD de edificios
- **Funcionalidad unificada**: Listar + filtrar en un solo caso de uso
- **Navegación consistente**: Sigue el patrón establecido del sistema

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [completarGestion()](../completeManagement/README.md) - Caso de uso previo
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada