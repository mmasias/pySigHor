<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../../00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../../../00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../README.md)|
|-:|
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../../conversation-log.md)|

</div>

# pySigHor > configurarPreferenciasProfesor > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-27
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `configurarPreferenciasProfesor()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar configuración de orden de prioridad de recursos para profesores específicos.

## diagrama de colaboración

<div align=center>

|![Análisis: configurarPreferenciasProfesor()](/images/RUP/01-analisis/casos-uso/configurarPreferenciasProfesor/configurarPreferenciasProfesor-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### ConfigurarPreferenciasProfesorView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de configuración de preferencias de profesor específico
- Interactuar con el controlador para obtener recursos disponibles y preferencias actuales
- Presentar lista de recursos con orden de prioridad actual del profesor
- Permitir solicitar modificación del orden de prioridad de recursos
- Mantener sesión de configuración activa para modificaciones continuas
- Permitir solicitar guardar configuración o cancelar configuración

**Colaboraciones**:
- **Entrada**: Recibe `configurarPreferenciasProfesor(profesorId)` desde `:Profesor Abierto` (estado PROFESOR_ABIERTO)
- **Control**: Se comunica con `PreferenciasProfesorController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirEdicionProfesor` para regresar a edición de profesor

### clases de control

#### PreferenciasProfesorController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la carga de recursos disponibles y preferencias actuales del profesor
- Validar que el profesor existe y tiene recursos para configurar
- Manejar la lógica de modificación del orden de prioridad de recursos
- Procesar guardado de configuración tras modificaciones de orden
- Coordinar navegación entre configuración continua y finalización
- Servir como intermediario entre la vista y los repositorios

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `ConfigurarPreferenciasProfesorView`
- **Repositorios**: Delega operaciones a `ProfesorRepository` y `RecursoRepository`

### clases de entidad (entity)

#### ProfesorRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de profesores y sus preferencias
- Proporcionar método para obtener profesor por ID con preferencias actuales
- Implementar actualización de orden de prioridad de recursos del profesor
- Validar restricciones de configuración antes de guardar
- Gestionar relación profesor-recursos con orden de prioridad

**Colaboraciones**:
- **Control**: Responde a `PreferenciasProfesorController`
- **Entidad**: Gestiona instancias de `Profesor` y sus `PreferenciasRecurso`

#### RecursoRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de recursos disponibles en el sistema
- Proporcionar lista completa de recursos configurables para profesores
- Validar que los recursos en la configuración existen y están activos
- Mantener información actualizada de recursos disponibles

**Colaboraciones**:
- **Control**: Responde a `PreferenciasProfesorController`
- **Entidad**: Gestiona instancias de `Recurso`

#### Profesor
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información del profesor con sus preferencias de recursos
- Encapsular atributos básicos del profesor para identificación
- Mantener relación con preferencias de recursos ordenadas por prioridad
- Validar cambios en el orden de prioridad de recursos

**Colaboraciones**:
- **Repositorio**: Es gestionado por `ProfesorRepository`
- **Entidad**: Se relaciona con `PreferenciasRecurso`

#### PreferenciasRecurso
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la relación ordenada entre profesor y recurso
- Encapsular el orden de prioridad específico para cada recurso
- Mantener la integridad del orden secuencial (sin duplicados)
- Validar que el orden de prioridad es coherente y completo

**Colaboraciones**:
- **Entidad**: Relaciona `Profesor` con `Recurso` mediante prioridad
- **Repositorio**: Es gestionada por `ProfesorRepository`

#### Recurso
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información de recursos disponibles para configuración
- Encapsular atributos: nombre, descripción, tipo de recurso
- Mantener estado de disponibilidad para configuración
- Proporcionar información para presentación en configuración

**Colaboraciones**:
- **Repositorio**: Es gestionado por `RecursoRepository`
- **Entidad**: Se relaciona con `PreferenciasRecurso`

## flujo de colaboración principal

### secuencia: configurar preferencias de profesor

1. **Inicio**: `:Profesor Abierto` → `ConfigurarPreferenciasProfesorView.configurarPreferenciasProfesor(profesorId)`
2. **Carga profesor**: `ConfigurarPreferenciasProfesorView` → `PreferenciasProfesorController.cargarPreferenciasProfesor(profesorId)`
3. **Obtener profesor**: `PreferenciasProfesorController` → `ProfesorRepository.obtenerConPreferencias(profesorId) : Profesor`
4. **Obtener recursos**: `PreferenciasProfesorController` → `RecursoRepository.obtenerRecursosDisponibles() : List<Recurso>`
5. **Presentación**: `ConfigurarPreferenciasProfesorView` presenta lista de recursos con orden de prioridad actual
6. **Modificación**: Administrador modifica orden de prioridad en `ConfigurarPreferenciasProfesorView`
7. **Guardado**: `ConfigurarPreferenciasProfesorView` → `PreferenciasProfesorController.guardarConfiguracion(nuevasPreferencias)`
8. **Persistencia**: `PreferenciasProfesorController` → `ProfesorRepository.actualizarPreferencias(profesorId, preferencias)`
9. **Continuación**: 
   - **Configuración continua**: Permanece en `ConfigurarPreferenciasProfesorView` para más modificaciones
   - **Finalización**: `ConfigurarPreferenciasProfesorView` → **&lt;&lt;include&gt;&gt;** `:Collaboration EditarProfesor.editarProfesor(profesorId)`

## patrón de configuración específica para profesores - "el gordo"

### configuración continua

Este análisis implementa configuración específica que:
- **Presenta configuración completa**: Lista completa de recursos con orden de prioridad actual
- **Permite modificación continua**: Múltiples ciclos de reordenamiento sin salir del contexto
- **Guarda cambios incrementales**: Cada reordenamiento puede guardarse independientemente
- **Mantiene sesión activa**: El contexto de configuración se preserva durante las modificaciones

### responsabilidades de configuración continua

**ConfigurarPreferenciasProfesorView** maneja configuración continua:
- **Presenta configuración**: Lista de recursos ordenable con prioridad actual visible
- **Captura modificaciones**: Cambios en el orden de prioridad de recursos
- **Mantiene contexto**: Sesión de configuración activa para múltiples reordenamientos
- **Permite guardado**: Guardado incremental sin salir del contexto de configuración

**PreferenciasProfesorController** coordina configuración continua:
- **Valida orden**: Verifica que el nuevo orden de prioridad es válido y completo
- **Procesa incrementalmente**: Guarda cambios de orden específicos sin afectar otros datos
- **Mantiene coherencia**: Verifica integridad de la secuencia de prioridades
- **Gestiona navegación**: Permite continuar configurando o finalizar

## patrones arquitectónicos aplicados

### patrón MVC para configuración de preferencias

- **Model**: `Profesor` + `PreferenciasRecurso` + `Recurso` + Repositorios (datos y persistencia)
- **View**: `ConfigurarPreferenciasProfesorView` (configuración continua e interacción)
- **Controller**: `PreferenciasProfesorController` (coordinación y validación de configuración)

### patrón Repository con configuración específica

- **Abstracción de persistencia**: Repositorios encapsulan lógica de actualización de preferencias
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia de preferencias
- **Transacciones**: Puede implementar guardado transaccional de orden completo
- **Validaciones específicas**: Verifica restricciones de orden y secuencia en cada modificación

### configuración continua con múltiples ciclos

- **Ciclo 1**: Presentar orden actual → Modificar → Guardar → Continuar
- **Ciclo 2**: Reordenar más recursos → Guardar → Continuar o Finalizar
- **Flexibilidad**: Administrador controla cuándo finalizar la configuración
- **Contexto preservado**: Configuración de preferencias se mantiene durante todos los ciclos

## consideraciones de diseño específicas para preferencias de profesores

### separación de responsabilidades por entidades

El diseño separa claramente:
- **Profesor**: Datos básicos del profesor sin lógica de recursos
- **PreferenciasRecurso**: Relación específica profesor-recurso con prioridad
- **Recurso**: Información de recursos independiente de profesores
- **Repositorios especializados**: Cada entidad tiene su repositorio especializado

### validaciones de orden de prioridad

**PreferenciasProfesorController** debe verificar:
- **Secuencia completa**: Todos los recursos disponibles tienen prioridad asignada
- **Sin duplicados**: Cada posición de prioridad es única
- **Orden secuencial**: Prioridades van de 1 a N sin saltos
- **Recursos válidos**: Todos los recursos en el orden existen y están disponibles

### patrón include para navegación específica

- **Separación de responsabilidades**: configurarPreferenciasProfesor() se enfoca en configuración
- **Reutilización**: **&lt;&lt;include&gt;&gt;** editarProfesor() regresa al contexto de edición
- **Entrada específica**: Solo funciona desde `:Profesor Abierto` (estado PROFESOR_ABIERTO)
- **Navegación controlada**: Regresa específicamente a edición del mismo profesor

### flexibilidad de configuración continua

**ConfigurarPreferenciasProfesorView** puede implementar:
- **Reordenamiento visual**: Arrastrar y soltar recursos para cambiar prioridad
- **Configuración incremental**: Modificación prioridad por prioridad
- **Guardado automático**: Guardado inmediato tras cada reordenamiento
- **Validación en tiempo real**: Verificación inmediata de orden completo

## diferencias con editarProfesor()

### configurarPreferenciasProfesor() vs editarProfesor()

**configurarPreferenciasProfesor():**
- **Objetivo**: Configuración específica de orden de prioridad de recursos
- **Interacción**: Configuración continua de preferencias en contexto especializado
- **Datos**: Solo orden de prioridad de recursos, no datos básicos del profesor
- **Navegación**: Regresa específicamente a edición del mismo profesor

**editarProfesor():**
- **Objetivo**: Modificación de datos básicos del profesor
- **Interacción**: Edición completa de todos los campos del profesor
- **Datos**: Información básica del profesor (nombres, apellidos, contacto, etc.)
- **Navegación**: Puede ir a lista de profesores o continuar editando

### complementariedad con edición de profesores

- **editarProfesor()**: Modifica datos básicos del profesor
- **configurarPreferenciasProfesor()**: Configura preferencias específicas de recursos
- **Separación clara**: Cada caso maneja un aspecto específico de la información del profesor
- **Navegación integrada**: configurarPreferenciasProfesor() regresa a editarProfesor()

## impacto en el algoritmo de generación de horarios

### utilización de las preferencias configuradas

Las preferencias configuradas son utilizadas por:
- **generarHorario()**: El algoritmo considera el orden de prioridad para asignar aulas con recursos preferidos
- **Optimización**: Mejor puntuación en asignaciones que coinciden con preferencias del profesor
- **Resolución de conflictos**: Preferencias ayudan a decidir entre múltiples opciones válidas

### validaciones relacionadas con el algoritmo

**PreferenciasProfesorController** debe considerar:
- **Disponibilidad de recursos**: Solo recursos existentes en aulas pueden configurarse
- **Impacto en horarios existentes**: Cambios en preferencias pueden requerir regeneración
- **Coherencia algorítmica**: Orden de prioridad debe ser utilizable por el algoritmo de generación

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/configurarPreferenciasProfesor/README.md)
- [editarProfesor() - Caso relacionado](../editarProfesor/README.md)
- [generarHorario() - Caso dependiente](../generarHorario/README.md)
- [abrirProfesores() - Contexto de navegación](../abrirProfesores/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)