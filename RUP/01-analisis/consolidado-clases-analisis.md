# Análisis Arquitectónico - Clases de Análisis Consolidadas

> |[🏠️](/README.md)|[📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[RUP](/RUP/README.md)|[Análisis](/RUP/01-analisis/README.md)|**Consolidado**|
> |-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration (Elaboración)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-01-10
- **Autor**: Equipo de desarrollo

## Propósito

Este diagrama consolida **todas las clases de análisis identificadas en los 31 casos de uso** del sistema SigHor, organizadas según el patrón MVC y con sus relaciones explícitas, proporcionando un **mapa arquitectónico limpio** que sirve como base para las decisiones de diseño.

## Diagrama consolidado

<div align=center>

|![Clases de Análisis Consolidadas](/images/RUP/01-analisis/consolidado-clases-analisis.svg)|
|-|
|**Código fuente**: [consolidado-clases-analisis.puml](consolidado-clases-analisis.puml)|

</div>

## Análisis arquitectónico

### Métricas del modelo

| Estereotipo | Cantidad | Descripción |
|------------|----------|-------------|
| **VIEW (Boundary)** | 31 clases | Interfaces de usuario especializadas por funcionalidad |
| **CONTROLLER (Control)** | 18 clases | Coordinadores de lógica de negocio |
| **MODEL (Entity)** | 23 clases | Entidades de dominio, repositorios y servicios especializados |
| **TOTAL** | **72 clases** | Modelo completo de análisis MVC |

### Patrones arquitectónicos identificados

#### 1. Patrón de controladores duales

**Problema resuelto**: Separación de responsabilidades entre listado y operaciones CRUD

| Tipo | Patrón | Ejemplos | Responsabilidad |
|------|--------|----------|-----------------|
| **Colección** | `[Entidades]Controller` | `CursosController`, `AulasController` | Gestión de listados y filtros |
| **Individual** | `[Entidad]Controller` | `CursoController`, `AulaController` | Operaciones CRUD de entidad específica |

**Validación del patrón**:
- ✅ **Consistente**: Se aplica a todas las entidades principales (Programa, Curso, Profesor, Edificio, Aula, Recurso)
- ✅ **Separación clara**: Colección = listados, Individual = CRUD
- ✅ **Escalable**: Permite especializaciones independientes

#### 2. Patrón repository por entidad

**Problema resuelto**: Abstracción uniforme del acceso a datos

```
[Entidad] ←--o [EntidadRepository] ←-- [EntidadController]
```

**Validación**:
- ✅ **Completo**: Todos los controladores acceden vía repository
- ✅ **Consistente**: Un repository por entidad de dominio
- ✅ **Separación**: Lógica de acceso a datos aislada

#### 3. Entidades de relación especializadas

**Problema resuelto**: Gestión de relaciones many-to-many complejas

| Entidad | Propósito | Gestión |
|---------|-----------|---------|
| `AsignacionProfesorCurso` | Relación profesor-curso con metadatos | `ProfesorRepository` |
| `PreferenciasRecurso` | Preferencias profesor-recurso | `ProfesorRepository` |

### Controladores especializados

#### Controladores del sistema
- `IniciarSesionController` - Autenticación
- `CompletarGestionController` - Hub de navegación central  
- `CerrarSesionController` - Terminación de sesión
- `HorarioController` - Gestión algorítmica de horarios

#### Controladores de proceso
- `AsignacionProfesorCursoController` - Proceso de asignación
- `PreferenciasProfesorController` - Configuración de preferencias

### Entidades especiales identificadas

| Entidad | Tipo | Propósito |
|---------|------|-----------|
| `HorarioGenerator` | Servicio algorítmico | Ejecuta el algoritmo de 4 fases de generación |
| `Validador` | Servicio de validación | Valida datos mínimos y integridad |
| `OpcionesMenu` | Entidad de presentación | Estructura de opciones disponibles |
| `Sesion` | Entidad de estado | Mantiene contexto de usuario autenticado |

## Validaciones arquitectónicas

### ✅ Coherencia en nombres

**Patrón de colección vs individual**:
- **Controladores de colección**: Todos usan plural (`CursosController`, `AulasController`)
- **Controladores individuales**: Todos usan singular (`CursoController`, `AulaController`)
- **Sin inconsistencias**: No se detectaron violaciones del patrón

### ✅ Ausencia de dependencias circulares

**Verificación**:
- **View → Controller**: Unidireccional ✅
- **Controller → Repository**: Unidireccional ✅  
- **Repository → Entity**: Unidireccional ✅
- **Sin ciclos detectados**: Arquitectura en capas respetada ✅

### ✅ Trazabilidad con casos de uso

**Validación completa**:
- **31 casos de uso** → **31 vistas específicas** ✅
- **Controladores únicos** por responsabilidad ✅
- **Entidades** corresponden al modelo del dominio ✅

## Recomendaciones para el diseño

### 1. Mantenimiento del patrón dual

**Recomendación**: Preservar la separación controlador colección/individual durante el diseño tecnológico.

**Beneficios**:
- **Escalabilidad**: Listados y CRUD pueden evolucionar independientemente
- **Mantenibilidad**: Responsabilidades claras y separadas
- **Testabilidad**: Casos de prueba específicos por tipo de operación

### 2. Implementación de entidades especiales

**HorarioGenerator**:
- Implementar como servicio algorítmico independiente
- Encapsular las 4 fases del algoritmo legacy
- Permitir evolución independiente del algoritmo

**Validador**:
- Implementar como servicio transversal
- Reutilizable por múltiples controladores
- Centralizar reglas de validación

### 3. Gestión de sesión y permisos

**Patrón identificado**:
- `Sesion` es compartida por múltiples controladores
- `PermisosRepository` centraliza lógica de autorización
- `OpcionesMenu` estructura la presentación de capacidades

**Recomendación**: Implementar como servicios transversales del framework.

## Conexión con disciplinas RUP

### Desde requisitos
- **31 casos de uso detallados** → **Clases de análisis específicas**
- **Modelo del dominio** → **Entidades y repositorios**
- **Prototipos SALT** → **Vistas especializadas**

### Hacia diseño
- **Clases conceptuales** → Base para clases de diseño tecnológico
- **Patrones identificados** → Guía para selección de frameworks
- **Responsabilidades** → Distribución en arquitectura técnica

### Hacia implementación
- **72 clases de análisis** → Estructura base del código
- **Relaciones explícitas** → Configuración de dependencias
- **Entidades especiales** → Componentes algorítmicos específicos

## Métricas de complejidad

| Métrica | Valor | Evaluación |
|---------|-------|------------|
| **Clases totales** | 72 | ✅ Manejable para el dominio |
| **Relaciones** | 101 | ✅ Bien estructuradas |
| **Profundidad de herencia** | 0 | ✅ Composición sobre herencia |
| **Acoplamiento** | Bajo | ✅ Responsabilidades separadas |
| **Cohesión** | Alta | ✅ Clases con propósito específico |

## Referencias

- [Casos de uso analizados](casos-uso/README.md)
- [Disciplina de Análisis](README.md)
- [Modelo del dominio](../00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)
- [conversation-log.md](../../conversation-log.md) - Metodología de análisis aplicada
- [Dashboard de seguimiento](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)

---

**Nota metodológica**: Este análisis consolida el trabajo de análisis MVC realizado de forma sistemática en 31 casos de uso, aplicando consistentemente los patrones establecidos en las leyes del proyecto y siguiendo la metodología RUP adaptada para arqueología de software.