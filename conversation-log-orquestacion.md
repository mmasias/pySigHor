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

*"Hacer las cosas bien no es pedantería académica: es inversión que se amortiza en cada línea de código escrita después."*

---

*Este registro se actualizará continuamente conforme avance el rol de orquestador.*
