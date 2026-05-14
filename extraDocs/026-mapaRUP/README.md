# Artículo 026: Mapa RUP - Disciplinas, actividades y artefactos concretos

## ¿Por qué?

En ingeniería de software se enseña RUP como proceso amén de los principios de diseño. La aproximación es teórica, y se echa en falta un mapa que conecte "cuándo se hace qué" con "qué sale de ahí". 

Este documento responde a preguntas concretas:

- ¿Cómo conecta todo?
- ¿En qué momento del proceso se toman decisiones tecnológicas?
- ¿Cuándo diseño las tablas de la base de datos?
- ¿Cuándo hago el diagrama de arquitectura?
- ¿Cuándo defino los endpoints de la API?

pySigHor es un proyecto donde cada disciplina RUP produjo artefactos reales, en orden, con trazabilidad. Este artículo mapea ese recorrido.

## ¿Qué?

### Las 6 disciplinas RUP y su orden de aparición en pySigHor

RUP no es lineal, pero en un proyecto real las disciplinas tienen un orden natural de primera aparición. Este es el orden que siguió pySigHor:

```
1. Modelado del Negocio        <- ¿De qué habla el sistema?
2. Requisitos                  <- ¿Qué debe hacer el sistema?
3. Análisis y Diseño           <- ¿Cómo se estructura la solución?
4. Implementación              <- ¿Cómo se traduce a código?
5. Pruebas                     <- ¿Funciona lo que se construyó?
6. Despliegue                  <- ¿Cómo llega al usuario?
```

Cada disciplina se cruza transversalmente con las fases RUP (Inicio, Elaboración, Construcción, Transición), pero lo que interesa aquí es: **qué artefacto concreto se produjo en cada disciplina, dónde está, y qué pregunta responde**.

### Vista general del recorrido

```
Disciplina                      Artefacto pySigHor                             Respuesta a
---------------------------------------------------------------------------------------------------------
Modelado del Negocio      -->   modelo-dominio.puml                       -->  ¿De qué habla el sistema?
Requisitos                -->   actores-casos-uso.puml                    -->  ¿Quién usa qué?
Requisitos                -->   diagrama-contexto.puml                    -->  ¿Qué puede hacer el actor?
Requisitos                -->   especificacion.puml (x30)                 -->  ¿Cómo es cada caso de uso?
Requisitos                -->   prototipo.puml (x30)                      -->  ¿Qué ve el usuario?
Análisis                  -->   colaboracion.puml (x30)                   -->  ¿Qué clases participan?
Análisis                  -->   secuencia.puml (análisis)                 -->  ¿En qué orden interactúan?
Diseño                    -->   arquitectura.puml                         -->  ¿Qué stack tecnológico?
Diseño                    -->   clases-diseño.puml                        -->  ¿Cómo se mapean las clases?
Diseño                    -->   configuracion-proyecto.md                 -->  ¿Cómo se estructura el código?
Diseño                    -->   secuencia.puml (diseño, x10)              -->  ¿Qué endpoints/api calls?
Implementación            -->   routers/models/services/repos             -->  El código ejecutable
Implementación            -->   React components + pages                  -->  La interfaz ejecutable
Pruebas                   -->   tests/conftest.py + test_*.py             -->  ¿Funciona?
Control de Calidad        -->   auditoria.md + seguimiento.md             -->  ¿El código cumple el diseño?
---------------------------------------------------------------------------------------------------------
```

## ¿Para qué?

### Para responder "¿cuándo hago X?"

| Pregunta del alumno | Disciplina RUP | Actividad | Artefacto pySigHor |
|---|---|---|---|
| ¿Cuándo diseño las tablas de la BD? | Diseño | Diseño de datos | [`configuracion-proyecto.md`](../../RUP/02-diseño/configuracion-proyecto.md) sección "Esquema de base de datos" |
| ¿Cuándo hago el diagrama de arquitectura? | Diseño | Diseño arquitectónico | [`arquitectura.puml`](../../RUP/02-diseño/arquitectura.puml) |
| ¿Cuándo defino los endpoints? | Diseño | Diseño de componentes | [`secuencia.puml`](../../RUP/02-diseño/casos-uso/abrirAulas/README.md) por caso de uso |
| ¿Cuándo decido la tecnología? | Diseño (Elaboración) | Decisión arquitectónica | [`README.md de diseño`](../../RUP/02-diseño/README.md) sección "Stack tecnológico" |
| ¿Cuándo hago el modelo del dominio? | Modelado del Negocio | (Primera actividad) | [`modelo-dominio.puml`](../../RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) |
| ¿Cuándo identifico actores y casos de uso? | Requisitos | Encontrar actores y CdU | [`actores-casos-uso.puml`](../../RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) |
| ¿Cuándo detallo un caso de uso? | Requisitos | Detallar casos de uso | [`especificacion.puml`](../../RUP/00-casos-uso/02-detalle/abrirAulas/README.md) (diagrama de estados) |
| ¿Cuándo hago prototipos? | Requisitos | Prototipar IU | [`prototipo.puml`](../../RUP/00-casos-uso/02-detalle/abrirAulas/README.md) (wireframes Salt) |
| ¿Cuándo hago el análisis MVC? | Análisis | Análisis de casos de uso | [`colaboracion.puml`](../../RUP/01-analisis/casos-uso/abrirAulas/README.md) |
| ¿Cuándo diseño la API REST? | Diseño | Diseño de componentes | Diagramas de secuencia de diseño |
| ¿Cuándo escribo código? | Implementación | Implementación | [`backend/app/`](../../backend/app/) + [`frontend/src/`](../../frontend/src/) |
| ¿Cuándo hago pruebas? | Pruebas | Pruebas de integración | [`backend/tests/`](../../backend/tests/) |
| ¿Cuándo verifico que el código cumple el diseño? | Control de calidad | Revisión técnica | [`auditoria.md`](../024-auditoria-diseno-vs-implementacion/auditoria.md) |

### Para conectar IDSW1 e IDSW2 con un caso de estudio real

| Asignatura | Tema | Sección del temario | Artefacto pySigHor |
|---|---|---|---|
| IDSW1 | RUP: visión general | [`00002-rup.md`](https://github.com/mmasias/idsw1/blob/main/temario/00002-rup.md) | [`RUP/README.md`](../../RUP/README.md) - dashboard de 30 casos de uso x 6 disciplinas |
| IDSW1 | Disciplina de requisitos | [`00003-disciplinaDeRequisitos.md`](https://github.com/mmasias/idsw1/blob/main/temario/00003-disciplinaDeRequisitos.md) | Toda la sección [`RUP/00-casos-uso/`](../../RUP/00-casos-uso/README.md) |
| IDSW1 | Modelo del dominio | [`00004-MdD.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00004-MdD.md) | [`modelo-dominio.puml`](../../RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) |
| IDSW1 | Encontrar actores y CdU | [`00006-CdU.eAyCdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00006-CdU.eAyCdU.md) | [`actores-casos-uso.puml`](../../RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) + [`diagrama-contexto.puml`](../../RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) |
| IDSW1 | Priorizar CdU | [`00007-CdU.PCdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00007-CdU.PCdU.md) | [`99-seguimiento/`](../../RUP/99-seguimiento/README.md) - iteraciones planificadas |
| IDSW1 | Detallar CdU | [`00008-Cdu.dCdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00008-Cdu.dCdU.md) | [`02-detalle/<nombre>/especificacion.puml`](../../RUP/00-casos-uso/02-detalle/README.md) (x30 casos) |
| IDSW1 | Prototipar CdU | [`00009-CdU.ICdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00009-CdU.ICdU.md) | [`02-detalle/<nombre>/prototipo.puml`](../../RUP/00-casos-uso/02-detalle/README.md) (wireframes Salt) |
| IDSW1 | Estructurar modelo CdU | [`00010-eCdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00010-eCdU.md) | Relaciones `<<include>>` en diagramas de colaboración de análisis |
| IDSW2 | Clasificación de clases | [`01-estrategiasClasificacion.md`](https://github.com/mmasias/idsw2/blob/main/temario/01-dise%C3%B1o/01-estrategiasClasificacion.md) | Estereotipos Boundary/Control/Entity en [`análisis`](../../RUP/01-analisis/casos-uso/README.md) |
| IDSW2 | Relaciones entre clases | [`02-relacionesClases.md`](https://github.com/mmasias/idsw2/blob/main/temario/01-dise%C3%B1o/02-relacionesClases.md) | [`clases-diseño.puml`](../../RUP/02-diseño/clases-diseño.puml) |
| IDSW2 | Cohesión y acoplamiento | [`cohesion.md`](https://github.com/mmasias/idsw2/blob/main/temario/02-dise%C3%B1oModular/cohesion.md) + [`acoplamiento.md`](https://github.com/mmasias/idsw2/blob/main/temario/02-dise%C3%B1oModular/acoplamiento.md) | Arquitectura por capas: repositorio -> servicio -> router en [`configuracion-proyecto.md`](../../RUP/02-diseño/configuracion-proyecto.md) |
| IDSW2 | SRP (S de SOLID) | [`SOLID_S.md`](https://github.com/mmasias/idsw2/blob/main/temario/03-dise%C3%B1oOO/SOLID_S.md) | Cada archivo tiene una responsabilidad: modelo, schema, repo, servicio, router |
| IDSW2 | DIP (D de SOLID) | [`SOLID_D.md`](https://github.com/mmasias/idsw2/blob/main/temario/03-dise%C3%B1oOO/SOLID_D.md) | `Depends(get_db)` y `Depends(get_current_user)` como inyección de dependencias en FastAPI |
| IDSW2 | ISP (I de SOLID) | [`SOLID_I.md`](https://github.com/mmasias/idsw2/blob/main/temario/03-dise%C3%B1oOO/SOLID_I.md) | Schemas separados: `XxxCreate`, `XxxUpdate`, `XxxResponse` por caso de uso |

## ¿Cómo?

### Cronología del proyecto: cada disciplina con sus artefactos

#### 1. Modelado del Negocio (Fase de Inicio)

**Pregunta que responde**: ¿De qué habla el sistema?

**Artefacto**: [`modelo-dominio.puml`](../../RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)

El modelo del dominio es lo primero que se produce. No habla de software, no habla de tecnología. Habla de entidades conceptuales del negocio universitario: Aula, Edificio, Curso, Profesor, Recurso, Programa, Horario y sus relaciones.

```
Aula "se ubica en" --> Edificio
Aula "tiene" --> Recurso
Profesor "dicta" --> Curso
Curso "pertenece a" --> Programa
Profesor "tiene" --> PreferenciaRecurso
```

**Conexión con IDSW1**: [`00004-MdD.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00004-MdD.md)

---

#### 2. Requisitos (Fase de Inicio + Elaboración)

**Pregunta que responde**: ¿Qué debe hacer el sistema?

##### Actividad 2.1: Encontrar actores y casos de uso

**Artefactos**:
- [`actores-casos-uso.puml`](../../RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) - identificación del actor Administrador y sus 30 casos de uso
- [`diagrama-contexto.puml`](../../RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) - diagrama de estados del actor: qué puede hacer y cómo navega

**Resultado**: 1 actor (Administrador), 30 casos de uso identificados y organizados en grupos funcionales.

**Conexión con IDSW1**: [`00006-CdU.eAyCdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00006-CdU.eAyCdU.md)

##### Actividad 2.2: Priorizar casos de uso

**Artefacto**: [`99-seguimiento/`](../../RUP/99-seguimiento/README.md) - dashboard visual que muestra qué casos se desarrollan en cada iteración

**Decisión**: Se priorizaron los casos de uso por complejidad creciente:
- Iteración 1: iniciarSesion + CRUD Aulas (vertical slice completo)
- Iteración 2: CRUD Edificios (referential integrity)
- Iteración 3+: Casos restantes

**Conexión con IDSW1**: [`00007-CdU.PCdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00007-CdU.PCdU.md)

##### Actividad 2.3: Detallar casos de uso

**Artefactos**: 30 directorios en [`02-detalle/`](../../RUP/00-casos-uso/02-detalle/README.md), cada uno con `especificacion.puml`

Cada caso de uso se detalla como un diagrama de estados que muestra la conversación actor-sistema paso a paso, usando vocabulario RUP puro ("el actor solicita...", "el sistema presenta...").

**Ejemplo**: [`abrirAulas/especificacion.puml`](../../RUP/00-casos-uso/02-detalle/abrirAulas/README.md)

**Conexión con IDSW1**: [`00008-Cdu.dCdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00008-Cdu.dCdU.md)

##### Actividad 2.4: Prototipar interfaz de usuario

**Artefactos**: 30 archivos `prototipo.puml` en [`02-detalle/`](../../RUP/00-casos-uso/02-detalle/README.md)

Wireframes tecnología-agnósticos usando la sintaxis Salt de PlantUML. No son pantallas de React ni de ninguna tecnología específica: son abstracciones de lo que el usuario ve.

**Ejemplo**: [`crearAula/prototipo.puml`](../../RUP/00-casos-uso/02-detalle/crearAula/README.md)

**Conexión con IDSW1**: [`00009-CdU.ICdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00009-CdU.ICdU.md)

##### Actividad 2.5: Estructurar modelo de casos de uso

**Artefacto**: Relaciones `<<include>>` y `<<extend>>` capturadas en los diagramas de análisis (colaboración)

Las relaciones entre casos de uso (crearAula incluye abrirAulas, editarAula extiende abrirAulas) se materializan en la disciplina de análisis mediante las colaboraciones MVC.

**Conexión con IDSW1**: [`00010-eCdU.md`](https://github.com/mmasias/idsw1/blob/main/temario/contenidos/00010-eCdU.md)

---

#### 3. Análisis (Fase de Elaboración)

**Pregunta que responde**: ¿Cómo se estructura la solución sin atarse a tecnología?

**Artefactos**: 30 directorios en [`01-analisis/casos-uso/`](../../RUP/01-analisis/casos-uso/README.md), cada uno con `colaboracion.puml`

##### Actividad 3.1: Análisis MVC de cada caso de uso

Se aplica sistemáticamente el patrón Boundary-Control-Entity a cada caso de uso:

```
Boundary (Vista)     --> Clases que interactúan con el actor
Control (Controlador) --> Coordinación de la lógica del caso de uso
Entity (Modelo)      --> Entidades del dominio y acceso a datos
```

Cada diagrama de colaboración muestra:
- Qué clases participan
- Qué responsabilidades tiene cada una
- Qué otros casos de uso se invocan (`<<include>>`)

**Ejemplo**: [`crearAula/colaboracion.puml`](../../RUP/01-analisis/casos-uso/crearAula/README.md)

##### Actividad 3.2: Identificación de patrones

Del análisis surgieron patrones recurrentes que se repiten por grupo de entidades:

| Patrón | Casos de uso | Característica |
|---|---|---|
| Apertura | abrirXxx() | Vista presenta lista, controlador coordina carga |
| "El delgado" | crearXxx() | Vista mínima, redirige a edición |
| "El gordo" | editarXxx() | Vista completa, sesión continua |
| Eliminación segura | eliminarXxx() | Confirmación + validación de dependencias |

**Conexión con IDSW2**: [`01-estrategiasClasificacion.md`](https://github.com/mmasias/idsw2/blob/main/temario/01-dise%C3%B1o/01-estrategiasClasificacion.md) - las estrategias de clasificación se ven en la decisión de qué estereotipo MVC asignar a cada clase.

---

#### 4. Diseño (Fase de Elaboración)

**Pregunta que responde**: ¿Cómo se materializa la solución en tecnología concreta?

##### Actividad 4.1: Selección tecnológica

**Artefacto**: [`README.md de diseño`](../../RUP/02-diseño/README.md) sección "Stack tecnológico"

Aquí es donde se decide: FastAPI + React + SQLite. Hasta este momento, ningún artefacto mencionaba tecnología. El modelo del dominio, los casos de uso y el análisis son tecnología-agnósticos.

**Conexión con artículo 003**: [`003-rup-independencia-tecnologica`](../003-rup-independencia-tecnologica/README.md) demuestra este principio con implementaciones paralelas.

##### Actividad 4.2: Diagrama de arquitectura

**Artefacto**: [`arquitectura.puml`](../../RUP/02-diseño/arquitectura.puml)

Muestra la estructura SPA + API REST + SQLite y la comunicación entre contenedores.

##### Actividad 4.3: Diagrama de clases de diseño

**Artefacto**: [`clases-diseño.puml`](../../RUP/02-diseño/clases-diseño.puml)

Traducción de las clases de análisis (Boundary/Control/Entity) a clases de diseño concretas:
- Entity --> SQLAlchemy models
- Control --> FastAPI routers + services
- Boundary --> React components

##### Actividad 4.4: Diseño de base de datos

**Artefacto**: [`configuracion-proyecto.md`](../../RUP/02-diseño/configuracion-proyecto.md) sección "Esquema de base de datos"

Aquí se definen las tablas, columnas, tipos, foreign keys y constraints. Responde a "¿cuándo diseño las tablas?" - en Diseño, no antes.

```
edificios: id, nombre, ubicacion, created_at, updated_at
aulas: id, nombre, capacidad, edificio_id (FK), created_at, updated_at
...
```

##### Actividad 4.5: Diseño detallado por caso de uso (diagramas de secuencia)

**Artefactos**: ~10 directorios en [`02-diseño/casos-uso/`](../../RUP/02-diseño/casos-uso/), cada uno con `secuencia.puml`

Los diagramas de secuencia de diseño muestran la interacción concreta con la tecnología:
- HTTP methods (GET, POST, PATCH, DELETE)
- Rutas de endpoints (`/api/v1/aulas`)
- Componentes React específicos
- Formatos de datos (JSON)

**Ejemplo**: [`iniciarSesion/secuencia.puml`](../../RUP/02-diseño/casos-uso/iniciarSesion/README.md)

**Conexión con IDSW2**: [`cohesion.md`](https://github.com/mmasias/idsw2/blob/main/temario/02-dise%C3%B1oModular/cohesion.md) y [`acoplamiento.md`](https://github.com/mmasias/idsw2/blob/main/temario/02-dise%C3%B1oModular/acoplamiento.md) - la separación en capas (router -> service -> repository) aplica directamente los principios de alta cohesión y bajo acoplamiento.

---

#### 5. Implementación (Fase de Construcción)

**Pregunta que responde**: ¿Cómo se traduce el diseño en código ejecutable?

##### Actividad 5.1: Estructura del proyecto

**Artefactos en código**:
- [`backend/app/models/`](../../backend/app/models/) - modelos SQLAlchemy (mapeo de Entity de análisis)
- [`backend/app/schemas/`](../../backend/app/schemas/) - esquemas Pydantic (contratos de API)
- [`backend/app/repositories/`](../../backend/app/repositories/) - acceso a datos
- [`backend/app/services/`](../../backend/app/services/) - lógica de negocio (mapeo de Control de análisis)
- [`backend/app/routers/`](../../backend/app/routers/) - endpoints REST (mapeo de Boundary de análisis)
- [`frontend/src/pages/`](../../frontend/src/pages/) - componentes de página (mapeo de Boundary de análisis)
- [`frontend/src/services/api.ts`](../../frontend/src/services/api.ts) - cliente HTTP

##### Actividad 5.2: Implementación iterativa

**Artefactos**: Documentación en [`03-desarrollo/casos-uso/`](../../RUP/03-desarrollo/casos-uso/)

Cada caso de uso implementado tiene su README con endpoints, flujo de datos, y curl de prueba.

##### Actividad 5.3: Control de calidad

**Artefactos**:
- [`024-auditoria-diseno-vs-implementacion/`](../024-auditoria-diseno-vs-implementacion/articulo.md) - auditoría formal de 20 desviaciones
- [`025-postAuditoria/`](../025-postAuditoria/README.md) - resolución y lecciones aprendidas

Este es un artefacto que no está en el temario de RUP pero que surge naturalmente: cuando un equipo distinto implementa, hay que verificar fidelidad al diseño.

**Conexión con IDSW2**:
- [`SOLID_S.md`](https://github.com/mmasias/idsw2/blob/main/temario/03-dise%C3%B1oOO/SOLID_S.md) - cada archivo tiene una responsabilidad
- [`SOLID_D.md`](https://github.com/mmasias/idsw2/blob/main/temario/03-dise%C3%B1oOO/SOLID_D.md) - `Depends(get_db)` como inversión de dependencia
- [`SOLID_I.md`](https://github.com/mmasias/idsw2/blob/main/temario/03-dise%C3%B1oOO/SOLID_I.md) - schemas segregados por caso de uso (Create, Update, Response)

---

#### 6. Pruebas (Fase de Construcción)

**Pregunta que responde**: ¿Funciona lo que se construyó?

**Artefactos**:
- [`backend/tests/conftest.py`](../../backend/tests/conftest.py) - fixtures async con BD en memoria
- [`backend/tests/test_auth.py`](../../backend/tests/test_auth.py) - pruebas de autenticación
- [`backend/tests/test_aulas.py`](../../backend/tests/test_aulas.py) - pruebas CRUD de aulas

---

### Resumen visual: de la pregunta al artefacto

```
"¿De qué va el sistema?"
  --> Modelo del dominio
  --> RUP/00-casos-uso/00-modelo-del-dominio/

"¿Qué puede hacer el usuario?"
  --> Actores y casos de uso + Diagrama de contexto
  --> RUP/00-casos-uso/01-actores-casos-uso/

"¿Cómo es cada funcionalidad paso a paso?"
  --> Especificación de caso de uso (diagrama de estados)
  --> RUP/00-casos-uso/02-detalle/<nombre>/

"¿Qué ve el usuario?"
  --> Prototipo de IU (wireframe)
  --> RUP/00-casos-uso/02-detalle/<nombre>/prototipo.puml

"¿Qué clases participan?"
  --> Diagrama de colaboración MVC
  --> RUP/01-analisis/casos-uso/<nombre>/

"¿Qué tecnología uso?"
  --> Decisión arquitectónica
  --> RUP/02-diseño/README.md (stack)

"¿Cómo se conectan los componentes?"
  --> Diagrama de arquitectura
  --> RUP/02-diseño/arquitectura.puml

"¿Cómo son las tablas de la BD?"
  --> Esquema de base de datos
  --> RUP/02-diseño/configuracion-proyecto.md

"¿Qué endpoints tiene la API?"
  --> Diagrama de secuencia de diseño
  --> RUP/02-diseño/casos-uso/<nombre>/secuencia.puml

"¿Cómo es el código?"
  --> Implementación
  --> backend/app/ + frontend/src/

"¿Funciona?"
  --> Pruebas
  --> backend/tests/

"¿El código cumple el diseño?"
  --> Auditoría
  --> extraDocs/024-auditoria-diseno-vs-implementacion/
```

## ¿Y ahora qué?

### Extensiones posibles

- **Diagrama visual del mapa**: Un PlantUML que muestre la cronología con flechas entre disciplinas y artefactos
- **Sección por iteración**: Mostrar qué disciplinas se activan en cada iteración RUP (no solo la primera aparición)
- **Código de ejemplo por conexión IDSW2**: Extraer fragmentos concretos que ilustren cada principio SOLID

### Vacíos identificados

| Disciplina | Estado | Observación |
|---|---|---|
| Modelado del Negocio | Completo | 1 modelo del dominio |
| Requisitos | Completo | 30 casos de uso detallados + prototipos |
| Análisis | Completo | 30 colaboraciones MVC |
| Diseño | Parcial | Arquitectura + clases + config + ~10 secuencias. Faltan ~20 |
| Implementación | Parcial | CRUD de 6 entidades + auth. Faltan relaciones y algoritmo core |
| Pruebas | Parcial | auth + aulas. Faltan el resto de entidades |
| Despliegue | Sin iniciar | No hay artefactos de despliegue |
| Control de Calidad | Un ciclo completo | Auditoría 024 + resolución 025 |

## Referencias

- **Repositorio pySigHor**: [github.com/mmasias/pySigHor](https://github.com/mmasias/pySigHor)
- **IDSW1 - Ingeniería de Software 1**: [github.com/mmasias/idsw1](https://github.com/mmasias/idsw1)
- **IDSW2 - Ingeniería de Software 2**: [github.com/mmasias/idsw2](https://github.com/mmasias/idsw2)
- **Dashboard RUP**: [`RUP/README.md`](../../RUP/README.md)
- **Auditoría diseño vs código**: [`extraDocs/024`](../024-auditoria-diseno-vs-implementacion/articulo.md)
