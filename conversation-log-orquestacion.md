# Registro de conversaciones -- pySigHor como orquestador/revisor

## Qué es este archivo

Este registro es distinto de `conversation-log.md` (que sigue viviendo en `main`, la narrativa metodológica del propio proyecto RUP de pySigHor). Aquí se documenta el **otro** rol que esta misma identidad (`Claude-pySigHor-<MÁQUINA>`) ejerce: orquestador/revisor de los proyectos hermanos `pyCelda` y `pySesion`, sin construir código propio de pySigHor.

Nace el 2026-08-30, extraído de `diseño-fastapi-react` -- las Conversaciones 50-54 vivían ahí por accidente de qué rama estaba abierta en el momento en que el rol de orquestador empezó (ver Conversación 50), no porque tuvieran relación con el port FastAPI/React de esa rama. Esta rama (`leConsultor`) parte de `main` en su lugar porque hereda los artículos completos de `extraDocs/999-leyes-proyecto/` y `extraDocs/0XX-*` (000 a 027) que el rol de orquestador necesita como fuente de criterio -- `diseño-fastapi-react` solo llega hasta el artículo 013, el punto donde se bifurcó de `main`. El rol de orquestador no necesita `backend/`/`frontend/` ni el resto del árbol de código de ninguna de las dos ramas -- por eso vive aparte, no como merge de ninguna.

La numeración de "Conversación N" continúa la que ya traían estas mismas conversaciones en `diseño-fastapi-react` (50 en adelante) -- no se renumeró para evitar perder la trazabilidad de lo ya referenciado en otros sitios (memoria, discussions cruzadas).

---

## Conversación 50: Orquestación cruzada con pyCelda -- UI de autoría Profesor, IDOR y despliegue
**Fecha**: 2026-08-22
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor)

### Contexto de la Sesión

Sesión sin trabajo directo sobre el código de `pySigHor` -- esta sesión operó como nodo orquestador/revisor del proyecto hermano `pyCelda` (`/home/manuel/misRepos/_PROYECTOS/pyCelda`, GitHub `mmasias/pyCelda`), coordinando con las sesiones `Claude-pyCelda` (constructora) y `Claude-Prometeus` (despliegue en el servidor de producción) vía `SendMessage`. Rol ya establecido en sesiones previas (ver memoria de proyecto): pyCelda construye, pySigHor verifica cada lote por fork independiente contra repo/ejecución real, Manuel decide cada merge y cada ciclo de despliegue.

### Desarrollo Principal

#### 1. **Cierre de la UI de autoría `Profesor` (issue #93 de pyCelda)**
Retomado el fleco que quedó abierto la sesión anterior: `AbrirGuia.tsx` del lado `Profesor` seguía en el esqueleto mínimo de la rebanada de calibración (18/08), con botones/campos hardcodeados "Fuera de alcance". Verificado que los wireframes de los 14 CU de `Profesor` ya existían completos -- transferencia de wireframe ya cerrado a pantallas reales, no decisión de diseño nueva. Reparto en 3 lotes (acciones directas sobre `Guia`; CRUD `PonderacionEvaluacion`; CRUD `ReferenciaBibliografica`), delegado por pyCelda a OpenCode, verificado por pySigHor con fork independiente en cada uno (diff real, `pytest`, `tsc`, tests reales de "profesor no dueño"). PRs #98/#99/#100 mergeados sin discrepancias de fondo.

#### 2. **Issue #96 -- IDOR del lado `Profesor`, resuelto intercalado por lote**
pyCelda encontró, al planificar, que el gap de pertenencia (mismo patrón que el issue #86 ya conocido) cubría también `Profesor`, más 2 endpoints sin autenticación en absoluto. Decisión de pySigHor, avalada por Manuel: en vez de posponer el fix hasta cerrar los 3 lotes, intercalarlo en el mismo PR que cada lote ya tocaba el fichero correspondiente -- razón: ya hay 30 `Profesor` reales en producción (a diferencia del precedente #86, un solo `DirectorGrado` de prueba).

#### 3. **Decisión de diseño en el camino: `sessionStorage` sobre `location.state`**
Para que `eliminarPonderacionEvaluacion()`/`eliminarReferenciaBibliografica()` (sin endpoint de backend por decisión previa) sobrevivan a la navegación entre pantallas, pyCelda propuso `location.state` de React Router; pySigHor detectó que es insuficiente porque el listado tiene saltos intermedios hacia Crear/Abrir que perderían el estado acumulado -- confirmado contra los wireframes antes de objetar. Adoptado `sessionStorage` keyed por `guiaId` en su lugar.

#### 4. **Fleco final: aterrizaje de `Profesor` tras login**
Al revisar la bitácora publicada, Manuel notó que faltaba verificar si `Profesor` aterrizaba en `mis-asignaturas-grado` tras iniciar sesión. Verificado que no -- gap real, documentado en el propio código como pendiente desde la rebanada de calibración. Cerrado por pyCelda en PR #102, verificado, mergeado, desplegado.

#### 5. **Despliegue en producción, dos ciclos**
Sin cambio de esquema de BD en ningún PR de la sesión (verificado explícitamente en cada uno -- criterio nuevo fijado por Manuel hoy: si algún PR futuro toca el modelo, el despliegue debe ser extraer datos reales→aplicar esquema→reimportar, no un recreate, para no perder los datos ya corregidos que ya están en producción). Claude-Prometeus desplegó primero el rango `eb91821`→`447032c` (PRs #97-#100) y después `447032c`→`f2576d2` (PR #102), ambos con `GET /api/health` OK verificado independientemente.

#### 6. **Bitácora de la sesión, discussion #101**
Publicada por pySigHor (mismo patrón que #90/#61), revisada por pyCelda y Prometeus con correcciones de precisión incorporadas. Incidente menor en el camino: el primer intento de publicación salió con el body roto (error de sintaxis `-f body=@fichero` en una mutación GraphQL cruda), detectado por Prometeus, corregido, peaje pagado en la discussion #84 ("fustigamiento", convención ya establecida del proyecto pyCelda) -- por los tres agentes, incluido pySigHor, por no haber caído en el gap del aterrizaje de `Profesor` hasta que lo notó Manuel.

#### 7. **Extra fuera de alcance de #93: doble identidad `DirectorGrado`/`Profesor` (PR #103)**
Manuel retomó, ya cerrada la bitácora inicial, un hallazgo aparcado desde el 19/08: qué pasa cuando una misma persona es `DirectorGrado` y también `Profesor` a la vez -- caso real en dev (`manuel.masias@uneatlantico.es` tiene fila en ambas tablas), no hipotético. Reflexión de arquitectura antes de construir: no era un `<<choice>>` que exigiera retroceso formal a Requisitos (como `semestreDefault`, discussion #72) -- mismo patrón ya cerrado en discussion #47/#48 (`abrirAsignaturasGrado()` como `<<extend>>` condicionado por rol, tercer punto de extensión, no CU nuevo). pySigHor redactó el fragmento de documentación (comentario en el diagrama de contexto + párrafo en el README del CU) y el brief técnico, se lo pasó a pyCelda como borrador. pyCelda lo verificó contra el `.puml` real antes de aplicar -- el estado `ASIGNATURAS_GRADO_ABIERTO` ya tenía dos entradas distintas desde discussion #47, confirmó que el edge nuevo reconectaba con el sentido *heredado* correcto y añadió un comentario aclaratorio de las tres entradas. PR #103 (`de41909`): `es_tambien_profesor` en `get_current_rol()`, enlace condicional en `Grados.tsx`, 127/127 tests, `tsc` limpio, sin tocar `models/` -- verificado por pySigHor sin fork, mergeado, desplegado por Prometeus en un tercer ciclo.

### Estado del Proyecto (pyCelda, no pySigHor)

- **Issue #93**: cerrado -- 3 lotes de UI `Profesor` en producción.
- **Issue #96**: cerrado -- IDOR de `Profesor` resuelto en los 3 lotes.
- **Issue #86**: sigue abierto -- IDOR del lado `DirectorGrado`, pendiente sin fecha.
- **PR #103**: cerrado -- doble identidad `DirectorGrado`/`Profesor`, hallazgo del 19/08 resuelto.
- **Pendiente sin fecha**: retroceso a Requisitos de `editarAsignaturaGrado()`; revisión manual de Manuel sobre el checklist reorganizado por actor de #93.
- **Producción**: `https://mmasias.cloud-ip.cc/` en `de41909`, health-check OK.

### Para Próxima Sesión

Sin tareas activas de `pySigHor` en sí -- el próximo trabajo de esta sesión, si lo hay, depende de que Manuel retome alguno de los pendientes de `pyCelda` listados arriba, o pida trabajo directo sobre este repositorio. Manuel indicó que la siguiente actividad será probar manualmente la UI usando el checklist reorganizado del issue #93.

---

## Conversación 51: Corrección de alcance de memoria, lecciones meta de orquestación, y tres ajustes de calentamiento en pyCelda antes de la revisión CRUD
**Fecha**: 2026-08-22
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor), Claude-pyCelda (constructora), Claude-Prometeus (despliegue)

### Contexto de la Sesión

Sin trabajo directo sobre código de `pySigHor`. Continuación del rol de orquestador/revisor de `pyCelda` (ver Conversación 50), con una corrección de arquitectura de memoria al inicio y tres ajustes menores de UI como calentamiento antes de que Manuel empiece la revisión profunda de CRUD sobre entidades diversas de `pyCelda`.

### Desarrollo Principal

#### 1. **Corrección de arquitectura de memoria multi-sesión**
Manuel corrigió que esta sesión venía guardando en su propio directorio de memoria (`~/.claude/projects/.../pysighor/memory/`, symlink real hacia `myClaudeContext/projects/.../pysighor/memory/`) hechos específicos de `pyCelda` -- error de alcance. La memoria de cada proyecto vive en el directorio de su propia sesión nombrada (`Claude-pyCelda`, `Claude-Prometeus`); pySigHor dirige vía `SendMessage`/`ListAgents`, no almacena. Entradas antiguas de pyCelda en la memoria de pySigHor quedaron marcadas como residuo pendiente de migrar, sin borrar sin más instrucción.

#### 2. **Vistazo puntual autorizado a la memoria de pyCelda -- extracción de lecciones meta de orquestación**
Manuel autorizó explícitamente, por única vez, revisar la memoria de la sesión `Claude-pyCelda` (`myClaudeContext/projects/.../pyCelda/memory/`) para extraer aprendizajes generalizables de orquestación, no hechos del proyecto. Cinco memorias nuevas guardadas en pySigHor: malla multi-sesión y no relay de autorización entre peers (`feedback_malla_multisesion_confirmacion_propia`), diseñar antes de delegar a un becario (`feedback_disenar_antes_de_delegar`), mecánica de invocación de OpenCode -- workdir explícito (`feedback_opencode_workdir_explicito`), calibrar el esfuerzo de verificación (`feedback_calibrar_verificacion`), y verificar el punto de entrada real de un flujo construido por lotes (`feedback_verificar_punto_entrada_flujo`).

#### 3. **Tres ajustes de UI en pyCelda, diseñados por pySigHor y delegados a Claude-pyCelda**
Como forma de "cuantificar el alcance" antes de la revisión CRUD profunda, Manuel propuso tres ajustes pequeños que ejercitan el mismo tipo de relaciones que la revisión va a tocar. Cada uno se trabajó leyendo el código real de `pyCelda` (no ocurrencias sin verificar), resolviendo ambigüedades de diseño antes de delegar (ver [[feedback_disenar_antes_de_delegar]]):

- **Ítem 1** -- `/grados/:id/guias` (`ConsultarEstadoGuias.tsx`): columnas `AsignaturaGrado`/`Profesorado`, hoy con placeholder literal "Fuera de alcance de esta rebanada", rellenas con datos reales. Decisión: sin columnas nuevas, nombre de asignatura sin fallback (ya resuelto de antes), profesorado en emails coma-separados con fallback "Sin profesorado asignado" -- aplicado también a `AsignaturasGrado.tsx`, que tenía el mismo bug de celda en blanco.
- **Ítem 2** -- `/grados/:id/guias/:id` (`AbrirGuia.tsx`): completar semestre y fecha de PDF (ya venían del backend, solo faltaba pintarlos), nombre/contenido de asignatura y tablas de resultados de aprendizaje/metodologías docentes (requería exponer `Guia.asignatura_grado` en el schema, un solo cambio resolvía las cuatro filas). `fecha_creacion` se quedó fuera de alcance -- no existe como columna, decisión de no meter migración ahora. Añadido en el camino: columna "Sistema de evaluación" mostraba el id crudo en vez de un nombre -- corregido a `tipo -- descripcion` (patrón ya existente en `CrearPonderacionEvaluacion.tsx`), mismo fix aplicado también en `PonderacionesEvaluacion.tsx` por tener el bug idéntico.
- **Ítem 3** -- `MisAsignaturasGrado.tsx`: un DirectorGrado que entra a ver sus asignaturas como Profesor no tenía forma de volver a `/grados`. Simétrico al botón ya existente en `Grados.tsx`, pero sin necesidad de campo nuevo de backend -- `SesionResponse.rol === "director_grado"` ya es señal suficiente porque `get_current_rol()` prioriza esa identidad de forma absoluta.

Cada ítem siguió el mismo ciclo: pySigHor diseña -> Claude-pyCelda construye -> pySigHor revisa contra `git diff` real (no autoinforme) -> Manuel decide commit/push -> pySigHor o Manuel avisa a Claude-Prometeus -> despliegue verificado. Hallazgos menores en la revisión del ítem 1+2: eager-load faltante en `PonderacionEvaluacionRepository.obtener()` (corregido), `uv.lock` untracked dejado fuera del commit. Extra por iniciativa de Claude-pyCelda, avalado sin revertir: mismo fix de nombre de sistema de evaluación aplicado también en `PonderacionEvaluacion.tsx` (pantalla de detalle individual).

#### 4. **Incidente de despliegue: frontend horneado dentro de la imagen `caddy`**
Tras el primer push (`3744a3d`, más `c517e80` corrigiendo un `Deploy:` trailer olvidado), Manuel reportó no ver ningún cambio en producción pese a `/api/health` en verde. Causa real, diagnosticada por Claude-Prometeus: el stack no tiene contenedor `frontend` propio -- el bundle se compila dentro de un multi-stage build de la imagen `caddy`, y el deploy anterior solo había reconstruido `backend`. En el camino, un primer intento de verificar con `grep` de una frase esperada dio falso positivo por ser substring de otra cadena ya existente; la señal decisiva fue comparar `docker inspect --created` del contenedor contra la fecha del commit. Resultado: nueva **Regla 5** en `DEPLOY.md` (reconstruir siempre `caddy` si el rango de commits toca `frontend/`), propuesta por Prometeus, avalada por pySigHor, confirmada por Manuel, y ya validada con éxito en el despliegue del ítem 3 (`36f2935`).

#### 5. **Corrección de estilo: español peruano, no voseo**
Manuel corrigió un uso de "vos" dirigido a él ("lo compartimos vos y yo") -- el usuario habla español peruano (tuteo), no rioplatense. Guardado como preferencia global de comunicación, no específica de proyecto.

### Estado del Proyecto (pyCelda, no pySigHor)

- Tres ajustes de UI en producción: columnas de guías del grado, detalle completo de guía + nombre de sistema de evaluación, botón "Ver mis grados". Commits `3744a3d`/`c517e80`/`36f2935` en `main`, desplegados y verificados (`/api/health` + verificación de bundle real).
- `DEPLOY.md`: nueva Regla 5 (reconstruir `caddy` si el diff toca `frontend/`), commit `1117b9c` de Prometeus, integrado sin conflicto por Claude-pyCelda.
- Pendientes sin fecha (heredados de Conversación 50, sin cambios esta sesión): issue #86 (IDOR `DirectorGrado`), retroceso a Requisitos de `editarAsignaturaGrado()`.
- Ciclo cerrado, sin pendientes de esta sesión -- felicitación cruzada de Manuel (vía pySigHor) a Claude-pyCelda y Claude-Prometeus.

### Para Próxima Sesión

Manuel inicia la revisión profunda de CRUD sobre entidades diversas de `pyCelda` -- los tres ajustes de esta sesión fueron calentamiento explícito para esa revisión (ejercitan las mismas relaciones `Guia`/`AsignaturaGrado`/`Profesor`/`SistemaEvaluacion` que la revisión va a tocar). Sin tareas activas de `pySigHor` en sí.

---

## Conversación 52: Bug real del issue #93 (fantasma de `vinculada=False`), fix en dos rondas, despliegue y reset de datos de producción
**Fecha**: 2026-08-22/23
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor), Claude-pyCelda (constructora), Claude-Prometeus (despliegue)

### Contexto de la Sesión

Continuación directa de la Conversación 51, misma sesión de pySigHor. Tras cerrar los tres ajustes de calentamiento, Manuel señaló el último comentario del issue #93 de `pyCelda` (2026-08-22T22:26, guía id=2) como el único error significativo detectado hasta entonces, y pidió que pySigHor lo entendiera antes de delegarlo.

### Desarrollo Principal

#### 1. **Diagnóstico del bug -- fantasma de ponderaciones/referencias "eliminadas"**
Manuel reportó: al eliminar una `PonderacionEvaluacion` y crear una nueva bajo el mismo `SistemaEvaluacion`, tras guardar el borrador la eliminada reaparecía -- en la vista de DirectorGrado se veían la antigua y la nueva a la vez, y si el Profesor volvía a guardar, la antigua reaparecía también en su propia vista. pySigHor diagnosticó la causa raíz contra el código real (no hipótesis): `PonderacionEvaluacion.vinculada` (y su gemela en `ReferenciaBibliografica`) estaba sobrecargado con dos significados -- "recién creada, pendiente" y "desvinculada" -- y `desvincular()` solo cambiaba el flag sin borrar la fila, así que `listar_pendientes_de()` la resucitaba para siempre en cualquier vista (`abrir_guia()` es el mismo endpoint para Profesor y DirectorGrado, sin filtrado por rol). Un segundo bug compuesto: `AbrirGuia.tsx` limpiaba la exclusión de `sessionStorage` tras guardar sin refrescar `guia.ponderaciones`, haciendo que la fila fantasma reapareciera de inmediato en la misma pantalla.

#### 2. **Fix en dos rondas, cada una revisada por pySigHor contra `git diff` real**
- **Ronda 1**: `desvincular()` pasó a borrar la fila de verdad (`db.delete`) en ambos repositorios; `AbrirGuia.tsx` re-fetchea la guía completa tras guardar en vez de spread parcial. 2 tests de regresión nuevos reproduciendo el caso exacto de Manuel.
- **Hallazgo intercalado por Claude-pyCelda, honesto y sin corregir por su cuenta**: un test ya existente documentaba la misma causa por otra puerta -- una ponderación nunca vinculada, excluida antes del primer guardado, tampoco se borraba (`sincronizar_ponderaciones()` solo miraba `vinculadas_actuales`, no el total de filas de la guía). pySigHor confirmó que era el mismo bug y, con Manuel, decidió corregirlo en el mismo encargo en vez de abrir issue aparte.
- **Ronda 2**: `sincronizar_ponderaciones()`/`sincronizar_referencias()` (`backend/app/models/guia.py`) recalculadas sobre `todas_las_de_la_guia - deseadas`, no solo lo ya vinculado -- válido porque el frontend siempre manda el conjunto completo de lo visible, nunca un delta parcial. Test viejo dividido en dos, más un test nuevo simétrico para `ReferenciaBibliografica`. 135 tests en verde.
- **Nota para la cola, no bloqueante**: ni `vincular()` ni `desvincular()` verifican que el id recibido pertenezca a la guía que se está guardando -- mismo patrón que #86/#96, hoy no explotable porque el frontend nunca manda ids ajenos, pendiente para cuando la revisión profunda de CRUD llegue a `Guia`/`PonderacionEvaluacion`/`ReferenciaBibliografica`.

#### 3. **Despliegue verificado en dos ciclos**
Commit `de9d0d5` en `main`, con `Deploy: estándar`. Claude-pyCelda exigió confirmación directa de Manuel para el push (no aceptó el relay de pySigHor como autorización -- disciplina de malla funcionando como se diseñó). Claude-Prometeus aplicó la Regla 5 (reconstruir `caddy` además de `backend`, por tocar frontend), y verificó no solo por timestamp de contenedor sino leyendo el código real dentro del contenedor (`self.db.delete(ponderacion)` confirmado en la línea exacta). `/api/health` OK, sin incidencias.

#### 4. **Reset de datos de producción para pruebas cruzadas**
Manuel, directamente con Claude-Prometeus (operación de datos, no de código -- no toca `main`): restauró la BBDD de producción a la copia post-fix de la normalización de Materias (`pycelda_backup_20260821_224155.db` -- 16 Materia, 55 AsignaturaGrado, 182 ResultadoAprendizaje reconciliado), verificando primero cuál de las dos copias disponibles era la correcta antes de restaurar. Backup de seguridad de la producción previa tomado antes de sobrescribir. Alta de `ibuprofeno@uneatlantico.es` como Profesor (id=31) en 4 asignaturas para pruebas cruzadas de doble identidad/pertenencia. Snapshot final guardado como `BBDD_DATOS_LIMPIOS_CON_IBUPROFENO.db`. Efecto intencional: se pierde el estado de pruebas manuales del 22-23 de agosto para empezar con datos limpios.

### Estado del Proyecto (pyCelda, no pySigHor)

- **Issue #93**: cerrado del todo -- 3 ajustes de UI + el bug de ponderaciones/referencias fantasma, en producción (`de9d0d5`).
- **Producción**: `https://mmasias.cloud-ip.cc/` en `de9d0d5`, con datos reseteados a la copia limpia post-normalización + Ibuprofeno como profesor de prueba.
- **Pendientes sin fecha (sin cambios esta sesión)**: issue #86 (IDOR `DirectorGrado`), retroceso a Requisitos de `editarAsignaturaGrado()`, la nota de pertenencia cruzada en `vincular()`/`desvincular()` señalada en el punto 2.
- **Próximo hito de Manuel**: mañana por la mañana, sesión dedicada solo a testing y debugging manual con los datos limpios -- explícitamente no delegado, tiempo de Manuel probando la UI real.

### Para Próxima Sesión

Sin tareas activas de `pySigHor` en sí. Cuando Manuel retome, probablemente traiga hallazgos concretos de su sesión de testing/debugging para que pySigHor los diagnostique (mismo patrón que el issue #93 de esta sesión: entender primero contra el código real, luego delegar con el diseño ya resuelto) antes de delegarlos a Claude-pyCelda.

---

## Conversación 53: Validación manual del checklist v0.4.0 de pyCelda -- tres PRs de seguridad/UI, delegación de capitanía a pySigHor
**Fecha**: 2026-08-25/26
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor/capitán), Claude-pyCelda-SDF1 (constructora), Claude-pyCelda-Prometeus (despliegue)

### Contexto de la Sesión

Sin trabajo directo sobre código de `pySigHor` -- continuación del rol de orquestador/revisor de `pyCelda`. Nota metodológica al arrancar: la última entrada de este log (Conversación 52, 2026-08-22/23) quedó desactualizada respecto al estado real de `pyCelda` -- entre esa fecha y hoy hubo trabajo sustancial (bloque Admin bottom-up completo 2026-08-24/25, issue #86 IDOR cerrado por código el 2026-08-25) registrado solo en la memoria de proyecto (`project_pycelda_transferencia_rup.md`), no en este archivo. Esta conversación no reconstruye ese hueco -- documenta solo lo trabajado en esta sesión, partiendo del estado ya reflejado en memoria.

### Desarrollo Principal

#### 1. **Validación manual del checklist v0.4.0, discussion [#131](https://github.com/mmasias/pyCelda/discussions/131)**
Manuel fue marcando en vivo (`[x]`/comentarios) el checklist redactado por pySigHor tras el cierre de PR #129 (#86). Bloque 1 (Admin): 5 ítems del checklist corregidos por error propio de redacción (backend completo con frontend deferido a propósito, no bugs); 1 hallazgo real sin fix todavía ("Volver al panel"/"cerrar sesión" ausente en pantallas hijas de Admin). Bloque 2 (flujo legítimo de Director): sin sorpresas, 2 ítems más corregidos por error de redacción (acciones que nunca fueron de `DirectorGrado`).

#### 2. **Convención nueva: editar comentarios de GitHub directamente, no solo responder**
Descubierto (confirmado por Manuel) que `gh` está autenticado como la cuenta propia de Manuel -- pySigHor puede editar (`updateDiscussionComment`) cualquier comentario de la discussion, incluidos los del propio Manuel. Adoptada como convención: comentario original se tacha línea a línea (nunca todo el bloque en un solo `~~...~~`, rompe el renderizado GFM a través de límites de bloque) y la explicación de resolución se publica como respuesta aparte (`replyToId`), no inline.

#### 3. **Ramillete 1: tres hallazgos menores -> PR #132 (`03c3024`)**
Mensaje de revocación de Guia invisible para el Profesor (property `comentario_revocacion` nueva, simétrica a `comentario_rechazo`), 409 de `eliminarResultadoAprendizaje()` sin indicar a qué está asociado (`nombres_asignaciones()` nuevo), tabla vestigial "Asignaturas del grado" en `Grado.tsx` (causa raíz: calco de `GradoAdmin.tsx`, esos botones nunca fueron capacidad de `DirectorGrado` -- confirmado contra `diagramaContextoAdmin.puml` vs `diagramaContextoDirectorGrado.puml`). Diseñados por pySigHor, construidos por pyCelda (fix 1 ella misma, 2/3 delegados a OpenCode), verificados por pySigHor en clon propio (diff+tests+tsc) antes de aprobar. Desplegado por Prometeus, health-check OK.

#### 4. **Bloque 3, falsa alarma de IDOR -- investigación disciplinada antes de tocar código**
Probando pertenencia cruzada con un segundo director real (`ibuprofeno@uneatlantico.es`, director del grado de prueba y también Profesor de una asignatura de GII), Manuel reportó que "editar semestre" y "revocar aprobación" de una Guia ajena parecían funcionar -- riesgo de que PR #129 tuviera un hueco. pySigHor no aceptó la alarma sin verificar: código revisado (`dirige()` limpio en ambos endpoints), consulta de solo lectura pedida a Prometeus contra producción (`grados_directores_grado` confirmó sin asociación cruzada), y crucialmente **se le pidió a Manuel repetir la prueba hasta el envío real del formulario**, no solo cargar la página -- ambas veces `404`. Diagnóstico correcto: no había escritura cruzada, el hallazgo real era que `AbrirGuia.tsx` decidía la UI de Director solo por la forma de la URL (`modoRevisor`), dejando ver formularios de acción a cualquiera con acceso de lectura legítimo como Profesor. Fix: `puede_revisar: bool` en `AbrirGuiaResponse` -> PR #133 (`02b5e2a`), verificado y desplegado igual que el anterior.

#### 5. **Hallazgo más grave: el mismo formulario cargaba sin sesión en absoluto (incógnito)**
Manuel probó `CrearResultadoAprendizaje` en ventana de incógnito -- también cargaba. Causa raíz, verificada por pySigHor: `App.tsx` no tenía **ningún** guard de sesión centralizado, las ~50 rutas eran `<Route>` sueltos; páginas sin llamada de lectura previa al montar no tenían nada que las protegiera. Manuel pidió explícitamente: arreglarlo, auditoría sistemática del resto de pantallas de Director, y dejarlo como regla de validación permanente. Encargo de 3 partes a pyCelda: `RequireSession` (componente de layout que verifica `GET /auth/me` antes de renderizar cualquier ruta protegida), auditoría de pertenencia de `Materia`/`AsignaturaGrado`/`ResultadoAprendizaje`/`Grado` (resultado: todo ya limpio, solo un hueco de test de regresión), y documentación de la regla en `RUP/04-desarrollo/README.md`. PR #134 (`e0b6629`), verificado (247 tests, `tsc`, `vite build`) y desplegado. Manuel confirmó personalmente en navegador real que el redirect funciona.

#### 6. **Delegación de capitanía completa a pySigHor**
Manuel autorizó directamente (a pyCelda y a Prometeus, sin relay) que pySigHor "capitanee" este hilo -- diseño, delegación, verificación, petición de merge y de despliegue -- sin pasar por él turno a turno, hasta que quede "resuelto y estabilizado". pyCelda inicialmente no incluyó el merge en el alcance registrado; Manuel lo corrigió explícitamente ("el merge también"). Prometeus, al ejecutar el segundo despliegue del hilo, precisó que no asume la misma extensión indefinida para su propio dominio sin confirmación directa de Manuel -- comportamiento correcto, no fricción, mismo principio de "ningún peer autoriza en nombre de otro" ya establecido.

#### 7. **Incidente operativo menor: working tree compartido**
pySigHor verificó PR #132 y #133 haciendo `git checkout`/`diff` sobre `~/misRepos/_PROYECTOS/pyCelda`, el mismo directorio donde `Claude-pyCelda-SDF1` construía en paralelo -- le pisó un checkout a mitad de operación (detectado por ella vía reflog, sin daño real). Corregido: clon dedicado y persistente `~/misRepos/_PROYECTOS/pyCelda-verify-pysighor` (entornos backend/frontend instalados), usado desde entonces para toda verificación.

#### 8. **Cierre del checklist #131**: bloque 3 completado (salvo dos IDOR de cuerpo de petición, no reproducibles vía UI, pospuestos) y un tercer error de checklist corregido -- "B intenta eliminar una AsignaturaGrado de A" no aplica, `eliminar_asignatura_grado()` es exclusiva de `Admin` (`require_admin`), nunca fue capacidad de `DirectorGrado`, mismo patrón que el hallazgo de `Grado.tsx` de esta misma sesión.

#### 9. **Reflexión sobre GET vs POST, y trabajo nocturno autónomo -- `MetodologiaDocente`+`SistemaEvaluacion`**
Manuel preguntó si las URLs de acción debían convertirse a POST -- aclarado que las mutaciones reales ya eran POST/PUT (nunca GET) y que la navegación del navegador es intrínsecamente GET, sin relación con la autorización real (que es donde estaba y sigue el arreglo). Antes de cerrar la sesión, Manuel propuso dejar a pySigHor trabajando en los bloques restantes de `Admin` (`Profesor`/`MetodologiaDocente`/`SistemaEvaluacion`/`Cursos académicos`, discussion #113) -- pySigHor reflexionó primero (sin ejecutar) que "operativo" no ha coincidido con la experiencia real del proyecto (cada bloque "simple" de Admin ha tenido al menos un hallazgo real), y señaló riesgos concretos por entidad. Manuel corrigió el riesgo de `Profesor` (los scripts de Prometeus son parche temporal, no un segundo camino que pueda divergir), aceptó diferir `Profesor` y `Cursos académicos` (el segundo por sospecha real de que `CursoAcademico` no está modelado -- ver memoria de proyecto sobre `Guia.grado_id` denormalizado) y autorizó el ciclo completo -- diseño, construcción, verificación, PR, merge y despliegue, sin supervisión turno a turno -- para `MetodologiaDocente`+`SistemaEvaluacion`.

pySigHor verificó Requisitos (los 10 CU puramente `Admin` de ambas entidades ya existían completos, solo faltaba Análisis→Diseño→Desarrollo), wireframes, modelos/repos existentes y el patrón de bloqueo "en uso" ya usado en PR #132, y diseñó un encargo detallado para cada entidad antes de delegar. Trabajado de madrugada, sin Manuel presente:

- **PR #135** (`MetodologiaDocente`, `a47e7d6`→`564440e`): pipeline completo delegado a OpenCode con diseño ya cerrado, verificado por pyCelda antes de comitear (no se fió del resumen, que salió corrupto otra vez) y por pySigHor de forma independiente en su clon (270 tests, `tsc`/`vite build` limpios). pyCelda resolvió por su cuenta, con razonamiento verificado, que el bloqueo de borrado solo necesita comprobar uso en `Materia` (no `AsignaturaGrado` aparte) porque el invariante ya está garantizado por el guard de `desasociarMetodologiaDocenteMateria()`.
- **PR #136** (`SistemaEvaluacion`, `68c67f0`→`60fc17b`): mismo patrón. **Hallazgo real de pyCelda, autocorregido antes de comitear**: la instrucción original de pySigHor de tratar `tipo` como texto libre era un error -- el README de Requisitos de `crearSistemaEvaluacion()` fija explícitamente una lista cerrada (`"Evaluación continua"`/`"Evaluación final"`, issue #14) que pySigHor no había leído (solo verificó contra código/modelo/seed). Corregido con `Literal[...]` en los schemas y `<select>` en el frontend antes de comitear, con test de regresión del `422`. También se detectó y evitó una colisión de ruta real: el listado nuevo de Admin no podía usar `GET /materias/{id}/sistemas-evaluacion` porque ese path ya servía al selector de `Profesor` en `crearPonderacionEvaluacion()` -- resuelto namespacing bajo `/admin/`. 297 tests, `tsc`/`vite build` limpios, verificado por pySigHor.

Los tres despliegues de la noche (#134/#135/#136) los ejecutó Prometeus con el mismo rigor de siempre (Regla 3 de `DEPLOY.md`, health-check real), avisado por pySigHor sin que Manuel mediara -- Prometeus dejó explícito que actúa por la autorización directa que Manuel le dio para este lote, sin asumir que se extiende indefinidamente a peticiones futuras sin confirmación suya.

### Estado del Proyecto (pyCelda, no pySigHor)

- **Producción**: `https://mmasias.cloud-ip.cc/` en `60fc17b`. Cadena completa de la sesión (siete PRs, todos verificados por pySigHor y desplegados por Prometeus sin incidencias): `03c3024` (#132) → `02b5e2a` (#133) → `e0b6629` (#134) → `564440e` (#135) → `60fc17b` (#136).
- **Discussion #113 (Admin bottom-up)**: `MetodologiaDocente` y `SistemaEvaluacion` cerrados Requisitos→Producción. Quedan `Profesor` y `Cursos académicos` (el segundo posiblemente ni modelado -- pendiente de resolver mañana), ambos deliberadamente fuera del alcance de esta noche.
- **Checklist #131**: cerrado salvo los dos IDOR de cuerpo de petición (no reproducibles vía UI, sin urgencia) y la decisión pendiente sobre "Volver al panel"/"cerrar sesión" ausente en pantallas hijas de Admin (bloque 1, hallazgo real sin fix asignado todavía).
- **Clon de verificación de pySigHor**: `~/misRepos/_PROYECTOS/pyCelda-verify-pysighor`, usado en las siete verificaciones de la noche, listo para reutilizar.
- **Sin comitear en `pySigHor`**: esta actualización del log/memoria está hecha pero no comiteada -- Manuel no lo ha pedido todavía para este tramo (a diferencia del primer cierre de la noche, que sí se comiteó a petición explícita en `b4a20f8`).

### Para Próxima Sesión

Manuel indicó: mañana sigue con "pruebas ácidas" y "atajos de interfaz" nuevos (sin especificar todavía), más la decisión pendiente sobre `CursoAcademico`/`Profesor` de Admin. Verificar primero si `CursoAcademico` está realmente modelado antes de asumir que es CRUD simple -- la sospecha nace de que `Guia.grado_id` es un campo denormalizado documentado como simplificación. Confirmar con Manuel si la autorización de capitanía (diseño/delegación/verificación/merge/deploy sin supervisión turno a turno) sigue vigente para trabajo nuevo, o si aplicó solo a lo ya cerrado esta noche.

---

## Conversación 54: CRUD de Profesor, asociación a AsignaturaGrado, cierre real del issue #13, y el bug "Profesor sin botón Abrir guía"
**Fecha**: 2026-08-26 (mañana/tarde/noche, continuación directa de la Conversación 53)
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como capitán del hilo), Claude-pyCelda-SDF1 (constructora), Claude-pyCelda-Prometeus (despliegue)

### Contexto de la Sesión

Continuación de la misma sesión de pySigHor tras el cierre nocturno de la Conversación 53. Manuel volvió de una reunión, pidió reporte de situación, y amplió el encargo varias veces según fue probando en producción -- toda la capitanía (diseño/delegación/verificación/merge/deploy) siguió sin supervisión turno a turno, con Manuel interviniendo solo en las decisiones de diseño genuinas.

### Desarrollo Principal

#### 1. **CRUD completo de `Profesor` + gestión de `DirectorGrado`, PR #137**
Manuel notó, probando `SistemaEvaluacion`, que no había forma de asociar un Profesor a una AsignaturaGrado desde Admin. Reflexión previa: el modelo `Profesor` solo tenía `id`+`email`, migración real necesaria (`nombre`, backfill desde `docs/scripts/seed/profesores.json`, 30/30 reales). Hallazgo del issue #13 (bloqueo permanente de `eliminarProfesor()` por historial de Guias, palabras textuales de Manuel en el propio README de Requisitos) investigado y confirmado **inalcanzable hoy** (no existía `desasignarProfesorAsignaturaGrado()` todavía) -- documentado como nota, no bloqueante. OpenCode agotó su cuota de 5h a mitad del pipeline, pyCelda terminó lo que faltaba. Bug real de Prometeus al desplegar: ruta del script de backfill asumía raíz de repo, no funciona en el contenedor (workaround aplicado, pendiente de corregir la ruta).

#### 2. **`asignarProfesorAAsignaturaGrado()`/`desasignarProfesorAsignaturaGrado()`, PR #138 -- cierra el issue #13 de verdad**
Manuel pidió cerrar la pieza que faltaba, esta vez sin OpenCode ("está cansao"). Hallazgo real de pySigHor antes de delegar, confirmado contra 2 READMEs de Requisitos: `Guia -- Profesor` debe copiarse puntualmente al crear la Guia, no derivarse en vivo -- el código vigente lo violaba. Manuel confirmó el modelo mental completo (Guia vive en su CursoAcademico; `activarCursoAcademico()` futuro clonaría la plantilla en cada curso nuevo). Construido: tabla `guias_profesores` nueva, `Guia.profesorado` como relationship real, backfill de las 55 Guias reales. Bonus no pedido: `eliminarProfesor()` gana la tercera condición real de bloqueo, cierra el issue #13 de verdad, con test explícito.

#### 3. **Bitácora #139, tag `v0.5.0`, felicitaciones cruzadas**
Manuel pidió una discussion resumen del día completo -- publicada, pyCelda y Prometeus complementaron con su perspectiva. Reflexión sobre versión ("¿casi beta?"): aclarado que `0.x` en SemVer ya implica "en desarrollo", no hace falta sufijo -- tagueado `v0.5.0` sobre `536ba9a` a petición directa de Manuel.

#### 4. **Reflexión: ¿delegar a OpenCode desconectado, o seguir aquí?**
Manuel propuso un artefacto nuevo ("cronograma de sesiones docente + evaluaciones") y preguntó si convenía una sesión de OpenCode sin supervisión. Recomendación de pySigHor: no, al menos no Requisitos -- todo lo que funcionó bien dependía de tener Requisitos cerrados antes de delegar. Manuel aceptó, diseñaron juntos 4 decisiones (dueño = `Guia`, `tipo` en lista cerrada, sin enlace a `SistemaEvaluacion` en v1, mismo ciclo de aprobación que la Guia) -- **construcción pausada a propósito** para guardar saldo de uso, discussion #140, retomar el sábado.

#### 5. **El bug real: "Profesor sin botón Abrir guía", investigación de `CursoAcademico`, PRs #141/#142**
Manuel probó el ciclo completo (crear Grado → configurar como Director → asignar Profesor) y el Profesor no veía "Abrir guía". Causa verificada: `Guia()` solo se construye en `seed_grado.py`, ningún endpoint vivo crea una Guia al dar de alta una `AsignaturaGrado`. Investigación paso a paso con Manuel de `activarCursoAcademico()`: resultó que **`CursoAcademico` ya está completo en Requisitos** (4 CU, clase real en el modelo de dominio) -- la sospecha de "no modelado" era sobre el código, no Requisitos. Gap real encontrado en `crearAsignaturaGrado()` (cero menciones de `Guia`, confirmado con grep) -- resuelto reutilizando la misma rama "Guia nace vacía" que `activarCursoAcademico()` ya documentaba, disparada desde un segundo punto de entrada, con la simplificación de que `CursoAcademico` no existe aún como tabla (condición trivial hoy). PR #141 (fix para creaciones nuevas) + PR #142 (backfill retroactivo de las 4 AsignaturaGrado huérfanas ya en producción, encontradas por Prometeus por iniciativa propia: ids 56/57/58/59). PR #144: documentación del bug recurrente de nombrado de SVG de plantuml local (3 veces en la sesión).

#### 6. **Checklist nuevo, discussion #145, y cierre de discussion #131**
A petición de Manuel, checklist nuevo organizado por *proceso de trabajo* (no por CU aislado) cubriendo todo lo de la sesión -- 8 secciones, con el flujo completo Admin→Director→Profesor→Guia como primer punto y el test de "desasignar y comprobar que la Guia histórica sigue mostrando al profesor" marcado como el más importante. Discussion #131 (checklist anterior) cerrada y etiquetada (`estado:concluida`/`resultado:aplicado`) -- pero antes de cerrarla, verificación honesta a petición de Manuel ("¿había algo que se me escapó?") encontró un ítem real sin marcar (spot-check de aislamiento entre Profesores) que no se había trasladado -- añadido a #145 antes de dar el cierre por bueno.

### Estado del Proyecto (pyCelda, no pySigHor)

- **Producción**: `https://mmasias.cloud-ip.cc/` en `436037b`, tag `v0.5.0`. Trece PRs desde el inicio de la Conversación 53 (#132-#144), todos verificados por pySigHor y desplegados por Prometeus sin incidencias de fondo.
- **Checklist activo**: discussion #145 -- Manuel probando en vivo ahora mismo.
- **Discussion #131**: cerrada, ya no requiere atención.
- **Pendiente real, sin fecha**: resultado de las pruebas de Manuel contra #145 (lo que traiga es el punto de partida real); cronograma de sesiones (discussion #140, retomar sábado); `CursoAcademico`/`activarCursoAcademico()` (Requisitos completo, sin construir); "volver al panel" en pantallas hijas de Admin; 2 IDOR de cuerpo de petición; fix de ruta en `backfill_nombre_profesor.py`.
- **Clon de verificación**: `~/misRepos/_PROYECTOS/pyCelda-verify-pysighor`, usado en las trece verificaciones del día, listo para reutilizar.

### Para Próxima Sesión

Manuel limpiará el contexto de esta sesión para refrescarlo mañana. Memoria de proyecto (`project_pycelda_transferencia_rup.md`, sección "CIERRE DE SESIÓN") actualizada con el estado completo para retomar sin fricción. Prompt sugerido para mañana: pedir a pySigHor que lea su memoria de pyCelda y revise el estado real de discussions #145/#140 antes de que Manuel cuente cómo fueron sus pruebas. Sin comitear esta actualización del log -- Manuel no lo ha pedido para este tramo.

---

## Conversación 55: pySesion (Análisis cerrado), cuatro PRs de Admin en pyCelda, y extracción de este mismo log a la rama `leConsultor`
**Fecha**: 2026-08-30
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor), Claude-pyCelda-SDF1/Claude-pySesion-SDF1 (constructora, doble identidad según proyecto), Claude-pyCelda-Prometeus (despliegue)

### Contexto de la Sesión

Sesión larga con tres tramos: (1) housekeeping de identidad propia -- verificar que la sección "objeto de gestión" de `inputAgenteGestor.md` seguía vigente, descubrir que no (pySesion había nacido sin que quedara registrado), actualizar los tres `inputAgente*.md`; (2) revisión completa de Análisis de pySesion, ya construido por `Claude-pySesion-SDF1`/GLM antes de que Manuel volviera a la sesión; (3) tanda de cuatro PRs en pyCelda a partir de que Manuel fue probando el sistema en producción y anotando huecos. Cierra con esta misma extracción del log.

### Desarrollo Principal

#### 1. **`inputAgenteGestor.md` desactualizado -- pySesion existe y no estaba registrado**
Al arrancar, verificación de rutina encontró que la sección "objeto de gestión" del documento de onboarding (`~/misRepos/_ASIGNATURAS/mmasias_private/AGENTES/inputAgenteGestor.md`) describía un estado de pyCelda ya superado (discussion #140 "pausada" cuando en realidad ya se había construido y desplegado entera) y no mencionaba en absoluto un proyecto nuevo, `pySesion` -- nacido el 2026-08-28, hijo de pyCelda (control de asistencia por QR, consume su catálogo docente por identidad), con cadena de tres niveles: pySigHor diseña/revisa, `Claude-pyCelda-SDF1` ejecuta (identificándose como `Claude-pySesion-SDF1` en ese repo), GLM-5.3 vía OpenCode como becario mecánico. Los tres `inputAgente*.md` (Gestor/Developer/Despliegue) actualizados y comiteados por Manuel.

#### 2. **Revisión de Análisis de pySesion: 4 hallazgos reales, dos rondas de corrección**
Con Requisitos ya cerrado y auditado (discussion pySesion #5), y Análisis (12 colaboraciones B/C/E + consolidado) ya escrito pero sin comitear, pySigHor lo revisó contra los mismos criterios que pyCelda fijó en su día para sí misma (discussion #54/#59) -- fidelidad especificación→colaboración, consolidación por unión estricta, distinción real vs. ruido en naming. Cuatro problemas reales, publicados en discussion pySesion #9: gap de fidelidad en `iniciarClase()` (`GuiaDocente` huérfana, sin mensaje que liste las `SesionProgramada` pendientes pese a que el wireframe exige la tabla), asimetría de aterrizaje entre `abrirMisClases()`/`abrirAsignaturas()`, dos mecanismos sin justificar para "buscar o crear Alumno por email", y un método (`Profesor.identificar(email)`) presente en una colaboración individual pero ausente del consolidado. `Claude-pySesion-SDF1` corrigió los cuatro y encontró dos gaps propios más con su propia verificación de cierre literal -- verificado independientemente por pySigHor en las dos rondas, sin discrepancias. Comiteado y pusheado a `main` (`59850e3`).

#### 3. **Cierre administrativo de pySesion: 5 discussions, etiquetas replicadas de pyCelda**
A petición de Manuel, discussion #9 cerrada con comentario de cada parte identificado por separado. Réplica de las 9 etiquetas de bitácora que pyCelda ya usaba (`estado:*`/`agente:*`/`resultado:*`/`revisiones`) al repo pySesion, que no las tenía. Aplicadas retroactivamente a las 5 discussions existentes (#1/#2/#4/#5/#9), las 4 primeras cerradas también (estaban concluidas y aplicadas hacía días sin cerrar formalmente en GitHub). Autocorrección en el camino: `agente:humano` se había aplicado a la #9 sin comprobar los comentarios reales -- ninguno era de Manuel escrito directamente ahí (los tres llevan preámbulo "Soy X") -- retirada al notarlo, guardada como lección (`feedback_verificar_autoria_antes_etiquetar_agente`).

#### 4. **Cuatro PRs de Admin en pyCelda, a partir de que Manuel probó en producción**
- **PR #163**: `sistemas_evaluacion` expuesto en `MateriaAdminDetalleResponse`, tabla inline en `MateriaAdmin.tsx` (antes solo un botón a otra pantalla) + títulos de sección homogenizados a `<h2>`.
- **PR #164**: Admin gana edición de Materia/Curso/Carácter de `AsignaturaGrado` -- no existía ningún camino antes. Hallazgo real verificado antes de delegar: `AsignaturaGrado.grado_id` es `@property` derivada de `materia.grado_id`, no columna propia -- el selector de Materia se restringió al mismo Grado para no mover silenciosamente la asignatura de Grado (y desincronizar `Guia.grado_id`, ya denormalizado). Cambio de materia bloqueado si ya hay Guías creadas. Primera ejecución real confirmada del chequeo automático de hash de bundle en `deploy.sh` (PR #159).
- **PR #165**: mismo listado de `sistemas_evaluacion`, ahora en `Materia.tsx` (DirectorGrado), en solo lectura.
- **PR #166**: cierra discussion pyCelda #149 (navegación Admin, propuesta de Manuel con capturas) -- `Universidad.tsx`/`Facultad.tsx` fusionadas con el listado de sus hijos, un clic menos en cada nivel. Hallazgo útil: la fusión Facultad→Grados ya existía como `GradosAdmin.tsx` en ruta aparte, solo hubo que reubicarla. Efecto secundario: dos README de RUP que citaban el fichero borrado, corregidos con nota puntual sin reescribir el resto.

Método de la tanda: pySigHor diseña contra el código real antes de delegar, `Claude-pyCelda-SDF1` construye (directo o vía OpenCode según el tamaño del lote), pySigHor verifica cada PR de forma independiente en `pyCelda-verify-pysighor` (diff completo + tests + `tsc`/`build`) antes del OK, Prometeus despliega. Bitácora completa publicada en pyCelda como discussion #167.

#### 5. **Descubrimiento de la bifurcación de `conversation-log.md` entre `main` y `diseño-fastapi-react`, y esta extracción**
Manuel preguntó si el log de esta sesión estaba en `main` -- no lo estaba. Investigación reveló algo mayor: `main` y `diseño-fastapi-react` llevan **narrativas de "Conversación N" completamente independientes y sin relación** desde hace tiempo (61 commits de diferencia) -- `main` documenta la metodología RUP original de pySigHor (con los 28 artículos de `extraDocs/`, hasta el 027), `diseño-fastapi-react` documenta el port FastAPI/React (código real, RUP hasta 03-desarrollo, pero solo hasta el artículo 013, el punto de bifurcación). El hilo de orquestación de pyCelda/pySesion (Conversaciones 50-54) llevaba viviendo por accidente en `diseño-fastapi-react`, sin relación alguna con el port -- **y sin acceso, desde ahí, a los artículos 014-027 que pyCelda ya había citado como fuente** (discussion #54 de pyCelda cita literalmente el artículo 027). Se descartó fusionar el log a `main` (colisión de numeración: `main` tiene su propia Conversación 50-54 sobre otro tema) y también una rama huérfana solo-log (dejaría el hilo sin acceso a los artículos). Resuelto: rama nueva `leConsultor`, partiendo de `main` (hereda los 28 artículos completos, sin el ruido de `backend/`/`frontend/`), con este registro como fichero aparte (`conversation-log-orquestacion.md`, números sin renumerar) para no chocar con el `conversation-log.md` propio de `main`. `inputAgenteGestor.md` referenciará esta rama como la de lectura para el hilo de orquestación.

### Estado del Proyecto

- **pyCelda**: producción en `main`, `c4e1643`. Cuatro PRs de hoy en producción, bitácora en discussion #167.
- **pySesion**: Requisitos y Análisis cerrados (`main`, `59850e3`), Diseño siguiente sin empezar. Cinco discussions cerradas y etiquetadas.
- **pySigHor**: rama `leConsultor` creada hoy, partiendo de `main`, con este archivo como su único contenido nuevo -- `diseño-fastapi-react` recorta su log a la Conversación 49 con nota de continuación aquí.
- **Pendientes heredados de pyCelda, sin cambios hoy**: `CursoAcademico`/`activarCursoAcademico()`, 2 IDOR de cuerpo de petición, "volver al panel" en pantallas hijas de Admin, issue #148, script `corregir_curso_asignatura_grado.py` sin comitear, recuento de Análisis desincronizado, discussion #140 sin cerrar en GitHub pese al trabajo ya hecho.

### Para Próxima Sesión

Confirmar con Manuel si `leConsultor` se comitea/pushea ya o queda pendiente de su revisión. `inputAgenteGestor.md` necesita el ajuste explícito de referencia a esta rama (pendiente al cierre de esta conversación). Sin tareas activas de pyCelda/pySesion más allá de los pendientes heredados listados arriba.

---

## Conversación 56: pyCelda desde la máquina `oficina` -- `Guia.contenido`, modelo de datos, renombrado `Cronograma`->`Planificación docente`
**Fecha**: 2026-09-01 (tarde)
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor, renombrada `Claude-pySigHor-Oficina`), Claude-pyCelda-Oficina (constructora -- 2ª sesión en la misma máquina, NO `Claude-pyCelda-SDF1`), Claude-pyCelda-Prometeus (despliegue)

### Contexto de la Sesión

Primera sesión del rol de orquestador **desde la máquina `oficina`** (`aio@despacho.U`, Ubuntu 26.04), no SDF1. Consecuencias prácticas: ni `pyCelda-verify-pysighor` ni `pySesion` existían aquí. Recreé el clon de verificación (clon limpio de GitHub) e instalé el toolchain que faltaba -- `uv` y `plantuml 1.2026.7` (el `plantuml` del sistema es 1.2020, que da un diff de estilo masivo; el 1.2026.7 casa con los SVG ya committeados). El nodo constructor esta vez fue una segunda sesión Claude Code en `oficina`, también llamada `Claude-pyCelda-Oficina` -- colisión de nombre con la mía hasta que Manuel me renombró a `Claude-pySigHor-Oficina`.

Manuel presentó la aplicación a profesorado ese día y empezaron las pruebas reales. Siete PRs mergeados a partir de lo que fue apareciendo, todos con el flujo de siempre: diseño mío contra el repo -> discussion de criterio -> delegación a `Claude-pyCelda-Oficina` -> verificación independiente mía en el clon con ejecución real -> merge con OK explícito de Manuel PR a PR -> despliegue de Prometeus con runbook.

### Desarrollo Principal

#### 1. `Guia.contenido` como apartado propio de la fase de impartición (discussion pyCelda #191, PR #192)

El profesor pidió poder editar el temario al editar su guía docente. El modelo tenía `contenido` solo en la fase estructural (`AsignaturaGrado`, que la `Guia` heredaba al renderizar el PDF, sin materializarlo -- entrada explícita del README del modelo, wireframe "heredado de AsignaturaGrado"). Reflexión: la petición cruza la línea estructural/impartición, pero el temario de una guía docente es en la práctica real un artefacto redactado y revisado cada curso, y los demás apartados que el profesor edita (`PonderacionEvaluacion`, `ReferenciaBibliografica`, `semestre`) ya viven en la `Guia` y se siembran del curso anterior. Cuatro opciones evaluadas; elegida A: `Guia.contenido` propio, sembrado al nacer (copia puntual, no fallback en vivo -- coherente con el "snapshot por curso" del resto de la Guia), editado por `guardarBorradorGuia()` sin CU nuevo, renderizado en el PDF; `AsignaturaGrado.contenido` degradado a semilla + referencia estructural verificada. Retroceso puntual a Modelo/Requisitos (mecanismo de las discussions #47/#72, no reapertura de fase).

Lección propia reforzada con evidencia nueva: mi extracción de la agrupación Materia->Asignatura de las memorias ANECA, ya "verificada" por mí con conteos, tenía un bug estructural que solo salió cuando `Claude-pyCelda-Oficina` lo EJECUTÓ de verdad, no solo lo revisó. La verificación cruzada no es teatro ni cuando el diseñador cree haberlo probado.

Migración: `ADD COLUMN` en sitio, decisión de Manuel -- para un ADD-COLUMN-con-default SQLite lo hace nativo y el ritual extract/reimport es más superficie de riesgo (regla general "si toca `models/`, extract/reimport" intacta para el resto de casos). Backfill `Guia.contenido := AsignaturaGrado.contenido` de 108/108 guías en producción, verificado contra backup. **El conteo real de guías es 108** (GII 55 + GIOI 53).

Incidente de proceso en el despliegue: Prometeus iba a hacer un dry-run sobre copia antes del `apply`, pero el override `DATABASE_URL` no surtió efecto (`app.core.database` no lee esa var) y el `apply` corrió contra la BD real. Resultado correcto y verificado contra backup, script idempotente -- pero fuera del control pactado. Lección: el mecanismo de dry-run-sobre-copia asumía una palanca que no existe.

#### 2. Modelo de datos en `RUP/03-diseño/modelo-datos/` (discussion pyCelda #196, PR #197)

Hueco real detectado: `03-diseño` solo tenía la vista OO (`diagrama-clases-diseño.puml`); ninguna vista relacional del almacén de datos -- las 6 tablas de unión invisibles, la nulabilidad de las FK sin documentar, ni qué asociación es FK física vs lógica (issue #181). **Precedente en pySigHor**: la rama `diseño-fastapi-react` ya tiene `RUP/02-diseño/DER.puml` (notación `class` + `<<PK>>`/`<<FK>>`, crow's foot) -- transferido con juicio.

Artefactos: `DER.puml` (+SVG, 100% generado, 23 tablas en 3 packages), `diccionario-datos.md` (capa estructural generada entre marcadores `<!-- BEGIN/END GENERADO -->` + capa de intención a mano: dominios de los 8 enum, FK lógicas, denormalizaciones, reglas de consistencia -- enlazando al README del modelo de dominio sin duplicar el "por qué"), `backend/app/scripts/generar_modelo_datos.py` (introspección de `Base.metadata`, `--check`, sin BD, aborta si una tabla no está repartida en `PAQUETES`). Nivel lógico-físico híbrido (tipos SQLAlchemy, no storage classes de SQLite). **Regla de mantenimiento nueva** en `RUP/03-diseño/README.md`: un PR que toca `backend/app/models/` regenera DER + diccionario y revisa la capa de intención -- misma obligación que actualizar el README del modelo de dominio.

Dos hallazgos incidentales registrados, no corregidos (fuera de alcance): `asignaturas.contenido` es `String` sin longitud mientras `asignaturas_grado`/`guias` usan `Text`; `asignaturas_grado.estado` nace `'Activo'` (el README del modelo dice `Vigente`/`Extinguido`).

#### 3. `Cronograma` -> `Planificación docente` (renombrado completo) + `Sesion.tipo` 6º valor (discussion pyCelda #198, PR #199)

Mismo concepto, mejor nombre (el que usan las guías docentes reales). Renombrado completo, no solo etiqueta -- una etiqueta dejaría divergencia permanente doc<->código, justo lo que el proyecto elimina siempre. Alcance: entidad de dominio `PlanificacionDocente` (sigue colapsada, sin tabla -- `Sesion` va directo a `Guia`); casos de uso `abrirPlanificacionDocente` + `crear`/`editar`/`eliminarSesion`; tabla `sesiones_cronograma` -> `sesiones`; estados `PLANIFICACION_DOCENTE_ABIERTA`; 12 carpetas RUP (`git mv`) en Requisitos/Análisis/Diseño; backend, frontend, modelo de datos regenerado; 23 SVG. `git grep` confirmó cero identificadores residuales (los restos en `docs/scripts/seed/*.json` son temario real de asignaturas, no la entidad).

`Sesion.tipo` gana `CLASE_TEORICO_PRACTICA` ("Clase teórico/práctica") -- enmienda explícita en el README del modelo de dominio a la afirmación "sin candidatos adicionales" de la discussion #140. Sin cambio de esquema.

Migración: `ALTER TABLE sesiones_cronograma RENAME TO sesiones`, nativo en SQLite, mismo criterio que #192. En producción la tabla tenía 1 fila (una sesión de las pruebas de ese día), preservada por el RENAME. En #199 Manuel no estaba en la máquina y autorizó explícita y directamente a Prometeus a lanzar el `apply` -- no relayado por mí.

#### 4. PRs menores y deuda de SVG

- **#193**: textarea de `contenido` de la guía a `rows={35}`.
- **#195**: dimensionado de 10 textareas de `frontend/src/pages/` (grupos 1 y 2 de un audit -- editores de "Contenido" a `rows={35}` + ancho 100%, descripción/comentario a ancho 100%). Grupo 3 (referencias bibliográficas) aplazado a otra sesión, "hay ideas de fondo".
- **#194**: 11 SVG de `images/RUP/` que quedaron stale tras #192 -- regenerados con plantuml 1.2026.7. Manuel: "el cambio en la consistencia estética de un artefacto de requisitos es mal menor y perfectamente asumible; otra cosa son errores semánticos en ese mismo artefacto".

#### 5. Patrón de despliegue con migración, asentado

Aplicado dos veces esta sesión (#192, #199). Runbook en el cuerpo del PR: backup manual -> `git pull` -> script de migración `plan` (revisar conteos) -> `apply` contra el volumen **antes** de `./deploy.sh` (el backend nuevo declara el esquema nuevo y `create_all()` no migra tablas existentes) -> `deploy.sh` -> health + check funcional de la ruta/columna nueva. Scripts en `backend/app/scripts/`, modos `plan`/`apply`, idempotentes, SQL crudo (ejecutables en el contenedor viejo). El paso `apply` escribe en `pycelda.db` y el clasificador de auto-mode de Prometeus lo bloquea -> lo ejecuta Manuel con `!` o autoriza directamente a Prometeus.

#### 6. Importación de planificaciones docentes reales -- piloto de 5 asignaturas GII (discussion pyCelda #200, PR #201)

Manuel preguntó si se podía importar la planificación sesión a sesión (`PlanificacionDocente`/`Sesion`, recién renombrada en el punto 3) desde una hoja de cálculo real del profesorado. La planificación docente nunca estuvo en el corpus de las memorias ANECA -- dato nuevo, aportado por Manuel.

**Análisis del Excel real** (`CdM 26-27.xlsx`, ~54 hojas GII, ~16 vacías): metadatos de cabecera (`Grado`/`Curso`) inconsistentes, no sirven para emparejar; el tipo de sesión iba codificado por color de celda contra una leyenda de 4 valores, con ~25 variantes de tono. Manuel curó una segunda versión (`PLANIFICACION Docente curada.xlsx`) sustituyendo el color por el texto de la leyenda en una columna -- resuelve el problema de raíz.

**Iteración "vamos comentando" sobre 5 hojas reales** (Matemática I, Física, Tecnología y Estructura de Ordenadores, Programación I, Introducción a la gestión de proyectos software): celdas fusionadas resueltas a su ancla (un tema fusionado en N filas = N sesiones idénticas -- confirmado por Manuel con el ejemplo real de TEO); `EVALUACION_PARCIAL` no está en la leyenda, se infiere de la descripción y sobreescribe la columna de tipo salvo que empiece por "Revisión"; `numero` por orden de fila (la columna "Sesión" tiene huecos y duplicados reales); normalización `rpdR` -> "Revisión pública de Reto"; decisiones puntuales en vivo (Seminario -> práctica, fila en blanco -> saltar).

Resultado: 139 sesiones, cero sin clasificar. Material de referencia dejado en `~/misRepos/corral/tasks/planificacion-docente/` (primer uso de ese directorio en esta tanda) para que `Claude-pyCelda-Oficina` lo productivizara: `importar_planificaciones.py`, `sesiones.json` comiteado, loader idempotente en `seed_grado.py` + `cargar_sesiones.py` standalone. Verificado: parser vs. .xlsx real da salida byte-idéntica al JSON comiteado; seed y `cargar_sesiones` idempotentes. Desplegado por Prometeus como operación de datos (sin redeploy) -- fricción real: `docs/scripts/seed/` no está en la imagen Docker, tuvo que `docker cp` el JSON y los scripts nuevos al contenedor, registrado como [issue #202](https://github.com/mmasias/pyCelda/issues/202). 139 `Sesion` verificadas en producción por SQL y de forma independiente.

### Estado del Proyecto

- **pyCelda**: producción -- código en `main`, `a2719cd`; datos del piloto de planificaciones (139 `Sesion`) aplicados sin commit de deploy propio (`a4ce9ee` no toca código de app). `/api/health` `200`, verificado de forma independiente. Discussions #191/#196/#198/#200 cerradas (`concluida`+`aplicado`). Issue #202 abierto (fricción de despliegue de datos). Sin PRs ni deploys de código pendientes.
- **pySesion**: sin tocar esta sesión -- sigue donde quedó el 2026-08-30 (Requisitos y Análisis cerrados, Diseño sin empezar).
- **pySigHor**: esta Conversación 56 en `leConsultor`. Clon de verificación y toolchain (`uv`, plantuml 1.2026.7, `openpyxl`) instalados en `oficina`.
- **Pendientes heredados de pyCelda, sin tocar**: issues #179/#181/#184/#185/#187; `CursoAcademico`/`activarCursoAcademico()`; 2 IDOR de cuerpo de petición (discussion #131); issue #148 (`Grado.codigo` sin unicidad); auditoría de `curso`/`semestre` en el resto de `AsignaturaGrado` (discussion #128); grupo 3 de textareas (referencias bibliográficas); issue #202 (fricción `docs/` fuera de la imagen).
- **Pendiente nuevo, sin fecha**: el resto del Excel de planificaciones docentes de GII (~33 hojas sin curar) para escalar la importación más allá del piloto de 5.

### Para Próxima Sesión

`inputAgenteGestor.md` sigue asumiendo SDF1 y `Claude-pyCelda-SDF1` como constructor -- si se sigue trabajando desde `oficina`, conviene ajustar la sección 5 (objeto de gestión) o al menos anotar que el clon de verificación y el nodo constructor pueden estar en `oficina`. Si Manuel cura más hojas del Excel de planificaciones, retomar la importación desde `~/misRepos/corral/tasks/planificacion-docente/DECISIONES.md`. Sin más tareas activas.

---

## Conversación 57: Revisión y merge del PR #204 (sincronización de documentación de pyCelda), coordinación multi-sesión y cierre de discrepancias de estado
**Fecha**: 2026-09-01 noche -> 2026-09-02 (madrugada)
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor, `Claude-pySigHor-SDF1`), OpenCode (constructor de la rama `cc/sincronizar-readmes-estado` en pyCelda, sin sesión Claude propia identificada), Claude-pyCelda-Prometeus (despliegue/verificación), Claude-pySigHor-Oficina (sesión previa de la tarde, no viva durante esta ventana -- su trabajo se reconcilió por escrito, no en vivo)

### Contexto de la Sesión

Primera sesión desde SDF1 tras la tanda de la tarde en `oficina` (Conversación 56). Manuel trajo directamente el resultado de OpenCode: una rama de pyCelda (`cc/sincronizar-readmes-estado`) con un diagnóstico y corrección de la documentación RUP de estado, pidiendo opinión sobre si mergearla.

### Desarrollo Principal

#### 1. Revisión y merge del PR #204 (discussion implícita, sin discussion propia -- delegación directa de Manuel)

OpenCode caracterizó su propio trabajo como tres cosas distintas: diagnóstico (detectar y cuantificar la divergencia), corrección (aplicar solo afirmaciones de estado) y autoría nueva (8 fichas de Desarrollo de código ya existente pero indocumentado). Verificación independiente completa, no aceptando el resumen como prueba:

- **Alcance**: `git diff --stat` confirmó solo documentación -- ningún `.py` tocado salvo la línea `description` de `pyproject.toml`.
- **421/421 tests** ejecutados de verdad en un clon aislado (no el `pyCelda-verify-pysighor` compartido, que tenía otra tarea en curso -- incidente propio evitado a tiempo: un `git stash`+`checkout` mal pensado sobre ese clon compartido estuvo a punto de pisar trabajo de otra sesión; diagnosticado y revertido sin daño (el stash solo contenía un `uv.lock` generado). Lección reforzada: nunca mutar el working tree de un clon de verificación compartido sin comprobar antes su estado.
- **Cifras de divergencia recalculadas de forma independiente y exactas**: 46+46+38 CU con carpeta real sin fila en el índice (Análisis/Diseño/Desarrollo), 8 CU con código real sin ficha de Desarrollo (verificado que el código de las 8 ya existía en `main` antes de la rama -- no es documentación de código inexistente), 41 CU recoloreados en el dashboard (verificado a nivel de colores hex reales dentro del SVG generado, no solo en el `.puml` fuente: 46->190 líneas `#ADD8E6`, 0->31 `#FF0000` correspondientes exactas a las 9 CU de Admin realmente pendientes).
- **Cronología de la divergencia verificada contra `git log` real** de `main`: congelamiento de los resúmenes el 19-08 (último commit que tocó los índices antes del fix), primera divergencia real el 24-08 (todo el bloque Admin implementado ese día sin tocar un solo índice), sync del 29-08 (`c160411`) que ya nació caducado -- el propio README de Desarrollo seguía diciendo "40 de los 42" el mismo día que el commit se declaraba "sincroniza dashboard y README raíz".
- Tres fichas nuevas contrastadas línea a línea contra router/schema real (`crearSesion`, `eliminarAsignaturaGrado`, `eliminarSesion`): contrato exacto en los tres casos.
- Mergea limpio contra `origin/main` (verificado con `git merge-tree`).

Sin ningún hallazgo negativo en ningún ángulo verificado. Manuel autorizó "adelante, mergéalo" -- **PR #204 mergeado a `main`, `8cb2b09`**. Cierra el pendiente "recuento de Análisis desincronizado" que la memoria de pySigHor llevaba abierto desde el cierre de la Conversación 56.

#### 2. Discrepancia de estado en `inputAgenteDespliegue.md`, aviso cruzado a Prometeus

Al revisar si los tres `inputAgente*.md` necesitaban actualización, se detectó que `inputAgenteDespliegue.md` afirmaba producción en `c975aa1` (estado de las ~01:00 del 09-01, antes de la tanda de la tarde) cuando la memoria propia de pySigHor ya registraba `a2719cd`. Sin acceso directo a `.deployed-commit` de Prometeus para confirmar, se envió el hallazgo por `SendMessage` a `Claude-pyCelda-Prometeus` en vez de editar un fichero ajeno a ciegas -- **regla de oro del método aplicada literalmente** ("ningún nodo relaya autorización de otro" tiene su contraparte: ningún nodo asume el estado de la máquina de otro sin verificarlo). Prometeus confirmó contra la máquina real (`a2719cd`, health 200) y corrigió su propio runbook, más una nueva sección de memoria propia de verificación.

#### 3. Conflicto real de edición concurrente en `inputAgenteGestor.md`, reconciliado a mano

Al intentar reflejar el hito del PR #204 en `inputAgenteGestor.md` (repo `mmasias_private`), un `git status`/`fetch` de rutina reveló que `Claude-pySigHor-Oficina` había comiteado (`c731dfb`, 18:38 de ese mismo día) una reescritura amplia de la misma sección §5.2 sobre una base anterior a mis ediciones locales -- ambas tocaban el mismo bloque de tabla. Un `pull` directo habría fallado o mezclado mal dos reescrituras del mismo contenido. Protocolo aplicado: `git stash` de mis cambios, `pull --ff-only` limpio (trajo también el fix de Prometeus y un backup automático), y superposición manual de solo la información nueva (hito de esta noche, `main` a `8cb2b09`, cierre del pendiente de Análisis) sobre la base ya reescrita por Oficina, en vez de reaplicar mi diff antiguo a ciegas. Confirmado con Manuel, comiteado y pusheado (`d89098a`).

Mismo patrón de reconciliación (sin conflicto de fichero, pero sí de contenido narrativo) al revisar `myClaudeContext`: dos commits nuevos de Prometeus (verificación de producción, corrección de su propio puntero de `main`) coincidían exactos con lo verificado esta sesión -- `pull` limpio, sin correcciones necesarias, mi propia actualización de memoria comiteada encima (`e65d523`, escaneo de secretos limpio antes de pushear).

#### 4. Corrección de `inputAgenteDeveloper.md`

Al preguntar Manuel si el estado quedaba listo para retomar mañana, auditoría de los tres `inputAgente*.md` reveló que `inputAgenteDeveloper.md` (identidad de `Claude-pyCelda-Oficina`) afirmaba **"Despliegue pendiente en Prometeus"** para el PR #199 y **"Carga de datos pendiente en Prometeus"** para el PR #201 -- ambos ya hechos y verificados esta misma sesión. No solo desactualizado: engañoso, con riesgo real de que una sesión futura reintentara un despliegue o una carga ya completados. Sin sesión `Claude-pyCelda-Oficina` viva para avisar, corregido directamente con los hechos ya verificados (autorización general de ejecución rutinaria, corrección factual sin ambigüedad de diseño).

### Estado del Proyecto

- **pyCelda**: `main` en `8cb2b09` (PR #204). Producción en `a2719cd` + 139 `Sesion` del piloto de planificaciones, sin nada pendiente de desplegar (verificado por mí y por Prometeus, de forma independiente, la misma noche). Discussions activas ninguna nueva. Pendiente "recuento de Análisis desincronizado" **cerrado**.
- **pySesion**: sin tocar esta sesión.
- **pySigHor**: esta Conversación 57 en `leConsultor`. Los tres ficheros `AGENTES/inputAgente*.md` (`Gestor`, `Despliegue`, `Developer`) y la memoria de `myClaudeContext` quedan reconciliados y al día entre las cuatro sesiones que los tocaron esta ventana (SDF1, Oficina, Prometeus, esta misma).
- **Pendientes heredados de pyCelda, sin tocar**: issues #179/#181/#184/#185/#187/#202; `CursoAcademico`/`activarCursoAcademico()`; 2 IDOR de cuerpo de petición (discussion #131); issue #148; auditoría de `curso`/`semestre` (discussion #128); grupo 3 de textareas; resto del Excel de planificaciones docentes de GII (~33 hojas sin curar).

### Para Próxima Sesión

Ninguna tarea activa. Lección de proceso para dejar anotada: cuando varias sesiones (distintas máquinas) editan los mismos ficheros de infraestructura compartida (`AGENTES/*.md`, memoria de `myClaudeContext`) en la misma ventana de tiempo sin coordinarse en vivo, `git fetch`+diff antes de editar es obligatorio, no opcional -- un `pull` a ciegas sobre cambios locales pudo haber destruido o mezclado mal el trabajo de otra sesión. Ocurrió dos veces esta sesión (`inputAgenteGestor.md` con Oficina, working tree de `pyCelda-verify-pysighor` con una tarea ajena en curso) y las dos veces el chequeo previo evitó el daño.

---

## Conversación 58: Tanda #206 -- regla `c3` de planificación docente mínima + medidores de completitud, y la consolidación de RUP que se desvió cuatro veces
**Fecha**: 2026-09-02 (tarde-noche)
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor, `Claude-pySigHor-Oficina`), Claude-pyCelda-Oficina (constructor, apoyándose en OpenCode; Manuel le dio autorización explícita de "push, merges y PRs a indicación de pySigHor" para esta tanda), Claude-pyCelda-Prometeus (despliegue)

### Contexto de la Sesión

Sesión larga desde `oficina`; Manuel se marchó a casa a mitad y siguió el avance vía Claude Web Remoto, con capitanía completa delegada a pySigHor (diseño + verificación + merge + coordinación de despliegue sin confirmación turno a turno). Dos ajustes pedidos por Manuel tras las pruebas reales de la app con profesorado:

1. Que tener una planificación docente con un mínimo de sesiones sea de obligado cumplimiento para enviar la guía docente a revisión.
2. Que al gestionar las ponderaciones de evaluación se vea la suma agregada (vinculadas o no).

### Desarrollo Principal

#### 1. Discussion #206: el tema común y los dos escenarios

Reflexión previa: los dos ajustes son la misma cuestión -- `enviarGuiaARevision()` es el único punto donde se comprueba que la guía está lista, y en ambos casos el profesor solo descubre el incumplimiento al recibir el rechazo. Discussion #206 con el post común ("condiciones de envío de la `Guia` y su retroalimentación previa") + dos comentarios, "Escenario planificación" y "Escenario ponderación". Manuel decidió: umbral entre 25 y 30 (luego fijado en 25 por defecto), configurable por Admin, cota 1-100, snapshot en `Guia`, patrón `vinculada` para `Sesion` (Opción 2), `c3` encadenado tras `c2` en `especificacion.puml`, medidor total + subtotales por sistema, solo texto.

**Corrección propia registrada en el hilo**: escribí que `especificacion.puml` tenía un único `<<choice>>`; Manuel señaló que ya tenía dos encadenados (`c1` ítems sin guardar / `c2` rango o suma), añadidos por `3ee9d38`. Me apoyé en el "Hallazgo" caduco del README de Análisis sin abrir el `.puml`. Tachado y corregido con comentario aparte.

#### 2. Bloque 1 -- medidor de completitud de ponderaciones (PR #207, `d15ed02`)

Solo frontend, sin backend ni migración. `PonderacionesEvaluacion.tsx` y `AbrirGuia.tsx`: "Total asignado: X% / 100%" + "Asignado" por `SistemaEvaluacion` contra su rango. Retoque tras mi verificación: un sistema con 0% muestra "(sin asignar)" en gris, no rojo "(fuera de rango)" -- porque `puede_enviarse_a_revision()` no valida rango de un sistema sin ponderaciones vinculadas (hallazgo -> [issue #208](https://github.com/mmasias/pyCelda/issues/208)). Desplegado por Prometeus, bundle sha256-idéntico a mi build verificado.

#### 3. Bloque 2 -- `Sesion` entra en el ciclo `vinculada`/pending (PR #209, `dc2da1c`)

Bugfix aditivo: el RUP y el frontend ya especificaban Opción 2 completa (`crearSesion`/`editarSesion` "datos en memoria", `eliminarSesion` "N/A sin backend", `PlanificacionDocente.tsx` con lista de trabajo), pero el backend divergía. `SesionRepository.existe_pendiente_de`/`vincular`/`desvincular`, `Guia.sincronizar_sesiones`, `GuardarBorradorRequest.ids_sesiones_final`, `guardar_borrador_guia` sincroniza sesiones, el `409` de `enviar_guia_a_revision` las cuenta. `AbrirGuia.tsx` ahora respeta `claveSesionesExcluidas` -- bug de paso corregido: antes "eliminar sesión" en el front no persistía nunca. Sin cambio de esquema. Hallazgo transversal -> [issue #210](https://github.com/mmasias/pyCelda/issues/210): `sincronizar_*` no acota `a_vincular` a las filas de la guía (500 con id inexistente + manipulación cruzada del flag `vinculada` de otra guía). Pre-existente en las 3 colecciones. Lo más cercano a seguridad de la tanda.

#### 4. Bloque 3 -- regla `c3` + `sesiones_minimas` configurable (PR #211, `661e058`, con migración)

`AsignaturaGrado.sesiones_minimas` (default 25, cota 1-100 validada con `422`), `Guia.sesiones_minimas` (snapshot al nacer), `Guia.planificacion_docente_completa()`, rama `c3` en `enviar_guia_a_revision` (`422`, "N de M sesiones"). CRUD Admin. Envelope `AbrirPlanificacionDocenteResponse {sesiones, sesiones_minimas}` -- decisión mía (un solo consumidor, modelo correcto) frente a segunda llamada a `abrirGuia`. Medidor "N / M sesiones" en dos vistas. Migración `migrar_sesiones_minimas.py`: fix pedido en mi revisión -- backfill one-shot (dentro de `if not guias_existe`, no re-sincroniza -- coherente con "snapshot al nacer"). Prometeus la validó contra copia de la BD real antes del merge (108 guías -> 25, 0 fuera de rango, idempotente). En producción la lanzó Manuel con `!` porque el clasificador de auto-mode de Prometeus bloqueó el paso de escritura dos veces.

#### 5. La consolidación de RUP que se desvió cuatro veces

El Bloque 2 mergeó con `guardarBorradorGuia` Análisis/Diseño sin tocar pese a que su comportamiento cambió, y yo lo aprobé (verifiqué tests + diff + notas de Desarrollo, no "qué otros CU describen algo que acaba de cambiar"). Al verificar el Bloque 2 aseveré que "el RUP de `eliminarSesion` especifica exactamente el comportamiento posicional" habiendo leído solo Análisis y Diseño -- la ficha de Requisitos decía lo contrario (renumeración persistida "confirmada por Manuel"). Contradicción intra-CU de meses. Lo cazó el nodo constructor. Manuel decidió (vía diálogo): alinear Requisitos a lo construido (posicional, `Sesion.numero` conserva huecos). El arreglo debió ser un barrido; fueron cuatro rondas (`12bc082`/`e3b89f2`/`fc62c07`/`aa151da`) porque reaccioné a mi siguiente `grep` en vez de auditar. El nodo constructor forzó el cambio de método proponiendo un audit sistemático del clúster entero -- que reveló también deriva **anterior a #206** (`abrirGuia` desde #199, `abrirPonderacionesEvaluacion` #38 -> [issue #212](https://github.com/mmasias/pyCelda/issues/212)). Al final, `guardarBorradorGuia`, `abrirGuia`, `abrirPlanificacionDocente`, `eliminarSesion`, diagramas de clases y DER/diccionario quedaron consolidados; todos los SVG regeneran byte-idénticos.

#### 6. Retrospectiva -- discussion #213

A petición de Manuel ("esto es un aprendizaje de la hostia, hemos de saber dónde nos desviamos"). Causa raíz: no existe un paso explícito de "auditar la RUP del clúster afectado" cuando un PR cambia el comportamiento de un CU. Cambios de proceso propuestos: (a) audit-del-clúster obligatorio antes de merge que cambie comportamiento; (b) linter determinista de "hallazgos abiertos" en RUP (`no resuelto aquí`, `queda señalado`, `cuando se retoquen`, `dos colecciones`, `cinco lecturas`); (c) verificar siempre la ficha de Requisitos, no solo Análisis/Diseño; (d) resolver la fricción del `apply` de migración en Prometeus; (e) saldar #212 pronto en un PR corto de solo-RUP.

#### 7. Canal de escalada con Manuel ausente

Se probó la "consulta vía diálogo" (AskUserQuestion): **llega pero no notifica al móvil**. Acuerdo: la tanda avanza, lo que necesita criterio de Manuel se deja en diálogo + una línea en el terminal, lo bloqueante-e-irreversible detiene ese bloque hasta que responda, lo reversible y de bajo riesgo lo decide pySigHor y lo reporta. Manuel "al pendiente" pese a todo.

### Estado del Proyecto

- **pyCelda**: `main` y producción en `661e058`. Tanda #206 cerrada (3 bloques desplegados: `d15ed02` -> `dc2da1c` -> `661e058`). `/api/health` 200, integrity + FK check limpios en prod, 139 `Sesion` del piloto intactas, 108 guías con `sesiones_minimas=25`. Discussions #206 (`concluida`+`aplicado`) y #213 (retrospectiva, `en-curso`). Tag último `v0.6.0` sobre `7618f19` -- **sin bump de versión en esta tanda** (pendiente si se quiere reflejar #206).
- **pySesion**: sin tocar esta sesión (Requisitos y Análisis cerrados, Diseño sin empezar desde 2026-08-30).
- **pySigHor**: esta Conversación 58 en `leConsultor`. Clon de verificación `pyCelda-verify-pysighor` en `oficina`, en `main`.
- **Deuda nueva de #206, priorizada**: **#210** (`sincronizar_*` sin acotar `a_vincular` -- seguridad, prioridad sobre las otras dos) > **#208** (sistemas de evaluación requeridos vacíos sin validar) > **#212** (deriva RUP pre-#206, solo RUP).
- **Pendientes heredados de pyCelda, sin tocar**: issues #179/#181/#184/#185/#187/#202; `CursoAcademico`/`activarCursoAcademico()` (Requisitos completo, sin construir -- ahora también debe clonar `sesiones_minimas`, ya anotado en su README); 2 IDOR de cuerpo de petición (discussion #131, relacionado con #210); issue #148; auditoría de `curso`/`semestre` (discussion #128); grupo 3 de textareas; resto del Excel de planificaciones docentes de GII (~33 hojas sin curar).

### Para Próxima Sesión

Leer discussion #213 antes de nada -- el paso de audit-del-clúster aplica a cualquier PR de la deuda que toque comportamiento de un CU. Orden sugerido de la deuda: #210 (con las 3 colecciones a la vez, y de paso los 2 IDOR de cuerpo de #131), luego #208, luego #212 (solo-RUP, corto). No se sabe desde qué máquina se retoma -- confirmar contra `machine-id.md`; emparejamiento homogéneo (`Claude-pySigHor-<sufijo>` con `Claude-pyCelda-<mismo sufijo>`), Prometeus constante. El clon de verificación y su toolchain viven en `oficina`; si se retoma desde otra máquina, recrearlos allí.

---

*"Hacer las cosas bien no es pedantería académica: es inversión que se amortiza en cada línea de código escrita después."*

---

## Conversación 59: Deuda de #206 completa (#210/#208/#212), con capitanía total delegada y sin Manuel activo
**Fecha**: 2026-09-03
**Participantes**: Manuel (Usuario, ausente durante casi toda la sesión), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor, `Claude-pySigHor-SDF1`), Claude-pyCelda-SDF1 (constructor, apoyándose en OpenCode), Claude-pyCelda-Prometeus (despliegue)

### Contexto de la sesión

Retoma desde SDF1 (máquina confirmada contra `machine-id.md`, coincide con el nombre de la sesión). Manuel delega **capitanía completa** de la deuda de #206 (#210, #208, #212) y se desconecta -- diseño, verificación, aprobación de merges y coordinación de despliegue sin confirmación turno a turno, con el diálogo como único canal de escalada (llega al móvil pero no notifica, así que solo lo bloqueante-e-irreversible detiene un bloque). No hizo falta escalar nada -- las tres piezas eran de bajo riesgo y quedaban dentro de las reglas de autonomía ya fijadas.

Antes de empezar: `git remote -v` del propio repo pySigHor apuntaba a `https://github.com/mmasias/pyCelda.git` en vez de `pySigHor.git` -- corregido (`git remote set-url`), encargo explícito de Manuel al arrancar. Causa no investigada (probablemente copia de configuración entre proyectos en algún momento pasado); sin efecto práctico hasta ahora porque nunca se hizo push desde este repo.

### Desarrollo principal

#### 1. Recreación del clon de verificación en SDF1

`pyCelda-verify-pysighor` existía en SDF1 pero estaba 129 commits detrás de `main` (de una sesión de trabajo anterior, no de verificación). `git reset --hard origin/main` (repo desechable, sin trabajo propio que perder) + `uv sync` + 435 tests en verde como línea base. Detectado de paso: `plantuml` local es `1.2026.6`, el constructor (vía plantuml.com) generó con `1.2026.8` -- desfase de dos versiones menores que produce SVG **byte-distintos con contenido idéntico**. Ver `feedback_verificacion_svg_plantuml.md`.

#### 2. #210 (seguridad) -- PR #214, `ba5bbce`

`Guia.sincronizar_ponderaciones/_referencias/_sesiones` no intersectaba `deseadas` con las filas propias de la `Guia`: un id inexistente en el body de `PUT /guias/{id}/borrador` causaba 500, un id de otra `Guia` se le marcaba `vinculada=True` sin cambiar su `guia_id`. Diseño mío (intersectar en el único punto de entrada, sin duplicar la validación en los tres repositorios porque `vincular()` solo tiene ese call site), construido por el constructor, verificado reproduciendo los 6 tests fallando sin el fix antes de aprobar. Audit-del-clúster: no requería tocar RUP (la ficha de `guardarBorradorGuia`, las tres fases, no documentaba nada sobre pertenencia de ids). Los "2 IDOR de cuerpo" de discussion #131 que formaban parte del encargo original ya estaban resueltos desde `ab0f753` (25-08) -- verificado, no tocado. Desplegado, `/api/health` 200 verificado también de forma directa desde aquí (no solo por el reporte de Prometeus).

**Incidente propio, corregido en el momento**: al diseñar el fix escribí el cambio directamente en `/home/manuel/misRepos/_PROYECTOS/pyCelda/backend/app/models/guia.py` (el repo del constructor), rompiendo la separación de roles del método (orquestador diseña y verifica, constructor construye). Detectado antes de seguir, revertido con `git checkout --`, y el diseño se envió como especificación por `SendMessage` en su lugar. Ver `feedback_orquestacion_pycelda.md` (actualizado).

#### 3. #208 -- PR #215, `5cad9f8`, dos rondas de audit-del-clúster

`puede_enviarse_a_revision()` solo validaba el rango de los `SistemaEvaluacion` con alguna `PonderacionEvaluacion` vinculada -- uno requerido (`ponderacion_minima > 0`) en 0% se colaba. Propuesta de criterio publicada en el issue antes de construir (`Guia.bloqueo_ponderaciones() -> str | None`, recorre todos los sistemas de la materia, mensaje concreto "Falta asignar N%.../Sobra N%..."), sin objeción, autorizado a proceder por ser de bajo riesgo. Primer PR correcto en fix/tests/RUP del propio CU -- pero el **audit-del-clúster encontró 4 gaps reales fuera de `enviarGuiaARevision`**: los dos diagramas de clases consolidados sin el método nuevo, y un ejemplo de respuesta 422 en la ficha de Desarrollo que habría quedado directamente falso tras el merge. Devuelto al constructor con la lista completa (no reactivo), corregido en un segundo commit, reverificado antes de aprobar. Desplegado, verificado en producción.

#### 4. #212 (solo RUP) -- PR #216, `a1e6c2d`, tres rondas de audit-del-clúster

Deriva pre-#206 en `abrirGuia` (`profesorado`/`puede_revisar` ausentes de Análisis/Diseño) y `abrirPonderacionesEvaluacion` (segunda lectura de `SistemaEvaluacion` sin reflejar). El constructor contó las lecturas reales contra el código en vez de asumir "dos más" (`profesorado`/`asignatura_grado` viajan precargados en la misma consulta, solo `puede_revisar` es una lectura nueva genuina), y corrigió de oficio una caracterización errónea preexistente de `puede_revisar` en `RUP/04-desarrollo/README.md` (no es un toggle de UI, es defensa en profundidad -- verificado contra `AbrirGuia.tsx` antes de escribirlo). **El propio constructor aplicó el audit-del-clúster de forma proactiva, sin que se lo pidiera**, encontrando y corrigiendo 5 gaps (diagramas de clases, `03-diseño/README.md`, dos fichas de Desarrollo, nota de `consultarEstadoGuias` señalando fuera de alcance una deriva distinta que no cerró). Mi propia ronda final de verificación encontró un **sexto gap** que ni el constructor ni su propio barrido cazaron (`configuracion-proyecto.md`, conteo de funciones desactualizado) -- corregido en un tercer commit. Solo RUP, sin despliegue.

Cada afirmación factual del PR (precarga en `GuiaRepository.obtener()`, `GradoRepository.dirige()`, `Promise.all` en el frontend, orden exacto del campo Profesorado en wireframe y en `AbrirGuia.tsx`, los tres schemas Pydantic contra los JSON de ejemplo, `GuiaResumenResponse` real) verificada contra el código, no contra el resumen del constructor -- todo exacto, cero hallazgos falsos.

#### 5. Discussion #140 cerrada, #131 anotada, #213 cerrada

`Diseño (pausado): Cronograma de sesiones` (#140, "retomar sábado" desde el 29-08) cerrada: `Sesion` implementa las 4 decisiones de diseño allí cerradas, construido desde #199 y completado en #206 -- título limpiado, etiquetas de bitácora aplicadas. Los "2 IDOR de cuerpo" de discussion #131 (ya cerrada) anotados como resueltos desde `ab0f753`, sin reabrir la discussion. #213 (retrospectiva de #206) cerrada con el resumen completo de las tres piezas y evidencia concreta de que el cambio de proceso propuesto (§6.1, audit-del-clúster) funcionó -- incluida la lección de que ninguna pasada única agota el árbol RUP completo, ni siquiera cuando el método ya se interiorizó.

**Error propio, corregido**: el primer intento de cerrar #213 se publicó por error en discussion #206 (node id equivocado, copiado de una consulta anterior sin volver a verificarlo). Detectado antes de cerrar nada, corregido con un segundo comentario en el hilo correcto y un pointer cruzado -- ningún contenido se perdió, pero confirma la utilidad de verificar el id de destino antes de cada mutación GraphQL cuando se opera sobre varias discussions en la misma sesión.

### Estado del proyecto

- **pyCelda**: `main` en `a1e6c2d` (post-#216). Producción en `5cad9f8` (post-#215 -- #216 no despliega, es solo RUP). Deuda de #206 completa: #210/#208/#212 cerrados. Discussions #206 y #213 cerradas (`concluida`+`aplicado`), #140 cerrada. Tag sigue `v0.6.0`, sin bump (fuera del alcance delegado esta tanda).
- **pySesion**: sin tocar.
- **pySigHor**: esta Conversación 59 en `leConsultor`. Remote `origin` corregido a `pySigHor.git`. Clon `pyCelda-verify-pysighor` recreado y al día en SDF1.
- **Deuda nueva, sin issue todavía**: `RUP/04-desarrollo/casos-uso/consultarEstadoGuias/README.md` tiene su propia deriva de RUP (comparación con `AbrirGuiaResponse` obsoleta, `GuiaResumenResponse` real con 4 campos que la ficha no refleja) -- detectada como efecto colateral del audit de #212, señalada en el propio README, deliberadamente sin issue propio (fuera del alcance delegado). Candidata para cuando se retome pyCelda.
- **Pendientes heredados sin fecha, sin tocar**: issues #179/#181/#184/#185/#187/#202; `CursoAcademico`/`activarCursoAcademico()`; 2 IDOR de cuerpo de discussion #131 -- **ya no aplica, verificado resuelto en #210**; issue #148; auditoría de `curso`/`semestre` (discussion #128); grupo 3 de textareas; resto del Excel de planificaciones docentes de GII (~33 hojas sin curar).

### Para próxima sesión

Sin tarea activa de la deuda de #206 -- completa. Si se retoma pyCelda: considerar abrir issue para la deriva de `consultarEstadoGuias` antes de que crezca más (mismo patrón que motivó #212). Confirmar máquina contra `machine-id.md` al arrancar; si se retoma desde `oficina`, el clon de verificación y su toolchain (con `plantuml` en la versión que sea) viven ahí, no en SDF1 -- no asumir que el de SDF1 recreado hoy sigue siendo el vigente si pasa mucho tiempo sin uso.

---

*"Hacer las cosas bien no es pedantería académica: es inversión que se amortiza en cada línea de código escrita después."*

---

## Conversación 60: v1 del render de la guía docente en pyCelda -- plantilla oficial UNEA, `descargarGuiaPDF()` real + CU nuevo `previsualizarGuia()`, en producción
**Fecha**: 2026-09-03
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor como orquestador/revisor, `Claude-pySigHor-Oficina`), `Claude-pyCelda-Oficina` (constructor, apoyándose en OpenCode), `Claude-pyCelda-Prometeus` (despliegue)

### Contexto de la sesión

Retoma desde `oficina` (máquina confirmada contra `machine-id.md`, coincide con el nombre de la sesión -- emparejamiento homogéneo con `Claude-pyCelda-Oficina`). La deuda de #206 quedó completa en la Conversación 59; sin tarea activa al arrancar. Manuel trae **una plantilla de Guía Docente en Word** (`docs/PROPUESTA_PLANTILLA/Formulario-UNEA_GuiaDocente.docx`, oficial de la universidad): es lo que quiere que `pyCelda` exporte a partir de cada `Guia`, no en Word sino en HTML exportable a PDF.

### Desarrollo principal

#### 1. Discussion #217 -- el "qué" (diagnóstico de encaje de la plantilla)

Convertida la plantilla a texto (`soffice --headless`), contrastada bloque a bloque contra el modelo de dominio de pyCelda (`main` en `a1e6c2d`) y contra las guías reales (`docs/GII-IYA009.pdf`). Diagnóstico publicado como cuerpo, tres preguntas una por comentario. Respuestas de Manuel:

- **Plantilla oficial** = fuente de requisitos. El formato de salida sí es libre (HTML->PDF).
- **Enfoque B (incremental)**: escalar `generarGuiasPDF()`/`descargarGuiaPDF()` con lo que el modelo rinde hoy (6 bloques), el resto de gaps al backlog en su propio ciclo RUP.
- **Competencias**: ya resuelto en el modelo de dominio (entidad unificada `ResultadoAprendizaje`, sin clase `Competencia`). Matiz nuevo de Manuel, anotado en `project_pycelda_arquitectura_decisiones.md` y en el bullet del modelo de dominio: la universidad migra grado a grado de "Competencias" a "Resultados de aprendizaje", y **`ResultadoAprendizaje.tipo == "General"` es el discriminador del estado de esa migración** -- un grado con algún RA `"General"` no está migrado (sus RA son competencias), sin ninguno ya lo está; nunca coexisten los dos regímenes. El bullet del modelo decía "probablemente quede sin uso pronto" -- desmentido.

Gaps identificados que NO son de plantilla sino de requisitos/modelo (backlog ordenado por Manuel): normalizar `ReferenciaBibliografica.tipo`, requisitos previos, tabla de actividades formativas con horas/presencialidad, convocatoria extraordinaria, marca de superación obligatoria, distinción RA titulación/optativa, validación de forma de contenidos.

#### 2. Discussion #218 -- el "cómo" (motor de render)

D1-D4 cerradas con Manuel: **PDF oficial + página HTML subproducto de la misma plantilla** (D1); **WeasyPrint** (Jinja2 + CSS Paged Media, no Chromium) (D2); **re-render desde la fila `Guia` en cada descarga, sin almacenar bytes** (D3, `generarGuiasPDF()` intacto); **una sola plantilla** `backend/app/templates/guia_docente.html` + logo en `backend/app/static/` (no en `images/` ni `docs/` -- no viajan en la imagen Docker, familia #202) (D4).

P1-P4: **P1 = B, los RA se leen en vivo de `AsignaturaGrado`, NO se materializan** (razón de Manuel: los RA no deberían cambiar una vez definidos; materializarlos los duplica). Consecuencia: el v1 no toca modelo de dominio, sin migración de esquema, sin backfill. Deuda registrada en **issue #219** (`editarResultadoAprendizaje()` sobre la descripción altera guías ya aprobadas -- el reparto es inmutable pero la descripción no). P2 no aplica. **P3 = A**: la vista HTML usa la misma auth que `abrirGuia()` (`Profesor` autor + `DirectorGrado`), `Admin` fuera del v1. **P4**: vista HTML en cualquier estado, con banda de aviso roja si la guía no está `Aprobada`.

CU nuevo **`previsualizarGuia()`**: verbo nuevo del vocabulario cerrado, propuesto por el constructor con el precedente de `selecciona`, **ratificado por Manuel**. Ruta `GET /api/v1/guias/{id}/vista`.

#### 3. Desglose RUP del constructor y checkpoint intermedio

El constructor (`Claude-pyCelda-Oficina`, emparejamiento homogéneo) publicó el desglose RUP en #218 -- aprobado con matices. Se acordó **un solo PR** (RUP + código) con un **checkpoint intermedio**: comitear la prosa RUP en la rama, pushear y esperar revisión antes de escribir código (lección de la Conversación 58 / retrospectiva #206: la consolidación de RUP no es un añadido opcional del PR de feature).

Revisión del checkpoint (`e0c7be9`) en clon dedicado: recuentos de catálogo correctos (91 -> 96, verificados contra las carpetas reales: 98 en `03-detalle` = 96 + 2 primitivas, 89 fichas por fase). Un hallazgo real, **el patrón #213 otra vez**: los números que describen los diagramas *consolidados* (`"42 colaboracion.puml"`, `"88 secuencia.puml"`, `"21 colaboraciones"`) estaban stale en `main` desde antes de L10 y el constructor los había tocado a medias (un `+1` sobre un número mal por 47). Devuelto con la instrucción de grep completo de todos los números de diagrama consolidado y una sola pasada -- el constructor encontró más de los que yo señalé (`configuracion-proyecto.md`, `04-desarrollo/README.md`) y arregló el conjunto. Segundo cambio: las fichas de Desarrollo decían "✅ Completado" sin código -> a "🚧 RUP escrito, código pendiente" hasta que entrara el código.

#### 4. PR #221 -- código, revisión, dos rondas de fix

Clon de verificación **`pyCelda-verify-pysighor` recreado en `oficina`** (el de SDF1 quedó de la Conversación 59; el rol se ejecuta desde varias máquinas y el clon vive donde corrió la última tanda). venv con WeasyPrint 69.0 -- **las libs de sistema (pango/cairo/harfbuzz) ya estaban por el escritorio KDE, sin sudo**, así que la autoverificación real del PDF se pudo hacer aquí (el entorno del constructor tiene poetry roto y no puede instalar libs).

Verificación independiente de `db63cc6`: 453/453 tests (ejecución real, no el resumen del constructor); **PDF real generado** con WeasyPrint sobre una `Guia` rica y contrastado a ojo contra `GII-IYA009.pdf` -- layout fiel. Hallazgos:

- **Bloqueante**: la cabecera decía "GUÍA DOCENTE" **sin año** (`CursoAcademico` no está modelado). Expuesto a Manuel como decisión -> **constante de config** `Settings.curso_academico_vigente` (default "2026-2027") + **issue #222** para sustituirla por `CursoAcademico`.
- **No bloqueante aplicado**: viñetas de lista con guion largo (`\2013`) -> guion normal (regla tipográfica de Manuel + coherencia con `GII-IYA009`).
- **No bloqueante diferido**: logo SVG de 54 KB inline en base64 por respuesta (**issue #223**); `_contexto` usa `db.get(Grado, guia.grado_id)` (columna desnormalizada) en vez de la ruta estructural -- push-back razonado del constructor aceptado (consistente con `_es_director_de_la_guia`/`listar_del_grado`, robusto frente a `asignatura_grado is None`).
- **Deriva pre-existente del audit del clúster**: `descargar_guia_pdf` es `Profesor`-only en código vs su RUP con actor `Admin` -> **issue #220**, no tocado en esta tanda.

Re-check de `2a39aea` + `4ce674b`: 454/454, cabecera "GUÍA DOCENTE 2026-2027" y viñetas "-" verificadas en render real. (El `4ce674b` corrigió una regresión del propio constructor: el `<title>` perdió el acento al quitar un `--`.)

#### 5. Merge y despliegue

Manuel dio la palabra: merge + despliegue, y **fijó el canal de despliegue: pasa por pySigHor, el nodo constructor NO habla con Prometeus** (hub-and-spoke). Autorización explícita para dirigir la tanda ("lo que pida pySigHor, el constructor lo ejecuta").

- Merge: `13fcd94` (merge commit, no squash -- convención de pyCelda, los 6 commits conservados). Lo hizo el constructor.
- Despliegue: coordinado por mí con Prometeus. Build de imagen backend (capa apt de WeasyPrint: `libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz0b fonts-dejavu-core`) + caddy (frontend tocado). Sin migración. `apt-get update` no falló, sin `--no-cache`.
- Verificación independiente desde `oficina`: `/api/health` 200; rutas `/vista` y `/pdf` registradas (401 sin auth, no 404/500); bundle `index-fKWiju3i.js` servido; render de PDF real (WeasyPrint 69.0, `%PDF-1.7`, `<title>` con acento) contra el código exacto desplegado en mi clon.
- **Matiz operativo**: ninguna de las 108 guías tiene `fecha_generacion_pdf` seteada, así que `descargarGuiaPDF` devuelve 409 para todas. El timestamp lo pone `editarSemestreGuia()`/`generarGuiasPDF()`, ninguno disparado nunca. **El camino end-to-end vivo hoy es `previsualizarGuia()`** (vista HTML, cualquier estado).
- Dashboard `99-seguimiento`: `e5a9983` (commit directo a main, convención de pyCelda para docs de seguimiento), 95/95 -> 96/96.

#### 6. Error propio

Al justificar al constructor el commit directo a main del dashboard cité "**LEY 004** lo exceptúa". LEY 004 es una regla de **pySigHor** (rama `xRevisar` para artefactos RUP del propio port FastAPI/React), no existe en pyCelda y no aplica. El commit directo era correcto por la convención propia de pyCelda (precedente del git log), no por LEY 004. Corregido con el constructor.

### Estado del proyecto

- **pyCelda**: `main` y producción en `13fcd94` + `e5a9983` (dashboard, no despliega). v1 del render de la guía docente **en producción**. Discussions #217 (`concluida`/`pendiente` -- el backlog de gaps sigue abierto) y #218 (`concluida`/`aplicado`). Issues nuevos: **#219** (RA en vivo), **#220** (auth `Admin` del PDF), **#222** (`CursoAcademico` para el año), **#223** (logo SVG inline). Tag sigue `v0.6.0`.
- **pySesion**: sin tocar (Requisitos y Análisis cerrados, en pausa hasta Diseño).
- **pySigHor**: esta Conversación 60 en `leConsultor`. Clon `pyCelda-verify-pysighor` recreado y al día en **`oficina`** (con venv WeasyPrint) -- no en SDF1.
- **Memoria actualizada**: `project_pycelda_plantilla_guia_docente.md` (nuevo, historia completa de la tanda), `project_pycelda_arquitectura_decisiones.md` (bullet de `tipo == "General"`), `MEMORY.md` (pointer). El commit de myClaudeContext lo hace `Claude-pyCelda-Oficina` (se ofreció) -- recoge también estos cambios de pySigHor por ser repo compartido.

### Para próxima sesión

- **Ajuste adicional pendiente** que Manuel mencionó al cerrar, sin detallar -- preguntar.
- Siguiente pieza natural del render: escalar `generarGuiasPDF()` (`Admin`) o el flujo que setea `fecha_generacion_pdf`, sin lo cual el PDF oficial no llega a un usuario (solo la vista HTML).
- Backlog de #217: normalizar `ReferenciaBibliografica.tipo` es el primero, barato -- desbloquea el subbloqueo limpio de bibliografía.
- Deriva de `consultarEstadoGuias` (heredada de la Conversación 59) sigue sin issue.
- Confirmar máquina contra `machine-id.md` al arrancar. El clon de verificación vive en `oficina`.

---

*"Un documento oficial no debería salir sin el año: modelar la entidad completa es trabajo aparte, pero la constante de config cuesta una línea."*

---

## Conversación 61: v2 Frente A de la guía docente -- maquetación al formulario oficial, y el error de haberse basado en la guía vieja
**Fecha**: 2026-09-03 (noche) -- 2026-09-04
**Participantes**: Manuel (Usuario), Claude Sonnet 5 (Asistente, sesión pySigHor orquestador/revisor, `Claude-pySigHor-Oficina`), `Claude-pyCelda-Oficina` (constructor, contexto limpiado a mitad para entrar fresco a v2), `Claude-pyCelda-Prometeus` (despliegue)

### Contexto de la sesión

Continúa desde la Conversación 60 sin cortar sesión. Cerrada la tanda del v1 del render (PR #221, producción `13fcd94`), Manuel pidió: (1) escribir un `RESUMEN.md` del experimento de desarrollo con agentes en la raíz de pyCelda (publicación -- números del proyecto: ~20k LoC código, 7,8k tests, 23k RUP, 96 CU, 436 commits, 3,5 semanas de definición + 1,5 de construcción); (2) ajustes de maqueta del PDF.

### Desarrollo principal

#### 1. El diagnóstico que reabrió la maqueta

Manuel generó una guía, la aprobó, y no encontraba cómo generar el PDF. Diagnóstico: **no hay acción dedicada**. `fecha_generacion_pdf` solo lo sella `editar_semestre_guia` como efecto colateral (`guia.regenerar_pdf()`, DirectorGrado); `generarGuiasPDF()` (Admin, lote) especificado en RUP pero sin construir. Workaround: "Editar semestre -> guardar". Y `previsualizarGuia()` solo funciona para Profesor/DirectorGrado, no Admin (P3/opción a) -- si Manuel mira como Admin, 404.

Luego, revisando la cabecera repetida: la maqueta del v1 se basó **a ojo de `docs/GII-IYA009.pdf`** (una guía docente ya rellenada, formato antiguo) en vez de **`docs/PROPUESTA_PLANTILLA/Plantilla-GuiaDocente.pdf`** (el formulario oficial en blanco, 7 páginas, que Manuel también había puesto en el repo). El contenido salió bien (venía del `.docx`), el aspecto no. Renderizadas las 7 páginas del formulario oficial y contrastadas sección por sección: logo arriba izquierda (no centro), título en texto azul sin banda de fondo, secciones numeradas, celdas de etiqueta en azul saturado, campos "CENTRO"/"DOCENTE"/"EMAIL" (no "Facultad"/"Profesorado"/...). Manuel llevaba cinco ajustes sueltos reconstruyendo el formulario de memoria; se decidió una pasada de maquetación con `Plantilla-GuiaDocente.pdf` como única fuente visual.

#### 2. Discussion #224 -- v2, dos frentes

**Frente A -- maquetación al formulario oficial.** Todas las decisiones cerradas con Manuel: logo izquierda 75% + regla azul, título sin banda solo pág 1, secciones numeradas 1-6, celdas azul saturado, pie "Página X de Y" abajo derecha, **marca de agua diagonal "BORRADOR - NO OFICIAL" en todas las páginas** del PDF cuando `estado != Aprobada` (la vista HTML conserva la banda roja). 6 secciones siempre presentes con esqueleto: `_REQUISITOS_PREVIOS_AQUI_`, tabla de 10 actividades formativas en blanco (sustituye el marcador `ACTIVIDADES_FORMATIVAS_AQUI`), extraordinaria con texto fijo y "pendiente de concretar", 4 subsecciones fijas de bibliografía. "Interés y participación del alumno" NO es fila fija -- ponderación normal del profesor. Sin modelo, sin migración.

**Frente B -- `generarGuiaPDF()` para el usuario.** CU nuevo singular (DirectorGrado, `POST /guias/{id}/generar-pdf`, 409 si no Aprobada, reutiliza `regenerar_pdf()`), + cierre de #220 (`descargar_guia_pdf` Profesor-only -> `_tiene_acceso_a_guia`). **Manuel lo aparcó** ("no lo veo complejo") -- desglose cerrado en el hilo, sin construir.

Preguntas del desglose del constructor (8), resueltas: Análisis/Diseño de Frente A se tocan ligero; HTML conserva banda roja; ruta `/generar-pdf` no `/pdf`; 409; dos PRs; mapeo de bibliografía sobre valores reales de producción.

#### 3. El constructor entró fresco

Manuel limpió el contexto de `Claude-pyCelda-Oficina` para que entrara sin arrastre a v2. Briefing completo (bootstrap + encargo #224). Desglose RUP -> checkpoint de la prosa (8 fichas, 96/96 sin CU nuevo) -> revisión en clon dedicado.

**Deriva stale de #218 -- dos líneas, no una.** El barrido del constructor sobre "placeholder" cazó una (`04-desarrollo/README.md`); mi verificación independiente encontró la segunda (`editarSemestreGuia/README.md:26`). El patrón #213 recurrente: ninguna pasada única agota el árbol, conviene que barran los dos nodos por separado. Ambas dobladas en el PR-A.

#### 4. PR #225 -- código, un bloqueante

Plantilla reescrita a la maqueta oficial + `_contexto()` con flag `vista_html` (banda en HTML / marca de agua en PDF) + `_subseccion_biblio()` con mapeo defensivo. Prometeus consultó producción: `referencias_bibliograficas.tipo` tiene `Complementaria`/`Básica`/`Web` (seed), pero el frontend ofrece `"Webs de referencia"` y `"Otras fuentes de consulta"` -- **dos vocabularios**, columna libre sin validación. Registrado como **issue #226**, ligado al backlog #1 de #217. El mapeo trata ambos.

Verificación en clon dedicado con PDF real: 463/463 tests, maqueta fiel al formulario oficial. **Un bloqueante**: la marca de agua a 42pt con `left:0; right:0` hacía *wrap* a dos líneas y se recortaba por los dos bordes -- ilegible. Fix: `top:50%; left:50%; transform: translate(-50%,-50%) rotate(-45deg); white-space:nowrap; font-size:38pt` (commit `659e484`). Re-verificado: una línea diagonal limpia, centrada, tenue, repetida en las 3 páginas. Nits (cabecera de tabla a mayúsculas, prosa RUP sin corchetes) aplicados.

#### 5. Merge y despliegue

Merge `c21212f` (merge commit). Despliegue coordinado por pySigHor con Prometeus (el constructor no habla con Prometeus). Solo rebuild de backend (plantilla + módulo de render; sin migración, sin deps, sin env var, frontend intacto -- `deploy.sh` reconstruye caddy igual, mismo hash de bundle). Verificación: Prometeus rasterizó 3 PDFs en producción (Aprobada sin marca de agua, Borrador/EnRevisión con marca de agua diagonal, secciones 1-6, celdas azul saturado, pie "Página X de Y"); pySigHor `/api/health` 200 + visual en clon contra el SHA desplegado.

**Observación de Prometeus sin resolver**: `_REQUISITOS_PREVIOS_AQUI_` sale como literal en caja gris monoespaciada en el PDF -- Manuel lo aprobó (campo no modelado, backlog), pero se lee como una variable de plantilla sin resolver. Reconsiderar cuando empiecen a generarse PDFs de verdad.

### Estado del proyecto

- **pyCelda**: `main` y producción en `c21212f`. Render de la guía docente v1 + v2 Frente A en producción. Discussions #217 (`concluida`/`pendiente`), #218 (`concluida`/`aplicado`), #224 (`en-curso`/`pendiente` -- Frente B aparcado). Issues: #219, #220, #222, #223, #226. Catálogo 96/96. Tag `v0.6.0`. `RESUMEN.md` en la raíz (`1b8307a`).
- **pySesion**: sin tocar.
- **pySigHor**: esta Conversación 61 en `leConsultor`. Clon `pyCelda-verify-pysighor` en `oficina` con venv WeasyPrint 69, al día con `main`.
- **Memoria**: `project_pycelda_plantilla_guia_docente.md` reorganizado con bloques "ESTADO ACTUAL" + "PENDIENTES" arriba. Commit myClaudeContext `1a1d391` (más `cef40f6` de Prometeus).

### Para próxima sesión -- encargo activo

**Seguir ajustando la maqueta del PDF de la guía docente.** Manuel revisa los PDF de muestra y pide cambios; es iteración de plantilla (`guia_docente.html` + `_contexto()`), sin modelo. Pendientes concretos en `project_pycelda_plantilla_guia_docente.md` "PENDIENTES":

1. Más ajustes de maqueta según lo que Manuel vea.
2. `_REQUISITOS_PREVIOS_AQUI_` literal -> ¿"Pendiente"/"No aplica"?
3. Frente B (`generarGuiaPDF()` DirectorGrado + #220), aparcado, desglose ya cerrado en #224.
4. Backlog de #217 (7 gaps) -- normalizar `ReferenciaBibliografica.tipo` (#226) es el primero y barato.
5. `generarGuiasPDF()` en lote -- depende de `CursoAcademico`.

Confirmar máquina contra `machine-id.md` al arrancar. El clon de verificación vive en `oficina`.

---

*"La maqueta se basó en la guía vieja rellenada, no en el formulario oficial en blanco. El cliente lo detectó preguntando en qué me había basado -- la pregunta correcta antes de aceptar un iterar-ajuste-a-ajuste."*

---

## Conversación 62: purga "módulo"->"materia" (#252/#253, checkpoint sin cerrar) y diseño de #254 -- profesorado de la Guia sin mantenedor

**Hueco 61->62.** Este log se quedó en la 61. Entre medias hubo varias sesiones cuyo registro real vive en la memoria de proyecto, no aquí: cierre de Frente B / PDF-al-aprobar (#238), tanda de 8 issues técnicos (#240-#245) + tag **`v0.7.0`**, portada de guías (#239), y el **pase de cierre de issues de abajo arriba** -- #14 (→ #248/#249), #23, #181 (PR #250, FK real `AsignaturaGrado.asignatura_id`), #184 (PR #251, importar bibliografía/planificación entre `AsignaturaGrado` hermanas). Producción efectiva en `ab2febe`, `main` en `b6d7701`. Ver `project_pycelda_transferencia_rup.md` (índice), `project_pycelda_tanda_8_issues_tecnicos.md`, `project_pycelda_limpieza_issues_abiertos.md`, y las discussions [#246](https://github.com/mmasias/pyCelda/discussions/246)/[#247](https://github.com/mmasias/pyCelda/discussions/247). El diario narrativo se ha vuelto stub a favor del sistema de memoria (patrón ya anticipado en `feedback_memoria_un_fichero_un_hecho`).

### 1. Manuel creó tres issues; pySigHor los revisó y corrigió

- **#252**: la vista Admin de `AsignaturaGrado` (`AsignaturaGradoAdmin.tsx`) solo tiene "Volver al Grado"; la del DirectorGrado ya tiene el par "Volver al Grado" + "Volver a la materia". Añadir el segundo. Impacto RUP: la ficha `abrirAsignaturaGrado` documenta ese 2.º retorno como "exclusivo de DirectorGrado" -- deja de serlo.
- **#253**: botón "Volver al módulo" -> "Volver a la materia". Manuel lo amplió a **purga completa** de "módulo" (sinónimo de Materia) -> "materia" en UI **+ artefactos RUP de esas pantallas** (opción confirmada por él). Fuera: `Login.tsx`/`AdminLogin.tsx` ("Módulo académico"/"de Administración" = área de la app), y todo "módulo de código" en `03-diseño/`.
- **#254**: la delicada. Ver punto 2.

Encargo de #252+#253 al constructor (`Claude-pyCelda-Oficina`) -- una rama, un PR, con los `file:line` pre-rastreados en clon por pySigHor y la nota de Manuel de apoyarse en OpenCode para el barrido mecánico.

### 2. #254 -- debate largo, lento y socrático con Manuel; cerrado en discussion #255

Manuel condujo el análisis paso a paso ("muy, muy lentamente, sin adelantarnos"). pySigHor verificó cada afirmación contra el código y contra **datos de producción** (consulta de solo lectura vía Prometeus).

**Diagnóstico**: `guia.profesorado` (`guias_profesores`) es una copia materializada que **nunca se re-deriva** de `asignatura_grado.profesorado`. Se siembra al nacer la guía (o en la 1.ª asignación si la copia está vacía) y después nada la actualiza -- ni aprobar, ni `regenerar_pdf()`, ni editar, ni `desasignar`. `Guia.contenido` es el mismo tipo de campo (copia sembrada, patrón #191) pero **tiene mantenedor** (el profesor lo reescribe cada curso, y editarlo degrada `Aprobada->Borrador`). `Guia.profesorado` no tiene camino de edición: es el hueco. Producción: 6 de 108 guías divergen (1, 5, 13, 30, 64, 100), todas copia < plantilla.

**Solución acordada** (detalle en #255 y en `project_pycelda_profesorado_guia_254.md`):
- `aprobar()`/`escalar_a_aprobada()` re-derivan `guia.profesorado := list(asignatura_grado.profesorado)` (Fat Model).
- El Admin, al cambiar la plantilla de verdad y si la guía activa está `Aprobada` -> la pasa a `EnRevision` + fila de `HistorialCambio` (`autor_id=0` centinela, comentario "En revisión por cambio en los profesores que la imparten"), expuesta como banner. Otros estados: transparente.
- Vistas en la app -> plantilla **en vivo**, siempre. PDF/previsualización -> copia **congelada**, siempre.
- Solo guías activas; las archivadas (con #222) quedan congeladas. Consecuencia interina aceptada: al desasignar de todo + re-aprobar, el profesor pasa a ser borrable físicamente.
- Reconciliación de las 6 por opción (a): migración pone las `Aprobada` en `EnRevision`, Manuel re-aprueba por UI -- **prueba de aceptación del mecanismo con datos reales**.
- Arista **nueva en la máquina de estados de `Guia`**: `Aprobada -> EnRevision` por acción administrativa. Checkpoint de prosa RUP obligatorio.

**Error propio**: al publicar el primer análisis en #255 me inventé el node-id de la discussion y el comentario cayó en un repo público ajeno (`libigl/libigl` #2506); detectado en ~30 s, borrado, republicado en el sitio correcto. Método corregido: consultar el id, nunca construirlo.

### Estado del proyecto

- **pyCelda**: producción en `ab2febe`, `main` en `b6d7701` (RUP derivado encima, a propósito). Tag `v0.7.0`.
- **#252/#253**: checkpoint de prosa RUP del constructor pusheado a `cc/purga-modulo-materia-252-253` (`9bfb635`, 37 ficheros: RUP 4 fases + 10 SVGs + `generar_modelo_datos.py` + `DER.puml`/`DER.svg`). El constructor amplió a `RUP/00-modelo-del-dominio/README.md` + DER -- pendiente que pySigHor confirme o revierta. **Revisión de pySigHor en clon SIN HACER** (aparcada por saldo). Código del frontend escrito por el constructor pero fuera del checkpoint hasta el OK.
- **#254**: diseñado y cerrado en discussion #255. **Sin construir.**
- **pySesion**: sin tocar.
- **Memoria**: nuevo `project_pycelda_profesorado_guia_254.md`; `project_pycelda_limpieza_issues_abiertos.md` y `MEMORY.md` actualizados. Commit myClaudeContext de esta sesión (ver tag `stable-*`).

### Para próxima sesión -- encargos activos

1. **Revisar el checkpoint de #252/#253** en `cc/purga-modulo-materia-252-253` (`9bfb635`): `tsc`+`vite build`, 10 SVGs por contenido, grep "módulo" limpio, coherencia UI<->wireframe, la reescritura de la prosa de asimetría de `abrirAsignaturaGrado`, y decidir sobre la ampliación al Modelo del dominio + DER. Luego: el constructor mete el código -> PR -> revisión del PR -> despliegue coordinado con Prometeus (`./deploy.sh` estándar, sin migración de esquema).
2. **Encargo de #254** al constructor cuando Manuel dé el "adelante": checkpoint de prosa RUP primero (arista nueva en la máquina de estados de `Guia`, fichas en 4 fases, migración de datos para las 6). Detalle completo en discussion #255 y `project_pycelda_profesorado_guia_254.md`.
3. De fondo, el pase de issues sigue en **#219** (RA en vivo) y luego **#222** (`CursoAcademico`, del que #254 depende para "solo guías activas").

Confirmar máquina contra `machine-id.md` al arrancar. El clon de verificación vive en `oficina`.

---

*"Sí hay lógica, pero es invisible y está diseñada para un futuro que todavía no existe. `Guia.contenido` tiene quien lo mantenga; `Guia.profesorado` no tiene a nadie."*

---

*Este registro se actualizará continuamente conforme avance el rol de orquestador.*
