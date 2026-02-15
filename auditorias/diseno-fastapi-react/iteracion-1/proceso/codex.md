# AUDITORÍA DE PROCESO RUP - Iteración 1

**Auditor**: Codex (OpenAI)
**Fecha de auditoría**: 2025-02-15
**Rama**: diseño-fastapi-react
**Commit auditado**: `a8894e2`
**Ver código en GitHub**: https://github.com/mmasias/pySigHor/commit/a8894e2

---

## RESUMEN EJECUTIVO
La trazabilidad existe y es legible entre Requisitos → Análisis → Diseño → Desarrollo, pero hay desviaciones importantes en autenticación y CRUD de Aulas. Se observan gaps funcionales (campos/validaciones/flujo) y drifts de implementación sin actualización upstream, por lo que el objetivo pedagógico se cumple solo parcialmente.

## MATRIZ DE TRAZABILIDAD
| Caso Uso | Req→Aná | Aná→Dis | Dis→Dev | Gaps | Drifts | Inconsistencias | Alineación % |
|---------|---------|---------|---------|------|-------|-----------------|-------------|
| iniciarSesion | ✅ | ✅ | ❌ | AuthService/UsuarioRepository/BD no implementados; creación de Sesión no modelada en dev | Endpoint extra `verify-token`; usuario hardcodeado | `/token` (diseño) vs `/api/v1/auth/login` (dev); Sesión vs JWT sin mapeo | 55% |
| abrirAulas | ✅ | ❌ | ❌ | Filtro por ID/nombre/edificio no implementado; protección real por token ausente en código | Paginación (skip/limit) añadida sin diseño | `AulasController` vs `AulaService`; `AulaList` vs `AulasPage` | 50% |
| crearAula | ✅ | ❌ | ❌ | “El delgado” (crear mínimo + pasar a editar) no implementado; falta campo `codigo` y validación de edificio | Campos extra en creación (capacidad/especial/bloqueada) no estaban en requisitos | “crear y editar” no ocurre; unicidad por nombre vs por código | 45% |
| editarAula | ✅ | ✅ | ❌ | Campos completos (tipo/recursos/observaciones/código) no existen; flujo “continuar editando” no reflejado | PATCH en lugar de PUT | `PUT /aulas/{id}` (diseño) vs `PATCH /aulas/{id}` (dev) | 40% |
| eliminarAula | ✅ | ✅ | ❌ | No se presentan datos completos ni dependencias; no se valida integridad referencial | — | Confirmación detallada requerida vs confirmación mínima en UI | 60% |

## 🔴 GAPS DETECTADOS
- iniciarSesion(): Falta implementación de `AuthService`, `UsuarioRepository` y persistencia de usuarios; no existe entidad/flujo de “Sesión” explícito (se usa JWT sin mapeo con análisis).
- abrirAulas(): No se implementa filtrado por ID/nombre/edificio definido en requisitos/análisis; el diseño omite esa capacidad y el desarrollo no la implementa.
- crearAula(): No existe el flujo “crear con datos mínimos + transferir a editarAula()”; faltan campos y validaciones de “código” y “edificio válido”.
- editarAula(): No se implementan campos completos (recursos, observaciones, tipo, código), ni el flujo “continuar editando”.
- eliminarAula(): No se valida integridad referencial ni se muestran los datos completos del aula antes de confirmar.

## 🟡 DRIFTS DETECTADOS
- iniciarSesion(): Endpoint adicional `verify-token` y uso de usuario hardcodeado no aparecen en análisis/diseño.
- abrirAulas(): Paginación (skip/limit) y supuestos de “endpoint protegido” aparecen en desarrollo pero no están diseñados formalmente (y el backend no los aplica).
- crearAula(): Se agregan campos de creación que pertenecen al flujo de edición completa (capacidad, especial, bloqueada).
- editarAula(): Se implementa PATCH cuando el diseño describe PUT.

## 🟠 INCONSISTENCIAS DE NOMBRES
- Endpoint de login: Diseño `/token` vs Desarrollo `/api/v1/auth/login`.
- Controladores/servicios: `AulasController`/`AulaController` (análisis) vs `AulaService` (dev).
- Vista/Componente: `AulaList`/`AulaForm` (diseño) vs `AulasPage` con `Dialog` (dev).
- Identificador de aula: requisitos/análisis enfatizan “código” pero el desarrollo opera con `nombre` e `id`.

## 📊 EVALUACIÓN DE TRAZABILIDAD
- Promedio de alineación: **50%**
- Disciplina mejor alineada: **Requisitos → Análisis**, porque conserva actores, objetivos y flujos principales sin grandes divergencias.
- Disciplina con más problemas: **Diseño → Desarrollo**, porque los endpoints, reglas y flujos críticos no se implementan tal como fueron diseñados.

## 💡 RECOMENDACIONES DE PROCESSO
1. **Cerrar gaps antes de avanzar iteraciones**: implementar filtrado en abrirAulas, flujo “crear y editar”, y campos/validaciones completas en editarAula/eliminarAula.
2. **Actualizar diseño cuando se introduce un drift**: documentar explícitamente cambios (paginación, PATCH, verify-token) en los artefactos de diseño y análisis.
3. **Crear una sección fija de “Decisiones de implementación”** en cada README de Desarrollo para registrar desviaciones con justificación y fecha.
4. **Normalizar nombres y contratos**: alinear endpoints (`/token` vs `/auth/login`) y entidades (código vs nombre) entre disciplinas.
5. **Definir una política de seguridad trazable**: si “endpoint protegido” es requisito, debe existir en diseño y verificarse en desarrollo.
6. **Automatizar verificación de trazabilidad**: checklist por caso de uso antes de marcar “Completado” en desarrollo.

---

**Conclusión pedagógica**: La base RUP sí permite construir con trazabilidad, pero en Iteración 1 hay desviaciones no retro-documentadas. Para cumplir plenamente el objetivo, los ajustes de implementación deben propagarse hacia análisis/diseño o bien adaptarse el código a lo diseñado.
