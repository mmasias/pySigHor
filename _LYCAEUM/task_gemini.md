# RONDA 1 — Tarea para Gemini

## Objetivo global
Determinar cuáles son los próximos pasos más prioritarios para el proyecto pySigHor, dado que la Iteración 1 del Vertical Slice está completa.

## Tu tarea esta ronda

Analiza el proyecto desde su dimensión pedagógica y estratégica para proponer la secuencia de próximas iteraciones que maximice el valor didáctico para alumnos universitarios de ingeniería de software.

Concretamente, responde:

1. **Valor pedagógico diferencial de cada iteración**: El proyecto tiene ~26 casos de uso agrupados en entidades (Edificios, Cursos, Profesores, Recursos, Horarios). Desde el punto de vista didáctico, ¿cada iteración adicional enseña algo nuevo, o a partir de cierto punto se convierte en repetición mecánica? Identifica qué concepto nuevo introduce cada grupo de CdU y en qué punto la curva de aprendizaje se aplana.

2. **Momento óptimo para introducir pruebas (testing)**: La columna "Pruebas" del dashboard está vacía en todos los CdU. ¿Cuándo debe introducirse el testing en la narrativa didáctica del proyecto: antes de Iteración 2, después de completar las entidades CRUD básicas, o solo cuando se llegue a `generarHorario()`? Argumenta.

3. **El salto hacia `generarHorario()`**: Este caso de uso es el núcleo del sistema legacy (algoritmo de 4 fases en VB3.0). Desde la perspectiva del proyecto como herramienta didáctica, ¿cuándo y cómo debería introducirse este CdU para que tenga el máximo impacto? ¿Tiene sentido implementar todas las entidades CRUD primero, o es mejor introducir `generarHorario()` en paralelo como hilo conductor?

## Contexto relevante

- El proyecto tiene propósito dual: modernización técnica del sistema SigHor (1998, VB3.0) + material didáctico para alumnos universitarios
- La audiencia son alumnos universitarios de ingeniería de software
- Iteración 1 completa: iniciarSesion, abrirAulas, crearAula, editarAula, eliminarAula
- Iteraciones planificadas: Edificios → Cursos → Profesores → Horarios → Consultas → Reportes
- El caso de uso `generarHorario()` implementa un algoritmo de investigación de operaciones (optimización combinatoria)
- Manuel es el docente que usa este proyecto como caso de estudio con sus alumnos

## Formato de respuesta esperado

- Tabla: CdU / Concepto nuevo que introduce / Valor didáctico (alto/medio/bajo/repetición)
- Recomendación clara sobre cuándo introducir testing (con justificación de 2-3 líneas)
- Una propuesta narrativa de cómo estructurar las iteraciones restantes como historia didáctica coherente (no como lista de tareas)
