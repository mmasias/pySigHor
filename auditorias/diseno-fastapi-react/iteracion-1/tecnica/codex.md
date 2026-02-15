# AUDITORÍA TÉCNICA - Iteración 1 pySigHor

**Auditor**: Codex (OpenAI)
**Fecha de auditoría**: 2025-02-15
**Rama**: diseño-fastapi-react
**Commit auditado**: `a8894e2`
**Ver código en GitHub**: https://github.com/mmasias/pySigHor/commit/a8894e2

---

## RESUMEN EJECUTIVO
La base técnica cumple con la arquitectura propuesta y el CRUD de aulas está implementado, pero hay brechas críticas de seguridad y arranque que afectan el uso real. La documentación RUP es extensa, aunque presenta inconsistencias con el comportamiento actual del código.

## 🔴 ISSUES CRÍTICOS
1. **Endpoints de Aulas sin protección JWT**
   - Los endpoints `GET/POST/PATCH/DELETE /api/v1/aulas` no aplican ninguna dependencia de autenticación/autoridad. Cualquier cliente puede acceder sin token.
   - Evidencia: `backend/app/routers/aulas.py` no usa `Depends(oauth2_scheme)` ni `get_current_user()`.
   - Impacto: rompe el caso de uso de seguridad y permite operaciones no autorizadas.

2. **Fallo de arranque por falta de import en security.py**
   - Se usa `Optional` en las anotaciones de `create_access_token` sin importar `Optional`.
   - Evidencia: `backend/app/core/security.py`.
   - Impacto: error en tiempo de importación (NameError) al iniciar la app en Python 3.11 sin `from __future__ import annotations`.

## 🟡 ISSUES MEDIOS
1. **Documentación afirma seguridad inexistente en código**
   - Los README de casos de uso y `SETUP-INICIAL.md` indican que los endpoints están protegidos con token, pero el backend no lo implementa.
   - Evidencia: `RUP/03-desarrollo/casos-uso/*/README.md`, `SETUP-INICIAL.md` vs. `backend/app/routers/aulas.py`.

2. **Credenciales y SECRET_KEY por defecto**
   - Se usa `SECRET_KEY` hardcodeado y usuario hardcodeado en backend. Está bien para prototipo, pero no debe figurar como “listo” sin advertencia fuerte.
   - Evidencia: `backend/app/core/config.py`, `backend/app/routers/auth.py`.

3. **Persistencia de token sin verificación de expiración**
   - El frontend considera autenticado si hay token en localStorage, sin verificar validez/expiración.
   - Evidencia: `frontend/src/context/AuthContext.tsx`.

4. **Gestión de errores DB sin rollback**
   - En caso de error durante `commit`, la sesión queda en estado inválido (falta rollback).
   - Evidencia: `backend/app/repositories/aula_repository.py`.

5. **Manejo de entradas numéricas en frontend**
   - `parseInt` puede producir `NaN` si el input queda vacío, enviando datos inválidos.
   - Evidencia: `frontend/src/pages/AulasPage.tsx`.

## 🟢 ISSUES MENORES
1. **Parámetro `db` sin uso en login**
   - Se inyecta `db: Session` y no se utiliza.
   - Evidencia: `backend/app/routers/auth.py`.

2. **Uso extendido de `any` en errores del frontend**
   - Reduce el beneficio de TypeScript y hace más frágil el manejo de errores.
   - Evidencia: `frontend/src/pages/LoginPage.tsx`, `frontend/src/pages/AulasPage.tsx`.

3. **Falta de paginación en UI**
   - El backend soporta `skip/limit`, pero no se expone en la UI.
   - Evidencia: `frontend/src/pages/AulasPage.tsx`.

4. **Theme MUI incompleto**
   - `createTheme` usa `colorScheme` (propiedad no estándar en MUI v5); no rompe, pero no tiene efecto.
   - Evidencia: `frontend/src/App.tsx`.

## ⭐ ASPECTOS POSITIVOS
- Arquitectura por capas clara (Router → Service → Repository → Model) con separación de responsabilidades.
- Validaciones básicas bien definidas en Pydantic (longitud, rango, opcionales).
- Scripts `setup.sh` completos, con verificación de dependencias y pasos guiados.
- Documentación RUP organizada y trazable para cada caso de uso.
- UI funcional para CRUD con estados de carga/errores y confirmación en borrado.

## 📊 EVALUACIÓN DE CALIDAD
- Código Backend: 6/10
- Código Frontend: 7/10
- Documentación: 7/10
- Arquitectura: 8/10
- Configuración: 7/10

## 💡 RECOMENDACIONES
1. **Implementar protección real en endpoints**
   - Crear `get_current_user()` en `backend/app/core/security.py` y agregar `Depends()` en routers de aulas.

2. **Corregir el bug de importación en security.py**
   - Añadir `from typing import Optional` o activar `from __future__ import annotations`.

3. **Alinear documentación con implementación**
   - Actualizar RUP/README para reflejar el estado real o implementar lo documentado.

4. **Endurecer la configuración de seguridad**
   - Mover `SECRET_KEY` y credenciales a `.env` obligatorio, y dejar un warning explícito en docs.

5. **Mejorar manejo de errores y consistencia de sesión DB**
   - Envolver commits con try/except y rollback en repositorio o en servicio.

6. **Validación de token en frontend**
   - Usar `verify-token` al iniciar la app o manejar 401 globalmente con interceptor.

7. **Robustecer validaciones de formulario**
   - Evitar `NaN`, usar `TextField` con `value` controlado y validación previa a submit.

8. **Agregar pruebas mínimas**
   - Tests de API (auth + CRUD) y pruebas de UI básicas para login y CRUD.

---

**Nota**: No se ejecutaron pruebas end-to-end en este entorno; la verificación es por inspección de código.
