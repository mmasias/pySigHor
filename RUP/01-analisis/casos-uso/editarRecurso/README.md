# pySigHor > editarRecurso > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarRecurso/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-24
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `editarRecurso()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar edición completa de recursos.

## diagrama de colaboración

<div align=center>

|![Análisis: editarRecurso()](/images/RUP/01-analisis/casos-uso/editarRecurso/editarRecurso-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### EditarRecursoView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de edición de recurso existente
- Presentar datos de edición con todos los campos del recurso
- Permitir modificación de campos del recurso
- Gestionar guardado de cambios y continuación de edición
- Manejar navegación de vuelta a la lista de recursos

**Colaboraciones**:
- **Entrada**: Recibe `editarRecurso()` desde `:Recursos Abierto` o desde `crearRecurso()`
- **Control**: Se comunica con `RecursoController`
- **Salida**: **\<\<include>>** `:Collaboration AbrirRecursos` al guardar y salir

### clases de control

#### RecursoController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar el proceso de edición completa de recurso
- Cargar datos existentes del recurso para edición
- Validar modificaciones proporcionadas por el administrador
- Procesar guardado de cambios en el recurso
- Gestionar sesión continua de edición
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `EditarRecursoView`
- **Repositorio**: Delega operaciones de datos a `RecursoRepository`

### clases de entidad (entity)

#### RecursoRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de recursos existentes
- Implementar carga de recurso por ID para edición
- Implementar actualización de recurso con datos completos
- Validar integridad de datos durante modificaciones
- Gestionar persistencia de cambios del recurso

**Colaboraciones**:
- **Control**: Responde a `RecursoController`
- **Entidad**: Gestiona instancias de `Recurso`

#### Recurso
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información completa del recurso a editar
- Encapsular todos los atributos: código, nombre, descripción del recurso
- Validar datos completos proporcionados durante edición
- Mantener integridad de datos durante modificaciones
- Aplicar reglas de negocio para edición completa

**Colaboraciones**:
- **Repositorio**: Es gestionado por `RecursoRepository`

## patrón de edición completa para recursos - "el gordo"

### edición con funcionalidad completa

Este análisis implementa edición completa que:
- **Presenta todos los campos**: Información completa del recurso para modificación
- **Permite edición continua**: Sesión de edición que puede mantenerse activa
- **Valida integridad**: Verificaciones completas de negocio durante guardado
- **Gestiona persistencia**: Guardado confiable de todos los cambios

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/editarRecurso/README.md)
- [crearRecurso() - Caso de transferencia](../crearRecurso/README.md)
- [eliminarRecurso() - Caso complementario](../eliminarRecurso/README.md)
- [abrirRecursos() - Contexto de navegación](../abrirRecursos/README.md)
- [editarEdificio() - Patrón de referencia](../editarEdificio/README.md)
- [editarAula() - Patrón de referencia](../editarAula/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)