# pySigHor > deleteCourse > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/deleteCourse/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-19
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `deleteCourse()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar eliminación segura de cursos con confirmación.

## diagrama de colaboración

<div align=center>

|![Análisis: deleteCourse()](/images/RUP/01-analisis/casos-uso/deleteCourse/deleteCourse-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### deleteCourseView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de eliminación de curso
- Interactuar con el controlador para obtener información del curso
- Presentar información completa del curso a eliminar
- Presentar advertencia de eliminación irreversible
- Permitir solicitar confirmación o cancelación del administrador

**Colaboraciones**:
- **Entrada**: Recibe `deleteCourse(cursoId)` desde `:Cursos Abierto` o `:Curso Abierto`
- **Control**: Se comunica con `CursoController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirCursos` para mostrar lista actualizada

### clases de control

#### CursoController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la carga de datos del curso a eliminar
- Validar que el curso existe y puede ser eliminado
- Verificar restricciones de integridad (no hay matrículas activas)
- Manejar la lógica de eliminación tras confirmación
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `deleteCourseView`
- **Repositorio**: Delega operaciones de datos a `CursoRepository`

### clases de entidad (entity)

#### CursoRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de cursos académicos
- Proporcionar método para obtener curso por ID
- Implementar eliminación física o lógica del curso
- Verificar restricciones de integridad antes de eliminar
- Gestionar relaciones con programas académicos

**Colaboraciones**:
- **Control**: Responde a `CursoController`
- **Entidad**: Gestiona instancias de `Curso`

#### Curso
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información del curso a eliminar
- Encapsular atributos: código, nombre, descripción, créditos, horas
- Mantener relación con programa académico
- Validar si el curso puede ser eliminado
- Mantener la integridad de los datos durante eliminación

**Colaboraciones**:
- **Repositorio**: Es gestionado por `CursoRepository`

## flujo de colaboración principal

### secuencia: eliminar curso

1. **Inicio**: `:Cursos Abierto` → `deleteCourseView.deleteCourse(cursoId)`
2. **Carga**: `deleteCourseView` → `CursoController.cargarCursoParaEliminacion(cursoId)`
3. **Obtención**: `CursoController` → `CursoRepository.obtenerPorId(cursoId) : Curso`
4. **Presentación**: `deleteCourseView` presenta información del `Curso` con advertencia
5. **Confirmación**: Administrador confirma o cancela en `deleteCourseView`
6. **Eliminación**: `deleteCourseView` → `CursoController.deleteCourse(cursoId)`
7. **Persistencia**: `CursoController` → `CursoRepository.eliminar(cursoId)`
8. **Finalización**: `deleteCourseView` → **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirCursos.abrirCursos()`

## patrón de eliminación segura para cursos

### confirmación obligatoria

Este análisis implementa eliminación con confirmación que:
- **Muestra información completa**: Todos los datos del curso académico
- **Advierte sobre irreversibilidad**: Mensaje claro de advertencia
- **Requiere confirmación explícita**: No permite eliminación accidental
- **Verifica dependencias**: No hay estudiantes matriculados

### responsabilidades de seguridad

**deleteCourseView** maneja confirmación:
- **Presenta datos**: Información académica completa del curso
- **Muestra advertencias**: Mensajes de eliminación irreversible
- **Captura decisión**: Confirmación o cancelación explícita

**CursoController** valida eliminación:
- **Verifica existencia**: Curso existe y es válido
- **Controla restricciones**: Verifica que puede ser eliminado
- **Valida dependencias**: No hay matrículas activas
- **Procesa eliminación**: Solo tras confirmación explícita

## patrones arquitectónicos aplicados

### patrón MVC para eliminación de cursos

- **Model**: `Curso` + `CursoRepository` (datos académicos y eliminación)
- **View**: `deleteCourseView` (confirmación e interacción)
- **Controller**: `CursoController` (coordinación y validación académica)

### patrón Repository con eliminación académica

- **Abstracción de eliminación**: `CursoRepository` encapsula lógica de borrado
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Flexibilidad**: Puede implementar eliminación física o lógica
- **Validaciones académicas**: Verifica restricciones de integridad curricular

### confirmación de dos pasos para cursos

- **Paso 1**: Presentar información académica completa
- **Paso 2**: Confirmar eliminación explícitamente
- **Cancelación**: Disponible en cualquier momento
- **Validación**: Verificar que no hay matrículas activas

## consideraciones de diseño específicas para cursos

### reutilización del controlador

El diseño permite que `CursoController` sea reutilizado:
- **Compartido**: Con crearCurso() y editarCurso()
- **Método específico**: deleteCourse() con validaciones académicas propias
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para entidad académica

### patrón include para navegación

- **Separación de responsabilidades**: deleteCourse() se enfoca en eliminar
- **Reutilización**: **&lt;&lt;include&gt;&gt;** abrirCursos() evita duplicar funcionalidad de listado
- **Doble entrada**: Funciona desde `:Cursos Abierto` o `:Curso Abierto`
- **Navegación consistente**: Regresa siempre a lista actualizada

### flexibilidad de eliminación académica

- **CursoRepository** puede implementar:
  - **Eliminación física**: Borrado real de la base de datos
  - **Eliminación lógica**: Marcado como eliminado/inactivo
  - **Archivo académico**: Mover a histórico de cursos
  - **Preservación curricular**: Mantener para consultas históricas

### experiencia de usuario académica

- **Información clara**: Muestra datos académicos completos del curso
- **Advertencias específicas**: Destaca impacto en programa académico
- **Navegación consistente**: Regresa al contexto de gestión de cursos

## validaciones de negocio académicas

### restricciones de integridad curricular

**CursoController** debe verificar:
- **Existencia del curso**: Curso válido y encontrado
- **Dependencias curriculares**: No hay estudiantes matriculados
- **Relaciones académicas**: Verificar impacto en programa académico
- **Permisos administrativos**: Administrador autorizado para eliminar cursos

### manejo de errores académicos

- **Curso no encontrado**: Mensaje informativo
- **Restricciones curriculares**: Explicación de dependencias con matrículas
- **Error de sistema**: Manejo graceful de fallos de persistencia

## diferencias con otros casos CRUD de cursos

### deleteCourse() vs editarCurso()

**deleteCourse():**
- **Objetivo**: Confirmación y eliminación
- **Interacción**: Solo lectura + confirmación
- **Validaciones**: Restricciones de integridad curricular
- **Resultado**: Curso removido del sistema

**editarCurso():**
- **Objetivo**: Modificación de datos académicos
- **Interacción**: Lectura + escritura múltiple
- **Validaciones**: Restricciones académicas de contenido
- **Resultado**: Curso actualizado en sistema

### complementariedad CRUD para cursos

- **crearCurso()**: Añade nuevos cursos al programa
- **editarCurso()**: Modifica cursos existentes del programa
- **deleteCourse()**: Remueve cursos del programa académico
- **abrirCursos()**: Lista y selecciona cursos del programa

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/deleteCourse/README.md)
- [editarCurso() - Caso complementario](../editarCurso/README.md)
- [crearCurso() - Caso complementario](../crearCurso/README.md)
- [abrirCursos() - Contexto de navegación](../abrirCursos/README.md)
- [eliminarPrograma() - Patrón de referencia](../eliminarPrograma/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)