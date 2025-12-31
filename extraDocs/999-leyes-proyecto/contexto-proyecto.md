# Contexto Esencial del Proyecto pySigHor

**Última actualización**: 2025-12-31 (Conversación 51)

Este documento contiene el contexto esencial del proyecto que Claude debe conocer en cada sesión. Se lee automáticamente al inicio según CLAUDE.md.

---

## 1. Visión del Proyecto

### SigHor: Arqueología de Software (1998)

**Sistema original**:
- Visual Basic 3.0 con GUI Windows
- Algoritmo de generación de horarios universitarios
- Aplicación avanzada de investigación de operaciones

**Proyecto pySigHor (2024-2025)**:
- **NO es un port**: Es un ejercicio metodológico con RUP
- **Objetivo**: Demostrar que un análisis riguroso puede soportar múltiples implementaciones tecnológicas
- **Valor**: Material didáctico de calidad excepcional para ingeniería de software

### Naturaleza Experimental del Proyecto

Este proyecto es un **laboratorio metodológico en tiempo real**:
- Valida promesas de RUP con evidencia verificable
- Documenta TODAS las decisiones (extraDocs, conversation-log)
- Prioriza valor didáctico sobre completitud de implementación
- Colaboración humano-IA documentada éticamente

---

## 2. Decisiones Metodológicas Fundamentales

### Artículo 003: Independencia Tecnológica RUP (Julio 2025)

**Hipótesis central**:
> "Un análisis RUP completo y riguroso puede soportar múltiples implementaciones tecnológicas sin modificaciones sustanciales a los artefactos de análisis."

**Decisión estratégica**:
- Completar TODO el análisis (32 casos de uso) ANTES de abordar tecnología específica
- Validar con implementaciones en stacks radicalmente diferentes

**Estado**: ✅ Análisis 100% completado (rama `main`)

📄 [Artículo completo](/extraDocs/003-rup-independencia-tecnologica/)

### Artículo 004: Dashboard Visual con Código de Colores

**Sistema de seguimiento visual**:
- 🔘 Gris punteado: Identificado
- 🔴 Rojo: Detalle/Prototipado
- 🟫 Amarillo oscuro: Análisis
- 🟢 Verde: Diseño
- 🔵 Celeste: Desarrollo
- 🔵 Azul: Pruebas
- ⚫ Negro continuo: Completado

**Propósito**: Visualizar progreso del experimento de independencia tecnológica en diagrama de contexto.

📄 [Artículo completo](/extraDocs/004-dashboard-visual-rup-casos-uso/)

### Artículo 014: Prototipado Más Allá de GUI

**Expansión del concepto de prototipado**:
- Los wireframes SALT son abstracciones de interacción, NO solo GUI
- El prototipado valida contratos de interfaz, no tecnologías específicas
- Múltiples puntos de contacto (GUI, API, CLI) pueden compartir el mismo análisis

**Implicación**: El análisis debe ser independiente del paradigma de interfaz.

📄 [Artículo completo](/extraDocs/014-prototipado-mas-alla-gui/)

### Artículo 015: Validación Multi-Stack Web

**Experimento**: Diseñar mismos 5 casos de uso en dos stacks diferentes

**Stacks validados**:
- FastAPI/React (Python, minimalista)
- Spring/Angular (Java, enterprise)

**Resultados**:
- ✅ 100% de artefactos de análisis sin modificación
- ✅ Consistencia arquitectónica alta
- ⚠️ Limitación: Ambos son web con GUI

📄 [Artículo completo](/extraDocs/015-dashboards-multistack-validacion-experimental/)

### Artículo 016: CLI como Validación (Actual)

**Experimento**: Validar independencia tecnológica con paradigma radicalmente diferente

**Dos arquitecturas CLI**:
1. CLI HTTP: Reusa backend FastAPI existente
2. CLI Standalone: Reimplementa pila completa sin HTTP

**Estado**: 🟢 Fase de diseño conceptual (documentación completa)

📄 [Artículo completo](/extraDocs/016-validacion-cli/)

---

## 3. Estado Actual del Repositorio

### Rama `main` (Análisis Puro)

**Análisis RUP 100% completado**:
- 32 casos de uso con especificación detallada completa
- 32 casos de uso con análisis MVC completo
- Diagramas de colaboración para todos los casos
- Diagramas de secuencia para casos complejos
- Modelo del dominio refinado
- Wireframes SALT para interfaces críticas

**IMPORTANTE**: Esta rama NO tiene código tecnológico específico.

### Rama `diseño-fastapi-react`

**5 casos de uso diseñados**:
1. `iniciarSesion()` - Autenticación
2. `abrirAulas()` - Listado
3. `crearAula()` - Creación
4. `editarAula()` - Edición
5. `eliminarAula()` - Eliminación

**Artefactos**:
- Arquitectura C4
- Clases de diseño (Pydantic, SQLAlchemy, JWT)
- Diagramas de secuencia con endpoints HTTP
- Configuración completa del proyecto

### Rama `diseño-spring-angular`

**Mismos 5 casos de uso diseñados**:
- Arquitectura C4 equivalente
- Clases de diseño (JPA, Spring Security)
- Diagramas de secuencia con endpoints HTTP
- Configuración Maven/Angular

**Propósito**: Validar que el análisis soporta stack radicalmente diferente.

### Artículos en `extraDocs/`

14 artículos documentando decisiones metodológicas, desde artículo 003 (independencia tecnológica) hasta 016 (validación CLI).

### Logs de Conversaciones

- `conversation-log-001.md`: Conversaciones 1-49 (histórico)
- `conversation-log.md`: Conversaciones 50+ (activo)

---

## 4. Convenciones Técnicas Establecidas

### Terminología: MVC (NO BCE)

**SIEMPRE usar**:
- ✅ Vista (View)
- ✅ Controlador (Controller)
- ✅ Modelo (Model)

**NUNCA usar**:
- ❌ Boundary
- ❌ Control
- ❌ Entity

**Rationale**: BCE es nomenclatura de Jacobson, pero el proyecto usa MVC por claridad y adopción universal.

### Idioma Vehicular: Español

**Obligatorio en**:
- Documentación markdown
- Comentarios de código
- Mensajes de commit
- Nombres de variables/funciones (cuando sea posible)
- Comunicación con Claude

**Excepción**: Código fuente legacy original (Visual Basic 3.0) se preserva tal cual.

### Eliminación de Anglicismos

**Preferencias establecidas**:
- ✅ "Reuso" (NO "reutilización")
- ✅ "Compromisos" (NO "trade-offs")
- ✅ "Sobrecarga" (NO "overhead")
- ✅ "Robusto/Robustez" (NO "resiliente/resiliencia")

**Principio**: Usar español técnico apropiado cuando existe equivalente claro.

### Formato de Documentación

**Tablas markdown**:
- Centrar tablas importantes con `<div align=center>`
- Usar formato de 5-6 columnas para navegación de artículos

**Diagramas**:
- PlantUML (.puml) como fuente
- SVG generados por Manuel (según Ley 004)

---

## 5. Leyes del Proyecto

### Ley 004: Rama de Revisión Obligatoria

**TODO trabajo Claude-Manuel → rama `xRevisar` primero**

**Flujo obligatorio**:
1. Proponer artefactos a Manuel
2. Manuel genera SVG de diagramas PlantUML
3. `git checkout xRevisar`
4. `git push -u origin xRevisar`
5. Esperar aprobación explícita de Manuel
6. Solo entonces: Pull Request a `main`

**Excepciones** (NO requieren xRevisar):
- Correcciones menores de typos
- Actualizaciones de conversation-log.md

📄 [Ley completa](/extraDocs/999-leyes-proyecto/ley-rama-revision.md)

---

## 6. Hitos Completados

### Fase de Análisis RUP ✅ (Nov 2025)

- 32 casos de uso analizados
- Patrón MVC riguroso aplicado
- Material didáctico excepcional

### Validación Multi-Stack Web ✅ (Dic 2025)

- FastAPI/React: 5 CdU diseñados
- Spring/Angular: 5 CdU diseñados
- 100% de análisis sin modificación

### Documentación CLI 🟢 (Dic 2025)

- Artículo 016 completado
- Comparativa de arquitecturas CLI
- Análisis de reuso vs reimplementación

---

## 7. Próximos Hitos Previstos

### Implementación CLI (Próximo)

- Crear rama `diseño-cli-python-http`
- Crear rama `diseño-cli-python-standalone`
- Validar análisis con paradigma no-GUI

### Expansión Futura (Por determinar)

- Desktop (Electron)
- Mobile (React Native)
- API GraphQL pura
- TUI (Terminal UI)

---

## 8. Métricas del Proyecto

| Métrica | Valor | Fecha |
|---------|-------|-------|
| Casos de uso analizados | 32/32 | Nov 2025 |
| Casos diseñados FastAPI/React | 5/32 | Dic 2025 |
| Casos diseñados Spring/Angular | 5/32 | Dic 2025 |
| Artículos extraDocs | 14 | Dic 2025 |
| Conversaciones documentadas | 51 | Dic 2025 |
| Artefactos de análisis modificados | 0 | - |

**Validación clave**: 0 modificaciones al análisis tras 3 implementaciones diferentes.

---

## 9. Colaboradores

**Manuel** (Usuario):
- Autor original de SigHor (1998)
- Director del experimento metodológico
- Revisor de calidad

**Claude Sonnet 4.5**:
- Asistente de análisis y diseño RUP
- Generador de diagramas y documentación
- Colaborador documentado éticamente

---

## 10. Referencias Clave

### Documentación Principal

- [README.md](/README.md) - Visión general del proyecto
- [CLAUDE.md](/CLAUDE.md) - Protocolo de trabajo con Claude
- [RUP/README.md](/RUP/README.md) - Estado de artefactos RUP

### Artículos Fundamentales

- [003: Independencia Tecnológica](/extraDocs/003-rup-independencia-tecnologica/)
- [004: Dashboard Visual](/extraDocs/004-dashboard-visual-rup-casos-uso/)
- [014: Prototipado Más Allá de GUI](/extraDocs/014-prototipado-mas-alla-gui/)
- [015: Validación Multi-Stack](/extraDocs/015-dashboards-multistack-validacion-experimental/)
- [016: CLI como Validación](/extraDocs/016-validacion-cli/)

### Leyes del Proyecto

- [Ley 004: Rama xRevisar](/extraDocs/999-leyes-proyecto/ley-rama-revision.md)

---

**Nota de mantenimiento**: Este documento debe actualizarse al final de cada sesión significativa cuando se tomen decisiones estratégicas, se completen hitos importantes, o se establezcan nuevas convenciones.
