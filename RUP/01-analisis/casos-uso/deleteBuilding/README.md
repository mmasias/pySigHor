<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../../00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../../../00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../README.md)|
|-:|
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../../conversation-log.md)|

</div>

# pySigHor > eliminarEdificio > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarEdificio/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-24
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `eliminarEdificio()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar eliminación segura de edificios con confirmación previa.

## diagrama de colaboración

<div align=center>

|![Análisis: eliminarEdificio()](/images/RUP/01-analisis/casos-uso/eliminarEdificio/eliminarEdificio-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### EliminarEdificioView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de eliminación de edificio existente
- Presentar información completa del edificio a eliminar
- Mostrar advertencia sobre eliminación irreversible
- Permitir confirmación o cancelación de eliminación
- Gestionar navegación de vuelta a la lista de edificios

**Colaboraciones**:
- **Entrada**: Recibe `eliminarEdificio()` desde `:Edificios Abierto`
- **Control**: Se comunica con `EdificioController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirEdificios` tras eliminación o cancelación

### clases de control

#### EdificioController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar el proceso de eliminación segura de edificio
- Cargar datos completos del edificio para confirmación
- Validar que el edificio puede ser eliminado
- Procesar eliminación tras confirmación del administrador
- Gestionar reglas de negocio para eliminación
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `EliminarEdificioView`
- **Repositorio**: Delega operaciones de datos a `EdificioRepository`

### clases de entidad (entity)

#### EdificioRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de edificios para eliminación
- Implementar carga de edificio por ID para confirmación
- Verificar dependencias antes de eliminación (aulas asociadas)
- Implementar eliminación segura del edificio
- Gestionar integridad referencial durante eliminación

**Colaboraciones**:
- **Control**: Responde a `EdificioController`
- **Entidad**: Gestiona instancias de `Edificio`

#### Edificio
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información completa del edificio a eliminar
- Encapsular todos los atributos para mostrar en confirmación
- Mantener información sobre dependencias (aulas asociadas)
- Validar que puede ser eliminado según reglas de negocio
- Proporcionar información para advertencias de eliminación

**Colaboraciones**:
- **Repositorio**: Es gestionado por `EdificioRepository`

## flujo de colaboración principal

### secuencia: eliminar edificio

1. **Inicio**: `:Edificios Abierto` → `EliminarEdificioView.eliminarEdificio(edificioId)`
2. **Carga**: `EliminarEdificioView` → `EdificioController.cargarParaEliminacion(edificioId)`
3. **Recuperación**: `EdificioController` → `EdificioRepository.obtenerConDependencias(edificioId) : Edificio`
4. **Presentación**: `EliminarEdificioView` presenta información completa del edificio y advertencia
5. **Confirmación**: Administrador confirma o cancela eliminación en `EliminarEdificioView`
6. **Validación**: `EliminarEdificioView` → `EdificioController.confirmarEliminacion(edificioId)`
7. **Verificación**: `EdificioController` → `EdificioRepository.validarEliminacion(edificioId) : boolean`
8. **Eliminación**: `EdificioController` → `EdificioRepository.eliminar(edificioId) : boolean`
9. **Navegación**: `EliminarEdificioView` → **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirEdificios`

## patrón de eliminación segura para edificios

### eliminación con confirmación previa

Este análisis implementa eliminación segura que:
- **Presenta información completa**: Todos los datos del edificio a eliminar
- **Muestra dependencias**: Información sobre aulas asociadas al edificio
- **Requiere confirmación**: Paso obligatorio de confirmación del administrador
- **Valida eliminación**: Verificaciones de integridad antes de proceder

### responsabilidades de eliminación segura

**EliminarEdificioView** maneja confirmación:
- **Presenta información completa**: Todos los datos del edificio para revisión
- **Muestra advertencias**: Información sobre consecuencias de eliminación
- **Captura confirmación**: Decisión explícita del administrador
- **Gestiona navegación**: Regreso a lista tras eliminación o cancelación

**EdificioController** coordina eliminación segura:
- **Carga datos completos**: Recupera información completa del edificio
- **Valida eliminación**: Verifica que edificio puede ser eliminado
- **Procesa eliminación**: Gestiona eliminación tras confirmación
- **Mantiene integridad**: Verifica reglas de negocio durante eliminación

## patrones arquitectónicos aplicados

### patrón MVC para eliminación de edificios

- **Model**: `Edificio` + `EdificioRepository` (eliminación y validación de integridad)
- **View**: `EliminarEdificioView` (confirmación y advertencias)
- **Controller**: `EdificioController` (coordinación y validación de eliminación)

### patrón Repository con eliminación segura

- **Abstracción de eliminación**: `EdificioRepository` encapsula lógica de eliminación
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Validaciones de integridad**: Verifica dependencias antes de eliminar
- **Eliminación transaccional**: Asegura consistencia durante eliminación

### confirmación previa obligatoria

- **Carga información completa**: Presenta todos los datos para revisión
- **Muestra consecuencias**: Advierte sobre impacto de eliminación
- **Requiere confirmación**: Paso obligatorio antes de proceder
- **Permite cancelación**: Opción de cancelar en cualquier momento

## consideraciones de diseño específicas para edificios

### reutilización del controlador

El diseño permite que `EdificioController` sea reutilizado:
- **Compartido**: Con crearEdificio() y editarEdificio()
- **Método específico**: eliminarEdificio() con capacidades de eliminación segura
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para eliminación segura de edificios

### patrón include para navegación

- **Separación de responsabilidades**: eliminarEdificio() se enfoca en eliminar
- **Reutilización**: **&lt;&lt;include&gt;&gt;** abrirEdificios() evita duplicar funcionalidad de navegación
- **Navegación fluida**: Regreso automático a lista tras eliminación o cancelación
- **Contexto actualizado**: Lista de edificios se actualiza tras eliminación

### validación de dependencias

- **EdificioRepository** debe verificar:
  - **Aulas asociadas**: Verificar si hay aulas en el edificio
  - **Dependencias activas**: Comprobar relaciones que impiden eliminación
  - **Integridad referencial**: Asegurar consistencia tras eliminación
  - **Reglas de negocio**: Verificar restricciones específicas del dominio

### experiencia de usuario para eliminación

- **Información completa**: Mostrar todos los datos del edificio a eliminar
- **Advertencias claras**: Explicar consecuencias de la eliminación
- **Confirmación explícita**: Requerir acción consciente del administrador
- **Cancelación fácil**: Permitir cancelar sin consecuencias

## validaciones de negocio para eliminación segura

### restricciones de eliminación

**EdificioController** debe verificar antes de eliminar:
- **Aulas asociadas**: No eliminar edificio con aulas activas
- **Dependencias del sistema**: Verificar relaciones con otros módulos
- **Restricciones temporales**: Verificar si hay restricciones por períodos activos
- **Permisos administrativos**: Administrador autorizado para eliminar edificios

### manejo de errores en eliminación

- **Dependencias encontradas**: Explicar por qué no se puede eliminar
- **Errores de sistema**: Manejo graceful de fallos de eliminación
- **Información de dependencias**: Mostrar qué impide la eliminación
- **Alternativas sugeridas**: Proponer acciones para resolver dependencias

## diferencias con otros casos CRUD de edificios

### eliminarEdificio() vs editarEdificio()

**eliminarEdificio():**
- **Objetivo**: Eliminación segura con confirmación previa
- **Interacción**: Confirmación de información completa
- **Validaciones**: Verificación de dependencias e integridad
- **Resultado**: Edificio eliminado y regreso a lista actualizada

**editarEdificio():**
- **Objetivo**: Modificación completa de datos existentes
- **Interacción**: Formulario completo con edición continua
- **Validaciones**: Restricciones completas de integridad de datos
- **Resultado**: Edificio modificado con sesión de edición activa

### complementariedad con otros casos CRUD

- **Depende de abrirEdificios()**: Recibe edificio seleccionado para eliminar
- **Coordina con editarEdificio()**: Alternativa de modificación vs eliminación
- **Relaciona con crearEdificio()**: Operación inversa de creación
- **Actualiza abrirEdificios()**: Lista actualizada tras eliminación

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/eliminarEdificio/README.md)
- [crearEdificio() - Caso complementario](../crearEdificio/README.md)
- [editarEdificio() - Caso complementario](../editarEdificio/README.md)
- [abrirEdificios() - Contexto de navegación](../abrirEdificios/README.md)
- [eliminarCurso() - Patrón de referencia](../eliminarCurso/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)