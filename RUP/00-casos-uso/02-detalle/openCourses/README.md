# pySigHor > abrirCursos > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-u../openCourses/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|


## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-10
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `abrirCursos()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la gestión de cursos académicos.

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|abrirCursos()|
|**Actor primario**|Administrador|
|**Objetivo**|Presentar lista de cursos académicos con capacidad de filtrado y navegación a operaciones CRUD|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Usuario autenticado como Administrador en estado SISTEMA_DISPONIBLE|
|**Postcondición exitosa**|Lista de cursos mostrada, usuario puede filtrar, crear, editar, eliminar o volver al menú|
|**Postcondición de fallo**|N/A - caso de uso sin condiciones de fallo|

## diagrama de especificación

<div align=center>

|![Caso de uso: abrirCursos()](/images/RUP/00-casos-uso/02-detalle/abrirCursos/abrirCursos.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo
**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: gestión de cursos académicos
<div align=center>

|![Wireframe: Gestión de cursos](/images/RUP/00-casos-uso/02-detalle/abrirCursos/abrirCursos-wireframe.svg)|
|-|
|**Estado**: MostrandoLista / FiltrandoLista|

</div>

**Correspondencia con especificación:**
- Sistema "presenta lista de cursos"
- Actor "visualiza cursos disponibles"
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
|**Administrador**|solicita abrir cursos||
||**Sistema**|presenta lista de cursos|• Código, nombre, descripción de cada curso<br>• Permite solicitar filtrar lista<br>• Permite solicitar crear curso nuevo<br>• Permite solicitar eliminar curso<br>• Permite solicitar editar curso|
|**Administrador**|solicita filtrar lista||(opcional)|
||**Sistema**|presenta lista filtrada|• Misma información con criterio aplicado|
|**Administrador**|solicita una de las opciones||

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**MostrandoLista**|Estado donde se muestra la lista completa de cursos|Sistema debe presentar todos los cursos sin filtro|
|**FiltrandoLista**|Estado donde se aplica criterio de búsqueda|Sistema debe filtrar y mostrar solo cursos que coincidan|

## funcionalidad unificada: listar = filtrar = buscar

### concepto clave
- **abrirCursos()** es un caso de uso que abarca:
  - **Listar** (sin criterio) → muestra todos los cursos
  - **Filtrar/Buscar** (con criterio) → muestra cursos que coinciden

### criterios de filtrado
- **Campo de búsqueda** aplica filtro a:
  - Código del curso
  - Nombre del curso
  - Descripción del curso

## opciones de navegación

### operaciones CRUD
- **Solicitar crear curso** → Navegar a `crearCurso()`
- **Solicitar editar curso** → Navegar a `editarCurso()`
- **Solicitar eliminar curso** → Navegar a `eliminarCurso()`

### navegación del sistema
- **Solicitar mostrar menú** → Navegar a `completarGestion()`

## conexión con diagrama de contexto

Este caso de uso corresponde a la transición:
- **SISTEMA_DISPONIBLE** → `abrirCursos()` → **CURSOS_ABIERTO**

Y las transiciones de salida:
- **CURSOS_ABIERTO** → `crearCurso()` → **CURSO_ABIERTO**
- **CURSOS_ABIERTO** → `editarCurso()` → **CURSO_ABIERTO**
- **CURSOS_ABIERTO** → `eliminarCurso()` → **CURSOS_ABIERTO**
- **CURSOS_ABIERTO** → `completarGestion()` → **SISTEMA_DISPONIBLE**

## vocabulario utilizado

### actor (Administrador)
- **solicita**: expresa la intención de realizar una acción
- **visualiza**: observa y comprende la información presentada
- **selecciona**: elige una opción específica o curso

### sistema
- **presenta**: muestra de forma organizada los cursos y opciones
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
- Tiene objetivo claro: gestionar cursos académicos
- Termina con selección de acción específica

### rol del actor
- **Entrada**: Administrador (desde menú principal)
- **Salida**: Administrador (con conocimiento de cursos disponibles)
- **Estado**: Permanece como Administrador durante toda la conversación

### patrón de gestión de datos maestros
- **Punto de entrada**: Hub para todas las operaciones CRUD de cursos
- **Funcionalidad unificada**: Listar + filtrar en un solo caso de uso
- **Navegación consistente**: Sigue el patrón establecido del sistema

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [completarGestion()](../completeManagement/README.md) - Caso de uso previo
- [abrirProgramas()](../openPrograms/README.md) - Caso de uso similar
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada
