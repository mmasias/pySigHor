# Evidencia: Dashboards multi-stack y validación experimental

<div align=right>

||||
|-|-|-|
|[🏠️](../README.md)|[Artículo](README.md)|[Contexto](contexto.md) \| **Evidencia** \| [Comparativa](comparativa-stacks.md)|

</div>

## Dashboard Main: Base tecnológicamente neutra

<div align=center>

|![Dashboard Main - Análisis completo](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|:-:|
|**Dashboard Main - 32 casos de uso analizados**|
|[Ver dashboard completo](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|[Código fuente PlantUML](https://github.com/mmasias/pySigHor/blob/main/RUP/99-seguimiento/diagrama-contexto-administrador.puml)|

</div>

### Características del dashboard main

**Estado visual:**
- ✅ Todos los casos de uso en 🟫 **Amarillo oscuro** (Analizado)
- ✅ Enlaces `[nombreCasoUso()]` → Especificación detallada en `/main/`
- ✅ Enlaces `[A]` → Análisis MVC en `/main/`
- ❌ Sin enlaces `[D]` - Diseño disponible en ramas específicas

**Leyenda:**
```
[nombreCasoUso()] -> Especificación detallada
[A] -> Análisis MVC
[D] -> Diseño (disponible en ramas específicas)

Enlaces a dashboards de diseño:
- FastAPI/React
- Spring/Angular
```

**Significado:**
- Representa la **base común** a todas las implementaciones
- Es el **single source of truth** para análisis
- **No tiene dependencias tecnológicas**
- Todos los cambios en análisis se hacen aquí

---

## Dashboard FastAPI/React: Primera implementación tecnológica

<div align=center>

|![Dashboard FastAPI/React](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|:-:|
|**Dashboard FastAPI/React - Diseño en progreso**|
|[Ver dashboard completo](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|[Código fuente PlantUML](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/99-seguimiento/diagrama-contexto-administrador.puml)|

</div>

### Características del dashboard FastAPI/React

**Estado visual:**
- ✅ 5 casos de uso en 🟢 **Verde** (Diseñado):
  - `iniciarSesion()`
  - `abrirAulas()`
  - `crearAula()`
  - `editarAula()`
  - `eliminarAula()`
- ✅ 27 casos de uso en 🟫 **Amarillo oscuro** (Análisis completo, diseño pendiente)
- ✅ Enlaces `[nombreCasoUso()]` y `[A]` → `/main/` (single source of truth)
- ✅ Enlaces `[D]` → `/diseño-fastapi-react/` (diseño específico)

**Leyenda:**
```
- Spring/Angular (enlace al dashboard alternativo)
- FastAPI/React (stack actual, sin enlace)
```

**Navegación:**
- Desde cualquier caso diseñado (verde), se puede navegar a:
  - Especificación detallada en `/main/`
  - Análisis MVC en `/main/`
  - **Diseño FastAPI/React** en `/diseño-fastapi-react/`
- Switching a Spring/Angular: Click en enlace de leyenda

---

## Dashboard Spring/Angular: Segunda implementación tecnológica

<div align=center>

|![Dashboard Spring/Angular](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|:-:|
|**Dashboard Spring/Angular - Diseño en progreso**|
|[Ver dashboard completo](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|[Código fuente PlantUML](https://github.com/mmasias/pySigHor/blob/diseño-spring-angular/RUP/99-seguimiento/diagrama-contexto-administrador.puml)|

</div>

### Características del dashboard Spring/Angular

**Estado visual:**
- ✅ 5 casos de uso en 🟢 **Verde** (Diseñado):
  - `iniciarSesion()`
  - `abrirAulas()`
  - `crearAula()`
  - `editarAula()`
  - `eliminarAula()`
- ✅ 27 casos de uso en 🟫 **Amarillo oscuro** (Análisis completo, diseño pendiente)
- ✅ Enlaces `[nombreCasoUso()]` y `[A]` → `/main/` (single source of truth)
- ✅ Enlaces `[D]` → `/diseño-spring-angular/` (diseño específico)

**Leyenda:**
```
- FastAPI/React (enlace al dashboard alternativo)
- Spring/Angular (stack actual, sin enlace)
```

**Navegación:**
- Desde cualquier caso diseñado (verde), se puede navegar a:
  - Especificación detallada en `/main/`
  - Análisis MVC en `/main/`
  - **Diseño Spring/Angular** en `/diseño-spring-angular/`
- Switching a FastAPI/React: Click en enlace de leyenda

---

## Comparación visual lado a lado

<div align=center>

|Spring/Angular|Main|FastAPI/React|
|:-:|:-:|:-:|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|![](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|**5 diseñados** (verde)|**32 analizados** (amarillo oscuro)|**5 diseñados** (verde)|
|**27 pendientes** (amarillo oscuro)|**0 diseñados** (sin verde)|**27 pendientes** (amarillo oscuro)|

</div>

### Observaciones clave

**Consistencia entre stacks:**
- ✅ Los mismos 5 casos de uso están diseñados en ambos stacks
- ✅ El mismo conjunto de 27 casos permanece en análisis en ambos
- ✅ La topología del diagrama es idéntica en los tres dashboards
- ✅ Solo cambia el color de los 5 casos diseñados (amarillo → verde)

**Independencia tecnológica validada:**
- ✅ Dashboard main NO cambió al diseñar en ramas tecnológicas
- ✅ Todos los enlaces `[nombreCasoUso()]` y `[A]` apuntan a `/main/`
- ✅ Solo enlaces `[D]` son específicos por stack
- ✅ Cero propagación de cambios entre ramas

---

## Evidencia de artefactos de diseño

### Casos de uso diseñados en FastAPI/React

**Estructura de directorios:**
```
diseño-fastapi-react/
└── RUP/
    └── 02-diseño/
        └── casos-uso/
            ├── iniciarSesion/
            │   ├── README.md          # Diseño específico FastAPI/React
            │   └── secuencia.puml     # Diagrama de secuencia de diseño
            ├── abrirAulas/
            │   ├── README.md
            │   └── secuencia.puml
            ├── crearAula/
            │   ├── README.md
            │   └── secuencia.puml
            ├── editarAula/
            │   ├── README.md
            │   └── secuencia.puml
            └── eliminarAula/
                ├── README.md
                └── secuencia.puml
```

**Contenido de artefactos de diseño:**
- Mapeo de clases de análisis a componentes tecnológicos específicos
- Diagramas de secuencia con clases de diseño (controllers, services, repositories, components)
- Decisiones de arquitectura específicas del stack (REST endpoints, React hooks, TypeScript types)

### Casos de uso diseñados en Spring/Angular

**Estructura de directorios:**
```
diseño-spring-angular/
└── RUP/
    └── 02-diseño/
        └── casos-uso/
            ├── iniciarSesion/
            │   ├── README.md          # Diseño específico Spring/Angular
            │   └── secuencia.puml     # Diagrama de secuencia de diseño
            ├── abrirAulas/
            │   ├── README.md
            │   └── secuencia.puml
            ├── crearAula/
            │   ├── README.md
            │   └── secuencia.puml
            ├── editarAula/
            │   ├── README.md
            │   └── secuencia.puml
            └── eliminarAula/
                ├── README.md
                └── secuencia.puml
```

**Contenido de artefactos de diseño:**
- Mapeo de clases de análisis a componentes tecnológicos específicos
- Diagramas de secuencia con clases de diseño (controllers, services, repositories, components)
- Decisiones de arquitectura específicas del stack (Spring annotations, Angular components, RxJS observables)

---

## Evidencia técnica: commits de Git

### Rama main

**Commit reciente relacionado:**
```
commit: feat: replica y dúplica
- Dashboard actualizado con enlaces a ambos stacks de diseño
- Leyenda incluye referencia [D] -> Diseño (disponible en ramas específicas)
```

**Archivos afectados:**
- `RUP/99-seguimiento/diagrama-contexto-administrador.puml`
- `RUP/99-seguimiento/README.md`

### Rama diseño-fastapi-react

**Commits relacionados:**
```
commit: feat: dashboard FastAPI/React con navegación coherente
- URLs cambiadas de /main/ a /diseño-fastapi-react/ para navegación coherente
- Footer indica stack tecnológico activo: FastAPI/React
- Enlace para cambiar a dashboard Spring/Angular
- Leyenda actualizada con referencia [D] -> Diseño
```

**Archivos afectados:**
- `RUP/99-seguimiento/diagrama-contexto-administrador.puml`
- 5 casos de uso cambiados de darkgoldenrod (#🟫) a green (#🟢)
- Enlaces [D] agregados apuntando a `/diseño-fastapi-react/RUP/02-diseño/`

### Rama diseño-spring-angular

**Commits relacionados:**
```
commit: feat: dashboard Spring/Angular con navegación coherente
- Actualización del dashboard de contexto en rama diseño-spring-angular
- URLs cambiadas de /main/ a /diseño-spring-angular/ para navegación coherente
- Footer indica stack tecnológico activo: Spring/Angular
- Enlace para cambiar a dashboard FastAPI/React
- Leyenda actualizada con referencia [D] -> Diseño
```

**Archivos afectados:**
- `RUP/99-seguimiento/diagrama-contexto-administrador.puml`
- 5 casos de uso cambiados de darkgoldenrod (#🟫) a green (#🟢)
- Enlaces [D] agregados apuntando a `/diseño-spring-angular/RUP/02-diseño/`

---

## Métricas del experimento

### Resistencia de artefactos de análisis

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| **Casos de uso analizados** | 32 | Base completa para experimentación |
| **Casos diseñados por stack** | 5 | Vertical slice representativo |
| **Artefactos de análisis modificados** | 0 | **100% de independencia tecnológica** |
| **Artefactos de requisitos modificados** | 0 | **100% de reutilización** |
| **Diagramas de colaboración MVC modificados** | 0 | **100% de validez** |

### Facilidad de implementación

| Métrica | FastAPI/React | Spring/Angular | Observación |
|---------|---------------|----------------|-------------|
| **Tiempo de mapeo análisis → diseño** | ~1h por caso | ~1h por caso | Comparable entre stacks |
| **Decisiones ya resueltas por análisis** | ~80% | ~80% | Análisis MVC efectivo |
| **Ajustes al análisis requeridos** | 0 | 0 | **Validación exitosa** |

### Calidad del resultado

| Aspecto | Evaluación | Evidencia |
|---------|-----------|-----------|
| **Consistencia arquitectónica** | ✅ Alta | Ambos stacks mantienen responsabilidades MVC |
| **Trazabilidad requisitos → código** | ✅ Completa | Enlaces navegables en dashboards |
| **Coherencia de navegación** | ✅ Perfecta | Single source of truth funciona |

---

## Lecciones aprendidas documentadas

### Lo que funcionó

1. **Análisis MVC riguroso se traduce directamente a diseño**
   - Boundary → Controllers (backend) + Components (frontend)
   - Control → Services
   - Entity → Repositories + Models

2. **Especificaciones detalladas permanecen válidas**
   - Diagramas de estado aplicables sin cambios
   - Wireframes SALT sirven de base para ambos frontends

3. **Arquitectura de navegación con punto central**
   - Cero duplicación
   - Cero conflictos de merge
   - Switching intuitivo entre stacks

### Lo que se refinó

1. **Nomenclatura de stacks**
   - Decisión: "FastAPI/React" > "FART"
   - TypeScript implícito (estándar en 2025)

2. **Placement de enlaces de switching**
   - Leyenda > Footer
   - Líneas separadas para stack actual y enlace a alternativo

3. **Granularidad de validación**
   - 5 casos de uso = sweet spot
   - Cubre CRUD + autenticación + navegación

---

## Próxima evidencia esperada

### Fase de expansión

**Objetivo:** Diseñar `generarHorario()` en ambos stacks

**Complejidad:**
- Algoritmo de 4 fases de optimización
- Lógica de negocio sofisticada
- Estructuras de datos complejas

**Hipótesis:** El análisis permanecerá inalterado incluso con algoritmos complejos

**Evidencia a generar:**
- Dashboards actualizados con `generarHorario()` en verde
- Artefactos de diseño específicos para el algoritmo en ambos stacks
- Medición de ajustes al análisis (esperado: 0)

---

## Referencias

- [Dashboard Main](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)
- [Dashboard FastAPI/React](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)
- [Dashboard Spring/Angular](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)
- [Repositorio pySigHor](https://github.com/mmasias/pySigHor)
