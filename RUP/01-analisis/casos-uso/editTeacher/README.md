<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../../00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../../../00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../README.md)|
|-:|
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../../conversation-log.md)|

</div>

# pySigHor > editarProfesor > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarProfesor/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-20
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `editarProfesor()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar edición completa de profesores con capacidad de modificación continua.

## diagrama de colaboración

<div align=center>

|![Análisis: editarProfesor()](/images/RUP/01-analisis/casos-uso/editarProfesor/editarProfesor-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### EditarProfesorView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de edición de profesor
- Interactuar con el controlador para obtener datos del profesor
- Presentar datos completos de edición del profesor
- Permitir solicitar modificación de campos específicos
- Mantener sesión de edición activa para modificaciones continuas
- Permitir solicitar guardar cambios o cancelar edición

**Colaboraciones**:
- **Entrada**: Recibe `editarProfesor(profesorId)` desde `:Profesores Abierto`, `:Profesor Abierto` o desde `:Collaboration CrearProfesor`
- **Control**: Se comunica con `ProfesorController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirProfesores` para mostrar lista actualizada o mantiene `:Profesor Abierto`

### clases de control

#### ProfesorController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la carga de datos del profesor para edición
- Validar que el profesor existe y es editable
- Manejar la lógica de modificación de campos del profesor
- Procesar guardado de cambios tras modificaciones
- Coordinar navegación entre edición continua y finalización
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `EditarProfesorView`
- **Repositorio**: Delega operaciones de datos a `ProfesorRepository`

### clases de entidad (entity)

#### ProfesorRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de profesores
- Proporcionar método para obtener profesor por ID con datos completos
- Implementar actualización de campos del profesor
- Validar restricciones de integridad antes de guardar
- Gestionar relaciones con cursos asignados durante edición

**Colaboraciones**:
- **Control**: Responde a `ProfesorController`
- **Entidad**: Gestiona instancias de `Profesor`

#### Profesor
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información completa del profesor a editar
- Encapsular atributos: código, nombres, apellidos, correo, teléfono, observaciones
- Mantener relación con cursos asignados
- Validar cambios en campos específicos
- Mantener la integridad de los datos durante modificaciones continuas

**Colaboraciones**:
- **Repositorio**: Es gestionado por `ProfesorRepository`

## flujo de colaboración principal

### secuencia: editar profesor

1. **Inicio**: `:Profesores Abierto` → `EditarProfesorView.editarProfesor(profesorId)`
2. **Carga**: `EditarProfesorView` → `ProfesorController.cargarProfesorParaEdicion(profesorId)`
3. **Obtención**: `ProfesorController` → `ProfesorRepository.obtenerPorId(profesorId) : Profesor`
4. **Presentación**: `EditarProfesorView` presenta datos completos del `Profesor` para edición
5. **Modificación**: Administrador modifica campos en `EditarProfesorView`
6. **Guardado**: `EditarProfesorView` → `ProfesorController.guardarCambios(profesorModificado)`
7. **Persistencia**: `ProfesorController` → `ProfesorRepository.actualizar(profesor)`
8. **Continuación**: 
   - **Edición continua**: Permanece en `EditarProfesorView` para más modificaciones
   - **Finalización**: `EditarProfesorView` → **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirProfesores.abrirProfesores()`

## patrón de edición completa para profesores - "el gordo"

### edición continua

Este análisis implementa edición completa que:
- **Presenta datos completos**: Todos los campos del profesor disponibles para edición
- **Permite modificación continua**: Múltiples ciclos de edición sin salir del contexto
- **Guarda cambios incrementales**: Cada modificación puede guardarse independientemente
- **Mantiene sesión activa**: El estado `PROFESOR_ABIERTO` se preserva durante la edición

### responsabilidades de edición continua

**EditarProfesorView** maneja edición continua:
- **Presenta datos**: Información completa del profesor con campos editables
- **Captura modificaciones**: Cambios en cualquier campo del profesor
- **Mantiene contexto**: Sesión de edición activa para múltiples modificaciones
- **Permite guardado**: Guardado incremental sin salir del contexto

**ProfesorController** coordina edición continua:
- **Valida cambios**: Verifica que las modificaciones son válidas
- **Procesa incrementalmente**: Guarda cambios específicos sin afectar otros campos
- **Mantiene coherencia**: Verifica integridad durante modificaciones continuas
- **Gestiona navegación**: Permite continuar editando o finalizar

## patrones arquitectónicos aplicados

### patrón MVC para edición de profesores

- **Model**: `Profesor` + `ProfesorRepository` (datos del profesor y persistencia)
- **View**: `EditarProfesorView` (edición continua e interacción)
- **Controller**: `ProfesorController` (coordinación y validación de edición)

### patrón Repository con edición continua

- **Abstracción de persistencia**: `ProfesorRepository` encapsula lógica de actualización
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Transacciones**: Puede implementar guardado transaccional por campos
- **Validaciones continuas**: Verifica restricciones en cada modificación

### edición continua con múltiples ciclos

- **Ciclo 1**: Presentar datos → Modificar → Guardar → Continuar
- **Ciclo 2**: Modificar más campos → Guardar → Continuar o Finalizar
- **Flexibilidad**: Administrador controla cuándo finalizar la edición
- **Contexto preservado**: Estado `PROFESOR_ABIERTO` se mantiene durante todos los ciclos

## consideraciones de diseño específicas para profesores

### reutilización del controlador

El diseño permite que `ProfesorController` sea reutilizado:
- **Compartido**: Con crearProfesor() y eliminarProfesor()
- **Método específico**: editarProfesor() con capacidades de edición continua
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para edición continua de profesores

### patrón include para navegación flexible

- **Separación de responsabilidades**: editarProfesor() se enfoca en editar
- **Reutilización**: **&lt;&lt;include&gt;&gt;** abrirProfesores() evita duplicar funcionalidad de listado
- **Múltiples entradas**: Funciona desde `:Profesores Abierto`, `:Profesor Abierto` o desde creación
- **Navegación controlada**: Permite continuar editando o regresar a lista actualizada

### flexibilidad de edición continua

- **EditarProfesorView** puede implementar:
  - **Edición por campos**: Modificación campo por campo
  - **Edición en bloque**: Modificación de múltiples campos simultáneamente
  - **Guardado incremental**: Guardado automático o manual por cambios
  - **Validación en tiempo real**: Verificación inmediata de cambios

### experiencia de usuario para "el gordo"

- **Información completa**: Muestra todos los datos editables del profesor
- **Edición flexible**: Permite modificar cualquier combinación de campos
- **Sesión persistente**: Mantiene contexto de edición durante múltiples modificaciones
- **Navegación clara**: Opciones explícitas para continuar o finalizar edición

## validaciones de negocio para edición continua

### restricciones de integridad durante edición

**ProfesorController** debe verificar durante cada modificación:
- **Unicidad de código**: Código del profesor no duplicado
- **Formato de correo**: Correo electrónico válido si se modifica
- **Coherencia de datos**: Nombres y apellidos no vacíos
- **Relaciones activas**: Verificar impacto en cursos asignados si se modifican datos críticos

### manejo de errores en edición continua

- **Validación por campo**: Errores específicos para cada campo modificado
- **Preservación de cambios**: Mantener modificaciones válidas aunque otras fallen
- **Rollback parcial**: Revertir solo campos con errores
- **Continuidad**: Permitir continuar editando después de corregir errores

## diferencias con otros casos CRUD de profesores

### editarProfesor() vs crearProfesor()

**editarProfesor():**
- **Objetivo**: Modificación de datos existentes con edición continua
- **Interacción**: Múltiples ciclos de edición en sesión activa
- **Validaciones**: Preservar integridad con datos relacionados existentes
- **Resultado**: Profesor actualizado con posibilidad de continuar editando

**crearProfesor():**
- **Objetivo**: Entrada de datos nuevos con validación inicial
- **Interacción**: Formulario de creación con redirección a edición
- **Validaciones**: Verificar uniqueness y formato de datos nuevos
- **Resultado**: Profesor creado y redirigido a edición

### complementariedad CRUD para profesores

- **crearProfesor()**: Crea nuevos profesores y redirige a edición
- **editarProfesor()**: Modifica profesores existentes con edición continua
- **eliminarProfesor()**: Remueve profesores con confirmación segura
- **abrirProfesores()**: Lista y selecciona profesores para edición

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/editarProfesor/README.md)
- [crearProfesor() - Caso complementario](../crearProfesor/README.md)
- [eliminarProfesor() - Caso complementario](../eliminarProfesor/README.md)
- [abrirProfesores() - Contexto de navegación](../abrirProfesores/README.md)
- [editarCurso() - Patrón de referencia](../editarCurso/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)