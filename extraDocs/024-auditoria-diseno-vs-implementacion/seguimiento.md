# Seguimiento de resolución de desviaciones

## Registro de commits de refactoring

Cada entrada registra el commit, las desviaciones resueltas y los artefactos actualizados.

---

### R01: Actualización de dependencias
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D02 (parcial)
- **Artefactos actualizados**: `pyproject.toml`

---

### R02: Configuración central (pydantic-settings v2)
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D02 (completa), D03, D04 (parcial)
- **Artefactos actualizados**: `core/config.py`, `.env.example`

---

### R03: Capa de base de datos (async)
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D01 (parcial - motor async)
- **Artefactos actualizados**: `core/database.py`, `init_db.py`

---

### R04: Seguridad
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D10, D01 (parcial)
- **Artefactos actualizados**: `core/security.py`

---

### R05: Modelos (rol + timestamps)
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D06, D07
- **Artefactos actualizados**: `models/*.py`

---

### R06: Schemas (Pydantic v2)
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D02 (schema), D16
- **Artefactos actualizados**: `schemas/*.py`

---

### R07: Repositories (async)
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D01 (parcial), D17
- **Artefactos actualizados**: `repositories/*.py`

---

### R08: Services (async)
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D01 (parcial)
- **Artefactos actualizados**: `services/*.py`

---

### R09: Routers (async + auth protection)
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D01 (completa), D04 (completa), D05
- **Artefactos actualizados**: `routers/*.py`, `main.py`

---

### R10: Infraestructura Alembic + Tests
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D08, D09
- **Artefactos actualizados**: `alembic.ini`, `migrations/`, `tests/`

---

### R11: Frontend - bugs criticos
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D13, D14, D15
- **Artefactos actualizados**: `App.tsx`, `AuthContext.tsx`, `api.ts`

---

### R12: Frontend - navegacion + componentes + FK
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D11, D12, D18, D19
- **Artefactos actualizados**: nuevos `components/Layout.tsx`, `EntityTable.tsx`, `EntityDialog.tsx`, refactor de pages

---

### R13: Limpieza final + cierre documental
- **Commit**: _pendiente_
- **Desviaciones resueltas**: D20, cierre de todas
- **Artefactos actualizados**: cierre documental completo

---

## Estado global

| Desviación | Severidad | Resolución |
|---|---|---|
| D01 | CRITICA | [PENDIENTE] |
| D02 | CRITICA | [PENDIENTE] |
| D03 | CRITICA | [PENDIENTE] |
| D04 | ALTA | [PENDIENTE] |
| D05 | CRITICA | [PENDIENTE] |
| D06 | ALTA | [PENDIENTE] |
| D07 | ALTA | [PENDIENTE] |
| D08 | ALTA | [PENDIENTE] |
| D09 | ALTA | [PENDIENTE] |
| D10 | CRITICA | [PENDIENTE] |
| D11 | ALTA | [PENDIENTE] |
| D12 | MEDIA | [PENDIENTE] |
| D13 | MEDIA | [PENDIENTE] |
| D14 | MEDIA | [PENDIENTE] |
| D15 | MEDIA | [PENDIENTE] |
| D16 | BAJA | [PENDIENTE] |
| D17 | BAJA | [PENDIENTE] |
| D18 | MEDIA | [PENDIENTE] |
| D19 | BAJA | [PENDIENTE] |
| D20 | BAJA | [PENDIENTE] |

**Resueltas**: 0/20
**Pendientes**: 20/20
