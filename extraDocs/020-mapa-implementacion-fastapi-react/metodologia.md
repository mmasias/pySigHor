# Metodología de Implementación - FastAPI + React

<div align=right>

||||||
|-|-|-|-|
|[🏠️](../README.md)|**Artículo 020**|[Contexto](contexto.md)|[Plan de Iteraciones](plan-iteraciones.md)|[Metodología](metodologia.md)|

</div>

## Información del Artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Construcción (Construction)
- **Disciplina**: Implementación + Gestión de Configuración
- **Versión**: 1.0
- **Fecha**: 15 de febrero de 2026

## Flujo de Trabajo por Iteración

### Fase 1: Diseño (si no está listo)
**Duración**: 1-2 sesiones

### Fase 2: Implementación
**Duración**: 2-3 sesiones

**Commits descriptivos**:
```bash
git commit -m "feat(aulas): implementar abrirAulas con paginación"
git commit -m "fix(aulas): corregir validación de capacidad"
git commit -m "refactor(aulas): extraer lógica a servicio"
```

### Fase 3: Ejecutable Testeable
**Duración**: 1 sesión

- Backend: `uvicorn app.main:app --reload --port 8000`
- Frontend: `npm run dev` (localhost:5173)

### Fase 4: Validación y Documentación de Ajustes
**Duración**: 1 sesión

**Documentar en**:
- `conversation-log.md` (siempre)
- Casos de uso específicos (si aplica)
- Artículo 020 (actualización)

## Estrategia de Commits

Los commits son la **evidencia principal** del proceso:

- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `refactor`: Reestructuración sin cambio de comportamiento
- `docs`: Cambios en documentación
- `test`: Agregar o modificar tests

## Criterio de Éxito por Iteración

- ✅ Ejecutable funcional: Backend + Frontend corriendo en localhost
- ✅ Commits descriptivos: Historia clara en mensajes de commit
- ✅ Validación manual: Tests ejecutados sobre el ejecutable
- ✅ Ajustes documentados: En conversation-log + casos de uso + artículo 020

---

**Metodología** - Artículo 020
Fecha: 15 de febrero de 2026
pySigHor - Sistema generador de horarios
