# Contexto - Mapa de Implementación FastAPI + React

<div align=right>

||||||
|-|-|-|-|
|[🏠️](../README.md)|**Artículo 020**|[Contexto](contexto.md)|[Plan de Iteraciones](plan-iteraciones.md)|[Metodología](metodologia.md)|

</div>

## Información del Artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Construcción (Construction)
- **Disciplina**: Implementación + Gestión de Proyectos
- **Versión**: 1.0
- **Fecha**: 15 de febrero de 2026
- **Autor**: Manuel Masias (Usuario) + Claude Sonnet 4.5 (Asistente)

## Contexto del Proyecto

### Antecedentes Inmediatos

**Artículo 019** (21/01/2026): Extracción de BD Access 2.0
- ✅ Estructura completa de la base de datos documentada
- ✅ Coherencia validada: Modelo del dominio ↔ tablas BD Access
- ✅ Decisión pendiente: Motor de base de datos (SQLite → PostgreSQL)

**Artículo 015** (2025-12-29): Validación experimental de independencia tecnológica
- ✅ Hipótesis: Análisis RUP soporta múltiples stacks tecnológicos
- ✅ Diseño paralelo FastAPI+React vs Spring+Angular iniciado
- ✅ 5/32 casos de uso diseñados en FastAPI+React

**Conversación 50** (2025-12-29): Retomo del proyecto
- Manuel pregunta: "¿Sería guay terminar con todo el diseño?"
- Claude propone: Validar el experimento RUP con diseño alternativo
- Decisión: Crear rama `diseño-spring-angular` para comparar stacks

**Conversación 51** (2025-12-31): Pulido final del Artículo 016
- Artículo 016 completado (CLI como validación de independencia)
- Pendiente: Generar SVG y subir a rama `xRevisar`

### Estado Actual del Proyecto

**Análisis RUP**:
- ✅ 32/32 casos de uso analizados (diagramas de colaboración MVC)
- ✅ Modelo del dominio completo y validado
- ✅ Tecnológicamente neutro (sin HTTP, JSON, frameworks específicos)

**Diseño FastAPI+React**:
- ✅ 5/32 casos de uso diseñados (Iteración 1: Auth + CRUD Aulas)
- ✅ Arquitectura C4 de contenedores
- ✅ Clases de diseño (Pydantic, SQLAlchemy, JWT)
- ✅ Configuración de proyecto completa (pyproject.toml, package.json)
- ✅ Diagramas de secuencia con endpoints HTTP concretos

**Ramas de Git**:
- `main` - Análisis completo (32/32 CdU)
- `diseño-fastapi-react` - Diseño parcial (5/32 CdU)
- `diseño-spring-angular` - Diseño pendiente
- `betaDeTest` - Test Java de implementación
- `xRevisar` - Rama de revisión (Ley 004)

## El Problema: ¿Qué Implementar Primero?

### Pregunta Inicial de Manuel

> "habia una rama en la que habiamos empezado la implementación. No estoy seguro que sea una de las principales, por lo que dale un vistazo a las que existen. Además, cara a la implementación, creo recordar que dijimos que era necesario tener el modelo de datos. Revisa"

### Descubrimiento

1. **Rama `betaDeTest`**: Contiene `CrearCursoUseCaseTest.java` (arquitectura hexagonal)
2. **Modelo de datos**: Artículo 019 ya lo había extraído y documentado completamente
3. **Diseño FastAPI+React**: Más avanzado que Spring+Angular (5 vs 0 casos)

### Dilema Estratégico

Claude presentó tres opciones iniciales:

**Opción A**: Implementar con diseño PARCIAL (FastAPI+React 5/32)
- Enfoque: Pragmático, resultado rápido
- Riesgo: Los 27 casos restantes pueden requerir rediseño

**Opción B**: Construir sistema enterprise-ready (Spring+Angular)
- Enfoque: Robustez empresarial
- Desventaja: Más verboso, curva de aprendizaje más alta

**Opción C**: Completar diseño ANTES de implementar
- Enfoque: Metodológico, más rigor
- Ventaja: Evita rediseño durante implementación

## Clarificación del Objetivo del Proyecto

### Aporte Clave de Manuel

> "este proyecto quiere validar el hecho que RUP permite construir sobre una base arquitectónicamente definida, y que no es problema ajustar conforme vas construyendo. Me preocupa 'menos' ver el algoritmo funcionando que tener la aplicación completa habiendo y teniendo trazada su construcción (es, en esencia, un proyecto con naturaleza pedagógica)."

### Naturaleza Pedagógica Confirmada

**NO es**:
- Ver el algoritmo funcionar rápidamente
- Construir un sistema para producción inmediata
- Demostrar que diseñamos todo perfectamente desde el inicio

**SÍ es**:
- Validar que RUP permite construir sobre base arquitectónica
- Documentar ajustes entre diseño e implementación
- Tener trazabilidad completa de construcción
- Generar evidencia pedagógica para comunidad

## Evidencia que Queremos Generar

### Tipo 1: "Diseñamos todo perfecto" ❌

```
Diseño completo (32 CdU)
         ↓
Implementación perfecta
         ↓
Sin errores, sin ajustes
```

**Problema**: NO demuestra que RUP permite ajustarse durante construcción

### Tipo 2: "Diseñamos → Ajustamos → Documentamos" ✅

```
Diseño de 5 casos
         ↓
Implementación con ajustes reales
         ↓
Documentación de decisiones
         ↓
Diseño de siguientes 5 casos (mejorados)
         ↓
Implementación con nuevos ajustes
         ↓
...repetir hasta completar 32 casos
         ↓
Conclusión: "RUP permitió construir ajustándose"
```

**Ventaja**: SÍ demuestra que RUP permite construir ajustándose

## Solución: Implementación por Iteraciones

### Estrategia Definida

**Opción D+: Implementación por Iteraciones con Documentación de Ajustes**

```
Iteración 1: Implementar 5 casos YA DISEÑADOS
   ↓
Validar: ¿El diseño funcionó? ¿Qué ajustamos?
   ↓
Documentar ajustes (conversation-log + casos de uso)
   ↓
Iteración 2: Diseñar siguientes 5 casos (aplicando aprendizaje)
   ↓
Implementar casos 6-10
   ↓
Validar y documentar ajustes
   ↓
...repetir hasta completar 32 casos
   ↓
Conclusión: "RUP permitió construir ajustándose"
```

### Especificación de Manuel

1. **Evidencia**: Commits bien descritos del proyecto (no documentación formal forzada)
2. **Tamaño de iteraciones**: 5 CdU por iteración (un CRUD de entidad a la vez)
3. **Momento de documentación**: Al final de cada iteración (coincide con inicio de siguiente)
4. **Ubicación de documentación**: En los tres puntos (conversation-log, casos de uso, artículo 020)
5. **Requisito crítico**: Al finalizar cada iteración → **ejecutable testeable** en localhost
6. **Validación**: Se hace sobre el ejecutable, luego se procede a siguiente iteración

### Criterio de Éxito por Iteración

- ✅ Ejecutable funcional: Backend + Frontend corriendo en localhost
- ✅ Commits descriptivos: Historia clara en mensajes de commit
- ✅ Validación manual: Tests ejecutados sobre el ejecutable
- ✅ Ajustes documentados: En conversation-log + casos de uso + artículo 020

## Decisiones Tomadas

### Stack Tecnológico

**Seleccionado**: FastAPI + React + TypeScript

**Rationale**:
- Continuidad inmediata (5 casos ya diseñados)
- Prototipado rápido para llegar al algoritmo principal
- Stack moderno y demandado en el mercado
- Zero-config con SQLite para desarrollo
- Coherente con objetivo pedagógico (ver ajustes, no infraestructura enterprise)

**Descartado**: Spring + Angular
- Mejor para producción empresarial
- Pero más verboso y curva de aprendizaje más alta
- Diseño menos avanzado que FastAPI+React

### Motor de Base de Datos

**Fase de experimentación** (actual):
- **SQLite** para desarrollo rápido
- Zero-config, archivo único
- Esquema idéntico permite migrar posteriormente

**Fase de producción** (futura):
- **PostgreSQL** como motor unificado
- Transversal a todos los stacks
- SQL estándar evita vendor lock-in

**Decisión**: Empezar con SQLite, migrar a PostgreSQL cuando el sistema esté validado.

### Plan de Iteraciones

**7 iteraciones de ~5 casos cada una**:

1. Auth + Aulas (5 casos) - ✅ Diseño completo
2. Edificios (4 casos)
3. Recursos (4 casos)
4. Profesores + Preferencias (5 casos)
5. Programas (4 casos)
6. Cursos (5 casos)
7. Algoritmo Principal (3-4 casos) - 🎯 El corazón del sistema

## Próximos Pasos

1. ✅ Artículo 020 creado en rama `main` (este documento)
2. ⏳ Actualizar índice de `extraDocs/README.md`
3. ⏳ Cambiarse a rama `diseño-fastapi-react`
4. ⏾ Iniciar Iteración 1: Implementación de Auth + CRUD Aulas
5. ⏾ Validar ejecutable localhost
6. ⏾ Documentar ajustes de Iteración 1
7. ⏾ Continuar con Iteración 2

## Valor de la Sesión

### Alineación de Objetivos

- **Clarificación**: Naturaleza pedagógica del proyecto confirmada
- **Evidencia**: Commits como testimonio del proceso de ajuste
- **Estrategia**: Implementación por iteraciones con ejecutable testeable por iteración

### Metodología Validada

- **RUP flexible**: Permite construir sobre base arquitectónica definida
- **Ajustes documentados**: No hay perfección inicial, hay mejora continua
- **Trazabilidad completa**: Cada commit cuenta una historia

---

**Contexto** - Artículo 020
Fecha: 15 de febrero de 2026
Conversación: 52
pySigHor - Sistema generador de horarios
