# Reuso vs Reimplementación

<div align=right>

|||||||
|-|-|-|-|-|-|
|[🏠️](../README.md)|[Artículo](README.md)|[Contexto](contexto.md)|[Evidencia](evidencia.md)|[Comparativa](comparativa-arquitecturas-cli.md)|**Reuso**|

</div>

## La paradoja del reuso

El experimento CLI plantea una paradoja aparente:

<div align=center>

|Reuso máximo (CLI HTTP)|Reuso mínimo (CLI Standalone)|
|-|-|
|100% de backend reusado|0% de backend reusado
|2.5 horas de desarrollo|8 horas de desarrollo
|Dependencia de servidor HTTP|Independencia total

</div>

**La pregunta clave:** ¿Es siempre mejor reusar código?

**La respuesta metodológica:** Depende del contexto. El análisis RUP es **reusable** en ambos casos, pero el **código de diseño** puede o no serlo según decisiones arquitectónicas.

## Taxonomía de la reuso en RUP

### Nivel 1: Reuso de análisis (100% en todos los casos)

**Qué se reusa:**

- Especificaciones detalladas de casos de uso
- Diagramas de colaboración MVC
- Responsabilidades vista/controlador/modelo
- Diagramas de secuencia de análisis
- Modelo del dominio
- Wireframes SALT (conceptuales)

**Evidencia en el experimento:**

- FastAPI/React: Reusa análisis
- Spring/Angular: Reusa análisis
- CLI HTTP: Reusa análisis
- CLI Standalone: Reusa análisis

**Conclusión:** El análisis es **siempre reusable** independientemente de tecnología.

### Nivel 2: Reuso de diseño (variable según arquitectura)

**Qué *puede* reusarse:**

- Clases de diseño (controllers, services, repositories)
- Lógica de negocio (validaciones, transformaciones)
- Acceso a datos (queries, transacciones)
- Esquema de base de datos

**Evidencia en el experimento:**

<div align=center>

|Stack|Reusa diseño de|Porcentaje|
|-|-|-|
|**FastAPI/React**|Nada (primero implementado)|0%|
|**Spring/Angular**|Nada (familia diferente: Java vs Python)|0%|
|**CLI HTTP**|FastAPI/React (consume API)|100%|
|**CLI Standalone**|Nada (pila propia)|0%|

</div>

**Conclusión:** El diseño es **reusable solo dentro de la misma familia tecnológica**.

### Nivel 3: Reuso de implementación (muy variable)

**Qué *puede* reusarse:**

- Código fuente exacto
- Librerías y frameworks
- Configuración de infraestructura
- Scripts de despliegue

**Evidencia en el experimento:**

<div align=center>

|Stack|Reusa implementación de|Forma de reuso|
|-|-|-|
|**CLI HTTP**|FastAPI/React|**Consumo de API** - Reuso por delegación|
|**CLI Standalone**|Nada|**Reimplementación** - Código nuevo desde cero|

</div>

**Conclusión:** La implementación es **reusable solo con decisiones arquitectónicas específicas** (API, microservicios, librerías compartidas).

## Análisis de reuso por capa MVC

### Capa Vista

**Análisis:**

- Responsabilidad: Interacción con usuario
- Tecnología: Agnóstica (texto genérico en análisis)

**Diseño:**

<div align=center>

|Stack|Implementación Vista|Reuso|
|-|-|-|
|FastAPI/React|Componentes React (.tsx)|0% entre stacks|
|Spring/Angular|Componentes Angular (.ts)|0% entre stacks|
|CLI HTTP|Comandos Click (.py)|0% entre stacks|
|CLI Standalone|Comandos Click (.py)|Potencial 80% con CLI HTTP|

</div>

**Observación:** Vista siempre es **específica del paradigma de interfaz**. GUI web vs CLI terminal son **incompatibles** para reuso de código, pero **compatibles** para reuso de análisis.

### Capa Controlador

**Análisis:**

- Responsabilidad: Lógica de negocio y orquestación
- Tecnología: Agnóstica (pseudocódigo en análisis)

**Diseño:**

<div align=center>

|Stack|Implementación Controlador|Reuso|
|-|-|-|
|FastAPI/React|Services Python (FastAPI)|0% con Spring/Angular|
|Spring/Angular|Services Java (Spring)|0% con FastAPI/React|
|CLI HTTP|**Reusa** FastAPI Services|100% con FastAPI/React|
|CLI Standalone|Services Python (standalone)|0% (reimplementa)|

</div>

**Observación:** Controlador es **reusable dentro de la misma familia** (Python FastAPI ↔ Python CLI HTTP). Entre lenguajes diferentes (Python ↔ Java), el análisis se reusa pero el código se reimplementa.

### Capa Modelo

**Análisis:**

- Responsabilidad: Persistencia y recuperación de datos
- Tecnología: Agnóstica (CRUD genérico en análisis)

**Diseño:**

<div align=center>

|Stack|Implementación Modelo|Reuso|
|-|-|-|
|FastAPI/React|Repositories Python + SQLAlchemy|0% con Spring/Angular|
|Spring/Angular|Repositories Java + JPA|0% con FastAPI/React|
|CLI HTTP|**Reusa** FastAPI Repositories|100% con FastAPI/React|
|CLI Standalone|Repositories Python + SQLAlchemy|Potencial 70% con FastAPI|

</div>

**Observación:** Modelo es **reusable si comparten ORM y lenguaje**. CLI Standalone podría reusar modelos SQLAlchemy de FastAPI si existiera decisión arquitectónica de compartir librería.

## Cuantificación del esfuerzo: Reuso vs Reimplementación

### Caso de uso: `iniciarSesion()`

**Implementación desde análisis (sin reuso de código):**

<div align=center>

|Componente|FastAPI/React|Spring/Angular|CLI Standalone|
|-|-|-|-|
|Vista|1h (componente React)|1h (componente Angular)|0.5h (comando Click)|
|Controlador|0.5h (service Python)|0.5h (service Java)|0.5h (service Python)|
|Modelo|0.5h (repo Python)|0.5h (repo Java)|0.5h (repo Python)|
|**TOTAL**|**2h**|**2h**|**1.5h**|

</div>

**Implementación con reuso (CLI HTTP):**

<div align=center>

|Componente|Esfuerzo|Explicación|
|-|-|-|
|Vista|0.5h (comando Click)|Solo nueva vista|
|Controlador|0h (reusa FastAPI)|Ya existe|
|Modelo|0h (reusa FastAPI)|Ya existe|
|**TOTAL**|**0.5h**|**75% de ahorro**|

</div>

**Ahorro por reuso:** 1.5h por caso de uso

### Caso de uso: `abrirAulas()`

**Implementación desde análisis:**

<div align=center>

|Componente|FastAPI/React|Spring/Angular|CLI Standalone|
|-|-|-|-|
|Vista|1.5h (tabla React)|1.5h (tabla Angular)|0.5h (tabla terminal)|
|Controlador|0.5h (service + paginación)|0.5h (service + paginación)|0.5h (service)|
|Modelo|0.5h (repo + query)|0.5h (repo + query)|0.5h (repo)|
|**TOTAL**|**2.5h**|**2.5h**|**1.5h**|

</div>

**Implementación con reuso (CLI HTTP):**

<div align=center>

|Componente|Esfuerzo|Explicación|
|-|-|-|
|Vista|0.5h (formateo tabla)|Solo nueva vista|
|Controlador|0h (reusa paginación)|Ya existe|
|Modelo|0h (reusa query)|Ya existe|
|**TOTAL**|**0.5h**|**80% de ahorro**|

</div>

**Ahorro por reuso:** 2h por caso de uso

### Totales del experimento (5 casos de uso)

<div align=center>

|Métrica|CLI HTTP (reuso)|CLI Standalone (reimplementación)|Ahorro|
|-|-|-|-|
|**Tiempo total**|2.5h|8h|**5.5h (69%)**|
|**Archivos nuevos**|5|15|10 archivos menos|
|**LOC totales**|~350|~1,250|900 LOC menos|

</div>

## El costo oculto de la reuso

### Deuda técnica introducida por reuso

**CLI HTTP reusa FastAPI, pero introduce:**

<div align=center>

|Acoplamiento arquitectónico|Complejidad operacional|Limitaciones de portabilidad|Sobrecarga de red|
|-|-|-|-|
|CLI depende de API corriendo|Usuario debe iniciar servidor antes de usar CLI|No distribuible como ejecutable único|Latencia HTTP en cada comando
|Cambios en API pueden romper CLI|Configuración adicional (API_BASE_URL)|Requiere infraestructura de servidor|Serialización/deserialización JSON
|Versionado de API debe considerarse|Debugging más complejo (dos procesos)|No funciona offline|Posibles timeouts y reintentos

</div>

### Costo total de propiedad (TCO)

<div align=center>

||CLI HTTP (reuso)|CLI Standalone (reimplementación)|
|-|-|-|
Desarrollo inicial|2.5h|8h
Mantenimiento/año|2h (cambios sincronizados con API)|4h (cambios duplicados con backend)
Complejidad despliegue|Alta (servidor + CLI)|Baja (solo ejecutable)
Dependencias externas|FastAPI corriendo|Solo PostgreSQL
TCO a 3 años|8.5h + infraestructura servidor|20h + sin infraestructura adicional

</div>

**Punto de equilibrio:** ~5 años si mantenimiento es similar.

## El valor oculto de la reimplementación

### Beneficios de reimplementación deliberada

**CLI Standalone NO reusa código, pero gana:**

<div align=center>

|Independencia arquitectónica|Simplicidad operacional|Portabilidad máxima|Performance óptimo|
|-|-|-|-|
|Sin dependencias de servidor HTTP|Usuario solo ejecuta comando|Distribuible como ejecutable único (PyInstaller)|Sin latencia de red
|Evolución independiente del backend|Sin configuración de servidores|Funciona offline (solo requiere DB local)|Acceso directo a DB
|Decisiones técnicas propias|Debugging simple (un solo proceso)|Instalación trivial|Sin overhead de serialización

</div>

### Caso de uso real: Herramienta de migración de datos

**Escenario:** Script para migrar datos de sistema legacy a pySigHor.

<div align=center>

|Opción 1 - CLI HTTP|Opción 2 - CLI Standalone|
|-|-|
|Requiere FastAPI corriendo|Acceso directo a DB|
|10,000 registros → 10,000 llamadas HTTP|10,000 registros → 1 transacción batch|
|Tiempo: ~30 minutos (latencia + serialización)|Tiempo: ~2 minutos (sin latencia)|
|Punto de falla: Si API cae, migración incompleta|Robusto: Transacción atómica|

</div>

**En este caso:** Reimplementación es **15x más rápida** y **más confiable**.

## Matriz de decisión: ¿Reusar o reimplementar?

### Criterios de decisión

<div align=center>

|Criterio|Favorece Reuso|Favorece Reimplementación|
|-|-|-|
|**Tiempo disponible**|Bajo (días)|Alto (semanas)|
|**Presupuesto**|Limitado|Suficiente|
|**Portabilidad requerida**|Baja|Alta|
|**Usuario objetivo**|Técnico|No técnico|
|**Infraestructura disponible**|Servidor existe|Solo endpoint (DB)|
|**Frecuencia de cambios**|Backend estable|Backend cambia mucho|
|**Performance crítico**|No|Sí|
|**Offline capability**|No requerido|Requerido|
|**Complejidad aceptable**|Alta|Baja|
|**Mantenimiento a largo plazo**|Centralizado preferido|Distribuido aceptable|

</div>

### Ejemplos de decisión

**Caso 1: Herramienta de administración interna**

- Usuario: Equipo técnico
- Infraestructura: Servidor FastAPI ya deployado
- Tiempo: Urgente (2 días)
- **Decisión:** CLI HTTP (reuso)

**Caso 2: Herramienta de instalación para clientes**

- Usuario: Administradores de universidad (no técnicos)
- Infraestructura: Solo PostgreSQL disponible
- Tiempo: No urgente (2 semanas)
- **Decisión:** CLI Standalone (reimplementación)

**Caso 3: Script de migración batch**

- Performance: Crítico (millones de registros)
- Offline: Requerido (migración en mantenimiento)
- Tiempo: Moderado (1 semana)
- **Decisión:** CLI Standalone (reimplementación)

**Caso 4: Prototipo de validación**

- Objetivo: Validar análisis RUP
- Tiempo: Muy limitado (horas)
- Infraestructura: Servidor de desarrollo
- **Decisión:** CLI HTTP (reuso)

## La lección metodológica fundamental

### Lo que RUP garantiza

**Reuso de análisis (100%):**

Independientemente de si reusas o reimplementas código:

- Las responsabilidades MVC son las mismas
- Los casos de uso no cambian
- El modelo del dominio es válido
- Los diagramas de colaboración aplican

**El análisis es la inversión permanente.** El diseño y código son **tácticos** y se ajustan según contexto.

### Lo que RUP NO garantiza

**Reuso de código (variable):**

RUP no dice que debas reusar código. Dice que **puedes elegir** basándote en:

- Compromisos técnicos
- Restricciones de tiempo
- Requisitos no funcionales
- Contexto de despliegue

**La decisión de reusar vs reimplementar es de DISEÑO, no de ANÁLISIS.**

### La ecuación del valor

```
Valor de RUP = (Inversión en análisis riguroso) × (Número de implementaciones)
```

**Sin RUP:**

- Implementación 1 (React): 100h (análisis + código)
- Implementación 2 (Angular): 100h (re-análisis + código)
- Implementación 3 (CLI): 100h (re-análisis + código)
- **Total:** 300h

**Con RUP:**

- Análisis único: 40h
- Implementación 1 (React): 60h (solo código)
- Implementación 2 (Angular): 60h (solo código)
- Implementación 3 (CLI HTTP): 3h (reuso)
- Implementación 4 (CLI Standalone): 8h (reimplementación deliberada)
- **Total:** 171h

**Ahorro:** 43% en 4 implementaciones (129h)

**Y cada nueva implementación incrementa el ROI.**

## Estrategias híbridas: Lo mejor de ambos mundos

### Estrategia 1: Reuso progresiva

**Fase 1:** CLI HTTP (reuso rápida)

- Tiempo: 2.5h
- Objetivo: Validar análisis y obtener feedback rápido

**Fase 2:** CLI Standalone (reimplementación dirigida)

- Tiempo: +8h
- Objetivo: Portabilidad y distribución a usuarios finales
- **Reusa:** Lógica de negocio validada en Fase 1

**Beneficio:** Validación rápida + producto final robusto

### Estrategia 2: Librería compartida

**Crear librería Python común:**

```
pysighor-core/
├── services/       # Lógica de negocio
├── repositories/   # Acceso a datos
└── models/         # Entidades

Consumida por:
- FastAPI backend
- CLI Standalone
- Scripts de migración
```

**Beneficio:**

- Reuso de control + entity
- Independencia de boundary (API vs CLI)
- Mantenimiento centralizado de lógica de negocio

### Estrategia 3: Arquitectura de plugins

**CLI con arquitectura extensible:**

```python
# Core CLI
pysighor_cli/
├── core/           # Comandos base
└── plugins/
    ├── http/       # Plugin que consume API
    └── direct/     # Plugin con acceso directo a DB

# Usuario elige en runtime
$ pysighor --backend=http login
$ pysighor --backend=direct login
```

**Beneficio:**

- Flexibilidad máxima
- Usuario decide según contexto
- Una sola base de código con múltiples backends

## Conclusión

La dicotomía "reusar vs reimplementar" es una **falsa dicotomía**:

1. **Siempre se reusa el análisis** - Esta es la promesa de RUP
2. **A veces se reusa el código** - Decisión de diseño según contexto
3. **Ambas opciones son válidas** - Depende de compromisos específicos

**La metodología RUP:**

- Garantiza reuso de análisis (inversión permanente)
- Permite flexibilidad en reuso de código (decisión táctica)
- Habilita múltiples implementaciones sin re-análisis

**El experimento CLI demuestra:**

- Reuso (CLI HTTP): 2.5h, dependiente, rápido
- Reimplementación (CLI Standalone): 8h, independiente, robusto
- **Análisis sin cambios en ambos casos:** Validación exitosa de RUP

**La lección final:**

> No preguntes "¿Debo reusar código?". Pregunta:
>
> - ¿Qué compromisos estoy asumiendo?
> - ¿Qué requiere este contexto específico?
> - ¿Qué maximiza el valor a largo plazo?
>
> **El análisis RUP te da la libertad de elegir la respuesta correcta para cada caso.**

## Referencias

- [Artículo principal](README.md)
- [Contexto del experimento](contexto.md)
- [Evidencia de implementación](evidencia.md)
- [Comparativa de arquitecturas CLI](comparativa-arquitecturas-cli.md)
- [Artículo 015: Dashboards multi-stack](../015-dashboards-multistack-validacion-experimental/)
