# pySigHor > createCourse > Análisis

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/createCourse/README.md)|**Análisis**|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-07-19
- **Autor**: Equipo de desarrollo

## propósito

Análisis de colaboración del caso de uso `createCourse()` mediante el patrón MVC, identificando las clases de análisis, sus responsabilidades y colaboraciones necesarias para implementar creación rápida de cursos académicos con filosofía C→U.

## diagrama de colaboración

<div align=center>

|![Análisis: createCourse()](/images/RUP/01-analisis/casos-uso/createCourse/createCourse-analysis.svg)|
|-|
|Código fuente: [colaboracion.puml](colaboracion.puml)|

</div>

## clases de análisis identificadas

### clases de vista (boundary)

#### CrearCursoView
**Estereotipo**: Vista (Boundary)  
**Responsabilidades**:
- Recibir la solicitud de creación de curso nuevo
- Presentar solicitud de datos mínimos del curso
- Permitir solicitar crear curso o cancelar creación
- Transferir inmediatamente a edición completa tras creación

**Colaboraciones**:
- **Entrada**: Recibe `crearCurso()` desde `:Cursos Abierto`
- **Control**: Se comunica con `CursoController`
- **Salida**: **&lt;&lt;include&gt;&gt;** `:Collaboration EditarCurso` para completar datos

### clases de control

#### CursoController
**Estereotipo**: Control  
**Responsabilidades**:
- Coordinar la creación de curso con datos mínimos
- Validar nombre del curso (obligatorio)
- Verificar que no existe curso duplicado
- Manejar la lógica de creación básica
- Servir como intermediario entre la vista y el repositorio

**Colaboraciones**:
- **Vista**: Responde a solicitudes de `CrearCursoView`
- **Repositorio**: Delega operaciones de datos a `CursoRepository`

### clases de entidad (entity)

#### CursoRepository
**Estereotipo**: Entidad  
**Responsabilidades**:
- Abstraer el acceso a datos de cursos académicos
- Implementar creación de curso con datos mínimos
- Verificar unicidad del nombre del curso
- Generar ID único para el nuevo curso
- Gestionar relaciones iniciales con programas académicos

**Colaboraciones**:
- **Control**: Responde a `CursoController`
- **Entidad**: Gestiona instancias de `Curso`

#### Curso
**Estereotipo**: Entidad  
**Responsabilidades**:
- Representar la información mínima del curso a crear
- Encapsular atributos: nombre (obligatorio), otros campos opcionales
- Validar datos mínimos requeridos
- Mantener la integridad de los datos durante creación
- Permitir completar información en edición posterior

**Colaboraciones**:
- **Repositorio**: Es gestionado por `CursoRepository`

## flujo de colaboración principal

### secuencia: crear curso

1. **Inicio**: `:Cursos Abierto` → `CrearCursoView.crearCurso()`
2. **Presentación**: `CrearCursoView` presenta solicitud de datos mínimos del curso
3. **Datos**: Administrador proporciona nombre del curso (obligatorio)
4. **Validación**: `CrearCursoView` → `CursoController.validarDatosMínimos(nombre)`
5. **Creación**: `CursoController` → `CursoRepository.crear(nombre) : Curso`
6. **Persistencia**: `CursoRepository` crea `Curso` con datos mínimos
7. **Transferencia**: `CrearCursoView` → **&lt;&lt;include&gt;&gt;** `:Collaboration EditarCurso.editarCurso(cursoNuevo)`

## patrón de creación rápida para cursos

### filosofía C→U (Crear→Editar)

Este análisis implementa creación minimalista que:
- **Datos mínimos**: Solo nombre del curso (obligatorio)
- **Creación básica**: Curso válido con información esencial
- **Transferencia inmediata**: Pasa automáticamente a edición completa
- **Eficiencia**: "El delgado" permite crear rápido, "el gordo" completa

### responsabilidades de creación mínima

**CrearCursoView** maneja creación rápida:
- **Presenta solicitud**: Datos mínimos obligatorios únicamente
- **Valida entrada**: Nombre del curso no vacío
- **Transfiere control**: Pasa inmediatamente a edición completa

**CursoController** coordina creación:
- **Valida mínimos**: Verifica que nombre no esté vacío
- **Controla unicidad**: Verifica que no existe curso duplicado
- **Procesa creación**: Crea curso básico válido
- **Facilita transferencia**: Prepara curso para edición completa

## patrones arquitectónicos aplicados

### patrón MVC para creación de cursos

- **Model**: `Curso` + `CursoRepository` (datos académicos mínimos y creación)
- **View**: `CrearCursoView` (solicitud de datos mínimos e interacción)
- **Controller**: `CursoController` (coordinación y validación académica básica)

### patrón Repository con creación académica

- **Abstracción de creación**: `CursoRepository` encapsula lógica de creación
- **Separación de responsabilidades**: Controlador no conoce detalles de persistencia
- **Flexibilidad**: Puede implementar diferentes estrategias de creación
- **Validaciones académicas**: Verifica unicidad y restricciones básicas

### transferencia automática C→U para cursos

- **Creación mínima**: Solo datos esenciales para curso válido
- **Transferencia inmediata**: **&lt;&lt;include&gt;&gt;** editarCurso() automático
- **Completar en edición**: "El gordo" maneja información académica completa
- **Eficiencia de flujo**: Minimiza pasos para crear curso completo

## consideraciones de diseño específicas para cursos

### reutilización del controlador

El diseño permite que `CursoController` sea reutilizado:
- **Compartido**: Con editarCurso() y eliminarCurso()
- **Método específico**: crearCurso() con validaciones mínimas propias
- **Consistencia**: Mismo patrón de comunicación con repositorio
- **Validaciones**: Específicas para creación académica

### patrón include para edición

- **Separación de responsabilidades**: crearCurso() se enfoca en crear básico
- **Reutilización**: **&lt;&lt;include&gt;&gt;** editarCurso() evita duplicar funcionalidad de edición
- **Flujo natural**: Creación → Edición automática
- **Experiencia continua**: Usuario no percibe discontinuidad

### flexibilidad de creación académica

- **CursoRepository** puede implementar:
  - **Creación con plantilla**: Curso básico con valores por defecto
  - **Generación automática**: Código de curso automático
  - **Relaciones básicas**: Asociación con programa académico por defecto
  - **Auditoría**: Registro de creación y autor

### experiencia de usuario académica

- **Simplicidad**: Solo pide información esencial (nombre)
- **Rapidez**: Mínimos pasos para crear curso válido
- **Continuidad**: Transferencia automática a edición completa
- **Claridad**: Usuario entiende que debe completar en edición

## validaciones de negocio académicas

### restricciones de integridad curricular mínima

**CursoController** debe verificar:
- **Nombre obligatorio**: Campo nombre no puede estar vacío
- **Unicidad**: No existe otro curso con el mismo nombre
- **Formato básico**: Nombre cumple requisitos mínimos de formato
- **Permisos administrativos**: Administrador autorizado para crear cursos

### manejo de errores académicos

- **Nombre vacío**: Mensaje informativo sobre campo obligatorio
- **Curso duplicado**: Explicación de conflicto con curso existente
- **Error de sistema**: Manejo graceful de fallos de persistencia

## diferencias con otros casos CRUD de cursos

### crearCurso() vs editarCurso()

**crearCurso():**
- **Objetivo**: Creación básica con datos mínimos
- **Interacción**: Solicitud mínima + transferencia automática
- **Validaciones**: Restricciones básicas de creación
- **Resultado**: Curso básico creado + edición completa automática

**editarCurso():**
- **Objetivo**: Modificación de datos académicos completos
- **Interacción**: Lectura + escritura múltiple de todos los campos
- **Validaciones**: Restricciones académicas de contenido completo
- **Resultado**: Curso actualizado con información completa

### complementariedad CRUD para cursos

- **crearCurso()**: "El delgado" - añade curso básico al programa
- **editarCurso()**: "El gordo" - completa y modifica información académica
- **eliminarCurso()**: Remueve cursos del programa académico
- **abrirCursos()**: Lista y selecciona cursos del programa

## diagrama de secuencia

<div align=center>

|![Secuencia: crearCurso()](/images/RUP/01-analisis/casos-uso/crearCurso/crearCurso-analisis-secuencia.svg)|
|-|
|Código fuente: [secuencia.puml](secuencia.puml)|

</div>

## referencias

- [Caso de uso detallado](../../../00-casos-uso/02-detalle/crearCurso/README.md)
- [editarCurso() - Caso complementario](../editarCurso/README.md)
- [eliminarCurso() - Caso complementario](../eliminarCurso/README.md)
- [abrirCursos() - Contexto de navegación](../abrirCursos/README.md)
- [crearPrograma() - Patrón de referencia](../crearPrograma/README.md)
- [Modelo del dominio](../../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)