# pySigHor > editCourse > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-uso/editCourse/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-19
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `editCourse()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la edición de cursos académicos.

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|editCourse()|
|**Actor primario**|Administrador|
|**Objetivo**|Presentar datos de edición de curso académico con capacidad de modificación y guardado|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Curso seleccionado desde openCourses() o curso recién creado desde crearCurso()|
|**Postcondición exitosa**|Curso modificado guardado, usuario puede continuar editando en CURSO_ABIERTO o volver al sistema|
|**Postcondición de fallo**|N/A - caso de uso sin condiciones de fallo|

## diagrama de especificación

<div align=center>

|![Caso de uso: editarCurso()](/images/RUP/00-casos-uso/02-detalle/editCourse/editCourse.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo

**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: edición de curso académico

<div align=center>

|![Wireframe: Edición de curso](/images/RUP/00-casos-uso/02-detalle/editCourse/editCourse-wireframe.svg)|
|-|
|**Estado**: EditandoDatos / GuardandoDatos|

</div>

**Correspondencia con especificación:**
- Sistema "presenta datos de edición"
- Actor "solicita modificar campos"
- Sistema "permite solicitar modificar información"
- Actor "puede solicitar guardar o cancelar"

### validaciones del wireframe

- ¿El formulario muestra claramente los campos del curso?
- ¿Son intuitivos los campos de entrada?
- ¿Los botones de acción están bien posicionados?
- ¿Falta información que el wireframe revela?

**Código fuente:** [prototipo.puml](prototipo.puml)

## conversación detallada

### flujo principal (único)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**Administrador**|solicita editar curso||
||**Sistema**|presenta datos de edición|• Código, nombre, descripción del curso<br>• Créditos, horas teóricas, horas prácticas<br>• Programa académico asociado<br>• Permite solicitar modificar campos<br>• Permite solicitar guardar curso<br>• Permite solicitar cancelar edición|
|**Administrador**|solicita modificar campos||(opcional)|
||**Sistema**|permite solicitar modificar información|• Permite editar todos los campos<br>• Permite solicitar guardar cambios<br>• Permite solicitar continuar editando|
|**Administrador**|solicita guardar y salir||

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**EditandoDatos**|Estado donde se presentan los datos de edición del curso|Sistema debe presentar todos los campos editables del curso|
|**GuardandoDatos**|Estado donde se procesan las modificaciones del curso|Sistema debe procesar cambios y permitir continuar o salir|

## funcionalidad de edición completa

### concepto clave - "el gordo"

- **editarCurso()** es "el gordo" que:
  - **Presenta** datos completos con todos los campos
  - **Permite** modificación de cualquier campo del curso
  - **Mantiene** sesión de edición activa (puede continuar)
  - **Guarda** cambios cuando el administrador solicita

### información presentada

- **Datos básicos del curso**:
  - Código del curso
  - Nombre del curso
  - Descripción del curso
- **Datos académicos**:
  - Número de créditos
  - Horas teóricas por semana
  - Horas prácticas por semana
- **Relaciones**:
  - Programa académico asociado

## opciones de navegación

### operaciones de edición

- **Continuar editando** → Mantiene `CURSO_ABIERTO` en modo edición
- **Guardar y salir** → `openCourses()` con lista actualizada
- **Cancelar edición** → `openCourses()` sin cambios

### navegación del sistema

- **Continuar editando** → Permanece en `CURSO_ABIERTO`
- **Guardar y salir** → `CURSOS_ABIERTO` via `openCourses()`
- **Cancelación** → `CURSOS_ABIERTO` sin modificaciones

## conexión con diagrama de contexto

Este caso de uso corresponde a las transiciones:
- **CURSOS_ABIERTO** → `editCourse()` → **CURSO_ABIERTO**
- **CURSO_ABIERTO** → `editCourse()` → **CURSO_ABIERTO** (continuar editando)
- **CURSO_ABIERTO** → `editCourse()` → **CURSOS_ABIERTO** (guardar y salir)

## vocabulario utilizado

### actor (Administrador)

- **solicita**: expresa la intención de editar un curso específico
- **solicita**: expresa la intención de modificar campos específicos
- **solicita**: expresa la intención de guardar cambios

### sistema

- **presenta**: muestra datos de edición del curso
- **permite solicitar**: habilita modificación de campos específicos
- **procesa**: ejecuta guardado de cambios en el sistema

## características metodológicas

### separación de responsabilidades

- **Actor**: Solo solicita edición, modificaciones y guardado
- **Sistema**: Solo presenta datos y permite solicitar modificaciones

### ausencia de detalles de implementación

- No especifica tecnología de persistencia
- No incluye detalles de validaciones de campos
- No menciona estructura de almacenamiento

### conversación de edición interactiva

- El caso de uso representa edición con múltiples modificaciones
- Permite ciclo de edición continua
- Termina cuando administrador solicita salir

### rol del actor

- **Entrada**: Administrador (desde cursos abiertos o curso recién creado)
- **Salida**: Administrador (puede continuar editando o regresar a lista)
- **Estado**: Permanece como Administrador durante toda la conversación

### patrón de edición completa

- **Datos completos**: Todos los campos del curso disponibles
- **Edición interactiva**: Permite múltiples modificaciones en sesión
- **Persistencia flexible**: Guarda cuando administrador solicita
- **Navegación flexible**: Puede continuar editando o salir

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [openCourses()](../openCourses/README.md) - Caso de uso de navegación
- [crearCurso()](../createCourse/README.md) - Caso complementario del CRUD (el delgado)
- [eliminarCurso()](../deleteCourse/README.md) - Caso complementario del CRUD
- [editarPrograma()](../editProgram/README.md) - Patrón de referencia para edición
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada