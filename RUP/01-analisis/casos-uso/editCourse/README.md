# pySigHor > editarCurso > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarCurso/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-19
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `editarCurso()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar edición completa de cursos académicos con capacidad de modificación continua.

## diagrama de colaboración

<div align=center>

|![Análisis: editarCurso()](/images/RUP/01-analisis/casos-uso/editarCurso/editarCurso-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### EditarCursoView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de edición de curso
- Interactuar con el controlador para obtener datos del curso
- Presentar datos completos de edición del curso
- Permitir solicitar modificación de campos específicos
- Mantener sesión de edición activa para modificaciones continuas
- Permitir solicitar guardar cambios o cancelar edición

**Colaboraciones**:
- **Entrada**: Recibe `editarCurso(cursoId)` desde `:Cursos Abierto`, `:Curso Abierto` o desde `:Collaboration CrearCurso`
- **Control**: Se comunica con `CursoController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirCursos` para mostrar lista actualizada o mantiene `:Curso Abierto`

### clases de control

#### CursoController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la carga de datos completos del curso a editar
- Validar que el curso existe y puede ser modificado
- Manejar la lógica de modificación de campos académicos
- Procesar guardado de cambios tras confirmación
- Coordinar sesión de edición continua
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `EditarCursoView`
- **Repositorio**: Delega operaciones de datos a `CursoRepository`

### clases de entidad (entity)

#### CursoRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de cursos académicos
- Proporcionar método para obtener curso completo por ID
- Implementar actualización de campos académicos del curso
- Verificar restricciones de integridad durante modificación
- Gestionar relaciones con programas académicos durante edición
- Mantener historial de cambios académicos

**Colaboraciones**:
- **Control**: Responde a `CursoController`
- **Entidad**: Gestiona instancias de `Curso`

#### Curso
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información completa del curso a editar
- Encapsular atributos: código, nombre, descripción, créditos, horas académicas
- Mantener relación con programa académico
- Validar cambios en datos académicos
- Mantener la integridad de los datos durante modificación continua
- Permitir modificación de campos específicos

**Colaboraciones**:
- **Repositorio**: Es gestionado por `CursoRepository`

## flujo de colaboración principal

### secuencia: editar curso

1. **Inicio**: `:Cursos Abierto` o `:CrearCurso` → `EditarCursoView.editarCurso(cursoId)`
2. **Carga**: `EditarCursoView` → `CursoController.cargarCursoParaEdición(cursoId)`
3. **Obtención**: `CursoController` → `CursoRepository.obtenerPorId(cursoId) : Curso`
4. **Presentación**: `EditarCursoView` presenta datos completos de edición del `Curso`
5. **Modificación**: Administrador modifica campos en `EditarCursoView`
6. **Actualización**: `EditarCursoView` → `CursoController.modificarCampos(cursoId, cambios)`
7. **Persistencia**: `CursoController` → `CursoRepository.actualizar(curso)`
8. **Opciones**: 
   - **Continuar editando**: Permanece en `EditarCursoView`
   - **Guardar y salir**: `EditarCursoView` → **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirCursos.abrirCursos()`
   - **Cancelar**: `EditarCursoView` → **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirCursos.abrirCursos()`

## patrón de edición completa para cursos

### filosofía "el gordo"

Este análisis implementa edición integral que:
- **Datos completos**: Todos los campos académicos del curso disponibles
- **Edición continua**: Permite múltiples modificaciones en sesión
- **Persistencia flexible**: Guarda cuando administrador solicita
- **Navegación flexible**: Puede continuar editando o salir

### responsabilidades de edición académica

**EditarCursoView** maneja edición completa:
- **Presenta datos completos**: Información académica integral del curso
- **Permite modificaciones**: Campos editables de forma interactiva
- **Mantiene sesión**: Edición continua sin perder cambios
- **Controla salida**: Guardar, continuar o cancelar

**CursoController** coordina modificaciones:
- **Valida cambios**: Verifica integridad de datos académicos
- **Controla restricciones**: Verifica que modificaciones son válidas
- **Procesa actualizaciones**: Actualiza curso según cambios
- **Facilita continuidad**: Mantiene sesión de edición activa

## patrones arquitectónicos aplicados

### patrón MVC para edición de cursos

- **Model**: `Curso` + `CursoRepository` (datos académicos completos y modificación)
- **View**: `EditarCursoView` (edición interactiva y presentación completa)
- **Controller**: `CursoController` (coordinación y validación académica integral)

### patrón Repository con modificación académica

- **Abstracción de edición**: `CursoRepository` encapsula lógica de actualización
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Flexibilidad**: Puede implementar diferentes estrategias de actualización
- **Validaciones académicas**: Verifica restricciones de integridad curricular completa

### edición continua para cursos

- **Sesión persistente**: Mantiene estado de edición activo
- **Modificaciones incrementales**: Permite cambios múltiples sin salir
- **Persistencia controlada**: Guarda cuando administrador decide
- **Navegación flexible**: Continuar editando o regresar a lista

## consideraciones de diseño específicas para cursos

### reutilización del controlador

El diseño permite que `CursoController` sea reutilizado:
- **Compartido**: Con crearCurso() y eliminarCurso()
- **Método específico**: editarCurso() con validaciones de modificación propias
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para modificación académica completa

### múltiples puntos de entrada

El diseño permite entrada desde múltiples contextos:
- **Desde lista**: `:Cursos Abierto` → edición directa
- **Desde creación**: `:CrearCurso` → edición automática (C→U)
- **Desde detalle**: `:Curso Abierto` → continuar edición

### patrón include para navegación

- **Separación de responsabilidades**: editarCurso() se enfoca en editar
- **Reutilización**: **&lt;&lt;include&gt;&gt;** abrirCursos() evita duplicar funcionalidad de listado
- **Navegación consistente**: Regresa a contexto apropiado
- **Flexibilidad**: Puede permanecer en edición o salir

### flexibilidad de modificación académica

- **CursoRepository** puede implementar:
  - **Actualización incremental**: Solo campos modificados
  - **Versionado académico**: Historial de cambios curriculares
  - **Validación curricular**: Verificación de coherencia académica
  - **Sincronización**: Actualización de relaciones con programas

### experiencia de usuario académica

- **Información completa**: Muestra todos los datos académicos del curso
- **Modificación flexible**: Permite editar cualquier campo disponible
- **Sesión continua**: No pierde trabajo durante modificaciones múltiples
- **Control total**: Usuario decide cuándo guardar y cuándo salir

## validaciones de negocio académicas

### restricciones de integridad curricular completa

**CursoController** debe verificar:
- **Existencia del curso**: Curso válido y encontrado
- **Unicidad de nombre**: No duplicar nombres con otros cursos
- **Coherencia académica**: Créditos consistentes con horas académicas
- **Relaciones curriculares**: Verificar impacto en programa académico
- **Permisos administrativos**: Administrador autorizado para modificar cursos

### manejo de errores académicos

- **Curso no encontrado**: Mensaje informativo
- **Datos inconsistentes**: Explicación de restricciones académicas violadas
- **Conflictos curriculares**: Explicación de impacto en programa académico
- **Error de sistema**: Manejo graceful de fallos de persistencia

## diferencias con otros casos CRUD de cursos

### editarCurso() vs crearCurso()

**editarCurso():**
- **Objetivo**: Modificación de datos académicos completos
- **Interacción**: Lectura + escritura múltiple de todos los campos
- **Validaciones**: Restricciones académicas de contenido completo
- **Resultado**: Curso actualizado con información académica completa

**crearCurso():**
- **Objetivo**: Creación básica con datos mínimos
- **Interacción**: Solicitud mínima + transferencia automática
- **Validaciones**: Restricciones básicas de creación
- **Resultado**: Curso básico creado + transferencia a edición

### editarCurso() vs eliminarCurso()

**editarCurso():**
- **Objetivo**: Modificación de información académica
- **Interacción**: Lectura + escritura continua
- **Validaciones**: Restricciones académicas de contenido
- **Resultado**: Curso actualizado en sistema

**eliminarCurso():**
- **Objetivo**: Confirmación y eliminación
- **Interacción**: Solo lectura + confirmación
- **Validaciones**: Restricciones de integridad curricular
- **Resultado**: Curso removido del sistema

### complementariedad CRUD para cursos

- **crearCurso()**: "El delgado" - añade curso básico al programa
- **editarCurso()**: "El gordo" - completa y modifica información académica completa
- **eliminarCurso()**: Remueve cursos del programa académico con confirmación
- **abrirCursos()**: Lista y selecciona cursos del programa para operaciones

## diagrama de secuencia

<div align=center>

|![Secuencia: editarCurso()](/images/RUP/01-analisis/casos-uso/editarCurso/editarCurso-analisis-secuencia.svg)|
|-|
|Código fuente: [secuencia.puml](secuencia.puml)|

</div>

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/editarCurso/README.md)
- [crearCurso() - Caso complementario](../crearCurso/README.md)
- [eliminarCurso() - Caso complementario](../eliminarCurso/README.md)
- [abrirCursos() - Contexto de navegación](../abrirCursos/README.md)
- [editarPrograma() - Patrón de referencia](../editarPrograma/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)