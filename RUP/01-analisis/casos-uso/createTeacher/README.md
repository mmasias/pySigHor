# pySigHor > createTeacher > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/createTeacher/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-20
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `createTeacher()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar creación rápida de profesores con filosofía C→U.

## diagrama de colaboración

<div align=center>

|![Análisis: createTeacher()](/images/RUP/01-analisis/casos-uso/createTeacher/createTeacher-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### createTeacherView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de creación de profesor nuevo
- Presentar solicitud de datos mínimos del profesor
- Permitir solicitar crear profesor o cancelar creación
- Transferir inmediatamente a edición completa tras creación

**Colaboraciones**:
- **Entrada**: Recibe `createTeacher()` desde `:Profesores Abierto`
- **Control**: Se comunica con `ProfesorController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration EditarProfesor` para completar datos

### clases de control

#### ProfesorController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar el proceso de creación rápida de profesor
- Validar datos mínimos proporcionados por el administrador
- Crear profesor con información básica en el sistema
- Coordinar transferencia inmediata a edición completa
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `createTeacherView`
- **Repositorio**: Delega operaciones de datos a `ProfesorRepository`

### clases de entidad (entity)

#### ProfesorRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de profesores
- Implementar creación de profesor con datos mínimos
- Generar código único del profesor si no se proporciona
- Validar unicidad de código y datos básicos
- Preparar profesor para edición completa

**Colaboraciones**:
- **Control**: Responde a `ProfesorController`
- **Entidad**: Gestiona instancias de `Profesor`

#### Profesor
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información mínima del profesor a crear
- Encapsular atributos esenciales: código, nombres, apellidos
- Validar datos mínimos proporcionados
- Mantener estado preparado para edición completa
- Aplicar reglas de negocio para creación rápida

**Colaboraciones**:
- **Repositorio**: Es gestionado por `ProfesorRepository`

## flujo de colaboración principal

### secuencia: crear profesor

1. **Inicio**: `:Profesores Abierto` → `createTeacherView.createTeacher()`
2. **Solicitud**: `createTeacherView` → `ProfesorController.iniciarCreacion()`
3. **Presentación**: `createTeacherView` presenta formulario con campos mínimos
4. **Datos**: Administrador proporciona código, nombres, apellidos en `createTeacherView`
5. **Creación**: `createTeacherView` → `ProfesorController.createTeacher(datosMinimos)`
6. **Validación**: `ProfesorController` → `ProfesorRepository.validarDatosMinimos(datos)`
7. **Persistencia**: `ProfesorController` → `ProfesorRepository.crear(profesor) : Profesor`
8. **Transferencia**: `createTeacherView` → **&lt;&lt;include&gt;&gt;** `:Collaboration EditarProfesor.editarProfesor(profesorNuevo)`

## patrón de creación rápida para profesores - "el delgado"

### creación con filosofía C→U

Este análisis implementa creación rápida que:
- **Solicita datos mínimos**: Solo información esencial para crear el profesor
- **Crea inmediatamente**: Profesor funcional con datos básicos
- **Transfiere automáticamente**: Redirige a edición completa sin interrupciones
- **Aplica filosofía C→U**: Create→Update para eficiencia máxima

### responsabilidades de creación rápida

**createTeacherView** maneja creación mínima:
- **Presenta formulario**: Solo campos esenciales del profesor
- **Captura datos**: Información mínima necesaria para crear
- **Valida entrada**: Verificación básica antes de enviar
- **Transfiere automáticamente**: Redirige a edición completa tras creación

**ProfesorController** coordina creación rápida:
- **Valida mínimos**: Verifica que datos esenciales estén completos
- **Crea eficientemente**: Proceso de creación optimizado
- **Gestiona transferencia**: Coordina redirección a edición automática
- **Mantiene coherencia**: Verifica integridad durante creación

## patrones arquitectónicos aplicados

### patrón MVC para creación de profesores

- **Model**: `Profesor` + `ProfesorRepository` (creación y persistencia mínima)
- **View**: `createTeacherView` (formulario mínimo y transferencia)
- **Controller**: `ProfesorController` (coordinación y validación de creación)

### patrón Repository con creación rápida

- **Abstracción de creación**: `ProfesorRepository` encapsula lógica de creación mínima
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Validaciones esenciales**: Verifica solo restricciones críticas
- **Preparación para edición**: Deja profesor listo para completar datos

### filosofía C→U con transferencia automática

- **Create rápido**: Creación con datos mínimos indispensables
- **Update inmediato**: Transferencia automática a edición completa
- **Sin interrupciones**: Flujo continuo desde creación hasta edición
- **Eficiencia máxima**: Minimiza pasos y fricción del usuario

## consideraciones de diseño específicas para profesores

### reutilización del controlador

El diseño permite que `ProfesorController` sea reutilizado:
- **Compartido**: Con editarProfesor() y eliminarProfesor()
- **Método específico**: createTeacher() con capacidades de creación rápida
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para creación mínima de profesores

### patrón include para transferencia automática

- **Separación de responsabilidades**: createTeacher() se enfoca en crear
- **Reutilización**: **&lt;&lt;include&gt;&gt;** editarProfesor() evita duplicar funcionalidad de edición
- **Transferencia fluida**: Paso automático de creación a edición completa
- **Contexto preservado**: Profesor recién creado se abre inmediatamente en edición

### flexibilidad de creación rápida

- **createTeacherView** puede implementar:
  - **Validación en tiempo real**: Verificación inmediata de campos
  - **Generación automática**: Código del profesor auto-generado si se omite
  - **Sugerencias inteligentes**: Autocompletado basado en datos existentes
  - **Persistencia temporal**: Guardado automático de borradores

### experiencia de usuario para "el delgado"

- **Formulario mínimo**: Solo campos esenciales para reducir fricción
- **Creación inmediata**: Proceso rápido sin pasos innecesarios
- **Transferencia transparente**: Paso automático a edición completa
- **Contexto preservado**: Usuario continúa trabajando sin interrupciones

## validaciones de negocio para creación rápida

### restricciones mínimas durante creación

**ProfesorController** debe verificar durante creación:
- **Unicidad de código**: Código del profesor no duplicado (si se proporciona)
- **Completitud básica**: Nombres y apellidos no vacíos
- **Formato mínimo**: Datos con formato básico válido
- **Restricciones críticas**: Solo validaciones esenciales para crear

### manejo de errores en creación rápida

- **Validación inmediata**: Errores mostrados en tiempo real
- **Preservación de datos**: Mantener información ingresada válida
- **Corrección ágil**: Permitir corrección sin perder contexto
- **Alternativas**: Sugerir valores válidos cuando sea posible

## diferencias con otros casos CRUD de profesores

### createTeacher() vs editarProfesor()

**createTeacher():**
- **Objetivo**: Creación rápida con datos mínimos y transferencia automática
- **Interacción**: Formulario mínimo con redirección inmediata
- **Validaciones**: Solo restricciones críticas para creación
- **Resultado**: Profesor creado y transferido automáticamente a edición

**editarProfesor():**
- **Objetivo**: Modificación completa de datos existentes
- **Interacción**: Formulario completo con edición continua
- **Validaciones**: Restricciones completas de integridad
- **Resultado**: Profesor modificado con sesión de edición activa

### complementariedad CRUD para profesores

- **createTeacher()**: Crea profesores rápidamente y transfiere a edición
- **editarProfesor()**: Completa y modifica datos de profesores existentes
- **eliminarProfesor()**: Remueve profesores con confirmación segura
- **abrirProfesores()**: Lista y selecciona profesores para operaciones

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/createTeacher/README.md)
- [editarProfesor() - Caso de transferencia](../editarProfesor/README.md)
- [eliminarProfesor() - Caso complementario](../eliminarProfesor/README.md)
- [abrirProfesores() - Contexto de navegación](../abrirProfesores/README.md)
- [crearCurso() - Patrón de referencia](../crearCurso/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)