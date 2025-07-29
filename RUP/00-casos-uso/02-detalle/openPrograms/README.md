# pySigHor > abrirProgramas > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-uso/openPrograms/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-09
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `abrirProgramas()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la gestión de programas académicos.

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|abrirProgramas()|
|**Actor primario**|Administrador|
|**Objetivo**|Presentar lista de programas académicos con capacidad de filtrado y navegación a operaciones CRUD|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Usuario autenticado como Administrador en estado MENU_PRINCIPAL|
|**Postcondición exitosa**|Lista de programas mostrada, usuario puede filtrar, crear, editar, eliminar o volver al menú|
|**Postcondición de fallo**|N/A - caso de uso sin condiciones de fallo|

## diagrama de especificación

<div align=center>

|![Caso de uso: abrirProgramas()](/images/RUP/00-casos-uso/02-detalle/abrirProgramas/abrirProgramas.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo
**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: gestión de programas académicos
<div align=center>

|![Wireframe: Gestión de programas](/images/RUP/00-casos-uso/02-detalle/abrirProgramas/abrirProgramas-wireframe.svg)|
|-|
|**Estado**: MostrandoLista / FiltrandoLista|

</div>

**Correspondencia con especificación:**
- Sistema "presenta lista de programas"
- Actor "visualiza programas disponibles"
- Sistema "permite filtrar lista"
- Actor "puede seleccionar opciones de gestión"

### validaciones del wireframe
- ¿La tabla muestra claramente código, nombre y descripción?
- ¿Es intuitivo el campo de búsqueda?
- ¿Los botones de acción están bien posicionados?
- ¿Falta información que el wireframe revela?

**Código fuente:** [prototipo.puml](prototipo.puml)

## conversación detallada

### flujo principal (único)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**Administrador**|solicita listar programas||
||**Sistema**|presenta lista de programas|• Código, nombre, descripción de cada programa<br>• Permite solicitar filtrar lista<br>• Permite solicitar crear programa nuevo<br>• Permite solicitar eliminar programa<br>• Permite solicitar editar programa|
|**Administrador**|solicita filtrar lista||(opcional)|
||**Sistema**|presenta lista filtrada|• Misma información con criterio aplicado|
|**Administrador**|solicita una de las opciones||

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**MostrandoLista**|Estado donde se muestra la lista completa de programas|Sistema debe presentar todos los programas sin filtro|
|**FiltrandoLista**|Estado donde se aplica criterio de búsqueda|Sistema debe filtrar y mostrar solo programas que coincidan|

## funcionalidad unificada: listar = filtrar = buscar

### concepto clave
- **abrirProgramas()** es un caso de uso que abarca:
  - **Listar** (sin criterio) → muestra todos los programas
  - **Filtrar/Buscar** (con criterio) → muestra programas que coinciden

### criterios de filtrado
- **Campo de búsqueda** aplica filtro a:
  - Código del programa
  - Nombre del programa
  - Descripción del programa

## opciones de navegación

### operaciones CRUD
- **Solicitar crear programa** → Navegar a `crearPrograma()`
- **Solicitar editar programa** → Navegar a `editarPrograma()`
- **Solicitar eliminar programa** → Navegar a `eliminarPrograma()`

### navegación del sistema
- **Solicitar salir** → Navegar a `completarGestion()`

## conexión con diagrama de contexto

Este caso de uso corresponde a la transición:
- **SISTEMA_DISPONIBLE** → `abrirProgramas()` → **PROGRAMAS_ABIERTO**

Y las transiciones de salida:
- **LISTANDO_PROGRAMAS** → `crearPrograma()` → **EDITANDO_PROGRAMA**
- **LISTANDO_PROGRAMAS** → `editarPrograma()` → **EDITANDO_PROGRAMA**
- **LISTANDO_PROGRAMAS** → `eliminarPrograma()` → **LISTANDO_PROGRAMAS**
- **LISTANDO_PROGRAMAS** → `completarGestion()` → **MENU_PRINCIPAL**

## vocabulario utilizado

### actor (Administrador)
- **solicita**: expresa la intención de realizar una acción
- **visualiza**: observa y comprende la información presentada
- **selecciona**: elige una opción específica o programa

### sistema
- **presenta**: muestra de forma organizada los programas y opciones
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
- Tiene objetivo claro: gestionar programas académicos
- Termina con selección de acción específica

### rol del actor
- **Entrada**: Administrador (desde menú principal)
- **Salida**: Administrador (con conocimiento de programas disponibles)
- **Estado**: Permanece como Administrador durante toda la conversación

### patrón de gestión de datos maestros
- **Punto de entrada**: Hub para todas las operaciones CRUD de programas
- **Funcionalidad unificada**: Listar + filtrar en un solo caso de uso
- **Navegación consistente**: Sigue el patrón establecido del sistema

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [completarGestion()](../completeManagement/README.md) - Caso de uso previo
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada