<div align=right>
 
|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](/README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](/RUP/README.md) [![](https://img.shields.io/badge/-Modelo_del_dominio-FFF?style=flat&logo=freedesktop.org&logoColor=black)](/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md) [![](https://img.shields.io/badge/-Actores_&_Casos_de_Uso-FFF?style=flat&logo=crewunited&logoColor=black)](/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso.md) [![](https://img.shields.io/badge/-Diagrama_de_contexto-FFF?style=flat&logo=diagramsdotnet&logoColor=black)](/RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.md) [![](https://img.shields.io/badge/-Detalle_&_Prototipo-FFF?style=flat&logo=typeorm&logoColor=black)](/RUP/00-casos-uso/02-detalle/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](/RUP/01-analisis/casos-uso/README.md)
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](/RUP/README.md) [![](https://img.shields.io/badge/-Propuesta_de_dashboard-FFF?style=flat&logo=composer&logoColor=black)](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](/extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](conversation-log.md)

</div>

# Registro de Conversaciones - Proyecto pySigHor RUP

## Resumen

Este archivo mantiene un registro cronológico de todas las conversaciones, decisiones y evolución del proyecto de modernización de SigHor usando metodología RUP.

Dado el tamaño, continuamos aquí en la conversación 50: las anteriores están en el archivo [conversation-log-001.md](conversation-log-001.md)

## Conversación 50: Validación Experimental de Independencia Tecnológica RUP
**Fecha**: 2025-12-29
**Participantes**: Manuel (Usuario) + Claude Sonnet 4.5

### Contexto de la Sesión

Manuel retoma el proyecto tras un periodo inactivo (última conversación registrada: 2025-11-19). Solicita actualización del estado del proyecto y revisión de la rama `faseDiseño-Iteracion001`.

**Pregunta clave de Manuel**:
> "Sería guay terminar con todo el diseño, no? Por otro lado, un punto que tengo en la cabeza es, habiendo hecho el análisis, es ver qué tan independiente del diseño es un análisis bien hecho: mírate la reflexión 003 y comentamos"

Esta pregunta reconecta con la **decisión estratégica del Artículo 003** (julio 2025): validar experimentalmente la promesa fundamental de RUP sobre independencia tecnológica.

### Estado del Proyecto al Inicio de la Sesión

#### Rama `main`
- ✅ **Análisis RUP completo**: 32/32 casos de uso con diagramas de colaboración MVC
- ✅ **Análisis tecnológicamente neutro**: Sin menciones a HTTP, REST, frameworks específicos
- ✅ **Metodología consolidada**: Patrón MVC riguroso aplicado sistemáticamente
- ✅ **Material didáctico**: 14 artículos en extraDocs, 48 conversaciones documentadas

#### Rama `faseDiseño-Iteracion001`
- ✅ **Stack tecnológico definido**: Python + FastAPI + React + TypeScript
- ✅ **Diseño parcial**: 5/32 casos de uso diseñados (iniciarSesion + CRUD Aulas)
- ✅ **Artefactos creados**:
  - Arquitectura C4 (contenedores)
  - Clases de diseño (Pydantic, SQLAlchemy, JWT)
  - 5 diagramas de secuencia con endpoints HTTP específicos
  - Documento de configuración completo (672 líneas) con `pyproject.toml`, `package.json`, estructura de directorios

### Desarrollo Principal

#### 1. **Revisión del Artículo 003: La Promesa de RUP**

Claude lee y analiza el **Artículo 003: "RUP - Independencia Tecnológica"** (creado julio 2025):

**Hipótesis original**:
> "Un análisis RUP completo y riguroso puede soportar múltiples implementaciones tecnológicas sin modificaciones sustanciales a los artefactos de análisis"

**Estructura experimental propuesta en julio 2025**:
```
main/analisis-completo
├── rama-web-spa
├── rama-desktop
├── rama-mobile
├── rama-api-rest
└── rama-legacy-port
```

#### 2. **Evaluación del Estado Actual vs Hipótesis**

**Análisis crítico realizado**:

**✅ Análisis permanece independiente**:
- 32 diagramas de colaboración MVC sin tecnología específica
- No mencionan HTTP, JSON, FastAPI, React, Pydantic, SQLAlchemy, JWT
- Mapean perfectamente a cualquier stack (Spring/Django/Flutter/etc.)

**⚠️ Diseño es deliberadamente específico**:
- Rama `faseDiseño-Iteracion001` comprometida con FastAPI + React
- Diagramas de secuencia con endpoints HTTP concretos (`POST /token`, `GET /aulas`)
- Clases de diseño con tecnologías específicas

**🔬 Oportunidad experimental identificada**:
- Análisis completo (32 CdU) → **INMUTABLE**
- Diseño parcial (5 CdU FastAPI+React) → **Primera implementación**
- **Falta**: Segunda implementación con stack diferente para validar hipótesis

#### 3. **Decisión Estratégica: Validar el Experimento RUP**

**Pregunta de Claude a Manuel**:
> "¿Qué te emociona más ahora mismo?
> 1. Terminar el diseño FastAPI+React completo
> 2. Validar el experimento RUP con diseño alternativo
> 3. Otra idea"

**Respuesta de Manuel**:
> "Prefiero validar el experimento. Esta rama le podríamos dar un nombre más acorde al stack que estamos empleando y hacer un diseño paralelo en una rama faseDiseño-spring-angular. ¿Qué opinas?"

**Confirmación metodológica de Claude**:
> "¡ME ENCANTA! Es la decisión metodológicamente más valiosa."

### Plan de Validación Experimental Acordado

#### **Objetivo**
Probar con **evidencia verificable** que un análisis RUP bien hecho es independiente de tecnología.

#### **Diseño del Experimento**

**Variable independiente**: Análisis MVC (32 casos de uso) → **CONSTANTE**
**Variable dependiente**: Diseño tecnológico → **MÚLTIPLE**
**Hipótesis**: El análisis NO debe cambiar entre implementaciones tecnológicas

#### **Estructura de Ramas Propuesta**

```
main (Análisis completo 32/32 CdU - INMUTABLE)
│
├── diseño-fastapi-react          # Rama actual renombrada
│   ├── Backend: Python + FastAPI + SQLAlchemy + SQLite
│   ├── Frontend: React + TypeScript + Vite
│   └── Estado: 5/32 casos diseñados
│
└── diseño-spring-angular         # Nueva rama desde main
    ├── Backend: Java + Spring Boot + JPA + H2
    ├── Frontend: Angular + TypeScript
    └── Objetivo: MISMOS 5/32 casos diseñados
```

#### **Casos de Uso del Experimento (5 CdU)**

Los **mismos** en ambas ramas:
1. **iniciarSesion()** - Autenticación (JWT vs Spring Security)
2. **abrirAulas()** - Listado paginado
3. **crearAula()** - Creación con validación
4. **editarAula()** - Edición con merge parcial
5. **eliminarAula()** - Eliminación con confirmación

#### **Artefactos a Crear en Rama Spring-Angular**

Por coherencia con rama FastAPI-React:
- ✅ `RUP/02-diseño/README.md` - Stack Spring Boot + Angular
- ✅ `RUP/02-diseño/arquitectura.puml` - Diagrama C4 equivalente
- ✅ `RUP/02-diseño/clases-diseño.puml` - Entidades JPA, DTOs, Repositories
- ✅ `RUP/02-diseño/configuracion-proyecto.md` - `pom.xml`, `angular.json`, estructura Maven
- ✅ `RUP/02-diseño/casos-uso/[5 casos]/secuencia.puml` - Diagramas de secuencia Spring

#### **Métricas de Validación**

Al finalizar, se comparará:

| Métrica | Pregunta a Responder |
|---------|---------------------|
| **Cambios en Análisis** | ¿Se modificaron diagramas MVC entre ramas? |
| **Mapeo conceptual** | ¿Clases de análisis mapean 1:1 a ambos diseños? |
| **Decisiones tecnológicas** | ¿Qué decidió cada stack (FastAPI vs Spring)? |
| **Coherencia arquitectónica** | ¿Ambos respetan responsabilidades MVC? |

#### **Documentación Final Planificada**

**Artículo 015: Validación Experimental de Independencia Tecnológica RUP**

Contendrá:
- Hipótesis del Artículo 003 recordada
- Metodología experimental aplicada
- Evidencia concreta (commits, diagramas comparados)
- Hallazgos y conclusiones cuantificables
- Limitaciones identificadas
- Valor didáctico del experimento

### Plan de Ejecución Definido

#### **Fase 1: Reorganización de Ramas**

1. Renombrar `faseDiseño-Iteracion001` → `diseño-fastapi-react`
2. Actualizar remote en GitHub
3. Volver a `main` (análisis puro)
4. Crear rama `diseño-spring-angular` desde `main`

#### **Fase 2: Diseño con Spring Boot + Angular**

Crear artefactos equivalentes:
- Arquitectura Spring Boot + Angular (C4)
- Clases de diseño con JPA + Spring Data + Spring Security
- 5 diagramas de secuencia con endpoints REST Spring (`@RestController`)
- Configuración `pom.xml` + `angular.json` + estructura Maven
- Documento de configuración completo

#### **Fase 3: Comparación y Validación**

Verificar:
- ✅ Análisis MVC permanece inalterado en ambas ramas
- ✅ Ambos diseños son coherentes con el mismo análisis
- ✅ Diferencias son puramente tecnológicas, no conceptuales
- ✅ Mapeo clases de análisis → clases de diseño es consistente

#### **Fase 4: Documentación de Hallazgos**

Crear Artículo 015 con:
- Comparación lado a lado de ambos diseños
- Evidencia de commits mostrando análisis inmutable
- Identificación de patrones comunes vs específicos de tecnología
- Conclusiones sobre validez de independencia tecnológica RUP

### Valor de la Sesión

#### **Reconexión con Visión Metodológica Original**

- **Retorno al Artículo 003**: Recordar decisión estratégica de julio 2025
- **Validación pendiente**: Reconocer que el experimento aún no se ha ejecutado completamente
- **Oportunidad presente**: Tenemos el contexto perfecto para validar ahora

#### **Decisión Metodológica Crítica**

**Alternativas consideradas**:
- ❌ Completar diseño FastAPI+React (27 CdU restantes) → Valor: proyecto terminado
- ✅ **Validar experimento RUP** (diseño alternativo Spring+Angular) → Valor: evidencia científica

**Rationale de la decisión**:
- Coherencia con visión original del proyecto
- Evidencia experimental verificable sobre RUP
- Material didáctico de valor excepcional
- Respuesta científica a pregunta metodológica fundamental

#### **Diseño Experimental Riguroso**

- **Variable controlada**: Análisis (inmutable)
- **Variable experimental**: Stack tecnológico (2 implementaciones)
- **Medición objetiva**: Comparación de artefactos y decisiones
- **Evidencia verificable**: Commits de Git como testigos inmutables

### Reflexiones Metodológicas

#### **RUP Bajo Examen Real**

Esta sesión representa el momento donde el proyecto **trasciende la implementación** para convertirse en **laboratorio metodológico**:

- **Hipótesis clara**: Independencia tecnológica del análisis
- **Diseño experimental**: Dos implementaciones desde base común
- **Evidencia verificable**: Commits, diagramas, documentación
- **Honestidad intelectual**: Dispuestos a documentar éxitos y limitaciones

#### **Coherencia con Visión Original**

El Artículo 003 (julio 2025) estableció:
> "Estoy pensando que en este primer empujón lo dejaré todo con el análisis hecho y lo de tecnología lo abordaré(mos) luego, y en varias ramas."

**5 meses después**, estamos ejecutando exactamente esa visión con:
- ✅ Análisis 100% completado (32/32 CdU)
- ✅ Primera rama tecnológica (FastAPI+React) con 5 CdU
- 🎯 Segunda rama tecnológica (Spring+Angular) iniciando ahora
- 🎯 Validación experimental en curso

#### **Valor Didáctico Excepcional**

Este experimento generará:
- **Evidencia concreta** sobre promesas metodológicas de RUP
- **Comparación práctica** de stacks tecnológicos modernos
- **Material educativo** auténtico (no simulado)
- **Metodología replicable** para otros proyectos

### Próximos Pasos Inmediatos

1. ✅ **Documentar esta conversación** en conversation-log.md
2. 🎯 Renombrar rama `faseDiseño-Iteracion001` → `diseño-fastapi-react`
3. 🎯 Crear rama `diseño-spring-angular` desde `main`
4. 🎯 Diseñar arquitectura Spring Boot + Angular
5. 🎯 Diseñar los 5 casos de uso con Spring/Angular
6. 🎯 Comparar ambos diseños con análisis común
7. 🎯 Documentar hallazgos en Artículo 015

### Estado Final de la Sesión

- **Decisión tomada**: Validar experimento RUP mediante diseño paralelo
- **Estrategia definida**: Dos ramas de diseño desde análisis común
- **Metodología acordada**: Comparación rigurosa con métricas objetivas
- **Próxima acción**: Renombrar ramas e iniciar diseño Spring-Angular
- **Conversación documentada**: Lista para continuar trabajo

### Commits Pendientes

- Pendiente: Actualización de `conversation-log.md` con Conversación 50
- Rama actual: `faseDiseño-Iteracion001` (será renombrada)
- Siguiente: Reorganización de ramas y creación de diseño Spring-Angular

---

## Conversación 51: Pulido Final del Artículo 016 - CLI como Validación
**Fecha**: 2025-12-31
**Participantes**: Manuel (Usuario) + Claude Sonnet 4.5

### Contexto de la Sesión

Sesión continuada desde conversación previa que se quedó sin contexto. Manuel retoma el trabajo de pulido del **Artículo 016: CLI como validación** - la validación de independencia tecnológica RUP mediante interfaz de línea de comandos.

**Estado al inicio**: El artículo 016 ya tenía estructura completa con múltiples archivos markdown, pero requería refinamiento de terminología y formato.

### Desarrollo Principal

#### 1. **Eliminación Sistemática de Anglicismos**

Manuel solicitó eliminar anglicismos innecesarios a lo largo de todo el artículo 016:

**Cambios realizados**:
- ❌ "Overhead de red" → ✅ "Sobrecarga de red"
- ❌ "Resiliente/Resiliencia" → ✅ "Robusto/Robustez"
- ❌ "Trade-offs" → ✅ "Compromisos"

**Archivos afectados**:
- `comparativa-arquitecturas-cli.md`: 3 ocurrencias de "resiliente", 3 de "trade-offs"
- `reuso-vs-reimplementacion.md`: 1 "overhead", 1 "resiliente", 3 "trade-offs"

**Rationale**: Mantener pureza del español técnico, evitando anglicismos cuando existe terminología española equivalente y clara.

#### 2. **Cambio Terminológico Mayor: "Reutilización" → "Reuso"**

**Pregunta de Manuel**:
> "reuso o reutilización? qué término es más adecuado?"

**Análisis de Claude**:
- **"Reuso"**: Más técnico, conciso, adoptado en ingeniería de software
- **"Reutilización"**: Más genérico, suena redundante ("utilización" ya implica "usar")

**Decisión de Manuel**: Cambiar todo a "reuso"

**Operación sistemática ejecutada**:

```bash
# Cambios en todos los archivos .md del artículo 016
sed -i 's/Reutilización/Reuso/g; s/reutilización/reuso/g;
        s/Reutiliza/Reusa/g; s/reutiliza/reusa/g' *.md
```

**Alcance**:
- ✅ **119 ocurrencias** cambiadas en 5 archivos markdown
- ✅ Archivo renombrado: `reutilizacion-vs-reimplementacion.md` → `reuso-vs-reimplementacion.md`
- ✅ Todas las referencias cruzadas actualizadas
- ✅ Corrección de género: "la reuso máxima" → "el reuso máximo"
- ⚠️ Excepción mantenida: "reutilizable" (adjetivo estándar en español)

**Error detectado y corregido**:
- ❌ El `sed` inicial creó enlace malformado: "reusacion-vs-reimplementacion.md"
- ✅ Corregido con segundo `sed`: "reuso-vs-reimplementacion.md"

#### 3. **Centrado de Tablas**

Manuel indicó que había comenzado a centrar tablas manualmente pero se quedó en el caso de uso `iniciarSesion()`.

**Tablas centradas**:
- `abrirAulas()` - Implementación desde análisis
- `abrirAulas()` - Implementación con reuso (CLI HTTP)
- Totales del experimento (5 casos de uso)
- Criterios de decisión (matriz de arquitecturas)

**Formato aplicado**:
```markdown
<div align=center>

| Columna 1 | Columna 2 |
|-----------|-----------|
| Dato      | Dato      |

</div>
```

#### 4. **Corrección de Tablas de Navegación - Artículo 015**

Manuel detectó que las tablas de navegación del **Artículo 015** tenían formato incorrecto (3 columnas compactadas con `\|` en lugar de columnas separadas).

**Estado original (incorrecto)**:
```markdown
||||
|-|-|-|
|[🏠️](../README.md)|**Artículo**|[Contexto](contexto.md) \| [Evidencia](evidencia.md) \| [Comparativa](comparativa-stacks.md)|
```

**Estado corregido**:
```markdown
||||||
|-|-|-|-|-|
|[🏠️](../README.md)|**Artículo**|[Contexto](contexto.md)|[Evidencia](evidencia.md)|[Comparativa](comparativa-stacks.md)|
```

**Archivos corregidos**:
- ✅ `015-dashboards-multistack-validacion-experimental/README.md`
- ✅ `015-dashboards-multistack-validacion-experimental/contexto.md`
- ✅ `015-dashboards-multistack-validacion-experimental/evidencia.md`
- ✅ `015-dashboards-multistack-validacion-experimental/comparativa-stacks.md`

### Resumen de Cambios Totales

#### Archivos Modificados

**Artículo 016**:
- `reuso-vs-reimplementacion.md` (renombrado desde `reutilizacion-vs-reimplementacion.md`)
- `comparativa-arquitecturas-cli.md`
- `evidencia.md`
- `contexto.md`
- `README.md`

**Artículo 015**:
- `README.md`
- `contexto.md`
- `evidencia.md`
- `comparativa-stacks.md`

#### Métricas de Cambios

| Tipo de Cambio | Cantidad |
|----------------|----------|
| Anglicismos eliminados | ~10 ocurrencias |
| "Reutilización" → "Reuso" | 119 ocurrencias |
| Tablas centradas | 4 tablas |
| Tablas de navegación corregidas | 4 archivos |
| Archivos renombrados | 1 archivo |
| Enlaces actualizados | Todos los archivos relacionados |

### Valor de la Sesión

#### **Calidad de Documentación Técnica en Español**

Esta sesión demuestra compromiso con:
- **Pureza lingüística**: Eliminar anglicismos innecesarios
- **Terminología técnica apropiada**: "Reuso" > "Reutilización"
- **Consistencia**: Cambios sistemáticos en todos los archivos
- **Formato profesional**: Tablas centradas, navegación coherente

#### **Material Didáctico de Calidad**

El Artículo 016 ahora está listo como material educativo:
- ✅ Terminología española técnica apropiada
- ✅ Sin anglicismos innecesarios
- ✅ Formato visual consistente
- ✅ Navegación coherente entre archivos

#### **Metodología de Pulido Documental**

Esta sesión establece patrón para pulido de documentación:
1. **Identificación de anglicismos**: Revisión crítica de términos
2. **Análisis terminológico**: Evaluar alternativas en español
3. **Cambios sistemáticos**: Usar herramientas (`sed`) para consistencia
4. **Verificación de enlaces**: Asegurar referencias cruzadas correctas
5. **Formato visual**: Centrado de tablas, alineación consistente

### Reflexiones sobre Gestión de `conversation-log.md`

**Problema identificado**: El archivo `conversation-log.md` se volvió muy largo, por lo que se creó `conversation-log-001.md` para conversaciones 1-49.

**Discusión pendiente con Manuel**: ¿Cuál es la mejor estrategia para gestionar logs de conversaciones crecientes?

**Opciones a considerar**:
1. **Archivos numerados por rango**: `conversation-log-001.md` (Conv. 1-49), `conversation-log-002.md` (Conv. 50-99)
2. **Archivos por fecha**: `conversation-log-2025-Q4.md`, `conversation-log-2026-Q1.md`
3. **Archivos por fase RUP**: `conversation-log-analisis.md`, `conversation-log-diseño.md`
4. **Archivo índice + archivos individuales**: `conversation-log.md` (índice) + `conversations/051.md`

**Estado actual**: Conversación 51 añadida a `conversation-log.md`. Esperando feedback de Manuel sobre estrategia de gestión de logs.

### Estado Final de la Sesión

**Artefactos listos**:
- ✅ Artículo 016 completamente pulido
- ✅ Artículo 015 con tablas de navegación corregidas
- ✅ Terminología española consistente
- ✅ Formato profesional aplicado

**Pendiente**:
- 🎯 Decidir estrategia de gestión de `conversation-log.md`
- 🎯 Generar SVG de diagramas PlantUML (según Ley 004)
- 🎯 Subir a rama `xRevisar` para aprobación de Manuel

### Próximos Pasos

Según **Ley 004: Rama de Revisión Obligatoria**:

1. **Proponer artefactos**: "Artefactos listos, necesito que generes los SVG"
2. **Esperar SVG**: Manuel convierte archivos .puml a .svg
3. **Rama xRevisar**: `git checkout -b xRevisar` o `git checkout xRevisar`
4. **Push completo**: `git add . && git commit && git push -u origin xRevisar`
5. **Comunicar**: "Trabajo completado en rama xRevisar, listo para revisión"
6. **Esperar OK**: No proceder sin aprobación explícita
7. **Pull Request**: Solo después de "OK para PR"

---

## Conversación 52: Auditoría diseño vs implementación - Ciclo completo

**Fecha**: 2026-05-13
**Rama de trabajo**: `diseño-fastapi-react` (código) + `main` (documentación)
**Participantes**: Manuel, opencode (glm-5.1)

### Contexto

La rama `diseño-fastapi-react` contenía código generado por "equipo B" (sesiones previas de vibe coding con LLMs) que se había apartado del diseño especificado en `RUP/02-diseño/configuracion-proyecto.md`. Se detectó la necesidad de una auditoría formal antes de continuar la construcción.

### Actividad 1: Auditoría formal

Se creó el artículo 024 en `main` con 4 archivos:

- `articulo.md`: Presentación del problema y metodología
- `auditoria.md`: Tabla maestra de 20 desviaciones (D01-D20) con referencias exactas a línea de diseño vs línea de código
- `contexto.md`: Estado del proyecto en el momento de la auditoría
- `seguimiento.md`: Tabla de seguimiento commit por commit

**Tags de referencia**:
- `pre-auditoria-diseno-codigo` (`40af49d`): estado divergente inmutable
- `post-auditoria-diseno-codigo` (`fff93aa`): estado alineado al diseño

Las 20 desviaciones se clasificaron por severidad: CRITICA (D01 sync/async, D05 sin auth), ALTA (D02 pydantic, D08 sin alembic), MEDIA y BAJA.

### Actividad 2: Refactoring por capas (12 commits)

Cada commit resolvió desviaciones específicas con trazabilidad en el mensaje:

| Commit | Capa | Desviaciones resueltas |
|---|---|---|
| R01 | Dependencias (pyproject.toml) | D02 |
| R02 | Config (config.py) | D02, D03, D04 |
| R03 | Database (database.py) | D01 |
| R04 | Security (security.py) | D01, D10 |
| R05 | Models (todos) | D06, D07 |
| R06 | Schemas (todos) | D02, D16 |
| R07 | Repositories (todos) | D01, D17 |
| R08 | Services (todos) | D01, D17 |
| R09 | Routers (todos + main.py) | D01, D04, D05 |
| R10 | Infraestructura (alembic + tests) | D08, D09 |
| R11 | Frontend bugs (theme, auth, interceptor) | D13, D14, D15 |
| R12 | Navegacion (Layout, components/) | D11, D18, D20 |

**Resultado**: 18/20 desviaciones resueltas. D12 (selectores FK) y D19 (utils/) quedan pendientes.

### Actividad 3: Documentación post-auditoría

Se creó el artículo 025 en `main` cerrando el ciclo:

- README.md con la estructura metodológica estándar (por qué, qué, para qué, cómo, y ahora qué)
- Tabla de lecciones metodológicas aprendidas
- Evolución del flujo de trabajo: LEY 004 obsoleta para construcción
- Referencias cruzadas: artículo 024, tags pre/post, diff completo

### Decisiones tomadas

1. **Migración completa ahora** (sync->async, pydantic v1->v2) en lugar de documentar como deuda técnica
2. **Artículo 025 separado del 024**: separa "problema detectado" (024) de "resolución y lecciones" (025), consistente con la estructura un-artículo-por-momento de extraDocs
3. **LEY 004 obsoleta para construcción**: push directo a rama de desarrollo, revisión sobre la rama de construcción
4. **Refactoring por capas**: un commit por capa arquitectónica para trazabilidad granular

### Estado Final

**Artefactos completados**:
- Artículo 024 (auditoría) en `main` (`eab20ce` + `e3d99cf`)
- Artículo 025 (post-auditoría) en `main` (`d3ea8fc`)
- 12 commits de refactoring en `diseño-fastapi-react` (pushed a origin)
- Tags `pre-auditoria-diseno-codigo` y `post-auditoria-diseno-codigo` en remote
- `seguimiento.md` actualizado con hashes reales de todos los commits

**Pendiente**:
- D12: Selectores FK en AulasPage (Edificio) y CursosPage (Programa)
- D19: Directorio `frontend/src/utils/` cuando haya utilidades que extraer
- Continuar construcción del dominio core (generarHorario, consultarHorario)

---

*Este registro se actualizará continuamente conforme avance del proyecto*
