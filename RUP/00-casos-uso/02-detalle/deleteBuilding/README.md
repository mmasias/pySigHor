<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../../../01-analisis/casos-uso/README.md)|
|-:|
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../../conversation-log.md)|

</div>

# pySigHor > eliminarEdificio > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-u../deleteBuilding/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-24
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `eliminarEdificio()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la eliminación segura de edificios.

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|eliminarEdificio()|
|**Actor primario**|Administrador|
|**Objetivo**|Eliminar edificio de forma segura con confirmación previa|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Edificio seleccionado desde abrirEdificios(), usuario autenticado como Administrador|
|**Postcondición exitosa**|Edificio eliminado del sistema, usuario regresa a lista de edificios actualizada|
|**Postcondición de fallo**|N/A - caso de uso sin condiciones de fallo|

## diagrama de especificación

<div align=center>

|![Caso de uso: eliminarEdificio()](/images/RUP/00-casos-uso/02-detalle/eliminarEdificio/eliminarEdificio.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo

**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: confirmación de eliminación

<div align=center>

|![Wireframe: Eliminación de edificio](/images/RUP/00-casos-uso/02-detalle/eliminarEdificio/eliminarEdificio-wireframe.svg)|
|-|
|**Estado**: ConfirmandoEliminacion / EliminandoEdificio|

</div>

**Correspondencia con especificación:**
- Sistema "presenta información del edificio a eliminar"
- Actor "solicita confirmación de eliminación"
- Sistema "permite solicitar confirmar eliminación"
- Sistema "permite solicitar cancelar eliminación"

### validaciones del wireframe

- ¿Se presenta claramente la información del edificio a eliminar?
- ¿Es claro el impacto de la eliminación?
- ¿Las opciones de confirmación están bien diferenciadas?
- ¿La advertencia de eliminación es suficientemente visible?

**Código fuente:** [wireframes.puml](wireframes.puml)

## conversación detallada

### flujo principal (único)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**Administrador**|solicita eliminar edificio||
||**Sistema**|presenta información del edificio a eliminar|• Código, nombre del edificio<br>• Ubicación, descripción<br>• Observaciones, aulas asociadas<br>• Presenta advertencia de eliminación<br>• Permite solicitar confirmar eliminación<br>• Permite solicitar cancelar eliminación|
|**Administrador**|solicita confirmación de eliminación||(opcional)|
||**Sistema**|permite solicitar confirmar eliminación|• Permite confirmar eliminación<br>• Permite cancelar eliminación|
|**Administrador**|solicita una de las opciones||

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**ConfirmandoEliminacion**|Estado donde se presenta la información del edificio a eliminar|Sistema debe presentar todos los datos del edificio y advertencia de eliminación|
|**EliminandoEdificio**|Estado donde se procesa la eliminación del edificio|Sistema debe procesar eliminación y presentar resultado|

## funcionalidad de eliminación segura

### concepto clave

- **eliminarEdificio()** es un caso de uso que abarca:
  - **Presentar** información completa del edificio a eliminar
  - **Permitir solicitar** confirmación del administrador
  - **Procesar** eliminación del edificio del sistema

### información presentada

- **Datos del edificio** presentados para confirmación:
  - Código del edificio
  - Nombre del edificio
  - Ubicación del edificio
  - Descripción del edificio
  - Observaciones
  - Aulas asociadas al edificio
  - Advertencia sobre eliminación irreversible

## opciones de navegación

### operaciones de eliminación

- **Confirmar eliminación** → Edificio eliminado, **&lt;&lt;include&gt;&gt;** `abrirEdificios()` 
- **Cancelar eliminación** → **&lt;&lt;include&gt;&gt;** `abrirEdificios()` sin cambios

### navegación del sistema

- **Eliminación exitosa** → **&lt;&lt;include&gt;&gt;** `abrirEdificios()` con lista actualizada
- **Cancelación** → **&lt;&lt;include&gt;&gt;** `abrirEdificios()` sin modificaciones

## conexión con diagrama de contexto

Este caso de uso corresponde a las transiciones:
- **EDIFICIOS_ABIERTO** → `eliminarEdificio()` → **EDIFICIOS_ABIERTO**
- **EDIFICIO_ABIERTO** → `eliminarEdificio()` → **EDIFICIOS_ABIERTO**

Ambas transiciones incluyen:
- **&lt;&lt;include&gt;&gt;** `abrirEdificios()` → **EDIFICIOS_ABIERTO** (lista actualizada)

## vocabulario utilizado

### actor (Administrador)

- **solicita**: expresa la intención de eliminar un edificio específico
- **solicita**: expresa confirmación de eliminación del edificio

### sistema

- **presenta**: muestra información del edificio seleccionado
- **permite solicitar**: habilita confirmación o cancelación de eliminación
- **procesa**: ejecuta eliminación del edificio del sistema

## características metodológicas

### separación de responsabilidades

- **Actor**: Solo solicita eliminación y confirmación
- **Sistema**: Solo presenta información y permite solicitar confirmación

### ausencia de detalles de implementación

- No especifica tecnología de persistencia
- No incluye detalles de eliminación física vs lógica
- No menciona estructura de almacenamiento

### conversación de confirmación

- El caso de uso representa una conversación de verificación
- Tiene objetivo claro: eliminar edificio con confirmación
- Termina con confirmación o cancelación explícita

### rol del actor

- **Entrada**: Administrador (desde edificios abiertos)
- **Salida**: Administrador (con conocimiento de edificio eliminado o cancelación)
- **Estado**: Permanece como Administrador durante toda la conversación

### patrón de eliminación segura

- **Confirmación requerida**: Evita eliminaciones accidentales
- **Información completa**: Muestra qué se va a eliminar
- **Operación irreversible**: Claridad sobre las consecuencias
- **Navegación incluida**: **&lt;&lt;include&gt;&gt;** `abrirEdificios()` para mostrar lista actualizada

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [abrirEdificios()](../openBuildings/README.md) - Caso de uso de navegación
- [editarEdificio()](../editBuilding/README.md) - Caso complementario del CRUD
- [crearEdificio()](../createBuilding/README.md) - Caso complementario del CRUD
- [eliminarCurso()](../deleteCourse/README.md) - Patrón de referencia para eliminación
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada