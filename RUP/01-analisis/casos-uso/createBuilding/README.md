# pySigHor > createBuilding > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/createBuilding/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-24
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `createBuilding()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar creación rápida de edificios con filosofía C→U.

## diagrama de colaboración

<div align=center>

|![Análisis: createBuilding()](/images/RUP/01-analisis/casos-uso/createBuilding/createBuilding-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### createBuildingView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de creación de edificio nuevo
- Presentar solicitud de datos mínimos del edificio
- Permitir solicitar crear edificio o cancelar creación
- Transferir inmediatamente a edición completa tras creación

**Colaboraciones**:
- **Entrada**: Recibe `createBuilding()` desde `:Edificios Abierto`
- **Control**: Se comunica con `EdificioController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration EditarEdificio` para completar datos

### clases de control

#### EdificioController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar el proceso de creación rápida de edificio
- Validar datos mínimos proporcionados por el administrador
- Crear edificio con información básica en el sistema
- Coordinar transferencia inmediata a edición completa
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `createBuildingView`
- **Repositorio**: Delega operaciones de datos a `EdificioRepository`

### clases de entidad (entity)

#### EdificioRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de edificios
- Implementar creación de edificio con datos mínimos
- Generar código único del edificio si no se proporciona
- Validar unicidad de código y datos básicos
- Preparar edificio para edición completa

**Colaboraciones**:
- **Control**: Responde a `EdificioController`
- **Entidad**: Gestiona instancias de `Edificio`

#### Edificio
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información mínima del edificio a crear
- Encapsular atributos esenciales: código, nombre del edificio
- Validar datos mínimos proporcionados
- Mantener estado preparado para edición completa
- Aplicar reglas de negocio para creación rápida

**Colaboraciones**:
- **Repositorio**: Es gestionado por `EdificioRepository`

## flujo de colaboración principal

### secuencia: crear edificio

1. **Inicio**: `:Edificios Abierto` → `createBuildingView.createBuilding()`
2. **Solicitud**: `createBuildingView` → `EdificioController.iniciarCreacion()`
3. **Presentación**: `createBuildingView` presenta formulario con campos mínimos
4. **Datos**: Administrador proporciona código, nombre en `createBuildingView`
5. **Creación**: `createBuildingView` → `EdificioController.createBuilding(datosMinimos)`
6. **Validación**: `EdificioController` → `EdificioRepository.validarDatosMinimos(datos)`
7. **Persistencia**: `EdificioController` → `EdificioRepository.crear(edificio) : Edificio`
8. **Transferencia**: `createBuildingView` → **&lt;&lt;include&gt;&gt;** `:Collaboration EditarEdificio.editarEdificio(edificioNuevo)`

## patrón de creación rápida para edificios - "el delgado"

### creación con filosofía C→U

Este análisis implementa creación rápida que:
- **Solicita datos mínimos**: Solo información esencial para crear el edificio
- **Crea inmediatamente**: Edificio funcional con datos básicos
- **Transfiere automáticamente**: Redirige a edición completa sin interrupciones
- **Aplica filosofía C→U**: Create→Update para eficiencia máxima

### responsabilidades de creación rápida

**createBuildingView** maneja creación mínima:
- **Presenta formulario**: Solo campos esenciales del edificio
- **Captura datos**: Información mínima necesaria para crear
- **Valida entrada**: Verificación básica antes de enviar
- **Transfiere automáticamente**: Redirige a edición completa tras creación

**EdificioController** coordina creación rápida:
- **Valida mínimos**: Verifica que datos esenciales estén completos
- **Crea eficientemente**: Proceso de creación optimizado
- **Gestiona transferencia**: Coordina redirección a edición automática
- **Mantiene coherencia**: Verifica integridad durante creación

## patrones arquitectónicos aplicados

### patrón MVC para creación de edificios

- **Model**: `Edificio` + `EdificioRepository` (creación y persistencia mínima)
- **View**: `createBuildingView` (formulario mínimo y transferencia)
- **Controller**: `EdificioController` (coordinación y validación de creación)

### patrón Repository con creación rápida

- **Abstracción de creación**: `EdificioRepository` encapsula lógica de creación mínima
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Validaciones esenciales**: Verifica solo restricciones críticas
- **Preparación para edición**: Deja edificio listo para completar datos

### filosofía C→U con transferencia automática

- **Create rápido**: Creación con datos mínimos indispensables
- **Update inmediato**: Transferencia automática a edición completa
- **Sin interrupciones**: Flujo continuo desde creación hasta edición
- **Eficiencia máxima**: Minimiza pasos y fricción del usuario

## consideraciones de diseño específicas para edificios

### reutilización del controlador

El diseño permite que `EdificioController` sea reutilizado:
- **Compartido**: Con editarEdificio() y eliminarEdificio()
- **Método específico**: createBuilding() con capacidades de creación rápida
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para creación mínima de edificios

### patrón include para transferencia automática

- **Separación de responsabilidades**: createBuilding() se enfoca en crear
- **Reutilización**: **&lt;&lt;include&gt;&gt;** editarEdificio() evita duplicar funcionalidad de edición
- **Transferencia fluida**: Paso automático de creación a edición completa
- **Contexto preservado**: Edificio recién creado se abre inmediatamente en edición

### flexibilidad de creación rápida

- **createBuildingView** puede implementar:
  - **Validación en tiempo real**: Verificación inmediata de campos
  - **Generación automática**: Código del edificio auto-generado si se omite
  - **Sugerencias inteligentes**: Autocompletado basado en datos existentes
  - **Persistencia temporal**: Guardado automático de borradores

### experiencia de usuario para "el delgado"

- **Formulario mínimo**: Solo campos esenciales para reducir fricción
- **Creación inmediata**: Proceso rápido sin pasos innecesarios
- **Transferencia transparente**: Paso automático a edición completa
- **Contexto preservado**: Usuario continúa trabajando sin interrupciones

## validaciones de negocio para creación rápida

### restricciones mínimas durante creación

**EdificioController** debe verificar durante creación:
- **Unicidad de código**: Código del edificio no duplicado (si se proporciona)
- **Completitud básica**: Nombre del edificio no vacío
- **Formato mínimo**: Datos con formato básico válido
- **Restricciones críticas**: Solo validaciones esenciales para crear

### manejo de errores en creación rápida

- **Validación inmediata**: Errores mostrados en tiempo real
- **Preservación de datos**: Mantener información ingresada válida
- **Corrección ágil**: Permitir corrección sin perder contexto
- **Alternativas**: Sugerir valores válidos cuando sea posible

## diferencias con otros casos CRUD de edificios

### createBuilding() vs editarEdificio()

**createBuilding():**
- **Objetivo**: Creación rápida con datos mínimos y transferencia automática
- **Interacción**: Formulario mínimo con redirección inmediata
- **Validaciones**: Solo restricciones críticas para creación
- **Resultado**: Edificio creado y transferido automáticamente a edición

**editarEdificio():**
- **Objetivo**: Modificación completa de datos existentes
- **Interacción**: Formulario completo con edición continua
- **Validaciones**: Restricciones completas de integridad
- **Resultado**: Edificio modificado con sesión de edición activa

### complementariedad CRUD para edificios

- **createBuilding()**: Crea edificios rápidamente y transfiere a edición
- **editarEdificio()**: Completa y modifica datos de edificios existentes
- **eliminarEdificio()**: Remueve edificios con confirmación segura
- **abrirEdificios()**: Lista y selecciona edificios para operaciones

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/createBuilding/README.md)
- [editarEdificio() - Caso de transferencia](../editarEdificio/README.md)
- [eliminarEdificio() - Caso complementario](../eliminarEdificio/README.md)
- [abrirEdificios() - Contexto de navegación](../abrirEdificios/README.md)
- [crearCurso() - Patrón de referencia](../crearCurso/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)