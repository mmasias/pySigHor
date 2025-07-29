<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../../../01-analisis/casos-uso/README.md)|
|-:|
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../../conversation-log.md)|

</div>

# pySigHor > eliminarRecurso > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-u../deleteResource/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-24
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `eliminarRecurso()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la eliminación segura de recursos.

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|eliminarRecurso()|
|**Actor primario**|Administrador|
|**Objetivo**|Eliminar recurso de forma segura con confirmación previa|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Recurso seleccionado desde abrirRecursos(), usuario autenticado como Administrador|
|**Postcondición exitosa**|Recurso eliminado del sistema, usuario regresa a lista de recursos actualizada|
|**Postcondición de fallo**|N/A - caso de uso sin condiciones de fallo|

## diagrama de especificación

<div align=center>

|![Caso de uso: eliminarRecurso()](/images/RUP/00-casos-uso/02-detalle/eliminarRecurso/eliminarRecurso.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo

**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: confirmación de eliminación

<div align=center>

|![Wireframe: Eliminación de recurso](/images/RUP/00-casos-uso/02-detalle/eliminarRecurso/eliminarRecurso-wireframe.svg)|
|-|
|**Estado**: PresentingConfirmation / AwaitingDecision|

</div>

**Correspondencia con especificación:**
- Actor "solicita eliminar recurso"
- Sistema "presenta"
- Actor "solicita confirmar eliminación"
- Actor "solicita cancelar"

### validaciones del wireframe

- ¿Se presenta claramente la información del recurso a eliminar?
- ¿Es claro el impacto de la eliminación en preferencias y asignaciones?
- ¿Las opciones de confirmación están bien diferenciadas?
- ¿La advertencia de eliminación es suficientemente visible?

**Código fuente:** [wireframes.puml](wireframes.puml)

## conversación detallada

### flujo principal (único)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**Administrador**|solicita eliminar recurso||
||**Sistema**|presenta|• código del recurso<br>• nombre del recurso<br>• descripción del recurso<br>• profesores que lo prefieren<br>• aulas que lo ofrecen<br>• advertencia de eliminación|
|**Administrador**|solicita confirmar eliminación||
||**Sistema**|presenta resultado|• recurso eliminado exitosamente<br>• transferir a abrirRecursos()|
|**Administrador**|solicita cancelar||
||**Sistema**|presenta resultado|• transferir a abrirRecursos()|

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**PresentingConfirmation**|Estado donde el sistema presenta la información del recurso a eliminar|Sistema debe presentar datos del recurso, dependencias y advertencia|
|**AwaitingDecision**|Estado donde el administrador decide confirmar o cancelar|Administrador debe solicitar confirmar o cancelar eliminación|

## funcionalidad de eliminación segura

### concepto clave - eliminación con confirmación

- **eliminarRecurso()** implementa eliminación segura que:
  - **Presenta** información completa del recurso a eliminar
  - **Muestra** dependencias: profesores que lo prefieren y aulas que lo ofrecen
  - **Requiere** confirmación explícita del administrador
  - **Valida** que la eliminación no comprometa integridad del sistema

### información presentada (completa)

- **Datos del recurso**:
  - Código del recurso (identificación única)
  - Nombre del recurso (denominación)
  - Descripción del recurso (especificaciones)

### dependencias mostradas

- **Preferencias de profesores**: Profesores que han configurado este recurso como preferido
- **Recursos de aulas**: Aulas que declaran ofrecer este recurso
- **Impacto en horarios**: Posibles afectaciones en horarios generados

## opciones de navegación

### operaciones de eliminación

- **Confirmar y eliminar** → Recurso eliminado + **&lt;&lt;include&gt;&gt;** `abrirRecursos()`
- **Cancelar eliminación** → **&lt;&lt;include&gt;&gt;** `abrirRecursos()` sin cambios

### navegación del sistema

- **Eliminación exitosa** → **&lt;&lt;include&gt;&gt;** `abrirRecursos()` en `RECURSOS_ABIERTO`
- **Cancelación** → **&lt;&lt;include&gt;&gt;** `abrirRecursos()` en `RECURSOS_ABIERTO`

## conexión con diagrama de contexto

Este caso de uso corresponde a las transiciones:
- **RECURSOS_ABIERTO** → `eliminarRecurso()` → **RECURSOS_ABIERTO**
- **RECURSO_ABIERTO** → `eliminarRecurso()` → **RECURSOS_ABIERTO**

Las transiciones incluyen:
- **&lt;&lt;include&gt;&gt;** `abrirRecursos()` → **RECURSOS_ABIERTO** (tras eliminación o cancelación)

## vocabulario utilizado

### actor (Administrador)

- **solicita**: expresa la intención de eliminar un recurso
- **solicita**: expresa confirmación tras ver información completa
- **solicita**: expresa una de las opciones (confirmar o cancelar)

### sistema

- **presenta**: muestra información completa del recurso y dependencias
- **permite solicitar**: habilita confirmación tras mostrar advertencias
- **permite solicitar**: habilita cancelación en cualquier momento

## características metodológicas

### separación de responsabilidades

- **Actor**: Solicita eliminación, solicita confirmación de eliminación, solicita opción final
- **Sistema**: Presenta información completa y advertencias, permite solicitar confirmación

### ausencia de detalles de implementación

- No especifica tecnología de persistencia
- No incluye detalles de validación de integridad
- No menciona estructura de almacenamiento

### conversación de eliminación segura

- El caso de uso representa una conversación de eliminación con confirmación
- Tiene objetivo claro: eliminar recurso de forma segura
- Termina regresando a la lista de recursos actualizada

### rol del actor

- **Entrada**: Administrador (desde recursos abiertos o recurso específico)
- **Salida**: Administrador (con recurso eliminado y lista actualizada)
- **Estado**: Permanece como Administrador durante toda la conversación

### patrón de eliminación segura

- **Información completa**: Muestra todos los datos relevantes del recurso
- **Dependencias visibles**: Presenta impacto de la eliminación
- **Confirmación requerida**: Paso obligatorio de confirmación
- **Navegación incluida**: **&lt;&lt;include&gt;&gt;** `abrirRecursos()` para regresar

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [abrirRecursos()](../openResources/README.md) - Caso de uso de navegación
- [crearRecurso()](../createResource/README.md) - Caso complementario del CRUD
- [editarRecurso()](../editResource/README.md) - Caso complementario del CRUD
- [eliminarEdificio()](../deleteBuilding/README.md) - Patrón de referencia para eliminación segura
- [eliminarAula()](../deleteClassroom/README.md) - Patrón de referencia para eliminación segura
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada