# AUDITORÍA DE PROCESO RUP - Iteración 1

**Auditor**: Gemini (Google)
**Fecha de auditoría**: 2025-02-15
**Rama**: diseño-fastapi-react
**Commit auditado**: `a8894e2`
**Ver código en GitHub**: https://github.com/mmasias/pySigHor/commit/a8894e2

---

## RESUMEN EJECUTIVO
La Iteración 1 del proyecto pySigHor ha demostrado que la estructura RUP puede servir como un marco organizativo sólido para la documentación. Sin embargo, la trazabilidad entre las disciplinas de Diseño y, especialmente, Desarrollo es baja. Se identifican numerosos Gaps (funcionalidad diseñada no implementada) y Drifts (funcionalidad implementada no diseñada o con grandes desviaciones), así como inconsistencias en la terminología y la implementación de decisiones clave, como la seguridad. Esto sugiere que el objetivo pedagógico de construir sobre una base arquitectónica definida y ajustarse a ella no se cumplió de manera efectiva en la fase de implementación.

## MATRIZ DE TRAZABILIDAD

| Caso Uso | Req→Aná | Aná→Dis | Dis→Dev | Gaps                                                                                                                                                                                                                                                                                       | Drifts                                                                                                                                          | Inconsistencias                                                                                         | Alineación % |
| :------- | :------ | :------ | :------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ | :----------- |
| iniciarSesion | ✅       | ❌       | ❌       | Interacción con DB (UsuarioRepository), endpoint diseñado (`/token`).                                                                                                                                                                                              | Endpoint `/verify-token`, implementación contra usuario hardcodeado.                                                                            | Nombre endpoint (diseño `/token` vs desarrollo `/auth/login`), `AuthService` vs `IniciarSesionController`. | 50%          |
| abrirAulas | ✅       | ✅       | ❌       | Protección de seguridad (autenticación), funcionalidad de filtrado/búsqueda.                                                                                                                                                                                             | Ninguno.                                                                                                                                        | Ninguno.                                                                                                | 67%          |
| crearAula | ✅       | ✅       | ❌       | Campo 'Código' (requisito), flujo C→U (transferencia a edición), protección de seguridad.                                                                                                                                                                                  | Definición de 'datos mínimos' cambió (agregando capacidad, especial, bloqueada que no eran parte del requisito de creación mínima).             | Ninguno.                                                                                                | 67%          |
| editarAula | ✅       | ✅       | ❌       | Campos completos (código, tipo, recursos, observaciones), flujo C→U (precondición `crearAula`), protección de seguridad.                                                                                                                                                     | Ninguno.                                                                                                                                        | Método HTTP (diseño `PUT` vs desarrollo `PATCH`).                                                       | 67%          |
| eliminarAula | ✅       | ✅       | ❌       | Protección de seguridad, validación de dependencias/manejo de integridad referencial en servicio.                                                                                                                                                                        | Ninguno.                                                                                                                                        | Ninguno.                                                                                                | 67%          |

## 🔴 GAPS DETECTADOS
- **Seguridad (Crítico):** La protección de los endpoints CRUD de `aulas` (`abrirAulas`, `crearAula`, `editarAula`, `eliminarAula`) mediante autenticación JWT fue diseñada pero **no implementada**.
- **`iniciarSesion` (funcionalidad):** La interacción con la base de datos para la validación de credenciales (a través de un `UsuarioRepository`) fue diseñada pero **no implementada**, recurriendo a un usuario hardcodeado.
- **`abrirAulas` (funcionalidad):** La funcionalidad clave de "filtrar/buscar" aulas, especificada en Requisitos y Análisis, fue **omitida** en la implementación.
- **`crearAula` (funcionalidad):**
    - El campo `Código` (mandatorio en requisitos) fue **omitido** del esquema y la implementación.
    - La "filosofía C→U" (creación con datos mínimos y transferencia inmediata a edición completa) fue **abandonada**; se solicitaron más campos en la creación y la transición a edición no se implementó.
- **`editarAula` (funcionalidad):** Campos detallados en Requisitos/Análisis (ej., código, tipo de aula, recursos, observaciones) fueron **omitidos** en el esquema `AulaUpdate` y la implementación.
- **`eliminarAula` (funcionalidad):** La verificación explícita de dependencias y el manejo robusto de la integridad referencial (diseñados para el service layer) fueron **omitidos** o no implementados adecuadamente.

## 🟡 DRIFTS DETECTADOS
- **`iniciarSesion`:** Se implementó un endpoint `/verify-token` que no fue diseñado en ninguna fase previa.
- **`crearAula`:** La definición de "datos mínimos" para la creación de un aula cambió drásticamente de los requisitos/análisis (solo nombre, código, edificio) a la implementación (nombre, capacidad, especial, bloqueada, id_edificio).

## 🟠 INCONSISTENCIAS DE NOMBRES
- **`iniciarSesion`:** El `IniciarSesionController` definido en Análisis fue referido como `AuthService` en Diseño y su lógica se distribuyó en `routers/auth.py` y `core/security.py` en Desarrollo, sin un mapeo o justificación clara documentada.
- **`iniciarSesion`:** El endpoint se diseñó como `/token` pero se implementó como `/api/v1/auth/login`.
- **`editarAula`:** El método HTTP para la actualización de aulas se definió como `PUT` en Diseño pero se implementó como `PATCH` en Desarrollo.

## 📊 EVALUACIÓN DE TRAZABILIDAD
- **Promedio de alineación:** 63.6%
- **Disciplina mejor alineada:** **Requisitos a Análisis (Req→Aná)**. Esta transición muestra una excelente coherencia en todos los casos de uso (100% de alineación promedio). Los modelos de análisis capturan muy bien los requisitos detallados.
- **Disciplina con más problemas:** **Diseño a Desarrollo (Dis→Dev)**. Esta es la fase con la trazabilidad más rota (0% de alineación promedio en todos los casos de uso). Los Gaps de seguridad y funcionalidad, así como los Drifts e inconsistencias, son predominantes aquí, lo que indica una implementación que se desvió significativamente del diseño sin una documentación de los ajustes.

## 💡 RECOMENDACIONES DE PROCESO
1.  **Enfocar en la Trazabilidad Dis→Dev:** Es crucial implementar un proceso más riguroso para asegurar que las decisiones de diseño se reflejen fielmente en el desarrollo. Esto podría incluir revisiones de código y reuniones de seguimiento específicas para validar la implementación contra el diseño.
2.  **Actualización Bidireccional de la Documentación:** Si la implementación se desvía del diseño o de los requisitos (lo cual es natural en el desarrollo iterativo), estos cambios deben documentarse explícitamente en la disciplina correspondiente (Diseño, Análisis, Requisitos) para mantener la trazabilidad. No solo se debe actualizar "aguas abajo" (Desarrollo), sino también "aguas arriba".
3.  **Reforzar la Disciplina de Diseño:** Es fundamental que las decisiones de diseño (como la protección de endpoints, los esquemas de datos y los flujos de interacción) sean claras, completas y se respeten. Si hay cambios necesarios, deben ser revisados y aprobados formalmente antes de la implementación.
4.  **Uso Consistente de Nomenclatura:** Mantener la coherencia en los nombres de componentes, servicios y endpoints a través de todas las disciplinas para evitar confusiones e inconsistencias. Cualquier cambio de nombre debe ser rastreado y justificado.
5.  **Validación de Supuestos:** Evitar supuestos no documentados en las fases posteriores (ej. la seguridad de los endpoints). Cada decisión clave debe estar explícitamente detallada en su disciplina correspondiente.
6.  **Integrar Pruebas con Trazabilidad:** Las pruebas deberían no solo validar la funcionalidad, sino también la conformidad con los requisitos y el diseño. Esto implica crear casos de prueba que directamente verifiquen que lo diseñado se implementó.
