# Prompt: transferir criterio de análisis RUP de pySigHor a pyCelda

Repo de referencia (pySigHor): `/home/manuel/misRepos/_PROYECTOS/pysighor`
Todas las rutas de la Fase A, B y C de este prompt son relativas a esa raíz.

---

Vas a interiorizar el criterio metodológico de análisis RUP de otro proyecto
(pySigHor) para aplicarlo, con juicio propio, a la transición
Requisitos → Análisis de pyCelda, que acabas de completar en Requisitos
(catálogo de 91/91 casos de uso cerrado).

No es una plantilla a copiar literalmente: pySigHor tiene su propio dominio
(horarios universitarios) y su propia historia. Extrae el criterio, no el
texto. Y no todo en pySigHor es perfecto — varios documentos son errores
detectados y corregidos: extrae la lección, no el error como ejemplo a
seguir.

Nota de contexto: pyCelda ya practica auditoría cruzada de dos modelos
independientes (docs/AUDITORIAS/), algo que pySigHor sólo descubrió a mitad
de proyecto (ver Fase C más abajo). No partes de cero en rigor — partes con
una fase de Requisitos más exhaustiva que la de pySigHor en su momento. Lo
que buscas es lo específico de la transición a Análisis, que en pyCelda
todavía no existe.

Lee en este orden (repo pySigHor, `/home/manuel/misRepos/_PROYECTOS/pysighor`):

## FASE A — Reglas explícitas (constitución del proyecto de referencia)

1. `CLAUDE.md` (raíz del repo) completo
2. `extraDocs/999-leyes-proyecto/` — los ~6 archivos: `contexto-proyecto.md`,
   `ley-rama-revision.md`, `protocolo-gestion-contexto.md`,
   `ley-005-protocolo-gestion-dudas.md`, `coloresRUP.md`, `como-esquematizar.md`

## FASE B — Forma del artefacto de Análisis (lo que pyCelda no tiene todavía)

3. `RUP/01-analisis/README.md`
4. Estos 3 casos de uso completos, en sus dos capas — Requisitos
   (`RUP/00-casos-uso/02-detalle/<CU>`) y Análisis
   (`RUP/01-analisis/casos-uso/<CU>`) — para ver exactamente qué cambia al
   pasar de una capa a otra:
   - `crearAula`                (CRUD simple, caso base)
   - `asignarProfesorACurso`    (caso de relación)
   - `generarHorario`           (caso complejo, motor del sistema)
5. `RUP/01-analisis/clases-analisis*.puml` (las 4 variantes — cómo se
   deriva el diagrama de clases de análisis desde los CUs)

## FASE C — Artículos que codifican criterio de esta transición específica

6.  `extraDocs/008-filosofia-crud-creacion-edicion` — criterio C→U para CRUD,
    aplica directo a los ~40 CUs abrir/crear/editar/eliminar de pyCelda
7.  `extraDocs/011-sobreoptimizacion-llms-navegacion-rup` — antipatrón: un
    LLM anticipando pasos que no le corresponden en la transición
8.  `extraDocs/012-reflexion-fase-analisis-completada` — qué aspecto tiene
    una fase de Análisis terminada, métricas de completitud, criterios de
    cierre. Es la foto de destino: a dónde debe llegar pyCelda en esta
    disciplina.
9.  `extraDocs/013-consolidacion-arquitectonica` — triangulación con
    equipos independientes para la transición Análisis→Diseño. Relee esto
    sabiendo que pyCelda YA tiene la infraestructura de auditoría dual: la
    pregunta útil no es "cómo empiezo a auditar" sino "en qué momento de
    Análisis conviene disparar la primera pasada dual, y con qué aspectos
    nuevos (no los 8 ya cubiertos en Requisitos)".
10. `extraDocs/024-auditoria-diseno-vs-implementacion` +
    `extraDocs/025-postAuditoria` — 20 desviaciones diseño↔código
    encontradas y corregidas. Aplica el mismo tipo de pregunta hacia atrás:
    ¿qué desviaciones Requisitos↔Análisis hay que vigilar cuando aparezcan
    clases de análisis que no reflejan fielmente lo que el caso de uso
    especifica?
11. `extraDocs/026-mapaRUP` — mapa de qué disciplina RUP produce qué
    artefacto concreto, para situar Análisis en el mapa completo
12. `extraDocs/027-brecha-especificacion-diseno` — un requisito perdido
    entre especificación y diseño, implementado fielmente sin él.
    Advertencia concreta de qué vigilar al mapear CU → clases de análisis.

---

Al terminar, antes de tocar `RUP/02-analisis` (o como decidas nombrar la
carpeta) en pyCelda, abre un discussion en el que resumas en tus propias palabras (no cites literalmente):

- El patrón de artefactos de Análisis (Fase B) que vas a replicar en
  estructura para los 91 CUs de pyCelda, empezando por una muestra
  representativa (no los 91 a la vez).
- Los 5-6 criterios de juicio (Fase C) que vas a aplicar a la transición
  Requisitos→Análisis de pyCelda, con una frase de cuándo NO aplican
  literalmente por las diferencias de dominio (guías docentes con ciclo de
  aprobación vs horarios con motor de optimización).
- En qué punto del proceso de Análisis conviene la primera auditoría dual
  (Claude/glm), dado que ya tienes esa infraestructura — no reinventarla,
  sólo decidir el timing y los aspectos nuevos a auditar.

No propongas cambios de gobernanza del repo (CLAUDE.md, leyes-proyecto):
eso queda fuera de esta tarea, aunque una de las auditorías cualitativas
de pyCelda lo haya señalado como riesgo aparte.
