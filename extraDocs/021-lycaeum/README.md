# LYCAEUM — Bitácora de Sesión 01
**Fecha:** 7 de marzo de 2026  
**Proyecto:** pySigHor  
**Participantes:** Manuel (operador), Claude (orquestador), Opencode/GLM-4.6 (análisis técnico), Gemini (análisis pedagógico/estratégico), Qwen (contrargumentación)

---

## Contexto previo: de bundungún a LYCAEUM

La sesión surge de una discusión conceptual sobre la diferencia entre un **pipeline** y un **agente**. bundungún — el sistema original de Manuel, un bash script que lanza cuatro CLIs en un grid de Terminator — fue identificado como orquestador estático: los cuatro nodos responden al mismo prompt, el flujo es rígido, y la topología no cambia en tiempo de ejecución.

La pregunta que abrió el diseño: *¿y si designamos un jefe que decida a quién delegar y con qué instrucción?*

Eso derivó en la arquitectura **blackboard pattern**: un directorio compartido donde el orquestador escribe tareas y los subordinados escriben respuestas, con un estado global en `blackboard.md`.

---

## Diseño del sistema

### Estructura de archivos
```
~/misRepos/pysighor/_LYCAEUM/
  CLAUDE.md              ← instrucciones del orquestador
  contexto_opencode.md   ← rol y protocolo para Opencode
  contexto_gemini.md     ← rol y protocolo para Gemini
  contexto_qwen.md       ← rol y protocolo para Qwen
  task_opencode.md       ← tarea activa para Opencode
  task_gemini.md         ← tarea activa para Gemini
  task_qwen.md           ← tarea activa para Qwen
  response_opencode.md   ← respuesta de Opencode
  response_gemini.md     ← respuesta de Gemini
  response_qwen.md       ← respuesta de Qwen
  blackboard.md          ← estado global y resumen de rondas
  sintesis_rondaN.md     ← síntesis final por ronda
```

### Roles asignados
| Agente | Especialidad |
|---|---|
| Claude Code | Orquestador: descompone, delega, sintetiza |
| Opencode (GLM-4.6 / z.ai) | Análisis técnico, arquitectura, código |
| Gemini | Análisis amplio, perspectiva pedagógica/estratégica |
| Qwen | Contrargumentación, detección de inconsistencias lógicas |

### Protocolo de ronda
1. El orquestador lee el repo y el objetivo
2. Escribe `task_*.md` para cada agente con instrucción específica
3. Manuel entrega las tareas manualmente (modo mensajero)
4. Los agentes escriben sus `response_*.md`
5. El orquestador lee, triangula y actualiza el `blackboard.md`
6. Si hay resolución: síntesis final. Si no: nueva ronda (máx. 5)

---

## Sesión en el trabajo (primera ejecución)

### Objetivo
Analizar el estado actual del proyecto pySigHor y proponer los próximos pasos de desarrollo más prioritarios.

### Comportamiento del orquestador
Claude Code leyó el repo, detectó el estado de la Iteración 1, y delegó tres ángulos distintos:
- Opencode: dependencias técnicas y viabilidad de la secuencia de iteraciones
- Gemini: enfoque metodológico RUP y momento del testing
- Qwen: cuestionamiento de los supuestos implícitos de la ruta planificada

**Hallazgo destacado de Qwen:** detectó que `Programa` no aparece en ninguna iteración planificada pero `Curso` depende de él — gap en el modelo de dominio no señalado en ningún prompt.

### Síntesis del orquestador
Convergencia de los tres agentes en: adelantar `generarHorario()` a iteración 3 (no dejarlo para el final), atacar la deuda técnica de auth antes de Iteración 2, y resolver el gap de `Programa`.

---

## Sesión en casa (segunda ejecución, misma tarde)

### Diferencia respecto a la primera sesión
El orquestador leyó el repo más a fondo (git log, código real de auth.py, modelos, frontend) antes de escribir las tareas. Las instrucciones resultantes fueron significativamente más precisas.

### Hallazgos de los agentes

**Opencode:** Leyó código real — `auth.py`, modelos, repositorios, frontend. Identificó credenciales hardcodeadas y usuario sin BD como bloqueantes reales. Validó la secuencia de iteraciones como técnicamente correcta. Detectó que `edificio.py` ya existía en los modelos.

**Gemini:** Leyó `reflexionesAlgoritmo.md` (ingeniería inversa del legacy) — archivo que ningún otro agente tocó. Construyó tabla de valor didáctico por entidad. Propuso narrativa "La Búsqueda del Horario Perfecto". Recomendó introducir testing en Iteración 2 (Edificios) como terreno simple antes de llegar a complejidad de Profesores y `generarHorario()`.

**Qwen:** Verificó `RUP/README.md` contra `RUP/03-desarrollo/` para confirmar la inconsistencia del dashboard. Detectó tres tensiones reales: (1) RUP vs. velocidad, (2) dashboard inconsistente, (3) usuario hardcodeado. Generó hallazgo autónomo: ausencia de **Definition of Done** explícito por CdU — sin ese criterio, el dashboard siempre va a mentir por olvido.

### Correcciones previas a la síntesis
Antes de pedir síntesis al orquestador, Manuel aportó dos correcciones de contexto:
1. Qwen asumió 5 CdU implementados; el dato real era 8, todos con ruta RUP completa.
2. La repetición de CRUDs entre iteraciones es intencional — el objetivo pedagógico es que el alumno interiorice que cualquier dominio se factoriza en operaciones elementales. La "fatiga de CRUD" señalada por Gemini es el mecanismo de aprendizaje, no un problema.

### Síntesis del orquestador
El orquestador aplicó las correcciones con precisión: invalidó la motivación de Gemini (fatiga) pero preservó sus argumentos válidos (tabla de complejidad, testing en Iteración 2). Identificó el disenso real sobre el momento de `generarHorario()` y lo presentó como decisión de Manuel, no como conclusión del panel.

**Acciones resultantes:**

| Orden | Acción | Bloqueante de |
|---|---|---|
| 0-A | Corregir dashboard (8 CdU a ✅) | Integridad documental |
| 0-B | Diseño mínimo Edificios (4 diagramas de secuencia) | Coherencia RUP antes de codificar |
| 1 | Migrar auth hardcodeada → BD real | Todo lo que venga después |
| 2 | Iteración 2: Edificios + tests Pytest | Iteraciones 3+ |

---

## Ejecución de acciones

### Acción 0-A: Corrección del dashboard
Claude Code la ejecutó directamente (no delegó). Antes de modificar, verificó `RUP/03-desarrollo/` para confirmar el número exacto de CdU — y corrigió el dato de Manuel: eran 5, no 8. El orquestador corrigió al jefe.

**Observación sobre delegación:** para tareas de edición de ficheros simples, Claude Code ejecuta sin delegar. Comportamiento correcto.

### Acción 0-B: Diseño mínimo para Edificios
Claude Code la ejecutó directamente. Leyó los `.puml` de Aulas para replicar el formato exacto, leyó el análisis de `eliminarEdificio` para la restricción de integridad referencial, y produjo los cuatro diagramas de secuencia sin inventar convenciones nuevas.

### Acción 1: Migración de autenticación
Claude Code entró en **plan mode** antes de tocar nada. Exploró 301 tool uses · 48.7k tokens antes de escribir el plan. El plan fue presentado para aprobación antes de ejecutar.

**Aspectos destacados del plan:**
- Detectó que el proyecto usa synchronous SQLAlchemy (no async) y replicó el patrón exactamente
- Respetó el naming convention del proyecto (español en service/router, inglés en repository)
- El seed del admin es idempotente (comprueba existencia antes de insertar)
- Alcance explícito: roles, CRUD de usuarios y refresh tokens diferidos hasta que haya un caso de uso diseñado

**Verificación completa:**
- Login admin/admin → 200 + token JWT ✅
- verify-token → `{"username": "admin"}` ✅
- Credenciales incorrectas → 401 ✅
- Tabla usuarios en BD con registro `(1, 'admin', 1)` ✅

---

## Observaciones sobre el sistema

### Lo que funcionó bien
- El orquestador lee el repo de verdad antes de delegar — no inventa contexto
- Las tareas diferenciadas por ángulo producen respuestas genuinamente distintas y complementarias
- La triangulación de respuestas detecta cosas que ningún agente individual habría señalado (gap de `Programa`, DoD, inconsistencia dashboard)
- Claude Code distingue qué ejecutar él mismo vs. qué delegar (aunque con sesgo hacia ejecución propia en tareas de código)

### Lo que requiere ajuste
- **Delegación de código:** Claude Code no delega tareas de implementación aunque podría. Para forzar delegación en código de producción, añadir al CLAUDE.md: *"Tareas de creación o modificación de ficheros de producción se delegan siempre a los agentes especializados."*
- **Gemini y la escritura de archivos:** En las dos sesiones, Gemini respondió en chat pero no escribió `response_gemini.md` automáticamente. Requiere instrucción explícita: *"escribe tu respuesta en `_LYCAEUM/response_gemini.md`"*
- **Auto-compact en tareas largas:** La Acción 1 activó compactación en medio del plan mode. El sistema sobrevivió (el plan estaba escrito), pero es un riesgo en tareas de alta densidad de tokens.

### Pendiente de implementar
- **Definition of Done por CdU** — criterio explícito para marcar completado en el dashboard (hallazgo de Qwen)
- **Automatización del transporte** — `inotifywait` + keystroke para eliminar el rol de mensajero manual (Fase 2 del sistema)
- **Regla de delegación de código** en CLAUDE.md

---

## Commits de la sesión
```
LYCAEUM: ronda 1 completa - análisis estado pySigHor
LYCAEUM 0-A/0-B: dashboard actualizado + diseño mínimo Edificios (pre-it2)
LYCAEUM Acción 1: migrar auth hardcodeada a BD real - prereq Iteración 2
```

---

## Estado del proyecto al cierre de sesión
- Iteración 1: ✅ completa (auth + CRUD Aulas)
- Dashboard: ✅ actualizado
- Diseño Edificios: ✅ listo en RUP/02-diseño/
- Autenticación: ✅ migrada a BD real
- **Siguiente paso:** Iteración 2 — CRUD Edificios + tests Pytest