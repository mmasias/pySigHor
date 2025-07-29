# pySigHor > createCourse > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-uso/createCourse/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-19
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `createCourse()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la creación de cursos aplicando la filosofía C→U como "el delgado".

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|createCourse()|
|**Actor primario**|Administrador|
|**Objetivo**|Crear curso con datos mínimos y transferir inmediatamente a edición completa|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Usuario autenticado como Administrador en estado CURSOS_ABIERTO|
|**Postcondición exitosa**|Curso creado con datos mínimos, usuario en modo edición completa|
|**Postcondición de fallo**|N/A - caso de uso sin condiciones de fallo|

## diagrama de especificación

<div align=center>

|![Caso de uso: crearCurso()](/images/RUP/00-casos-uso/02-detalle/createCourse/createCourse.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo

**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: creación rápida de curso

<div align=center>

|![Wireframe: Creación de curso](/images/RUP/00-casos-uso/02-detalle/crearCurso/crearCurso-wireframe.svg)|
|-|
|**Estado**: SolicitandoDatos / CreandoCurso|

</div>

**Correspondencia con especificación:**
- Sistema "solicita datos mínimos del curso"
- Actor "proporciona nombre del curso"  
- Sistema "permite solicitar crear curso"
- Sistema "permite solicitar cancelar creación"

### validaciones del wireframe

- ¿El campo nombre del curso es claramente obligatorio?
- ¿Es intuitivo el formulario de creación rápida?
- ¿Los botones de acción están bien diferenciados?
- ¿La transición a edición completa es clara?

**Código fuente:** [prototipo.puml](prototipo.puml)

## conversación detallada

### flujo principal (único)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**Administrador**|solicita crear curso nuevo||
||**Sistema**|presenta solicitud de datos mínimos del curso|• Nombre del curso (obligatorio)<br>• Permite solicitar crear curso<br>• Permite solicitar cancelar creación|
|**Administrador**|proporciona datos mínimos||
||**Sistema**|crea curso y transfiere a edición|• Crea curso con datos proporcionados<br>• Transfiere inmediatamente a editarCurso()|

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**SolicitandoDatos**|Estado donde se solicitan los datos mínimos del curso|Sistema debe presentar formulario con campos obligatorios mínimos|
|**CreandoCurso**|Estado donde se procesa la creación del curso|Sistema debe crear curso y transferir a edición completa|

## funcionalidad de creación rápida

### concepto clave - filosofía C→U

- **crearCurso()** es "el delgado" que:
  - **Presenta** solicitud de datos mínimos obligatorios
  - **Crea** curso básico en el sistema
  - **Transfiere** inmediatamente a editarCurso() para completar

### datos mínimos requeridos

- **Nombre del curso** (obligatorio)
- Otros campos se completan en editarCurso()

## opciones de navegación

### operaciones de creación

- **Crear curso** → Curso creado básico, transfiere a `editarCurso(cursoNuevo)`
- **Cancelar creación** → Regresa a `CURSOS_ABIERTO` sin cambios

### navegación del sistema

- **Creación exitosa** → `CURSO_ABIERTO` via `editarCurso(cursoNuevo)`
- **Cancelación** → `CURSOS_ABIERTO` sin modificaciones

## conexión con diagrama de contexto

Este caso de uso corresponde a la transición:
- **CURSOS_ABIERTO** → `crearCurso()` → **CURSO_ABIERTO**

La creación exitosa incluye:
- Transferencia automática a `editarCurso(cursoNuevo)` → **CURSO_ABIERTO**

## vocabulario utilizado

### actor (Administrador)

- **solicita**: expresa la intención de crear un curso nuevo
- **proporciona**: suministra los datos mínimos requeridos

### sistema

- **presenta**: muestra solicitud de campos mínimos obligatorios del curso
- **crea**: genera curso básico en el sistema
- **transfiere**: pasa automáticamente a modo edición completa

## características metodológicas

### separación de responsabilidades

- **Actor**: Solo solicita creación y proporciona datos mínimos
- **Sistema**: Solo presenta solicitud de datos obligatorios y crea curso básico

### ausencia de detalles de implementación

- No especifica tecnología de persistencia
- No incluye detalles de estructura de base de datos
- No menciona validaciones específicas de negocio

### conversación de creación rápida

- El caso de uso representa creación con datos mínimos
- Tiene objetivo claro: crear curso y pasar a edición
- Aplica filosofía C→U (Crear→Editar)

### rol del actor

- **Entrada**: Administrador (desde cursos abiertos)
- **Salida**: Administrador (en modo edición de curso nuevo)
- **Estado**: Permanece como Administrador durante transición

### patrón de creación minimalista

- **Datos mínimos**: Solo información esencial para crear
- **Transición inmediata**: No permanece en estado de creación
- **Completar en edición**: El "gordo" maneja información completa
- **Filosofía C→U**: Crear delgado → Editar gordo

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [abrirCursos()](../openCourses/README.md) - Caso de uso de navegación
- [editarCurso()](../editCourse/README.md) - Caso complementario del CRUD (el gordo)
- [crearPrograma()](../createProgram/README.md) - Patrón de referencia C→U
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada