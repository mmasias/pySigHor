# Blackboard — pySigHor LYCAEUM

## Objetivo activo
Determinar cuáles son los próximos pasos más prioritarios para el proyecto pySigHor, dado que la Iteración 1 del Vertical Slice está completa.

## Contexto de partida (leído antes de Ronda 1)
- **Rama**: `diseño-fastapi-react`
- **Estado Iteración 1**: 5 CdU implementados (iniciarSesion, abrirAulas, crearAula, editarAula, eliminarAula) — backend FastAPI + frontend React
- **Documentación**: RUP completo para esos 5 CdU (requisitos → análisis → diseño → desarrollo)
- **Problema detectado**: dashboard (`RUP/README.md`) muestra ⚪ en columnas Desarrollo/Pruebas de los 5 CdU ya implementados
- **CdU pendientes**: 21 CdU tienen requisitos y análisis pero NO diseño técnico
- **Deuda técnica conocida**: usuario hardcodeado, sin tests, CORS permisivo

---

## Ronda 1
- Opencode: Arquitectura escalable sin refactor mayor. Credenciales hardcodeadas + usuario sin BD son bloqueantes reales para Iteración 2. Secuencia de iteraciones correcta técnicamente.
- Gemini: Mapa de valor didáctico por entidad (Profesores = M:N + pesos = preparación algorítmica = Alto). Testing desde Iteración 2 sobre entidades simples. Propuesta narrativa de introducir generarHorario() en Iteración 3 — invalidada por corrección de Manuel (fatiga intencional).
- Qwen: Tres riesgos reales: (1) dashboard inconsistente — cosmético, pero viola integridad documental; (2) usuario hardcodeado — deuda acumulativa, ventana estrecha; (3) 21 CdU sin diseño — riesgo pedagógico diferible. Detectó 5 CdU cuando son 6; no cambia el argumento de fondo.
- Estado: RESUELTO
