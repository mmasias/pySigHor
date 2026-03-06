# RONDA 1 — Tarea para Qwen

## Objetivo global
Determinar cuáles son los próximos pasos más prioritarios para el proyecto pySigHor, dado que la Iteración 1 del Vertical Slice está completa.

## Tu tarea esta ronda

Actúa como abogado del diablo: cuestiona las asunciones del plan actual e identifica riesgos no evidentes antes de que el proyecto avance.

Concretamente, analiza estas tres tensiones:

1. **Tensión entre trazabilidad RUP y velocidad de desarrollo**: El proyecto tiene documentación exhaustiva para los 5 CdU de Iteración 1 (detalle → análisis → diseño → desarrollo). Sin embargo, 21 CdU restantes solo tienen detalle y análisis, pero no diseño técnico (diagramas de secuencia, clases de diseño). La pregunta es: ¿es correcto pasar a Iteración 2 (código) sin tener diseño previo para esos CdU, o eso viola los principios RUP que este proyecto enseña? Si el proyecto es didáctico y RUP exige diseño antes de construcción, ¿no estaría el proyecto contradiciendo su propia metodología?

2. **El dashboard miente**: El archivo `RUP/README.md` muestra todas las celdas de "Desarrollo" y "Pruebas" en ⚪ (blanco/pendiente), incluidos los 5 CdU que ya están implementados y documentados en `RUP/03-desarrollo/`. Si un alumno consulta el dashboard, pensará que no hay nada implementado. ¿Debería ser prioritario corregir esta inconsistencia antes de añadir más funcionalidad? Argumenta si esto es un problema cosmético o un problema de integridad documental.

3. **Riesgo de la estrategia de Vertical Slice**: La Iteración 1 usa un usuario hardcodeado sin base de datos. Todas las iteraciones siguientes (Edificios, Cursos, Profesores) necesitarán una base de datos real con autenticación real. ¿Cuándo es el último momento seguro para introducir el cambio de usuario hardcodeado → usuarios en BD, sin que eso rompa todo lo construido? Si se espera demasiado, el refactor puede ser costoso.

## Contexto relevante

- El proyecto sigue metodología RUP estricta con fases: Requisitos → Análisis → Diseño → Desarrollo → Pruebas
- Solo 5 CdU tienen diseño técnico completo; 21 CdU tienen requisitos y análisis pero no diseño
- El dashboard (`RUP/README.md`) no refleja el trabajo de desarrollo ya realizado
- El sistema de autenticación actual usa un único usuario hardcodeado (`admin/admin`)
- El objetivo pedagógico exige coherencia metodológica visible para los alumnos

## Formato de respuesta esperado

- Para cada una de las tres tensiones: un veredicto claro (¿es un riesgo real o un falso problema?) + argumento en 3-5 líneas
- Una lista ordenada de los 3 problemas por urgencia (el más urgente primero), con justificación de por qué ese orden
