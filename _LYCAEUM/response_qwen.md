# Respuesta Qwen — Ronda 1

## Tensión 1: Trazabilidad RUP vs. Velocidad de desarrollo

**Veredicto: Riesgo real, pero matizable.**

El proyecto enseña RUP como metodología formal, donde Diseño precede a Desarrollo. Sin embargo, 21 de 26 CdU (81%) saltan directamente de Análisis a Desarrollo. Esto es una contradicción pedagógica visible: los alumnos verán que el dashboard marca "Diseño ⚪" y "Desarrollo ⚪" para CdU que podrían estar implementados. La justificación "velocidad" es válida en industria, pero en un proyecto *didáctico* que explícitamente enseña RUP, cada fase debe ser trazable. No se pide diseño exhaustivo, pero sí un mínimo (diagrama de secuencia + clases involucradas) por CdU antes de codificar.

---

## Tensión 2: El dashboard miente

**Veredicto: Riesgo real de integridad documental.**

No es un problema cosmético. Un dashboard que muestra ⚪ para 5 CdU implementados (iniciarSesion, CRUD Aulas) rompe la confianza del lector y oculta el progreso real. Si un alumno o evaluador consulta el estado del proyecto, concluye erróneamente que no hay nada implementado. Esto viola el principio RUP de visibilidad del estado. Además, el archivo `RUP/03-desarrollo/casos-uso/README.md` existe y documenta los 5 CdU, pero el dashboard principal no lo refleja. La inconsistencia entre artefactos es más grave que no tener dashboard.

---

## Tensión 3: Estrategia de Vertical Slice con usuario hardcodeado

**Veredicto: Riesgo real de deuda técnica acumulativa.**

El usuario hardcodeado (`admin/admin`) es válido para Iteración 1, pero las iteraciones 2-4 (Edificios, Cursos, Profesores) requerirán autenticación real con BD y roles. Cada iteración que se construye sobre el hardcodeo incrementa el acoplamiento: los endpoints actuales asumen un usuario fijo, el frontend guarda token estático, los tests manuales usan credenciales fijas. El refactor será más costoso cuanto más se espere. El **último momento seguro** es antes de Iteración 2 (Edificios), porque ahí se empieza a persistir entidades reales en BD. Hacerlo en la transición Iteración 1→2 minimiza el impacto: solo 5 CdU afectados vs. 9+ si se espera a Iteración 3.

---

## Priorización de problemas por urgencia

|Orden|Problema|Justificación|
|:-:|:-|:-|
|**1**|Dashboard inconsistente|Es el más visible y urgente: oculta trabajo completado y envía mensaje erróneo a cualquier stakeholder. Se corrige en <1 hora actualizando los emojis del README.md principal. Impacto inmediato en percepción del proyecto.|
|**2**|Refactor usuario hardcodeado → BD|Ventana de oportunidad estrecha: debe hacerse antes de Iteración 2. Si se posterga, la deuda técnica crece exponencialmente con cada nuevo CdU implementado. Requiere planificación (migración de auth, endpoints, frontend, tests).|
|**3**|Falta de diseño para 21 CdU|Es importante pero menos urgente: se puede resolver "just-in-time" antes de cada iteración. No bloquea Iteración 2 si se produce diseño mínimo para Edificios antes de codificar. Riesgo pedagógico, no técnico.|

---

## Objeciones o inconsistencias detectadas

1. **Asumición no justificada**: El plan asume que "Vertical Slice" justifica omitir diseño. Pero Vertical Slice se refiere a entregar funcionalidad end-to-end, no a saltar fases RUP.

2. **Contradicción interna**: El proyecto tiene carpetas `02-diseño/` y `03-desarrollo/` separadas, lo que implica fases distintas. Saltar de una a otra sin trazabilidad rompe el modelo mental que los propios artefactos sugieren.

3. **Lo que falta**: No hay criterio explícito de "Definition of Done" por CdU. ¿Qué condiciones debe cumplir un CdU para marcarse como completado en el dashboard? Sin esto, cualquier avance es subjetivo.

---

## Posición

Defendería: (1) Corregir el dashboard inmediatamente como tarea de higiene documental; (2) Planificar la migración a autenticación con BD como **prerrequisito** de Iteración 2, no como parte de ella; (3) Adoptar diseño "ligero pero trazable": un diagrama de secuencia por CdU antes de codificar, sin exigir documentación exhaustiva. Esto mantiene coherencia pedagógica sin paralizar el avance.
