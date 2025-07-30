# pySigHor > editBuilding > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editBuilding/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-24
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `editBuilding()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar edición completa de edificios.

## diagrama de colaboración

<div align=center>

|![Análisis: editBuilding()](/images/RUP/01-analisis/casos-uso/editBuilding/editBuilding-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### editBuildingView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de edición de edificio existente
- Presentar datos de edición con todos los campos del edificio
- Permitir modificación de campos del edificio
- Gestionar guardado de cambios y continuación de edición
- Manejar navegación de vuelta a la lista de edificios

**Colaboraciones**:
- **Entrada**: Recibe `editBuilding()` desde `:Edificios Abierto` o desde `crearEdificio()`
- **Control**: Se comunica con `EdificioController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirEdificios` al guardar y salir

### clases de control

#### EdificioController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar el proceso de edición completa de edificio
- Cargar datos existentes del edificio para edición
- Validar modificaciones proporcionadas por el administrador
- Procesar guardado de cambios en el edificio
- Gestionar sesión continua de edición
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `editBuildingView`
- **Repositorio**: Delega operaciones de datos a `EdificioRepository`

### clases de entidad (entity)

#### EdificioRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de edificios existentes
- Implementar carga de edificio por ID para edición
- Implementar actualización de edificio con datos completos
- Validar integridad de datos durante modificaciones
- Gestionar persistencia de cambios del edificio

**Colaboraciones**:
- **Control**: Responde a `EdificioController`
- **Entidad**: Gestiona instancias de `Edificio`

#### Edificio
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información completa del edificio a editar
- Encapsular todos los atributos: código, nombre, ubicación, descripción, observaciones
- Validar datos completos proporcionados durante edición
- Mantener integridad de datos durante modificaciones
- Aplicar reglas de negocio para edición completa

**Colaboraciones**:
- **Repositorio**: Es gestionado por `EdificioRepository`

## flujo de colaboración principal

### secuencia: editar edificio

1. **Inicio**: `:Edificios Abierto` → `editBuildingView.editBuilding(edificioId)`
2. **Carga**: `editBuildingView` → `EdificioController.cargarEdificio(edificioId)`
3. **Recuperación**: `EdificioController` → `EdificioRepository.obtenerPorId(edificioId) : Edificio`
4. **Presentación**: `editBuildingView` presenta formulario completo con datos del edificio
5. **Modificación**: Administrador modifica campos en `editBuildingView`
6. **Guardado**: `editBuildingView` → `EdificioController.guardarCambios(edificioModificado)`
7. **Validación**: `EdificioController` → `EdificioRepository.validarModificaciones(edificio)`
8. **Persistencia**: `EdificioController` → `EdificioRepository.actualizar(edificio) : Edificio`
9. **Navegación**: `editBuildingView` → **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirEdificios` (opcional)

## patrón de edición completa para edificios - "el gordo"

### edición con funcionalidad completa

Este análisis implementa edición completa que:
- **Presenta todos los campos**: Información completa del edificio para modificación
- **Permite edición continua**: Sesión de edición que puede mantenerse activa
- **Valida integridad**: Verificaciones completas de negocio durante guardado
- **Gestiona persistencia**: Guardado confiable de todos los cambios

### responsabilidades de edición completa

**editBuildingView** maneja edición completa:
- **Presenta formulario completo**: Todos los campos editables del edificio
- **Captura modificaciones**: Cambios en cualquier campo del edificio
- **Valida entrada**: Verificación completa antes de enviar
- **Gestiona navegación**: Opciones de continuar editando o salir

**EdificioController** coordina edición completa:
- **Carga datos completos**: Recupera toda la información del edificio
- **Valida modificaciones**: Verifica integridad de todos los cambios
- **Procesa guardado**: Gestiona persistencia confiable
- **Mantiene sesión**: Permite edición continua o finalización

## patrones arquitectónicos aplicados

### patrón MVC para edición de edificios

- **Model**: `Edificio` + `EdificioRepository` (edición y persistencia completa)
- **View**: `editBuildingView` (formulario completo y navegación)
- **Controller**: `EdificioController` (coordinación y validación de edición)

### patrón Repository con edición completa

- **Abstracción de edición**: `EdificioRepository` encapsula lógica de carga y actualización
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Validaciones completas**: Verifica todas las restricciones de integridad
- **Gestión de concurrencia**: Maneja actualizaciones concurrentes si es necesario

### filosofía de "el gordo" para edición

- **Carga completa**: Presenta toda la información disponible del edificio
- **Edición flexible**: Permite modificar cualquier campo
- **Sesión continua**: Mantiene estado de edición para múltiples operaciones
- **Validación exhaustiva**: Verifica integridad completa antes de guardar

## consideraciones de diseño específicas para edificios

### reutilización del controlador

El diseño permite que `EdificioController` sea reutilizado:
- **Compartido**: Con crearEdificio() y eliminarEdificio()
- **Método específico**: editBuilding() con capacidades de edición completa
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para edición completa de edificios

### patrón include para navegación

- **Separación de responsabilidades**: editBuilding() se enfoca en editar
- **Reutilización**: **&lt;&lt;include&gt;&gt;** abrirEdificios() evita duplicar funcionalidad de navegación
- **Navegación fluida**: Regreso automático a lista tras guardar y salir
- **Contexto actualizado**: Lista de edificios se actualiza con cambios realizados

### flexibilidad de edición completa

- **editBuildingView** puede implementar:
  - **Edición en línea**: Modificación directa de campos en vista
  - **Validación en tiempo real**: Verificación inmediata de cambios
  - **Guardado automático**: Persistencia de cambios incrementales
  - **Historial de cambios**: Registro de modificaciones realizadas

### experiencia de usuario para "el gordo"

- **Formulario completo**: Todos los campos disponibles para edición
- **Edición continua**: Sesión que puede mantenerse activa el tiempo necesario
- **Guardado flexible**: Opciones de guardar y continuar o guardar y salir
- **Navegación clara**: Opciones evidentes para finalizar o continuar editando

## validaciones de negocio para edición completa

### restricciones durante edición

**EdificioController** debe verificar durante edición:
- **Unicidad de código**: Código del edificio no duplicado con otros edificios
- **Completitud de datos**: Campos obligatorios (código, nombre) no vacíos
- **Formato de datos**: Todos los campos con formato válido
- **Restricciones de integridad**: Verificaciones completas de reglas de negocio

### manejo de errores en edición completa

- **Validación por campo**: Errores específicos para cada campo modificado
- **Preservación de cambios**: Mantener modificaciones válidas realizadas
- **Corrección guiada**: Indicar claramente qué debe corregirse
- **Recuperación de estado**: Permitir recuperar estado anterior si es necesario

## diferencias con otros casos CRUD de edificios

### editBuilding() vs crearEdificio()

**editBuilding():**
- **Objetivo**: Modificación completa de datos existentes
- **Interacción**: Formulario completo con edición continua
- **Validaciones**: Restricciones completas de integridad
- **Resultado**: Edificio modificado con sesión de edición activa

**crearEdificio():**
- **Objetivo**: Creación rápida con datos mínimos y transferencia automática
- **Interacción**: Formulario mínimo con redirección inmediata
- **Validaciones**: Solo restricciones críticas para creación
- **Resultado**: Edificio creado y transferido automáticamente a edición

### complementariedad con "el delgado"

- **Recibe de crearEdificio()**: Edificios recién creados para completar información
- **Proporciona funcionalidad completa**: Edición de todos los campos del edificio
- **Gestiona sesión continua**: Permite múltiples modificaciones en una sesión
- **Valida completamente**: Verificaciones exhaustivas de integridad

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/editBuilding/README.md)
- [crearEdificio() - Caso de transferencia](../crearEdificio/README.md)
- [eliminarEdificio() - Caso complementario](../eliminarEdificio/README.md)
- [abrirEdificios() - Contexto de navegación](../abrirEdificios/README.md)
- [editarCurso() - Patrón de referencia](../editarCurso/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)