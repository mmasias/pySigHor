# pySigHor > editProgram > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editProgram/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-17
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `editProgram()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para cumplir con los requisitos especificados aplicando la filosofía C→U.

## diagrama de colaboración

<div align=center>

|![Análisis: editProgram()](/images/RUP/01-analisis/casos-uso/editProgram/editProgram-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### editProgramView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de edición de programa
- Interactuar con el controlador para obtener datos del programa
- Presentar el formulario de edición al administrador
- Capturar modificaciones de campos del administrador
- Manejar las acciones de guardar y cancelar

**Colaboraciones**:
- **Entrada**: Recibe `editProgram(programaId)` desde `:Programas Abierto`
- **Control**: Se comunica con `ProgramaController`
- **Salida**: Retorna control a `:Programas Abierto`

### clases de control

#### ProgramaController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la carga de datos del programa específico
- Manejar la lógica de modificación de campos
- Validar información antes del guardado
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `editProgramView`
- **Repositorio**: Delega operaciones de datos a `ProgramaRepository`

### clases de entidad (entity)

#### ProgramaRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de programas académicos
- Proporcionar método para obtener programa por ID
- Implementar guardado de modificaciones del programa
- Mantener la consistencia de los datos de programas

**Colaboraciones**:
- **Control**: Responde a `ProgramaController`
- **Entidad**: Gestiona instancias de `Programa`

#### Programa
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información de un programa académico
- Encapsular atributos: código, nombre, descripción
- Mantener la integridad de los datos del programa
- Validar modificaciones de campos

**Colaboraciones**:
- **Repositorio**: Es gestionado por `ProgramaRepository`

## flujo de colaboración principal

### secuencia: editar programa

1. **Inicio**: `:Programas Abierto` → `editProgramView.editProgram(programaId)`
2. **Carga**: `editProgramView` → `ProgramaController.cargarPrograma(programaId)`
3. **Obtención**: `ProgramaController` → `ProgramaRepository.obtenerPorId(programaId) : Programa`
4. **Presentación**: `editProgramView` presenta formulario con datos del `Programa`
5. **Modificación**: Administrador modifica campos en `editProgramView`
6. **Guardado**: `editProgramView` → `ProgramaController.guardarPrograma(programa)`
7. **Persistencia**: `ProgramaController` → `ProgramaRepository.actualizar(programa)`
8. **Finalización**: `editProgramView` → `:Programas Abierto.abrirProgramas()`

## aplicación de filosofía C→U

### convergencia de flujos

Este análisis contempla que `editProgram()` es "el gordo" que recibe:
- **Programas existentes**: Desde `abrirProgramas()` con ID válido
- **Programas nuevos**: Desde `crearPrograma()` con programa recién creado

### responsabilidades unificadas

**ProgramaController** maneja ambos casos:
- **Carga existente**: `cargarPrograma(programaId)` obtiene datos persistidos
- **Carga nuevo**: `cargarPrograma(programaId)` obtiene programa con datos mínimos

**editProgramView** presenta el mismo formulario:
- **Datos existentes**: Campos poblados con información actual
- **Datos nuevos**: Campos poblados con información mínima inicial

## patrones arquitectónicos aplicados

### patrón MVC

- **Model**: `Programa` + `ProgramaRepository` (estado y persistencia)
- **View**: `editProgramView` (presentación e interacción)
- **Controller**: `ProgramaController` (lógica de coordinación)

### patrón Repository

- **Abstracción de datos**: `ProgramaRepository` encapsula acceso a persistencia
- **Separación de responsabilidades**: Controlador no conoce detalles de almacenamiento
- **Testabilidad**: Repositorio puede ser mockeado para pruebas

### separación de responsabilidades

- **Vista**: Solo presenta y captura, no procesa lógica de negocio
- **Control**: Solo coordina, no maneja datos directamente
- **Entidad**: Solo representa datos y reglas de dominio

## consideraciones de diseño

### reutilización

El diseño permite que `editProgramView` sea reutilizada por:
- `editProgram()` → formulario con datos existentes
- `crearPrograma()` → mismo formulario con datos mínimos

### flexibilidad

- **ProgramaController** puede manejar validaciones específicas
- **ProgramaRepository** puede cambiar implementación de persistencia
- **editProgramView** puede adaptarse a diferentes contextos de entrada

### mantenibilidad

- Cada clase tiene responsabilidad única y clara
- Colaboraciones están bien definidas y desacopladas
- Cambios en una capa no afectan a las otras

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/editProgram/README.md)
- [Filosofía C→U](../../../../extraDocs/008-filosofia-crud-creacion-edicion/README.md)
- [Análisis abrirProfesores](../abrirProfesores/README.md) - Patrón de referencia
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)