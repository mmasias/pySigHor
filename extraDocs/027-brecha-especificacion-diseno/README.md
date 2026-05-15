# Artículo 027: Brecha especificación - diseño

## ¿Por qué?

La auditoría 024 comparó diseño contra implementación y detectó 20 desviaciones. Pero asumía que el diseño era correcto. Este artículo documenta un tipo de error distinto y más silencioso: **un requisito que estaba en la especificación, desapareció en el diseño, y el código lo implementó fielmente... sin él**.

La implementación no falló. El diseño falló. Y un proceso RUP sin trazabilidad inversa no lo habría detectado nunca.

## ¿Qué?

### El requisito

El CdU `editarAula` especifica en `RUP/00-casos-uso/02-detalle/editarAula/especificacion.puml`:

```
Sistema presenta datos de edición:
• Código, nombre del aula
• Edificio asociado, capacidad
• Tipo de aula, recursos       ← aquí
• Observaciones del aula
```

El wireframe (`wireframes.puml`) lo confirma: campo "Recursos" como parte del formulario de edición.

### La brecha

El diagrama de secuencia de diseño (`RUP/02-diseño/casos-uso/editarAula/secuencia.puml`) modela el flujo así:

```
Admin → FE → API → AulaService → AulaRepository → UPDATE aulas SET ...
```

Los recursos no aparecen. Ni la tabla de unión, ni el repositorio de recursos, ni ninguna operación adicional. El diseñador (o el agente que generó el diagrama) omitió la parte de recursos sin dejar constancia.

### La implementación

`AulaRepository` implementa exactamente lo que el diagrama dice: CRUD básico sobre la tabla `aulas`. Sin relación many-to-many. Sin gestión de recursos. El código es correcto respecto al diseño. El diseño es incorrecto respecto a la especificación.

### El diagnóstico

| Artefacto | ¿Incluye recursos? |
|---|---|
| `editarAula/especificacion.puml` | Sí |
| `editarAula/wireframes.puml` | Sí |
| `editarAula/secuencia.puml` | No — **aquí se perdió** |
| `AulaRepository` | No (coherente con el diseño) |
| `AulasPage.tsx` | No (coherente con el diseño) |

## ¿Para qué?

Este caso ilustra que la trazabilidad RUP no es solo de arriba hacia abajo (especificación → diseño → código) sino también de vuelta. Si al implementar algo no encuentra su origen en el diseño, y el diseño no lo conecta con la especificación, hay una brecha.

La detección ocurrió de forma práctica: al intentar asociar recursos a aulas desde la UI, el modelo de datos no lo soportaba. Sin ese intento de uso real, la brecha podría haber permanecido invisible hasta la fase de pruebas o, peor, hasta producción.

## ¿Cómo se resuelve?

La corrección abarca cuatro capas y el propio artefacto de diseño:

### 1. Modelo de datos
Nueva tabla de asociación `aula_recursos` (many-to-many entre `aulas` y `recursos`). Relación declarada en el modelo SQLAlchemy `Aula` con `relationship("Recurso", secondary=aula_recursos)`.

### 2. Repositorio
`AulaRepository` necesita dos operaciones nuevas:
- `get_recursos(aula_id)` — devuelve los recursos asignados
- `set_recursos(aula, ids_recursos)` — reemplaza la lista de recursos del aula

### 3. Schema y router
`AulaUpdate` acepta `ids_recursos: list[int] | None`. El endpoint `PATCH /aulas/{id}` llama a `set_recursos` si el campo viene en el body.

### 4. Frontend
El formulario de `AulasPage` incluye un multi-select de recursos (checkboxes o chips MUI). La tabla principal muestra los recursos asignados como texto separado por comas.

### 5. Diagrama de diseño
`editarAula/secuencia.puml` debe actualizarse para reflejar las llamadas a `RecursoRepository` dentro del flujo de edición.

El issue de GitHub asociado a esta corrección es: [issue #23](https://github.com/mmasias/pySigHor/issues/23).

## ¿Y ahora qué?

- El issue en GitHub describe las 5 capas con suficiente detalle para que un agente (OpenCode) lo resuelva de forma autónoma.
- Una vez resuelto, el commit de cierre debe referenciar el issue y actualizar `editarAula/secuencia.puml`.
- Esta brecha motiva una práctica de revisión: al generar diagramas de secuencia con agentes, verificar manualmente que todos los campos del wireframe aparecen como mensajes en el diagrama.

### Referencias cruzadas

- Especificación: `RUP/00-casos-uso/02-detalle/editarAula/`
- Diseño incompleto: `RUP/02-diseño/casos-uso/editarAula/secuencia.puml`
- Auditoría previa: [Artículo 024](../024-auditoria-diseno-vs-implementacion/README.md)
- Post-auditoría: [Artículo 025](../025-postAuditoria/README.md)
