# Auditorias pySigHor

> [Metodología](metodologia.md) / [Cómo usar las auditorías](comoUsar.md)

Este directorio contiene todas las auditorias realizadas al proyecto pySigHor, organizadas por rama e iteracion.

## Indice de Auditorias

### [diseno-fastapi-react](./diseno-fastapi-react/)

**Stack Tecnologico**:
- Backend: FastAPI 0.100.1 + Pydantic 1.10.13 + SQLAlchemy 2.0.23
- Frontend: React 18 + Vite 5 + TypeScript 5 + Material-UI v5
- Base de datos: SQLite (desarrollo)

**Iteraciones Auditadas**:

#### [Iteracion 1](./diseno-fastapi-react/iteracion-1/) (2025-02-15)

- **Commit auditado**: `a8894e2`
- **Ver en GitHub**: https://github.com/mmasias/pySigHor/commit/a8894e2
- **Objetivo**: Autenticacion JWT + CRUD Aulas completo
- **Auditores**: Claude Sonnet (Anthropic), Codex (OpenAI), Qwen Code (Alibaba), Gemini (Google)

**Calificaciones**:
- **Tecnica**: 6.4/10 (Backend: 5.8/10, Frontend: 7.3/10, Docs: 7.0/10)
- **Proceso**: 63.6% (Req→Ana: 100%, Ana→Dis: ~75%, Dis→Dev: 0%)

**Estado**: CRITICO - NO es production-ready

**Principales hallazgos**:
- JWT no verificado en endpoints de aulas (diseno lo especificaba)
- Import `Optional` faltante → login roto
- Violacion de Unit of Work (architectural debt)
- Filosofia "el delgado" no implementada
- Campo `codigo` faltante en modelo

**Proximos pasos**:
- [ ] Corregir deudas criticas (15 min - 2 horas)
- [ ] Implementar Unit of Work correctamente
- [ ] Tests de trazaabilidad (recomendacion Gemini)

**Documentacion**:
- [Analisis tecnico detallado](./diseno-fastapi-react/iteracion-1/tecnica/)
- [Analisis de proceso detallado](./diseno-fastapi-react/iteracion-1/proceso/)
- [Reflexion tecnica sintetizada](./reflexiones/iteracion-1-tecnica.md)
- [Reflexion de proceso sintetizada](./reflexiones/iteracion-1-proceso.md)

---

## Futuras Auditorias

### [otra-rama-stack](./otra-rama-stack/)
Stack: TBD
- Sin auditorias aun
