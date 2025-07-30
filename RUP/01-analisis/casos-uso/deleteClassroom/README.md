# pySigHor > eliminarAula > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/eliminarAula/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-24
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `eliminarAula()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar eliminación segura de aulas con confirmación previa.

## diagrama de colaboración

<div align=center>

|![Análisis: eliminarAula()](/images/RUP/01-analisis/casos-uso/eliminarAula/eliminarAula-analisis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### EliminarAulaView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de eliminación de aula existente
- Presentar información completa del aula a eliminar
- Mostrar advertencia sobre eliminación irreversible
- Permitir confirmación o cancelación de eliminación
- Gestionar navegación de vuelta a la lista de aulas

**Colaboraciones**:
- **Entrada**: Recibe `eliminarAula()` desde `:Aulas Abierto`
- **Control**: Se comunica con `AulaController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration AbrirAulas` tras eliminación o cancelación

### clases de control

#### AulaController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar el proceso de eliminación segura de aula
- Cargar datos completos del aula para confirmación
- Validar que el aula puede ser eliminada
- Procesar eliminación tras confirmación del administrador
- Gestionar reglas de negocio para eliminación
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `EliminarAulaView`
- **Repositorio**: Delega operaciones de datos a `AulaRepository`

### clases de entidad (entity)

#### AulaRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de aulas para eliminación
- Implementar carga de aula por ID para confirmación
- Verificar dependencias antes de eliminación
- Implementar eliminación segura del aula
- Gestionar integridad referencial durante eliminación

**Colaboraciones**:
- **Control**: Responde a `AulaController`
- **Entidad**: Gestiona instancias de `Aula`

#### Aula
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información completa del aula a eliminar
- Encapsular todos los atributos para mostrar en confirmación
- Mantener información sobre dependencias
- Validar que puede ser eliminada según reglas de negocio
- Proporcionar información para advertencias de eliminación

**Colaboraciones**:
- **Repositorio**: Es gestionado por `AulaRepository`

## patrón de eliminación segura para aulas

### eliminación con confirmación previa

Este análisis implementa eliminación segura que:
- **Presenta información completa**: Todos los datos del aula a eliminar
- **Muestra dependencias**: Información sobre uso del aula
- **Requiere confirmación**: Paso obligatorio de confirmación del administrador
- **Valida eliminación**: Verificaciones de integridad antes de proceder

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/eliminarAula/README.md)
- [crearAula() - Caso complementario](../crearAula/README.md)
- [editarAula() - Caso complementario](../editarAula/README.md)
- [abrirAulas() - Contexto de navegación](../abrirAulas/README.md)
- [eliminarEdificio() - Patrón de referencia](../eliminarEdificio/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)