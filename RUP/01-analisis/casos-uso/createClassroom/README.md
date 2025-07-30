# pySigHor > createClassroom > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/createClassroom/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-24
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `createClassroom()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar creación rápida de aulas con filosofía C→U.

## diagrama de colaboración

<div align=center>

|![Análisis: createClassroom()](/images/RUP/01-analisis/casos-uso/createClassroom/createClassroom-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### createClassroomView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de creación de aula nueva
- Presentar solicitud de datos mínimos del aula
- Permitir solicitar crear aula o cancelar creación
- Transferir inmediatamente a edición completa tras creación

**Colaboraciones**:
- **Entrada**: Recibe `createClassroom()` desde `:Aulas Abierto`
- **Control**: Se comunica con `AulaController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration EditarAula` para completar datos

### clases de control

#### AulaController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar el proceso de creación rápida de aula
- Validar datos mínimos proporcionados por el administrador
- Crear aula con información básica en el sistema
- Coordinar transferencia inmediata a edición completa
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `createClassroomView`
- **Repositorio**: Delega operaciones de datos a `AulaRepository`

### clases de entidad (entity)

#### AulaRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de aulas
- Implementar creación de aula con datos mínimos
- Generar código único del aula si no se proporciona
- Validar unicidad de código y datos básicos
- Preparar aula para edición completa

**Colaboraciones**:
- **Control**: Responde a `AulaController`
- **Entidad**: Gestiona instancias de `Aula`

#### Aula
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información mínima del aula a crear
- Encapsular atributos esenciales: código, nombre del aula, edificio asociado
- Validar datos mínimos proporcionados
- Mantener estado preparado para edición completa
- Aplicar reglas de negocio para creación rápida

**Colaboraciones**:
- **Repositorio**: Es gestionado por `AulaRepository`

## flujo de colaboración principal

### secuencia: crear aula

1. **Inicio**: `:Aulas Abierto` → `createClassroomView.createClassroom()`
2. **Solicitud**: `createClassroomView` → `AulaController.iniciarCreacion()`
3. **Presentación**: `createClassroomView` presenta formulario con campos mínimos
4. **Datos**: Administrador proporciona código, nombre, edificio en `createClassroomView`
5. **Creación**: `createClassroomView` → `AulaController.createClassroom(datosMinimos)`
6. **Validación**: `AulaController` → `AulaRepository.validarDatosMinimos(datos)`
7. **Persistencia**: `AulaController` → `AulaRepository.crear(aula) : Aula`
8. **Transferencia**: `createClassroomView` → **&lt;&lt;include&gt;&gt;** `:Collaboration EditarAula.editarAula(aulaNueva)`

## patrón de creación rápida para aulas - "el delgado"

### creación con filosofía C→U

Este análisis implementa creación rápida que:
- **Solicita datos mínimos**: Solo información esencial para crear el aula
- **Crea inmediatamente**: Aula funcional con datos básicos
- **Transfiere automáticamente**: Redirige a edición completa sin interrupciones
- **Aplica filosofía C→U**: Create→Update para eficiencia máxima

### responsabilidades de creación rápida

**createClassroomView** maneja creación mínima:
- **Presenta formulario**: Solo campos esenciales del aula
- **Captura datos**: Información mínima necesaria para crear
- **Valida entrada**: Verificación básica antes de enviar
- **Transfiere automáticamente**: Redirige a edición completa tras creación

**AulaController** coordina creación rápida:
- **Valida mínimos**: Verifica que datos esenciales estén completos
- **Crea eficientemente**: Proceso de creación optimizado
- **Gestiona transferencia**: Coordina redirección a edición automática
- **Mantiene coherencia**: Verifica integridad durante creación

## patrones arquitectónicos aplicados

### patrón MVC para creación de aulas

- **Model**: `Aula` + `AulaRepository` (creación y persistencia mínima)
- **View**: `createClassroomView` (formulario mínimo y transferencia)
- **Controller**: `AulaController` (coordinación y validación de creación)

### patrón Repository con creación rápida

- **Abstracción de creación**: `AulaRepository` encapsula lógica de creación mínima
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Validaciones esenciales**: Verifica solo restricciones críticas
- **Preparación para edición**: Deja aula lista para completar datos

### filosofía C→U con transferencia automática

- **Create rápido**: Creación con datos mínimos indispensables
- **Update inmediato**: Transferencia automática a edición completa
- **Sin interrupciones**: Flujo continuo desde creación hasta edición
- **Eficiencia máxima**: Minimiza pasos y fricción del usuario

## consideraciones de diseño específicas para aulas

### reutilización del controlador

El diseño permite que `AulaController` sea reutilizado:
- **Compartido**: Con editarAula() y eliminarAula()
- **Método específico**: createClassroom() con capacidades de creación rápida
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para creación mínima de aulas

### patrón include para transferencia automática

- **Separación de responsabilidades**: createClassroom() se enfoca en crear
- **Reutilización**: **&lt;&lt;include&gt;&gt;** editarAula() evita duplicar funcionalidad de edición
- **Transferencia fluida**: Paso automático de creación a edición completa
- **Contexto preservado**: Aula recién creada se abre inmediatamente en edición

### flexibilidad de creación rápida

- **createClassroomView** puede implementar:
  - **Validación en tiempo real**: Verificación inmediata de campos
  - **Generación automática**: Código del aula auto-generado si se omite
  - **Sugerencias inteligentes**: Autocompletado basado en datos existentes
  - **Persistencia temporal**: Guardado automático de borradores

### experiencia de usuario para "el delgado"

- **Formulario mínimo**: Solo campos esenciales para reducir fricción
- **Creación inmediata**: Proceso rápido sin pasos innecesarios
- **Transferencia transparente**: Paso automático a edición completa
- **Contexto preservado**: Usuario continúa trabajando sin interrupciones

## validaciones de negocio para creación rápida

### restricciones mínimas durante creación

**AulaController** debe verificar durante creación:
- **Unicidad de código**: Código del aula no duplicado (si se proporciona)
- **Completitud básica**: Nombre del aula no vacío
- **Edificio válido**: Edificio asociado existe en el sistema
- **Restricciones críticas**: Solo validaciones esenciales para crear

### manejo de errores en creación rápida

- **Validación inmediata**: Errores mostrados en tiempo real
- **Preservación de datos**: Mantener información ingresada válida
- **Corrección ágil**: Permitir corrección sin perder contexto
- **Alternativas**: Sugerir valores válidos cuando sea posible

## diferencias con otros casos CRUD de aulas

### createClassroom() vs editarAula()

**createClassroom():**
- **Objetivo**: Creación rápida con datos mínimos y transferencia automática
- **Interacción**: Formulario mínimo con redirección inmediata
- **Validaciones**: Solo restricciones críticas para creación
- **Resultado**: Aula creada y transferida automáticamente a edición

**editarAula():**
- **Objetivo**: Modificación completa de datos existentes
- **Interacción**: Formulario completo con edición continua
- **Validaciones**: Restricciones completas de integridad
- **Resultado**: Aula modificada con sesión de edición activa

### complementariedad CRUD para aulas

- **createClassroom()**: Crea aulas rápidamente y transfiere a edición
- **editarAula()**: Completa y modifica datos de aulas existentes
- **eliminarAula()**: Remueve aulas con confirmación segura
- **abrirAulas()**: Lista y selecciona aulas para operaciones

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/createClassroom/README.md)
- [editarAula() - Caso de transferencia](../editarAula/README.md)
- [eliminarAula() - Caso complementario](../eliminarAula/README.md)
- [abrirAulas() - Contexto de navegación](../abrirAulas/README.md)
- [crearEdificio() - Patrón de referencia](../crearEdificio/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)