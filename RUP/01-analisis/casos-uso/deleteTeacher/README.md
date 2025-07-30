<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](../../../00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](../../../00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](../../../00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../README.md)|
|-:|
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../../../README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../../../conversation-log.md)|

</div>

# pySigHor > eliminarProfesor > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarProfesor/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-20
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `eliminarProfesor()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar eliminación segura de profesores con confirmación.

## diagrama de colaboración

<div align=center>

|![Análisis: eliminarProfesor()](/images/RUP/01-analisis/casos-uso/eliminarProfesor/eliminarProfesor-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### EliminarProfesorView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de eliminación de profesor
- Interactuar con el controlador para obtener información del profesor
- Presentar información completa del profesor a eliminar
- Presentar advertencia de eliminación irreversible
- Permitir solicitar confirmación o cancelación del administrador

**Colaboraciones**:
- **Entrada**: Recibe `eliminarProfesor(profesorId)` desde `:Profesores Abierto` o `:Profesor Abierto`
- **Control**: Se comunica con `ProfesorController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirProfesores` para mostrar lista actualizada

### clases de control

#### ProfesorController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la carga de datos del profesor a eliminar
- Validar que el profesor existe y puede ser eliminado
- Verificar restricciones de integridad (no hay cursos asignados activos)
- Manejar la lógica de eliminación tras confirmación
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `EliminarProfesorView`
- **Repositorio**: Delega operaciones de datos a `ProfesorRepository`

### clases de entidad (entity)

#### ProfesorRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de profesores
- Proporcionar método para obtener profesor por ID
- Implementar eliminación física o lógica del profesor
- Verificar restricciones de integridad antes de eliminar
- Gestionar relaciones con cursos asignados

**Colaboraciones**:
- **Control**: Responde a `ProfesorController`
- **Entidad**: Gestiona instancias de `Profesor`

#### Profesor
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información del profesor a eliminar
- Encapsular atributos: código, nombres, apellidos, correo, teléfono, observaciones
- Mantener relación con cursos asignados
- Validar si el profesor puede ser eliminado
- Mantener la integridad de los datos durante eliminación

**Colaboraciones**:
- **Repositorio**: Es gestionado por `ProfesorRepository`

## flujo de colaboración principal

### secuencia: eliminar profesor

1. **Inicio**: `:Profesores Abierto` → `EliminarProfesorView.eliminarProfesor(profesorId)`
2. **Carga**: `EliminarProfesorView` → `ProfesorController.cargarProfesorParaEliminacion(profesorId)`
3. **Obtención**: `ProfesorController` → `ProfesorRepository.obtenerPorId(profesorId) : Profesor`
4. **Presentación**: `EliminarProfesorView` presenta información del `Profesor` con advertencia
5. **Confirmación**: Administrador confirma o cancela en `EliminarProfesorView`
6. **Eliminación**: `EliminarProfesorView` → `ProfesorController.eliminarProfesor(profesorId)`
7. **Persistencia**: `ProfesorController` → `ProfesorRepository.eliminar(profesorId)`
8. **Finalización**: `EliminarProfesorView` → **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirProfesores.abrirProfesores()`

## patrón de eliminación segura para profesores

### confirmación obligatoria

Este análisis implementa eliminación con confirmación que:
- **Muestra información completa**: Todos los datos del profesor
- **Advierte sobre irreversibilidad**: Mensaje claro de advertencia
- **Requiere confirmación explícita**: No permite eliminación accidental
- **Verifica dependencias**: No hay cursos asignados activos

### responsabilidades de seguridad

**EliminarProfesorView** maneja confirmación:
- **Presenta datos**: Información completa del profesor
- **Muestra advertencias**: Mensajes de eliminación irreversible
- **Captura decisión**: Confirmación o cancelación explícita

**ProfesorController** valida eliminación:
- **Verifica existencia**: Profesor existe y es válido
- **Controla restricciones**: Verifica que puede ser eliminado
- **Valida dependencias**: No hay cursos asignados activos
- **Procesa eliminación**: Solo tras confirmación explícita

## patrones arquitectónicos aplicados

### patrón MVC para eliminación de profesores

- **Model**: `Profesor` + `ProfesorRepository` (datos del profesor y eliminación)
- **View**: `EliminarProfesorView` (confirmación e interacción)
- **Controller**: `ProfesorController` (coordinación y validación)

### patrón Repository con eliminación segura

- **Abstracción de eliminación**: `ProfesorRepository` encapsula lógica de borrado
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Flexibilidad**: Puede implementar eliminación física o lógica
- **Validaciones**: Verifica restricciones de integridad

### confirmación de dos pasos para profesores

- **Paso 1**: Presentar información completa del profesor
- **Paso 2**: Confirmar eliminación explícitamente
- **Cancelación**: Disponible en cualquier momento
- **Validación**: Verificar que no hay cursos asignados

## consideraciones de diseño específicas para profesores

### reutilización del controlador

El diseño permite que `ProfesorController` sea reutilizado:
- **Compartido**: Con crearProfesor() y editarProfesor()
- **Método específico**: eliminarProfesor() con validaciones propias
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para entidad profesor

### patrón include para navegación

- **Separación de responsabilidades**: eliminarProfesor() se enfoca en eliminar
- **Reutilización**: **&lt;&lt;include&gt;&gt;** abrirProfesores() evita duplicar funcionalidad de listado
- **Doble entrada**: Funciona desde `:Profesores Abierto` o `:Profesor Abierto`
- **Navegación consistente**: Regresa siempre a lista actualizada

### flexibilidad de eliminación

- **ProfesorRepository** puede implementar:
  - **Eliminación física**: Borrado real de la base de datos
  - **Eliminación lógica**: Marcado como eliminado/inactivo
  - **Archivo**: Mover a histórico de profesores
  - **Preservación**: Mantener para consultas históricas

### experiencia de usuario

- **Información clara**: Muestra datos completos del profesor
- **Advertencias específicas**: Destaca impacto en asignaciones
- **Navegación consistente**: Regresa al contexto de gestión de profesores

## validaciones de negocio

### restricciones de integridad

**ProfesorController** debe verificar:
- **Existencia del profesor**: Profesor válido y encontrado
- **Dependencias**: No hay cursos asignados activos
- **Relaciones**: Verificar impacto en asignaciones
- **Permisos administrativos**: Administrador autorizado para eliminar profesores

### manejo de errores

- **Profesor no encontrado**: Mensaje informativo
- **Restricciones**: Explicación de dependencias con cursos asignados
- **Error de sistema**: Manejo graceful de fallos de persistencia

## diferencias con otros casos CRUD de profesores

### eliminarProfesor() vs editarProfesor()

**eliminarProfesor():**
- **Objetivo**: Confirmación y eliminación
- **Interacción**: Solo lectura + confirmación
- **Validaciones**: Restricciones de integridad
- **Resultado**: Profesor removido del sistema

**editarProfesor():**
- **Objetivo**: Modificación de datos
- **Interacción**: Lectura + escritura múltiple
- **Validaciones**: Restricciones de contenido
- **Resultado**: Profesor actualizado en sistema

### complementariedad CRUD para profesores

- **crearProfesor()**: Añade nuevos profesores al sistema
- **editarProfesor()**: Modifica profesores existentes
- **eliminarProfesor()**: Remueve profesores del sistema
- **abrirProfesores()**: Lista y selecciona profesores

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/eliminarProfesor/README.md)
- [editarProfesor() - Caso complementario](../editarProfesor/README.md)
- [crearProfesor() - Caso complementario](../crearProfesor/README.md)
- [abrirProfesores() - Contexto de navegación](../abrirProfesores/README.md)
- [eliminarCurso() - Patrón de referencia](../eliminarCurso/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)