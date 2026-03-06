# SÍNTESIS FINAL — Próximos pasos prioritarios del proyecto pySigHor

**Fecha**: 2026-03-06
**Ronda**: 1 (única)
**Agentes consultados**: Opencode (técnico), Gemini (pedagógico/estratégico), Qwen (abogado del diablo)
**Estado**: RESUELTO

---

## Conclusión

Hay tres acciones que deben ejecutarse en orden antes de escribir una línea de código de Iteración 2. Ninguna es optativa.

---

## Fundamento

### Acción 0-A — Corregir el dashboard (urgencia inmediata, fricción mínima)

`RUP/README.md` muestra ⚪ en las columnas Desarrollo y Pruebas de los 6 CdU ya implementados y documentados en `RUP/03-desarrollo/`. Cualquier alumno o evaluador que consulte el estado del proyecto concluirá que no existe código. Esto rompe el principio de visibilidad de RUP y oculta trabajo real. La corrección tarda menos de una hora (actualizar 6 filas del README). No tiene sentido añadir Iteración 2 encima de un dashboard que ya miente sobre Iteración 1.

No es un problema cosmético: un artefacto de seguimiento inconsistente con los artefactos de desarrollo que referencia viola la integridad documental del proyecto.

**Soporte**: Qwen (urgencia #1). Sin contradicción de los otros dos agentes.

---

### Acción 0-B — Diseño mínimo para Iteración 2 (prerrequisito RUP)

El proyecto enseña que Diseño precede a Desarrollo. 21 de 26 CdU no tienen diseño técnico. Para Edificios específicamente, esto es subsanable con un diagrama de secuencia por CdU (4 CdU: abrirEdificios, crearEdificio, editarEdificio, eliminarEdificio) antes de codificar. No se exige documentación exhaustiva: se exige coherencia visible con la metodología que el proyecto enseña. Hacerlo *just-in-time* por cada iteración es el mínimo viable para mantener la trazabilidad y no contradecir ante los alumnos lo que el propio dashboard y la estructura de carpetas prometen.

**Soporte**: Qwen (riesgo pedagógico diferible en términos técnicos, pero no en términos metodológicos). Opencode confirma que la arquitectura está lista para recibir el código una vez exista el diseño.

---

### Acción 1 — Migrar autenticación de hardcodeado a BD real (bloqueante técnico)

Opencode y Qwen convergen independientemente: el usuario `admin/admin` en memoria debe resolverse antes, no durante, Iteración 2.

La razón concreta: Iteración 2 introducirá la primera entidad persistida en BD (Edificios). En ese momento, la inconsistencia entre una entidad real en BD y un usuario que no existe en BD se vuelve estructural. Cada iteración adicional construida sobre el hardcodeado incrementa el coste del refactor. La ventana para hacerlo con daño mínimo es ahora: solo 6 CdU afectados frente a 10+ si se espera a Iteración 3.

La migración implica:
- Modelo `Usuario` con SQLAlchemy
- `UsuarioRepository` + `UsuarioService`
- Modificar `auth.py` para consultar BD en lugar de diccionario en memoria
- Variables de entorno para `SECRET_KEY` y credenciales iniciales

**Soporte**: Opencode (bloqueante explícito) + Qwen (urgencia #2, "último momento seguro"). Sin contradicción de Gemini.

---

### Acción 2 — Iteración 2: Edificios, con tests desde el inicio

Con las tres acciones anteriores completadas, Iteración 2 puede avanzar. La secuencia Edificios → Cursos → Profesores → Recursos → Horarios → Consultas es correcta técnica y pedagógicamente:

- La relación FK `aulas ← edificios` ya existe en el modelo (Opencode)
- Edificios introduce integridad referencial: borrado en cascada, navegación entre entidades vinculadas
- Cursos añade lógica de negocio (restricciones créditos/horas)
- Profesores introduce relaciones M:N y pesos ponderados — preparación directa para el algoritmo
- Recursos introduce optimización de representación (BitSets, banderas)
- La repetición de CRUD entre iteraciones es el mecanismo pedagógico: el alumno interioriza que cualquier dominio se factoriza en operaciones elementales

**Sobre testing**: Gemini tiene el argumento más desarrollado. Introducir Pytest en Iteración 2, sobre la entidad más simple (Edificios), es el momento correcto por dos razones: (1) la carga cognitiva del stack ya fue absorbida en Iteración 1; (2) la red de seguridad es necesaria antes de llegar a Profesores (relaciones M:N) y `generarHorario()`, donde los errores son difíciles de trazar manualmente. Opencode marca los tests como diferibles pero no propone cuándo; la propuesta de Gemini es más específica y conveniente.

**Soporte**: Opencode (secuencia técnica correcta), Gemini (testing en Iteración 2, mapa de complejidad creciente por entidad).

---

## Disenso relevante: la propuesta narrativa de Gemini sobre `generarHorario()`

Gemini propone introducir una versión Alfa de `generarHorario()` en Iteración 3 —antes de completar todos los CRUDs— para generar un "momento WOW" que muestre a los alumnos el objetivo final del sistema y evite la "fatiga de CRUD".

**Aplicando la corrección de contexto de Manuel**: la repetición de CRUDs entre iteraciones es intencional. El objetivo pedagógico es que el alumno interiorice que cualquier dominio se factoriza en operaciones elementales. La "fatiga de CRUD" es el mecanismo de aprendizaje, no un problema a resolver. Esto invalida la motivación principal de la propuesta de Gemini.

Sin embargo, la idea de anticipar `generarHorario()` como hilo conductor tiene mérito independiente de esa motivación: los alumnos verían antes el propósito de todo lo que construyen. Queda registrada como decisión estratégica abierta para Manuel, no como conclusión del panel.

---

## Tabla resumen de próximos pasos

| Orden | Acción | Tipo | Bloqueante de |
|---|---|---|---|
| 0-A | Corregir dashboard: 6 CdU de ⚪ a su estado real | Documental | Integridad del proyecto |
| 0-B | Diseño mínimo para Edificios (4 diagramas de secuencia) | Metodológico | Coherencia RUP antes de codificar |
| 1 | Migrar auth hardcodeado → BD real (modelo Usuario + repo + service) | Técnico | Todo lo que venga después |
| 2 | Iteración 2: Edificios CRUD + tests Pytest | Construcción | Iteraciones 3+ |

---

## Observaciones del orquestador

Las tres correcciones más importantes de esta ronda no vienen de los agentes sino del contexto real del proyecto:

1. **Son 6 CdU implementados, no 5.** El error de Qwen no afecta la validez de su argumento sobre el dashboard, pero sí la magnitud: el artefacto oculta más trabajo del que se asumía.

2. **La repetición de CRUD es intencional.** Gemini construyó su propuesta narrativa asumiendo que la repetición era un problema pedagógico. Al caer esa premisa, su propuesta de estructura narrativa alternativa pierde su motivación principal, aunque el mapa de complejidad creciente por entidad que ofrece sigue siendo válido como guía de qué concepto introduce cada iteración.

3. **La convergencia más sólida del panel** es la urgencia de migrar la autenticación antes de Iteración 2. Opencode y Qwen llegaron a esa conclusión desde ángulos distintos (técnico vs. pedagógico/metodológico) y sin contradecirse.
