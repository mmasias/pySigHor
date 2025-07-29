<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../../../01-analisis/casos-uso/README.md)|
|-:|
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../../conversation-log.md)|

</div>

# pySigHor > viewSchedule > Detalle y prototipado

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|**Detalle**|[Análisis](/RUP/01-analisis/casos-uso/viewSchedule/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Versión**: 1.0
- **Fecha**: 2025-07-25
- **Autor**: Equipo de desarrollo

## propósito

Especificación detallada del caso de uso `viewSchedule()` mediante diagrama de estado, mostrando la conversación completa entre el Administrador y el Sistema para la visualización del horario académico generado.

## información del caso de uso

|Atributo|Valor|
|-|-|
|**Nombre**|viewSchedule()|
|**Actor primario**|Administrador|
|**Objetivo**|Visualizar horario académico generado con manejo de ausencia|
|**Tipo**|Primario, esencial, consulta|
|**Nivel**|Objetivo de usuario|
|**Precondición**|Usuario autenticado como Administrador, acceso desde menú principal o transferencia desde generateSchedule()|
|**Postcondición exitosa**|Horario visualizado, usuario mantiene estado HORARIO_ABIERTO|
|**Postcondición de fallo**|N/A - caso sin condiciones de fallo (maneja ausencia informativamente)|

## diagrama de especificación

<div align=center>

|![Caso de uso: viewSchedule()](/images/RUP/00-casos-uso/02-detalle/viewSchedule/viewSchedule.svg)|
|-|
|Código fuente: [especificacion.puml](especificacion.puml)|

</div>

## prototipo de interfaz

### propósito del prototipo

**Objetivo:** Que te digan que NO lo antes posible - validar la especificación antes de invertir en desarrollo.

### wireframes

#### pantalla 1: horario disponible

<div align=center>

|![Wireframe: Horario académico](/images/RUP/00-casos-uso/02-detalle/viewSchedule/viewSchedule-wireframe-schedule.svg)|
|-|
|**Estado**: ProvidingSchedule|

</div>

#### pantalla 2: sin horario generado

<div align=center>

|![Wireframe: Sin horario disponible](/images/RUP/00-casos-uso/02-detalle/viewSchedule/viewSchedule-wireframe-noSchedule.svg)|
|-|
|**Estado**: ProvidingSchedule - sin horario|

</div>

**Correspondencia con especificación:**
- Actor "solicita consultar horario"
- Sistema "presenta" horario completo o mensaje de ausencia
- Actor "solicita navegar" dentro del horario
- Actor "solicita salir" para volver al menú

### validaciones del wireframe

- ¿Se presenta claramente el horario académico en formato tabular comprensible?
- ¿Es claro el mensaje cuando no hay horario disponible?
- ¿La información de resumen del horario es útil y concisa?
- ¿Las opciones de navegación están accesibles y claras?

**Código fuente:** [wireframes.puml](wireframes.puml)

## conversación detallada

### flujo principal (único)

|Actor|Acción|Sistema|Respuesta|
|-|-|-|-|
|**Administrador**|solicita consultar horario||
||**Sistema**|presenta|• horario generado<br>• mensaje si no hay horario|
|**Administrador**|solicita continuar consultando||
||**Sistema**|presenta|• mantener vista horario|
|**Administrador**|solicita salir de consulta||
||**Sistema**|presenta resultado|• transferir a completarGestion()|

## estados internos del caso de uso

|Estado|Descripción|Responsabilidad|
|-|-|-|
|**RequiringConsultation**|Estado donde el administrador solicita consultar horario|Actor debe solicitar consultar horario|
|**ProvidingSchedule**|Estado donde el sistema presenta horario o mensaje|Sistema debe presentar horario generado o mensaje si no hay horario|
|**Choice point**|Punto de decisión con opciones de navegación|Evaluación de continuar consultando o salir de consulta|

## funcionalidad de consulta de horario

### concepto clave - visualización simple

- **consultarHorario()** implementa consulta simple que:
  - **Verifica** existencia de horario generado previamente
  - **Presenta** horario completo en formato académico estándar
  - **Informa** claramente cuando no hay horario disponible
  - **Proporciona** opciones de navegación apropiadas

### información presentada

- **Horario completo**: Distribución por días y horas académicas
- **Detalles por clase**: Curso, profesor, aula para cada sesión
- **Resumen estadístico**: Cursos, profesores, aulas, horas totales
- **Metadatos**: Fecha y hora de generación del horario

### manejo de ausencia

- **Mensaje claro**: Información directa sobre ausencia de horario
- **Instrucciones**: Pasos para generar horario académico
- **Estado del sistema**: Información sobre datos disponibles para generación
- **Navegación**: Opciones apropiadas para continuar

## opciones de navegación

### operaciones de consulta

- **Visualizar horario** → Permanece en `HORARIO_ABIERTO`
- **Navegar dentro del horario** → Futuras extensiones (filtros, vistas)
- **Salir de consulta** → **<<include>>** `completarGestion()`

### navegación del sistema

- **Con horario disponible** → Permanece en `HORARIO_ABIERTO`
- **Sin horario disponible** → **<<include>>** `completarGestion()` tras información
- **Salida del usuario** → **<<include>>** `completarGestion()` en `SISTEMA_DISPONIBLE`

## conexión con diagrama de contexto

Este caso de uso corresponde a las transiciones:
- **SISTEMA_DISPONIBLE** → `consultarHorario()` → **HORARIO_ABIERTO** (con horario)
- **SISTEMA_DISPONIBLE** → `consultarHorario()` → **SISTEMA_DISPONIBLE** (sin horario)
- **HORARIO_ABIERTO** → `consultarHorario()` → **HORARIO_ABIERTO** (navegación interna)

Las transiciones incluyen:
- **<<include>>** `completarGestion()` → **SISTEMA_DISPONIBLE** (al salir)
- Transferencia automática desde `generateSchedule()` → **HORARIO_ABIERTO**

## vocabulario utilizado

### actor (Administrador)

- **solicita**: expresa la intención de consultar horario
- **solicita**: expresa navegación dentro del horario visualizado
- **solicita**: expresa salir de la consulta
- **solicita**: expresa continuar tras ver mensaje de ausencia

### sistema

- **presenta**: muestra verificación de existencia de horario
- **presenta**: muestra horario académico completo con detalles
- **presenta**: muestra mensaje informativo de ausencia de horario
- **permite solicitar**: habilita navegación dentro del horario
- **permite solicitar**: habilita salida de la consulta

## características metodológicas

### separación de responsabilidades

- **Actor**: Solicita consulta, solicita navegación, solicita salir
- **Sistema**: Presenta verificaciones, presenta horario o ausencia, permite solicitar acciones

### ausencia de detalles de implementación

- No especifica formato técnico de almacenamiento del horario
- No incluye detalles de renderizado de la interfaz tabular
- No menciona optimizaciones de carga de datos
- Trata visualización como presentación de información estructurada

### conversación de consulta informativa

- El caso de uso representa una conversación de consulta simple
- Tiene objetivo claro: mostrar horario académico o informar ausencia
- Maneja graciosamente la ausencia de datos sin considerarlo error

### rol del actor

- **Entrada**: Administrador (desde menú principal o transferencia automática)
- **Salida**: Administrador (visualizando horario o informado de ausencia)
- **Estado**: Permanece como Administrador durante toda la conversación

### patrón de consulta simple

- **Verificación directa**: Chequeo inmediato de existencia de datos
- **Presentación completa**: Información completa cuando está disponible
- **Manejo informativo**: Ausencia tratada como información, no error
- **Navegación flexible**: **<<include>>** `completarGestion()` para salir

## referencias

- [Diagrama de contexto - Administrador](../../01-actores-casos-uso/diagrama-contexto-administrador.md)
- [Modelo del dominio](../../00-modelo-del-dominio/modelo-dominio.md)
- [generateSchedule()](../generateSchedule/README.md) - Caso que genera el horario consultado
- [completarGestion()](../completeManagement/README.md) - Caso de navegación de salida
- [Análisis algorítmico original](../../../../reverseEngineering.md) - Formato del horario legacy
- [conversation-log.md](../../../../conversation-log.md) - Metodología de especificación detallada
- [QyA.log](../../../../QyA.log) - Decisiones de diseño para caso de consulta