# Seguimiento de resolución de desviaciones

## Registro de commits de refactoring

Cada entrada registra el commit, las desviaciones resueltas y los artefactos actualizados.

---

### R01: Actualización de dependencias
- **Commit**: [`f513580`](https://github.com/mmasias/pySigHor/commit/f513580)
- **Desviaciones resueltas**: D02 (parcial)
- **Artefactos actualizados**: `pyproject.toml`

---

### R02: Configuración central (pydantic-settings v2)
- **Commit**: [`28cf236`](https://github.com/mmasias/pySigHor/commit/28cf236)
- **Desviaciones resueltas**: D02 (completa), D03, D04 (parcial)
- **Artefactos actualizados**: `core/config.py`, `.env.example`

---

### R03: Capa de base de datos (async)
- **Commit**: [`5757ca5`](https://github.com/mmasias/pySigHor/commit/5757ca5)
- **Desviaciones resueltas**: D01 (parcial - motor async)
- **Artefactos actualizados**: `core/database.py`, `init_db.py`

---

### R04: Seguridad
- **Commit**: [`9ae1175`](https://github.com/mmasias/pySigHor/commit/9ae1175)
- **Desviaciones resueltas**: D10, D01 (parcial)
- **Artefactos actualizados**: `core/security.py`

---

### R05: Modelos (rol + timestamps)
- **Commit**: [`d5c3b2b`](https://github.com/mmasias/pySigHor/commit/d5c3b2b)
- **Desviaciones resueltas**: D06, D07
- **Artefactos actualizados**: `models/*.py`

---

### R06: Schemas (Pydantic v2)
- **Commit**: [`4f70d23`](https://github.com/mmasias/pySigHor/commit/4f70d23)
- **Desviaciones resueltas**: D02 (schema), D16
- **Artefactos actualizados**: `schemas/*.py`

---

### R07: Repositories (async)
- **Commit**: [`0d82e46`](https://github.com/mmasias/pySigHor/commit/0d82e46)
- **Desviaciones resueltas**: D01 (parcial), D17
- **Artefactos actualizados**: `repositories/*.py`

---

### R08: Services (async)
- **Commit**: [`acad3a8`](https://github.com/mmasias/pySigHor/commit/acad3a8)
- **Desviaciones resueltas**: D01 (parcial)
- **Artefactos actualizados**: `services/*.py`

---

### R09: Routers (async + auth protection)
- **Commit**: [`0414a44`](https://github.com/mmasias/pySigHor/commit/0414a44)
- **Desviaciones resueltas**: D01 (completa), D04 (completa), D05
- **Artefactos actualizados**: `routers/*.py`, `main.py`

---

### R10: Infraestructura Alembic + Tests
- **Commit**: [`9ef0561`](https://github.com/mmasias/pySigHor/commit/9ef0561)
- **Desviaciones resueltas**: D08, D09
- **Artefactos actualizados**: `alembic.ini`, `migrations/`, `tests/`

---

### R11: Frontend - bugs criticos
- **Commit**: [`73cbbf7`](https://github.com/mmasias/pySigHor/commit/73cbbf7)
- **Desviaciones resueltas**: D13, D14, D15
- **Artefactos actualizados**: `App.tsx`, `AuthContext.tsx`, `api.ts`

---

### R12: Frontend - navegacion + componentes
- **Commit**: [`fff93aa`](https://github.com/mmasias/pySigHor/commit/fff93aa)
- **Desviaciones resueltas**: D11, D18, D19 (parcial), D20
- **Artefactos actualizados**: `components/Layout.tsx`, `App.tsx`, `public/.gitkeep`

---

### Pendientes de esta iteración

| Desviación | Estado | Nota |
|---|---|---|
| D12 | Pendiente | Selectores FK en AulasPage y CursosPage requieren refactor más profundo |
| D19 | Pendiente | Directorio `utils/` sin contenido específico aún |

---

## Estado global

| Desviación | Severidad | Resolución | Commit |
|---|---|---|---|
| D01 | CRITICA | RESUELTA | R03 + R04 + R07 + R08 + R09 |
| D02 | CRITICA | RESUELTA | R01 + R02 + R06 |
| D03 | CRITICA | RESUELTA | R02 |
| D04 | ALTA | RESUELTA | R02 + R09 |
| D05 | CRITICA | RESUELTA | R09 |
| D06 | ALTA | RESUELTA | R05 |
| D07 | ALTA | RESUELTA | R05 |
| D08 | ALTA | RESUELTA | R10 |
| D09 | ALTA | RESUELTA | R10 |
| D10 | CRITICA | RESUELTA | R04 |
| D11 | ALTA | RESUELTA | R12 |
| D12 | MEDIA | PENDIENTE | Requiere refactor de formularios |
| D13 | MEDIA | RESUELTA | R11 |
| D14 | MEDIA | RESUELTA | R11 |
| D15 | MEDIA | RESUELTA | R11 |
| D16 | BAJA | RESUELTA | R06 |
| D17 | BAJA | RESUELTA | R07 |
| D18 | MEDIA | RESUELTA | R12 |
| D19 | BAJA | PENDIENTE | Directorio vacío |
| D20 | BAJA | RESUELTA | R12 |

**Resueltas**: 18/20
**Pendientes**: 2/20 (D12 selectores FK, D19 utils/)
