# Sesiones de vibeCoding con agentes: LYCAEUM

<div align=right>

|||||
|-|-|-|-|
|[🏠️](../README.md)|**Artículo**|[Contexto](contexto.md)|[Evidencia](evidencia.md)

</div>

## El Sistema

### Origen: de bundungún a LYCAEUM

**bundungún** era un script bash que lanzaba cuatro CLIs de IA en un grid de Terminator. Los cuatro respondían al mismo prompt, el flujo era rígido, y la topología no cambiaba en tiempo de ejecución. Era un *pipeline*, no un agente: el humano era el único nodo con capacidad de decisión.

La pregunta que abrió el diseño de LYCAEUM fue simple: *¿y si designamos un jefe que decida a quién delegar y con qué instrucción?*

La respuesta fue el **blackboard pattern**: un directorio compartido donde el orquestador escribe tareas y los subordinados escriben respuestas, con un estado global persistido en `blackboard.md`.

### Arquitectura

```
_LYCAEUM/
  CLAUDE.md              ← instrucciones del orquestador
  contexto_*.md          ← rol y protocolo de cada agente
  task_*.md              ← tareas activas (escritas por el orquestador)
  response_*.md          ← respuestas (escritas por los subordinados)
  blackboard.md          ← estado global y resumen de rondas
  sintesis_rondaN.md     ← síntesis final por ronda
```

**Roles:**

| Agente | Especialidad |
|---|---|
| Claude Code | Orquestador: descompone, delega, sintetiza |
| Opencode (GLM-4.6 / z.ai) | Análisis técnico, arquitectura, código |
| Gemini | Análisis amplio, perspectiva pedagógica/estratégica |
| Qwen | Contrargumentación, detección de inconsistencias lógicas |

### Protocolo de ronda

1. El orquestador lee el repo y el objetivo — **sin inventar contexto**
2. Escribe `task_*.md` para cada agente con instrucción diferenciada por ángulo
3. Manuel entrega las tareas manualmente (modo mensajero — Fase 1)
4. Los agentes escriben sus `response_*.md`
5. El orquestador lee, triangula y actualiza `blackboard.md`
6. Si hay resolución: síntesis final. Si no: nueva ronda (máx. 5)

---

## La Sesión Fundacional

### Objetivo planteado

> Analizar el estado actual del proyecto pySigHor y proponer los próximos pasos de desarrollo más prioritarios.

### Comportamiento del orquestador

Claude Code leyó el repo antes de delegar: `git log`, `auth.py`, modelos, repositorios, frontend, diagramas PlantUML existentes. Las tareas resultantes estaban fundamentadas en evidencia real, no en suposiciones.

Las tres tareas de Ronda 1 cubrieron ángulos genuinamente distintos:
- **Opencode**: dependencias técnicas entre entidades, escalabilidad de la arquitectura, secuencia de iteraciones
- **Gemini**: valor pedagógico diferencial por iteración, momento óptimo del testing, arco narrativo didáctico
- **Qwen**: cuestionamiento de los supuestos implícitos de la ruta planificada

### Hallazgos destacados por agente

**Opencode** leyó código real antes de responder. Detectó que `edificio.py` ya existía en los modelos — dato concreto que los otros dos no mencionaron. Validó la secuencia de iteraciones como técnicamente correcta.

**Gemini** leyó `reflexionesAlgoritmo.md` — el archivo de ingeniería inversa del legacy VB3.0 de 1998, que ningún otro agente tocó. Por eso pudo hablar con precisión sobre las fases del algoritmo, los pesos R1-R5 y los BitSets. Propuso estructurar las iteraciones como arco narrativo: *"La Búsqueda del Horario Perfecto"*.

**Qwen** verificó `RUP/README.md` contra `RUP/03-desarrollo/` para confirmar la inconsistencia del dashboard con sus propios ojos, no por la descripción del task. Generó un hallazgo autónomo no solicitado en ningún prompt: ausencia de **Definition of Done** explícito por CdU. Sin ese criterio, el dashboard siempre va a mentir por olvido, porque nadie sabe cuándo actualizar qué.

### Correcciones previas a la síntesis

Antes de pedir la síntesis, Manuel aportó dos correcciones de contexto:

1. **Corrección factual**: Qwen asumió 5 CdU implementados. El dato real era 8, todos con ruta RUP completa.
2. **Corrección pedagógica**: La repetición de CRUDs entre iteraciones es intencional. La *"fatiga de CRUD"* señalada por Gemini es el mecanismo de aprendizaje — el objetivo es que el alumno interiorice que cualquier dominio se factoriza en operaciones elementales.

### Síntesis del orquestador

El orquestador no limitó a resumir — triangulólas tres respuestas. Invalidó la motivación de Gemini (fatiga) pero preservó sus argumentos válidos. Identificó el disenso real sobre el momento de `generarHorario()` y lo presentó como decisión de Manuel, no como conclusión del panel.

**Acciones resultantes:**

| Orden | Acción | Tipo |
|---|---|---|
| 0-A | Corregir dashboard (8 CdU a ✅) | Higiene documental — inmediata |
| 0-B | Diseño mínimo Edificios (4 diagramas de secuencia) | Coherencia RUP — prerrequisito |
| 1 | Migrar auth hardcodeada → BD real | Bloqueante técnico — prerrequisito |
| 2 | Iteración 2: Edificios + tests Pytest | Desarrollo — siguiente paso |

---

## Ejecución de Acciones

### Comportamiento de delegación observado

Una pregunta crítica del sistema era: ¿cuándo decide el orquestador ejecutar él mismo vs. delegar a los subordinados?

**Acción 0-A** (editar un README): ejecutada directamente. Antes de modificar, verificó `RUP/03-desarrollo/` para confirmar el número exacto de CdU — y corrigió el dato de Manuel: eran 5, no 8. **El orquestador corrigió al jefe.**

**Acción 0-B** (diagramas de secuencia): ejecutada directamente. Leyó los `.puml` de Aulas para replicar el formato exacto, leyó el análisis de `eliminarEdificio` para la restricción de integridad referencial. Produjo los cuatro diagramas sin inventar convenciones.

**Acción 1** (migración de autenticación): ejecutada directamente, pero con un comportamiento diferente — entró en **plan mode** antes de tocar nada. Exploró el proyecto con 301 tool uses · 48.7k tokens antes de escribir el plan. El plan fue presentado para aprobación antes de ejecutar.

El orquestador no delegó código en ningún caso. El CLAUDE.md no contenía instrucción explícita sobre cuándo delegar vs. ejecutar, y Claude Code tiene sesgo natural hacia la ejecución propia. **Punto de mejora identificado para la siguiente iteración del sistema.**

### Migración de autenticación — detalles

El plan de la Acción 1 detectó y respetó:
- Patrón synchronous SQLAlchemy (no async) del proyecto
- Naming convention: métodos service/router en español, repository en inglés
- Seed idempotente del admin (comprueba existencia antes de insertar)
- Alcance mínimo: roles, CRUD de usuarios y refresh tokens diferidos hasta que haya un CdU diseñado

Verificación completa antes de cerrar:
- Login admin/admin → 200 + token JWT ✅
- verify-token → `{"username": "admin"}` ✅
- Credenciales incorrectas → 401 ✅
- Tabla usuarios en BD con registro `(1, 'admin', 1)` ✅

---

## Lecciones Aprendidas

### 1. El blackboard pattern funciona para proyectos reales

Los agentes leen el repo, no inventan contexto. Los hallazgos emergentes (gap de `Programa`, DoD, inconsistencia de dashboard) surgieron de la lectura real de artefactos, no de razonamiento abstracto. Eso es trazabilidad real, no apariencia de análisis.

### 2. La diferenciación de ángulos produce resultados genuinamente distintos

Dar a cada agente un rol y una pregunta distinta es la diferencia entre un panel y un eco. Qwen detectó cosas que Gemini y Opencode no detectaron precisamente porque su tarea era buscar fallos, no validar.

### 3. El orquestador corrige al humano

La corrección del número de CdU (Manuel dijo 8, eran 5) no fue un error menor. Demuestra que el sistema funciona como un segundo par de ojos sobre los propios datos del proyecto — incluso sobre los datos que aportó el operador.

### 4. El Definition of Done es un artefacto metodológico, no cosmético

El hallazgo de Qwen sobre la ausencia de DoD es transferible a cualquier proyecto: sin criterio explícito de qué significa *completado*, el dashboard siempre va a mentir por olvido. Esto aplica independientemente de si hay IA involucrada o no.

### 5. El auto-compact es un riesgo en tareas de alta densidad

La Acción 1 activó compactación en medio del plan mode tras 48.7k tokens de exploración. El sistema sobrevivió porque el plan ya estaba escrito, pero es un vector de fallo en tareas largas. Estrategia de mitigación: dividir tareas complejas en subtareas antes de llegar al límite de contexto.

---

## Estado del Sistema al Cierre de Sesión

**Pendiente de implementar:**
- Definition of Done por CdU (propuesto por Qwen, pendiente de artefacto formal)
- Regla de delegación de código en CLAUDE.md
- Automatización del transporte (Fase 2: `inotifywait` + keystroke)

**Próximo paso del proyecto:** Iteración 2 — CRUD Edificios + tests Pytest

---

## Conclusión

LYCAEUM demostró que la arquitectura blackboard con roles diferenciados produce análisis que ningún agente individual habría generado solo. La triangulación de perspectivas, la corrección mutua y la síntesis estructurada son propiedades emergentes del sistema, no de ninguno de sus nodos.

bundungún era cuatro voces al mismo tiempo. LYCAEUM es un panel con un presidente.