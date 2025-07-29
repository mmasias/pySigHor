# pySigHor > crearPrograma > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-u../createProgram/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-17
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `crearPrograma()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la creación de programas académicos aplicando la filosofía C→U como "el delgado".

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|crearPrograma()|
|**Actor primario**|Administrador|
|**Objetivo**|Crear programa académico con datos mínimos y transferir inmediatamente a edición completa|
|**Tipo**|Primario, esencial|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Usuario autenticado como Administrador en estado PROGRAMAS_ABIERTO|
|**Postcondición exitosa**|Programa creado con datos mínimos, usuario en modo edición completa|
|**Postcondición de fallo**|N/A - caso de uso sin condiciones de fallo|

## diagrama de especificación

<div align=center>

|![Caso de uso: crearPrograma()](/images/RUP/00-casos-uso/02-detalle/crearPrograma/crearPrograma.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo

**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: creación rápida de programa

<div align=center>

|![Wireframe: Creación de programa](/images/RUP/00-casos-uso/02-detalle/crearPrograma/crearPrograma-wireframe.svg)|
|-|
|**Estado**: SolicitandoDatos / CreandoPrograma|

</div>

**Correspondencia con especificación:**
- Sistema "solicita datos mínimos del programa"
- Actor "proporciona nombre del programa"
- Sistema "crea programa y transfiere a edición"
- Actor "llega automáticamente a editarPrograma()"

### validaciones del wireframe

- ¿El diálogo muestra claramente los campos mínimos requeridos?
- ¿Es intuitivo el proceso de creación rápida?
- ¿Los botones de acción están bien posicionados?
- ¿La transición a edición es clara para el usuario?

**Código fuente:** [prototipo.puml](prototipo.puml)

## conversación detallada

### flujo principal (único)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**Administrador**|solicita crear programa nuevo||
||**Sistema**|solicita datos mínimos del programa|• Nombre del programa (obligatorio)<br>• Permite solicitar crear programa<br>• Permite solicitar cancelar creación|
|**Administrador**|proporciona datos mínimos||
||**Sistema**|crea programa y transfiere a edición|• Programa creado con datos básicos<br>• Navegación automática a editarPrograma()|

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**SolicitandoDatos**|Estado donde se solicitan los datos mínimos para crear el programa|Sistema debe presentar formulario simple con campos obligatorios|
|**CreandoPrograma**|Estado donde se crea el programa y se transfiere control|Sistema debe crear entidad y navegar a editarPrograma()|

## funcionalidad delgada: crear = transferir

### concepto clave

- **crearPrograma()** es "el delgado" de la filosofía C→U que:
  - **Solicita** únicamente datos mínimos necesarios
  - **Crea** programa con información básica
  - **Transfiere** inmediatamente a editarPrograma() para completar

### datos mínimos requeridos

- **Nombre del programa** (único campo obligatorio)
- **Código automático** (generado por el sistema)
- **Estado inicial** (activo por defecto)

## opciones de navegación

### transición principal

- **Crear programa exitoso** → Navegar a `editarPrograma(programaNuevo)`

### navegación alternativa

- **Cancelar creación** → Navegar a `abrirProgramas()`

## conexión con diagrama de contexto

Este caso de uso corresponde a la transición:
- **PROGRAMAS_ABIERTO** → `crearPrograma()` → **PROGRAMA_ABIERTO**

Donde el programa llega a editarPrograma() con:
- **Datos mínimos**: Nombre proporcionado por el administrador
- **Datos automáticos**: Código generado, estado activo
- **Modo edición**: Formulario completo disponible para completar información

## vocabulario utilizado

### actor (Administrador)

- **solicita**: expresa la intención de crear un nuevo programa
- **proporciona**: suministra los datos mínimos requeridos

### sistema

- **solicita**: requiere información específica del administrador
- **crea**: genera nueva entidad programa con datos básicos
- **transfiere**: navega automáticamente al siguiente caso de uso

## características metodológicas

### separación de responsabilidades

- **Actor**: Solo proporciona datos mínimos esenciales
- **Sistema**: Solo crea entidad básica y transfiere control

### ausencia de detalles de implementación

- No especifica tecnología de persistencia
- No incluye detalles de generación de códigos
- No menciona estructura de almacenamiento

### conversación atómica delgada

- El caso de uso representa una conversación mínima y enfocada
- Tiene objetivo específico: crear y transferir
- Termina con navegación automática

### rol del actor

- **Entrada**: Administrador (desde programas abiertos)
- **Salida**: Administrador (en modo edición de programa nuevo)
- **Estado**: Permanece como Administrador durante toda la conversación

### patrón "el delgado" (filosofía C→U)

- **Funcionalidad mínima**: Solo crea con datos esenciales
- **Transferencia inmediata**: Pasa control a editarPrograma() automáticamente
- **Experiencia fluida**: Usuario no regresa a lista, continúa editando
- **Reutilización**: Aprovecha toda la funcionalidad de "el gordo"

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [editarPrograma()](../editProgram/README.md) - "El gordo" que recibe el control
- [abrirProgramas()](../openPrograms/README.md) - Caso de uso de origen
- [Filosofía C→U](../../../../extraDocs/008-filosofia-crud-creacion-edicion/README.md) - Metodología aplicada
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada