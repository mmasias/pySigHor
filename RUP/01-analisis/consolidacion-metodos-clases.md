# Consolidación de Métodos de las Clases de Análisis

## Información del Artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-08-14
- **Autor**: Equipo de desarrollo

## Propósito

Obtener un **mapa detallado de interfaces** que revele la distribución real de responsabilidades y sirva como especificación para el diseño de componentes, consolidando las interfaces públicas y responsabilidades específicas de cada clase basándose en los mensajes de colaboración, responsabilidades documentadas y flujos de secuencia analizados en los 31 casos de uso.

## Resumen Ejecutivo

### Datos de Consolidación

- **Casos de uso analizados**: 31
- **Clases consolidadas**: 73
- **Métodos únicos identificados**: 186
- **Patrones arquitectónicos detectados**: 4 principales

### Distribución de Responsabilidades

| Estereotipo | Cantidad | Porcentaje | Responsabilidad Principal |
|-------------|----------|------------|---------------------------|
| **VIEW (Boundary)** | 31 clases | 42.5% | Interfaces de usuario y presentación |
| **CONTROLLER (Control)** | 18 clases | 24.7% | Coordinación y lógica de casos de uso |
| **MODEL (Entity)** | 24 clases | 32.8% | Entidades de dominio y repositorios |

## Diagrama de Clases Consolidado

<div align=center>

|![Consolidación de Métodos](/images/RUP/01-analisis/consolidacion-metodos-clases-analisis.svg)|
|-|
|**Mapa de Interfaces para Especificación de Componentes**<br>Código fuente: [consolidacion-metodos-clases.puml](consolidacion-metodos-clases.puml)|

</div>

## Análisis de Patrones Identificados

### 1. CRUD Pattern (Create, Read, Update, Delete)

**Implementación consistente en Repositories**:

```plantuml
interface RepositoryPattern {
    +obtenerTodos() : List<T>
    +obtenerPorId(id: String) : T
    +buscarPorCriterio(criterio: String) : List<T>
    +crear(...) : T
    +actualizar(entity: T) : boolean/void
    +eliminar(id: String) : void
    +verificarUnicidad(value: String) : boolean
}
```

**Entidades que implementan CRUD completo**:
- ProgramaRepository
- CursoRepository  
- ProfesorRepository
- EdificioRepository
- AulaRepository
- RecursoRepository

### 2. Repository Pattern

**Características identificadas**:
- Abstracción del acceso a datos
- Métodos estándar de consulta y manipulación
- Validaciones de unicidad
- Búsquedas por criterios dinámicos

### 3. Controller Pattern

**Responsabilidades identificadas**:
- Coordinación de casos de uso
- Validaciones de negocio
- Orquestación entre View y Model
- Transformación de datos

### 4. View Pattern

**Responsabilidades identificadas**:
- Presentación de datos al usuario
- Captura de solicitudes del actor
- Navegación entre estados
- Delegación de lógica de negocio

## Inconsistencias Detectadas

### 1. Signature Inconsistencies ❌

#### Problema: Métodos con mismo nombre pero signatures diferentes

**Método `verificarUnicidad()`**:
```java
// Inconsistencia de parámetros
ProfesorRepository.verificarUnicidad(codigo: String) : boolean
CursoRepository.verificarUnicidad(nombre: String) : boolean    // ❌ Parámetro diferente
```

**Método `actualizar()`**:
```java  
// Inconsistencia de tipos de retorno
ProfesorRepository.actualizar(profesor: Profesor) : boolean
ProgramaRepository.actualizar(programa: Programa) : void      // ❌ Retorno diferente
```

#### Recomendación:
Estandarizar signatures usando generics o interfaces comunes.

### 2. Method Duplications ⚠️

#### Problema: Métodos duplicados entre View y Controller

```java
// Duplicación detectada
EliminarProgramaView.eliminarPrograma(programaId: String) : void
ProgramaController.eliminarPrograma(programaId: String) : void
```

#### Recomendación:
Views deben delegar toda lógica a Controllers, manteniendo solo responsabilidades de presentación.

### 3. Repository Patterns Incompletos ⚠️

#### Repositories con CRUD incompleto:
- **UsuarioRepository**: Solo tiene `validarCredenciales()`
- **HorarioRepository**: Solo tiene métodos de consulta
- **SesionRepository**: No implementado completamente

#### Recomendación:
Completar implementación CRUD según necesidades del dominio o justificar la excepción.

### 4. Cohesion Issues ❌

#### Problema: Lógica de negocio en Views

```java
// ❌ View con lógica de negocio
GenerarHorarioView.generarHorario() : void
```

#### Recomendación:
Mover lógica de generación a `HorarioController`.

## Recomendaciones de Refactorización

### 1. Estandarización de Interfaces

#### Crear interfaces genéricas:

```java
interface Repository<T, ID> {
    List<T> obtenerTodos();
    T obtenerPorId(ID id);
    List<T> buscarPorCriterio(String criterio);
    T crear(T entity);
    boolean actualizar(T entity);
    void eliminar(ID id);
    boolean verificarUnicidad(String field, String value);
}
```

### 2. Separación de Responsabilidades

#### Views → Solo presentación:
```java
interface View {
    void presentar(Object data);
    void capturarSolicitud();
    void mostrarError(String mensaje);
    void navegar(String destino);
}
```

#### Controllers → Solo coordinación:
```java
interface Controller {
    void coordinar();
    boolean validar(Object data);
    void procesar();
}
```

### 3. Consolidación de Métodos Similares

#### Antes (inconsistente):
```java
editarPrograma(programaId: String) : void
editarPrograma(programaNuevo: Programa) : void
```

#### Después (consolidado):
```java
editarPrograma(programa: Programa) : void
editarPrograma(programaId: String) : void  // Sobrecarga clara
```

## Oportunidades de Optimización

### 1. Detección de Funcionalidad Duplicada

**Métodos que podrían consolidarse**:
- `listarX()` en todos los Controllers → `ControllerBase.listar()`
- `filtrarX()` en todos los Controllers → `ControllerBase.filtrar()`
- `verificarUnicidad()` en Repositories → `RepositoryBase.verificarUnicidad()`

### 2. Validación de Cohesión por Clase

**Classes con responsabilidades cohesivas** ✅:
- LoginView (solo autenticación)
- IniciarSesionController (solo coordinación de login)
- Usuario (solo datos de usuario)

**Clases candidatas a separación**:
- ProfesorController (demasiadas responsabilidades: CRUD + preferencias + asignaciones)

### 3. Identificación de Acoplamiento Mínimo

**Dependencias bien definidas** ✅:
- Views → Controllers
- Controllers → Repositories  
- Repositories → Entities

**Acoplamiento indebido detectado** ❌:
- Ningún acoplamiento indebido detectado

## Contratos para Fase de Diseño

### 1. Interfaces Públicas Estandarizadas

Cada clase de análisis define un contrato claro para implementación:

**VIEW contracts**:
- Métodos de presentación con signatures consistentes
- Delegación obligatoria de lógica de negocio
- Patrones de navegación estandarizados

**CONTROLLER contracts**:
- Coordinación de casos de uso sin lógica de presentación
- Validaciones de negocio centralizadas
- Interfaces consistentes con Views y Repositories

**REPOSITORY contracts**:
- CRUD completo o justificación de excepción
- Signatures estandarizadas con generics
- Validaciones de integridad implementadas

### 2. Distribución de Responsabilidades Validada

| Responsabilidad | Ubicación Correcta | Ubicación Incorrecta |
|-----------------|-------------------|----------------------|
| Presentar datos | VIEW | CONTROLLER/MODEL |
| Validar negocio | CONTROLLER | VIEW/MODEL |
| Persistir datos | REPOSITORY | VIEW/CONTROLLER |
| Lógica de dominio | ENTITY | VIEW/REPOSITORY |

## Próximos Pasos

### Para Fase de Diseño:

1. **Aplicar refactorizaciones recomendadas**
   - Estandarizar signatures
   - Eliminar duplicaciones
   - Completar patrones Repository

2. **Seleccionar tecnologías** basándose en interfaces definidas
   - Framework web para Views
   - Container de inyección para Controllers
   - ORM para Repositories

3. **Crear arquitectura técnica** que implemente contratos definidos
   - Mapeo clase análisis → componente tecnológico
   - Configuración de dependencias
   - Estrategias de testing por capa

## Referencias

- [Análisis de Casos de Uso](../casos-uso/README.md) - Casos de uso individuales analizados
- [Modelo del Dominio](../../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) - Entidades del dominio
- [Conversation Log](../../../conversation-log.md) - Metodología de análisis aplicada
- [Leyes del Proyecto](../../../extraDocs/999-leyes-proyecto/) - Estándares metodológicos aplicados

---

**Este análisis establece las bases técnicas para la transición de la fase de análisis a la fase de diseño, proporcionando contratos claros y identificando oportunidades de optimización para la implementación de componentes.**