# Auditorias - Rama: diseno-fastapi-react

## Stack Tecnologico

### Backend
- **Framework**: FastAPI 0.100.1
- **Validacion**: Pydantic 1.10.13
- **ORM**: SQLAlchemy 2.0.23
- **Base de datos**: SQLite (desarrollo)
- **Autenticacion**: JWT + OAuth2PasswordBearer

### Frontend
- **Framework**: React 18
- **Build tool**: Vite 5
- **Lenguaje**: TypeScript 5
- **UI Library**: Material-UI v5
- **HTTP Client**: Axios

### Arquitectura
- **Patron**: Layered Architecture (Router → Service → Repository → Model)
- **Separacion**: MVC frontend, API backend

---

## Iteraciones Auditadas

### [Iteracion 1](./iteracion-1/) (2025-02-15)

**Commit auditado**: `a8894e2`
**Ver codigo auditado**: https://github.com/mmasias/pySigHor/commit/a8894e2

#### Resumen Ejecutivo

**Objetivo**: Implementar autenticacion JWT + CRUD completo de Aulas

**Casos de uso implementados**:
1. `iniciarSesion` - Login con JWT
2. `abrirAulas` - Listado de aulas
3. `crearAula` - Creacion de aula
4. `editarAula` - Actualizacion de aula
5. `eliminarAula` - Eliminacion de aula

**Calificaciones**:
- **Tecnica**: 6.4/10
  - Backend: 5.8/10 (Gemini: 4/10)
  - Frontend: 7.3/10
  - Documentacion: 7.0/10
- **Proceso RUP**: 63.6%
  - Req→Ana: 100%
  - Ana→Dis: ~75%
  - Dis→Dev: 0%

**Estado**: NO es production-ready

#### Principales Hallazgos Criticos

**Tecnicos**:
1. JWT no verificado en endpoints de aulas (seguridad critica)
2. Import `Optional` faltante → login roto (bug bloqueante)
3. Violacion de Unit of Work (Repository hace commit)
4. Dependencias circulares (importaciones locales en services)
5. SECRET_KEY hardcoded
6. Usuarios hardcodeados

**Proceso**:
1. Dis→Dev tiene 0% de alineacion (diseno no se siguio)
2. Seguridad disenada, no implementada (todos los endpoints CRUD)
3. Filosofia "el delgado" de crearAula abandonada
4. Campo `codigo` faltante en modelo
5. Validacion de dependencias en eliminarAula omitida

#### Acciones Requeridas

**Antes de Iteracion 2** (CRITICO):
- [ ] Corregir import `Optional` en `security.py` (1 minuto)
- [ ] Agregar `Depends(get_current_user)` a endpoints de aulas (15 min)
- [ ] Mover SECRET_KEY a variables de entorno (10 min)
- [ ] Mover `db.commit()` del Repository al Service layer (2 horas)
- [ ] Resolver dependencias circulares (1 hora)

**Recomendado para Iteracion 2**:
- [ ] Implementar filosofia "el delgado" en crearAula
- [ ] Agregar campo `codigo` al modelo Aula
- [ ] Implementar filtrado en abrirAulas
- [ ] Validar dependencias en eliminarAula
- [ ] Tests de trazaabilidad (recomendacion Gemini)

#### Documentacion

**Analisis primario**:
- [Auditoria tecnica](./iteracion-1/tecnica/) - Analisis detallado de 4 LLMs
- [Auditoria de proceso](./iteracion-1/proceso/) - Analisis de trazaabilidad RUP

**Sintesis**:
- [Reflexion tecnica](../reflexiones/iteracion-1-tecnica.md) - Lecciones aprendidas tecnicas
- [Reflexion de proceso](../reflexiones/iteracion-1-proceso.md) - Lecciones aprendidas RUP

---

## Iteracion 2 (Pendiente)

**Fecha estimada**: TBD
**Objetivo**: TBD (posiblemente Edificios o Horarios)

**Requisitos previos**:
- Deudas tecnicas de Iteracion 1 resueltas
- Tests de trazaabilidad implementados
- Trazabilidad Dis→Dev > 90%

---

## Metricas de Calidad

| Iteracion | Tecnica | Proceso | Estado |
|-----------|---------|---------|--------|
| 1 | 6.4/10 | 63.6% | Critico |
| 2 | TBD | TBD | Pendiente |

---

## Lecciones Aprendidas

### Lo que funciono
- Arquitectura Layered se respeto (estructura)
- Req→Ana tiene 100% de alineacion
- Stack moderno bien seleccionado
- Scripts de setup automatizados

### Lo que NO funciono
- Dis→Dev esta roto (0% de alineacion)
- Seguridad disenada no se implemento
- Decisiones de implementacion no documentaron upstream
- Cortocircuitos de disciplina (implementar sin diseno)

### Cambios de proceso para Iteracion 2
1. Verificacion de implementacion contra diseno
2. Tests de conformidad con diseno
3. Actualizacion bidireccional de documentacion
4. No "suponer" - validar contra Diseno
5. Code reviews que verifican trazaabilidad
