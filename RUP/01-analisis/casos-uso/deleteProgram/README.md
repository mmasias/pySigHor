# pySigHor > deleteProgram > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/deleteProgram/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-18
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `deleteProgram()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar eliminación segura con confirmación.

## diagrama de colaboración

<div align=center>

|![Análisis: deleteProgram()](/images/RUP/01-analisis/casos-uso/deleteProgram/deleteProgram-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### deleteProgramView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de eliminación de programa
- Interactuar con el controlador para obtener información del programa
- Presentar información completa del programa a eliminar
- Presentar advertencia de eliminación irreversible
- Permitir solicitar confirmación o cancelación del administrador

**Colaboraciones**:
- **Entrada**: Recibe `deleteProgram(programaId)` desde `:Programas Abierto` o `:Programa Abierto`
- **Control**: Se comunica con `ProgramaController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirProgramas` para mostrar lista actualizada

### clases de control

#### ProgramaController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la carga de datos del programa a eliminar
- Validar que el programa existe y puede ser eliminado
- Manejar la lógica de eliminación tras confirmación
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `deleteProgramView`
- **Repositorio**: Delega operaciones de datos a `ProgramaRepository`

### clases de entidad (entity)

#### ProgramaRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de programas académicos
- Proporcionar método para obtener programa por ID
- Implementar eliminación física o lógica del programa
- Verificar restricciones de integridad antes de eliminar

**Colaboraciones**:
- **Control**: Responde a `ProgramaController`
- **Entidad**: Gestiona instancias de `Programa`

#### Programa
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información del programa a eliminar
- Encapsular atributos: código, nombre, descripción
- Validar si el programa puede ser eliminado
- Mantener la integridad de los datos durante eliminación

**Colaboraciones**:
- **Repositorio**: Es gestionado por `ProgramaRepository`

## flujo de colaboración principal

### secuencia: eliminar programa

1. **Inicio**: `:Programas Abierto` → `deleteProgramView.deleteProgram(programaId)`
2. **Carga**: `deleteProgramView` → `ProgramaController.cargarProgramaParaEliminacion(programaId)`
3. **Obtención**: `ProgramaController` → `ProgramaRepository.obtenerPorId(programaId) : Programa`
4. **Presentación**: `deleteProgramView` presenta información del `Programa` con advertencia
5. **Confirmación**: Administrador confirma o cancela en `deleteProgramView`
6. **Eliminación**: `deleteProgramView` → `ProgramaController.deleteProgram(programaId)`
7. **Persistencia**: `ProgramaController` → `ProgramaRepository.eliminar(programaId)`
8. **Finalización**: `deleteProgramView` → **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirProgramas.abrirProgramas()`

## patrón de eliminación segura

### confirmación obligatoria

Este análisis implementa eliminación con confirmación que:
- **Muestra información completa**: Todos los datos del programa
- **Advierte sobre irreversibilidad**: Mensaje claro de advertencia
- **Requiere confirmación explícita**: No permite eliminación accidental

### responsabilidades de seguridad

**deleteProgramView** maneja confirmación:
- **Presenta datos**: Información completa del programa
- **Muestra advertencias**: Mensajes de eliminación irreversible
- **Captura decisión**: Confirmación o cancelación explícita

**ProgramaController** valida eliminación:
- **Verifica existencia**: Programa existe y es válido
- **Controla restricciones**: Verifica que puede ser eliminado
- **Procesa eliminación**: Solo tras confirmación explícita

## patrones arquitectónicos aplicados

### patrón MVC para eliminación

- **Model**: `Programa` + `ProgramaRepository` (datos y eliminación)
- **View**: `deleteProgramView` (confirmación e interacción)
- **Controller**: `ProgramaController` (coordinación y validación)

### patrón Repository con eliminación

- **Abstracción de eliminación**: `ProgramaRepository` encapsula lógica de borrado
- **Separación de responsabilidades**: Controlador no conoce detalles de eliminación
- **Flexibilidad**: Puede implementar eliminación física o lógica

### confirmación de dos pasos

- **Paso 1**: Presentar información completa
- **Paso 2**: Confirmar eliminación explícitamente
- **Cancelación**: Disponible en cualquier momento

## consideraciones de diseño

### reutilización del controlador

El diseño permite que `ProgramaController` sea reutilizado:
- **Compartido**: Con crearPrograma() y editarPrograma()
- **Método específico**: deleteProgram() con validaciones propias
- **Consistencia**: Mismo patrón de comunicación con repositorio

### patrón include para navegación

- **Separación de responsabilidades**: deleteProgram() se enfoca en eliminar
- **Reutilización**: **&lt;&lt;include&gt;&gt;** abrirProgramas() evita duplicar funcionalidad de listado
- **Doble entrada**: Funciona desde `:Programas Abierto` o `:Programa Abierto`

### flexibilidad de eliminación

- **ProgramaRepository** puede implementar:
  - **Eliminación física**: Borrado real de la base de datos
  - **Eliminación lógica**: Marcado como eliminado/inactivo
  - **Archivo**: Mover a tabla de históricos

### experiencia de usuario

- **Información clara**: Muestra exactamente qué se eliminará
- **Advertencias visibles**: Destaca la irreversibilidad
- **Navegación consistente**: Regresa al contexto de origen

## validaciones de negocio

### restricciones de integridad

**ProgramaController** debe verificar:
- **Existencia del programa**: Programa válido y encontrado
- **Dependencias**: No hay cursos asociados al programa
- **Permisos**: Administrador autorizado para eliminar

### manejo de errores

- **Programa no encontrado**: Mensaje informativo
- **Restricciones de integridad**: Explicación de dependencias
- **Error de sistema**: Manejo graceful de fallos

## diferencias con otros casos CRUD

### deleteProgram() vs editarPrograma()

**deleteProgram():**
- **Objetivo**: Confirmación y eliminación
- **Interacción**: Solo lectura + confirmación
- **Resultado**: Programa removido del sistema

**editarPrograma():**
- **Objetivo**: Modificación de datos
- **Interacción**: Lectura + escritura múltiple
- **Resultado**: Programa actualizado en sistema

### complementariedad CRUD

- **crearPrograma()**: Añade nuevos programas
- **editarPrograma()**: Modifica programas existentes  
- **deleteProgram()**: Remueve programas del sistema
- **abrirProgramas()**: Lista y selecciona programas

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/deleteProgram/README.md)
- [editarPrograma() - Caso complementario](../editarPrograma/README.md)
- [crearPrograma() - Caso complementario](../crearPrograma/README.md)
- [abrirProgramas() - Contexto de navegación](../abrirProgramas/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)