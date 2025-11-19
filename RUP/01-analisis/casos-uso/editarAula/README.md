# pySigHor > editarAula > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/editarAula/README.md)|**Análisis**|[Diseño](/RUP/02-diseño/casos-uso/editarAula/README.md)|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-24
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `editarAula()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar edición completa de aulas.

## diagrama de colaboración

<div align=center>

|![Análisis: editarAula()](/images/RUP/01-analisis/casos-uso/editarAula/editarAula-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### EditarAulaView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de edición de aula existente
- Presentar datos de edición con todos los campos del aula
- Permitir modificación de campos del aula
- Gestionar guardado de cambios y continuación de edición
- Manejar navegación de vuelta a la lista de aulas

**Colaboraciones**:
- **Entrada**: Recibe `editarAula()` desde `:Aulas Abierto` o desde `crearAula()`
- **Control**: Se comunica con `AulaController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirAulas` al guardar y salir

### clases de control

#### AulaController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar el proceso de edición completa de aula
- Cargar datos existentes del aula para edición
- Validar modificaciones proporcionadas por el administrador
- Procesar guardado de cambios en el aula
- Gestionar sesión continua de edición
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `EditarAulaView`
- **Repositorio**: Delega operaciones de datos a `AulaRepository`

### clases de entidad (entity)

#### AulaRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de aulas existentes
- Implementar carga de aula por ID para edición
- Implementar actualización de aula con datos completos
- Validar integridad de datos durante modificaciones
- Gestionar persistencia de cambios del aula

**Colaboraciones**:
- **Control**: Responde a `AulaController`
- **Entidad**: Gestiona instancias de `Aula`

#### Aula
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información completa del aula a editar
- Encapsular todos los atributos: código, nombre, edificio, capacidad, tipo, recursos, observaciones
- Validar datos completos proporcionados durante edición
- Mantener integridad de datos durante modificaciones
- Aplicar reglas de negocio para edición completa

**Colaboraciones**:
- **Repositorio**: Es gestionado por `AulaRepository`

## patrón de edición completa para aulas - "el gordo"

### edición con funcionalidad completa

Este análisis implementa edición completa que:
- **Presenta todos los campos**: Información completa del aula para modificación
- **Permite edición continua**: Sesión de edición que puede mantenerse activa
- **Valida integridad**: Verificaciones completas de negocio durante guardado
- **Gestiona persistencia**: Guardado confiable de todos los cambios

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/editarAula/README.md)
- [crearAula() - Caso de transferencia](../crearAula/README.md)
- [eliminarAula() - Caso complementario](../eliminarAula/README.md)
- [abrirAulas() - Contexto de navegación](../abrirAulas/README.md)
- [editarEdificio() - Patrón de referencia](../editarEdificio/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)