# pySigHor > createProgram > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/createProgram/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-17
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `createProgram()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar la filosofía C→U como "el delgado".

## diagrama de colaboración

<div align=center>

|![Análisis: createProgram()](/images/RUP/01-analisis/casos-uso/createProgram/createProgram-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### CrearProgramaView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de creación de programa nuevo
- Presentar diálogo simple para datos mínimos
- Capturar nombre del programa del administrador
- Manejar creación y transferencia automática a edición

**Colaboraciones**:
- **Entrada**: Recibe `createProgram()` desde `:Programas Abierto`
- **Control**: Se comunica con `ProgramaController`
- **Salida**: Transfiere control a `:Collaboration EditarPrograma`

### clases de control

#### ProgramaController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la creación de programa con datos mínimos
- Generar código automático del programa
- Validar nombre único del programa
- Transferir control a editProgram()

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `CrearProgramaView`
- **Repositorio**: Delega creación a `ProgramaRepository`

### clases de entidad (entity)

#### ProgramaRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer la creación de nuevos programas
- Generar código único para el programa
- Verificar unicidad del nombre
- Persistir programa con datos mínimos

**Colaboraciones**:
- **Control**: Responde a `ProgramaController`
- **Entidad**: Crea nuevas instancias de `Programa`

#### Programa
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar programa académico recién creado
- Encapsular datos mínimos: código (auto), nombre, estado (activo)
- Validar información básica
- Prepararse para edición completa

**Colaboraciones**:
- **Repositorio**: Es creado por `ProgramaRepository`

## flujo de colaboración principal

### secuencia: crear programa (delgado)

1. **Inicio**: `:Programas Abierto` → `CrearProgramaView.createProgram()`
2. **Solicitud**: `CrearProgramaView` presenta diálogo de datos mínimos
3. **Captura**: Administrador proporciona nombre en `CrearProgramaView`
4. **Creación**: `CrearProgramaView` → `ProgramaController.crearProgramaMinimo(nombre)`
5. **Generación**: `ProgramaController` → `ProgramaRepository.crear(nombre) : Programa`
6. **Persistencia**: `ProgramaRepository` crea nueva instancia de `Programa`
7. **Transferencia**: `CrearProgramaView` → `:Collaboration EditarPrograma.editarPrograma(programaNuevo)`

## aplicación de filosofía C→U

### rol de "el delgado"

Este análisis implementa `createProgram()` como "el delgado" que:
- **Minimiza complejidad**: Solo captura datos esenciales
- **Transfiere inmediatamente**: Pasa control a editProgram()
- **Reutiliza funcionalidad**: No duplica lógica de edición

### responsabilidades minimalistas

**CrearProgramaView** es deliberadamente simple:
- **No incluye**: Formulario completo de edición
- **Solo maneja**: Nombre del programa y creación
- **Transfiere**: Inmediatamente a EditarProgramaView

**ProgramaController** maneja creación básica:
- **Crear entidad**: Con datos mínimos únicamente
- **Generar automáticos**: Código y estado por defecto
- **Validar esencial**: Solo unicidad del nombre

## patrones arquitectónicos aplicados

### patrón MVC simplificado

- **Model**: `Programa` + `ProgramaRepository` (creación mínima)
- **View**: `CrearProgramaView` (diálogo simple)
- **Controller**: `ProgramaController` (coordinación básica)

### patrón Factory implícito

- **ProgramaRepository** actúa como factory para crear programas con:
  - Código auto-generado
  - Nombre proporcionado
  - Estado activo por defecto

### transferencia de control

- **Patrón C→U**: CrearProgramaView transfiere a EditarProgramaView
- **Estado compartido**: Programa recién creado pasa como parámetro
- **Experiencia fluida**: Usuario no regresa a lista intermedia

## diferencias con editProgram()

### simplicidad vs complejidad

**createProgram() - "El delgado":**
- **Vista**: Diálogo simple con un campo
- **Controlador**: Lógica mínima de creación
- **Flujo**: Rápido y directo hacia edición

**editProgram() - "El gordo":**
- **Vista**: Formulario completo multi-campo
- **Controlador**: Lógica completa de modificación
- **Flujo**: Edición completa con múltiples opciones

### colaboraciones complementarias

- **createProgram()**: Produce input para editProgram()
- **editProgram()**: Consume y completa lo iniciado por createProgram()
- **Reutilización**: Un solo formulario complejo vs múltiples simples

## consideraciones de diseño

### reutilización arquitectónica

El diseño permite que ambos casos de uso compartan:
- **ProgramaRepository**: Mismo repositorio para crear y editar
- **Programa**: Misma entidad en diferentes estados de completitud
- **Navegación**: Flujo natural de creación → edición

### escalabilidad

- **Fácil extensión**: Agregar campos mínimos sin afectar edición
- **Mantenimiento**: Cambios en creación no afectan edición completa
- **Testing**: Casos de uso independientes para pruebas

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/crearPrograma/README.md)
- [editProgram() - "El gordo"](../editarPrograma/README.md)
- [Filosofía C→U](../../../../extraDocs/008-filosofia-crud-creacion-edicion/README.md)
- [Análisis abrirProfesores](../abrirProfesores/README.md) - Patrón de referencia