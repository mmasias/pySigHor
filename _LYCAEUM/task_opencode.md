# RONDA 1 — Tarea para Opencode

## Objetivo global
Determinar cuáles son los próximos pasos más prioritarios para el proyecto pySigHor, dado que la Iteración 1 del Vertical Slice está completa.

## Tu tarea esta ronda

Analiza el estado técnico de lo que se ha implementado en la Iteración 1 y evalúa si es correcto avanzar a la Iteración 2, o si hay deuda técnica que resolver primero.

Concretamente, responde estas tres preguntas:

1. **Deuda técnica de Iteración 1**: El código implementado incluye credenciales hardcodeadas (`username: admin`, `password: admin`), un único usuario sin base de datos, CORS permisivo, y sin tests automatizados. ¿Cuál de estos problemas es un bloqueante real para continuar hacia Iteración 2 (Edificios), y cuál puede diferirse?

2. **Arquitectura lista para escalar**: La estructura de directorios establecida en `configuracion-proyecto.md` (models/schemas/repositories/services/routers) fue diseñada para 5 CdU. ¿Es esa arquitectura suficientemente genérica para soportar ~26 CdU sin necesidad de refactorización mayor? Señala específicamente qué piezas hay que añadir para Iteración 2.

3. **Secuencia técnica óptima**: Las próximas iteraciones documentadas son: Edificios → Cursos → Profesores → Generación de Horarios → Consulta → Reportes. Desde una perspectiva puramente técnica (dependencias de datos, complejidad creciente, reutilización de patrones), ¿es correcta esa secuencia o propondrías alterarla?

## Contexto relevante

- Stack: FastAPI + SQLAlchemy async + JWT/bcrypt en backend; React 18 + TypeScript + Material-UI + Axios en frontend
- El código de Iteración 1 existe en la rama `diseño-fastapi-react`
- Archivos clave: `backend/app/routers/auth.py`, `backend/app/models/`, `backend/app/services/`, `frontend/src/`
- El documento `RUP/02-diseño/configuracion-proyecto.md` define la estructura del proyecto
- Hay 26 casos de uso identificados, de los cuales solo 5 tienen diseño técnico (diagramas de secuencia)

## Formato de respuesta esperado

- Una tabla de deuda técnica: problema / severidad (bloqueante / diferible) / justificación
- Un párrafo sobre la escalabilidad de la arquitectura actual
- Una evaluación de la secuencia de iteraciones: ✅ correcta / ⚠️ ajustar / ❌ reordenar, con justificación
