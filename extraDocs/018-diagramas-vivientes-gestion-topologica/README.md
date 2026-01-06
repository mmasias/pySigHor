# Diagramas vivientes: gestión topológica de proceso mediante artefactos de análisis

<div align=right>

|||||
|-|-|-|-|
|[🏠️](../README.md)|**Artículo**|[Contexto](contexto.md)|[Evidencia](evidencia.md)

</div>

## Resumen

Este artículo propone el concepto de **"Diagramas vivientes"** como innovación metodológica para gestión de proyectos RUP: reutilizar artefactos de análisis estándar (diagramas de contexto de casos de uso) añadiéndoles una capa de metadatos de gestión mediante código de colores. Esta técnica transforma un mapa estático de "qué hace el sistema" en un mapa dinámico de "cómo va la construcción del sistema", proporcionando **visibilidad topológica** del progreso proyectado sobre la propia arquitectura funcional.

**Diferencia clave con el artículo 004:** El artículo 004 documentó el descubrimiento y diseño técnico del dashboard visual como herramienta práctica. Este artículo analiza el concepto subyacente desde una perspectiva metodológica comparativa, posicionándolo frente a herramientas de gestión existentes y proponiendo "diagramas vivientes" como patrón metodológico generalizable.

## El problema de la gestión de procesos RUP

### La dicotomía metodológica

La gestión de proyectos guiados por RUP tradicionalmente adolece de dos problemas opuestos:

#### 1. Opacidad estructural

Es difícil saber el estado real de avance en una estructura compleja de casos de uso interdependientes. Los artefactos RUP (diagramas de contexto, especificaciones, análisis MVC) son ricos conceptualmente pero **estáticos en cuanto a gestión**.

**Consecuencias:**

- Pérdida de visibilidad del progreso global
- Dificultad para identificar cuellos de botella
- Desconexión entre artefactos técnicos y seguimiento gerencial

#### 2. Sobrecarga de herramientas

Las herramientas clásicas de gestión RUP (Rational Suite, IBM RTC) eran pesadas, caras y separaban la gestión de la arquitectura, creando **duplicidad de esfuerzo**.

**Consecuencias:**

- Inversión prohibitiva para proyectos pequeños/educativos
- Doble mantenimiento (artefactos RUP + tickets de gestión)
- Barrera de entrada metodológica

### La trampa de las herramientas ágiles lineales

Las herramientas modernas (Jira, Trello, Azure DevOps) solucionaron el problema de accesibilidad, pero introdujeron una **limitación conceptual fundamental**:

#### Paradigma lineal

```
┌─────────┐    ┌─────────┐    ┌─────────┐
│ To Do   │ -> │ Doing   │ -> │  Done   │
└─────────┘    └─────────┘    └─────────┘
```

#### Qué pierden

- Perspectiva **topológica**: cómo las piezas se relacionan arquitectónicamente
- Impacto **sistémico**: cómo el avance de una pieza afecta al sistema completo
- Contexto **funcional**: qué áreas del negocio están maduras vs verdes

### Contraste fundamental

<div align=center>

|Herramientas ágiles lineales|Perspectiva topológica necesaria|
|-|-|
|Lista de tareas independientes|Mapa de funcionalidades interdependientes|
|Progreso secuencial (To Do → Done)|Progreso proyectado sobre arquitectura|
|Vista gerencial desconectada|Vista integrada (arquitectura + gestión)|
|¿Cuántas tareas completadas?|¿Qué partes del sistema están maduras?|

</div>

## Diagramas vivientes como solución

### Definición conceptual

**"Diagrama viviente"** es un artefacto técnico de análisis que incorpora metadatos de gestión de proceso mediante semántica visual (colores, estilos), permitiendo que el mismo diagrama comunique simultáneamente:

1. **Arquitectura funcional** (qué hace el sistema)
2. **Estado de construcción** (cómo va el desarrollo)
3. **Dependencias sistémicas** (qué afecta a qué)

### El "hack metodológico"

La innovación consiste en **reutilizar** el diagrama de contexto de casos de uso (artefacto RUP estándar) y **superponerle** una capa de gestión mediante código de colores que representa fases RUP:

```
Artefacto base:        Diagrama de contexto de casos de uso
                       (Tecnológicamente neutro, estándar RUP)
                                    +
Capa de gestión:       Código de colores semántico
                       (🔘 Gris: Identificado, 🟫 Amarillo: Análisis,
                        🟢 Verde: Diseño, 🔵 Azul: Implementación)
                                    ||
                                    \/
Diagrama viviente:     Mapa funcional + Dashboard de progreso
```

### Principio de simplicidad tecnológica

**Implementación minimalista:**

1. **Artefacto base**: Archivo fuente PlantUML (`.puml`) del diagrama de contexto
2. **Semántica de color**: Leyenda estandarizada vinculando colores a fases RUP
3. **Actualización continua**: Editar color en archivo `.puml` como parte del trabajo técnico
4. **Renderizado automático**: Git/IDE renderiza el nuevo estado visualmente

**Ejemplo de sintaxis PlantUML:**
```plantuml
NoAuth -[#darkgoldenrod,thickness=2]-> PreMenu
    note on link
        iniciarSesion()
        (Análisis completado)
    end note
```

## Comparativa con herramientas existentes

### Diferencia con C4 Model / Structurizr

<div align=center>

|Característica|Diagramas vivientes (este artículo)|C4 Model / Structurizr|
|-|-|-|
|**Propósito principal**|Gestión de proceso (Dinámico)|Documentación de estructura (Estático)|
|**Pregunta clave**|¿Cómo vamos con el desarrollo?|¿Qué es este sistema?|
|**Audiencia primaria**|Equipo de desarrollo + gestión|Arquitectos + nuevos desarrolladores|
|**Enfoque**|Minimalista / Topológico|Formal / Descriptivo|
|**Actualización**|Continua (cada avance técnico)|Puntual (cambios arquitectónicos)|
|**Semántica de color**|Estado de construcción (fases RUP)|Tipos de componentes (sistemas, contenedores)|
|**Ciclo de vida**|Evoluciona hasta completar proyecto|Estable después de arquitectura establecida|

</div>

**Complementariedad:** C4 documenta arquitectura estática. Diagramas vivientes rastrean construcción dinámica. Ambos son valiosos para propósitos diferentes.

### Diferencia con dashboards de herramientas ágiles

<div align=center>

|Característica|Diagramas vivientes|Jira/Trello/Azure DevOps|
|-|-|-|
|**Vista de progreso**|Topológica (sobre arquitectura)|Lineal (listas/tableros)|
|**Integración**|Unificada (artefacto = dashboard)|Separada (tickets ≠ código)|
|**Contexto arquitectónico**|Explícito (dependencias visibles)|Implícito (tags/épicas opcionales)|
|**Herramienta requerida**|Editor de texto + Git|Plataforma en la nube/servidor|
|**Costo**|$0 (archivos de texto versionados)|Licencias (nube/empresarial)|
|**Trazabilidad histórica**|Git log (automática)|Manual (actualizar estados)|

</div>

**Diferencia fundamental:** Herramientas ágiles gestionan **tareas**. Diagramas vivientes gestionan **capacidades del sistema**.

## Valor de la propuesta

### Visibilidad topológica

Permite ver el estado del proyecto **proyectado sobre la propia arquitectura**, identificando qué áreas funcionales están maduras y cuáles verdes.

**Pregunta respondida:** "De todas las capacidades del sistema, ¿cuáles están listas y cuáles no?"

**Contraste con vista lineal:** Kanban responde "¿cuántas tareas quedan?", diagramas vivientes responden "¿qué partes del negocio funcionan ya?"

### Economía de recursos

Integra arquitectura y gestión **reusando el diagrama** como reporte de estado. Elimina:

- Software externo de gestión (licencias, servidores)
- Duplicidad de mantener tickets separados de artefactos
- Desincronización entre código y seguimiento

**Principio:** Un solo artefacto, doble propósito (análisis + gestión).

### Trazabilidad histórica automática

Al estar versionado en Git, el historial del archivo genera automáticamente una **"película" de la evolución del proyecto** sin esfuerzo adicional.

**Ejemplo:**

```bash
# Ver evolución del diagrama
git log --all --graph -- RUP/99-seguimiento/diagrama-contexto-administrador.puml

# Comparar estado entre ramas
diff main diseño-cli-python diagrama-contexto-administrador.svg
```

### Valor didáctico

Enseña a visualizar el software como un **todo orgánico en evolución**, no como tickets aislados en un backlog.

**Para estudiantes:** Ven cómo el análisis RUP se materializa progresivamente en sistema funcional.

**Para profesionales:** Demostración de integración arquitectura-gestión sin herramientas complejas.

## Ejemplo de evolución: de análisis a diseño

El siguiente caso ilustra cómo el diagrama viviente refleja el progreso del proyecto al comparar el estado en la rama principal (`main`) frente a una rama de trabajo específica (`diseño-cli-python-http`).

<div align=center>

|Estado A: Rama `main`<br>(Hito de Análisis Completado)|Estado B: Rama `diseño-cli-python-http`<br>(Trabajo en Diseño)|
|-|-|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|![](https://raw.githubusercontent.com/mmasias/pySigHor/dise%C3%B1o-cli-python-http/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)
|Todos los casos de uso en amarillo (análisis completado)|Subconjunto de casos de uso en verde (diseño iniciado)

</div>

**Interpretación visual:**

- **Estado A:** Color predominante amarillo/marrón → proyecto en fase de análisis uniforme
- **Estado B:** Mezcla amarillo + verde → progreso heterogéneo (análisis vs diseño por caso de uso)
- **Observación clave:** Qué partes del sistema están evolucionando tecnológicamente mientras otras permanecen conceptuales

**Técnica de actualización:**

```bash
# Desarrollador avanza un caso de uso a diseño
# 1. Edita el archivo .puml cambiando color
vim RUP/99-seguimiento/diagrama-contexto-administrador.puml
# (Cambia #darkgoldenrod por #green en el caso de uso trabajado)

# 2. Genera imagen SVG
plantuml diagrama-contexto-administrador.puml

# 3. Commit que registra progreso
git add diagrama-contexto-administrador.{puml,svg}
git commit -m "Diseño: iniciarSesion() - análisis MVC → diseño CLI Python"
```

Esta técnica convierte la actualización del estado del proyecto en una **operación de código** (`git commit`), integrando perfectamente la gestión en el flujo de trabajo del desarrollador.

## Limitaciones y contextos de aplicación

### Cuándo NO usar diagramas vivientes

**1. Equipos muy grandes (>20 personas)**

- Demasiados casos de uso simultáneos en progreso
- Conflictos de fusión frecuentes en archivo `.puml`
- Herramientas empresariales (Jira) escalan mejor

**2. Proyectos que requieren métricas cuantitativas detalladas**

- Gráficos de avance, seguimiento de velocidad, estimaciones
- Diagramas vivientes son **cualitativos** (topología), no cuantitativos (métricas)

**3. Organizaciones con flujos de trabajo complejos de aprobación**

- Múltiples participantes revisando tickets
- Diagramas vivientes asumen flujo de trabajo técnico simple

**4. Proyectos sin metodología RUP/casos de uso**

- Requiere tener diagrama de contexto como artefacto base
- Metodologías puramente ágiles sin análisis previo no aplican

### Cuándo SÍ usar diagramas vivientes

**Contextos ideales:**

- **Equipos pequeños/medianos** (2-15 personas)
- **Proyectos educativos** donde aprender RUP es objetivo
- **Startups/proyectos con restricciones de presupuesto** (sin licencias de herramientas)
- **Desarrollo con metodología RUP** bien aplicada
- **Proyectos open source** donde trazabilidad en Git es valiosa

## Conexión con artículos anteriores

### Artículo 003: Independencia tecnológica de RUP

El [artículo 003](/extraDocs/003-rup-independencia-tecnologica/) estableció el experimento de completar análisis antes de tecnología específica.

**Conexión:** Diagramas vivientes visualizan ese progreso. Cuando todos los casos de uso están en amarillo (análisis), se puede bifurcar a múltiples tecnologías (verde/azul) sin modificar análisis.

### Artículo 004: Dashboard visual RUP

El [artículo 004](/extraDocs/004-dashboard-visual-rup-casos-uso/) documentó el descubrimiento y diseño técnico de la solución práctica.

**Este artículo extiende el 004:**

- Artículo 004: **Qué es** el dashboard, **cómo implementarlo** técnicamente
- Artículo 018: **Por qué importa** metodológicamente, **cómo se compara** con alternativas

### Artículo 007: Diagramas de contexto múltiples por tecnología

El [artículo 007](/extraDocs/007-diagramas-contexto-multiples-tecnologias/) propuso separar diagrama conceptual puro de diagramas tecnológicos específicos.

**Sinergia:** Diagramas vivientes aplican a **ambos niveles**:

- Diagrama conceptual puro: colores muestran progreso de análisis
- Diagramas tecnológicos específicos: colores muestran progreso de implementación por stack

### Artículo 016: Validación CLI

El [artículo 016](/extraDocs/016-validacion-cli/) demostró independencia del análisis ante paradigma de interfaz (GUI vs CLI).

**Evidencia visual:** Las imágenes comparativas main vs diseño-cli-python-http en este artículo muestran cómo diagramas vivientes reflejan esa bifurcación tecnológica sin modificar casos de uso base.

## Potencial de extensión

### Otros artefactos RUP candidatos

**Diagramas de clases de análisis:**

- Colores por estado: 🔘 Identificada, 🟫 Especificada, 🟢 Diseñada, 🔵 Implementada
- Visualiza qué clases conceptuales han sido materializadas en código

**Diagramas de secuencia:**

- Colores por completitud: 🔘 Flujo básico, 🟫 Flujos alternativos, 🟢 Manejo de errores
- Rastrea complejidad capturada en cada interacción

**Diagramas de actividad (algoritmos):**

- Colores por validación: 🔘 Diseñado, 🟫 Prototipado, 🟢 Optimizado, 🔵 Probado
- Seguimiento de algoritmos complejos (ej. generarHorario() en pySigHor)

### Herramientas de automatización

**Generación automática desde metadatos:**

```python
# Script que lee estado de casos de uso desde base de datos
# y actualiza colores en archivo .puml automáticamente

casos_uso = get_casos_uso_from_db()
for cu in casos_uso:
    color = map_fase_to_color(cu.fase_actual)
    update_puml_color(cu.nombre, color)
```

**Integración con CI/CD:**

```yaml
# GitHub Actions que regenera diagramas en cada commit
- name: Regenerar diagramas vivientes
  run: |
    plantuml -tsvg **/*.puml
    git add images/
```

### Métricas derivadas

**Indicadores cuantitativos extraíbles:**

- Porcentaje de casos de uso por fase (identificados/análisis/diseño/implementación)
- Velocidad de transición entre fases (commits/semana por color)
- Detección de cuellos de botella (casos de uso estancados en una fase)

## Reflexión metodológica

### ¿Es esto una innovación metodológica auténtica?

**Criterios de innovación metodológica:**

1. **Originalidad:** ¿Resuelve un problema conocido de forma nueva? ✅
2. **Generalización:** ¿Es aplicable más allá del proyecto original? ✅
3. **Simplicidad:** ¿Minimiza complejidad añadida? ✅
4. **Coherencia:** ¿Respeta principios de la metodología base (RUP)? ✅

**Contraste con "mejores prácticas":**

- Mejores prácticas: adoptan herramientas/técnicas establecidas
- Innovación metodológica: propone nuevo patrón metodológico transferible

**Conclusión:** "Diagramas vivientes" es un patrón metodológico auténtico, no solo una herramienta específica del proyecto pySigHor.

### Coherencia con filosofía RUP

**Principios RUP preservados:**

- **Desarrollo iterativo:** Diagramas evolucionan por iteraciones
- **Arquitectura-céntrico:** Gestión proyectada sobre arquitectura funcional
- **Basado en artefactos:** Reutiliza artefactos RUP estándar
- **Controlado por riesgos:** Visibilidad topológica identifica áreas verdes (riesgo)

**Diferencia con Rational Suite:**

- Rational Suite: solución empresarial completa pero pesada
- Diagramas vivientes: solución minimalista pero práctica

Ambos son válidos para RUP, diagramas vivientes democratizan acceso.

## Conclusiones

### Resultado

Se ha identificado y formalizado un patrón metodológico generalizable: **"Diagramas vivientes"** como técnica de gestión topológica de proceso mediante reutilización de artefactos de análisis con superposición de metadatos de gestión.

### Características distintivas

**Simplicidad técnica con impacto visual:**

- Archivos de texto + colores
- Arquitectura + gestión en un solo diagrama
- Reutiliza artefactos estándar de RUP

**Aplicación práctica:**

- Implementación sin inversión (PlantUML + Git)
- Aplicable en cualquier proyecto RUP
- Curva de aprendizaje mínima

### Impacto esperado

**Para proyectos RUP:**

- Alternativa accesible a herramientas empresariales
- Integración natural arquitectura-gestión
- Valor didáctico en contextos educativos

**Para la comunidad de ingeniería de software:**

- Demostración de que metodologías maduras pueden innovar
- Evidencia de que simplicidad no implica superficialidad
- Contribución al arsenal de técnicas ágiles-formales híbridas

### Diferencia entre herramientas y metodología

**Herramientas:** Jira, Trello, Rational Suite (implementaciones específicas)

**Metodología:** "Diagramas vivientes" como patrón (independiente de herramienta)

**Generalización:** El patrón puede materializarse en diferentes herramientas (PlantUML, Mermaid, Structurizr con extensiones).

## Próximos pasos

### Validación en otros proyectos

Aplicar diagramas vivientes en contextos diferentes (dominio distinto a SigHor) para validar transferibilidad del patrón.

### Formalización académica

Considerar publicación en conferencia/revista de ingeniería de software educativa, posicionando diagramas vivientes como contribución metodológica formal.

### Desarrollo de herramientas de soporte

Crear scripts/extensiones que faciliten:

- Generación automática de leyendas de color
- Validación de consistencia entre colores y estado real
- Extracción de métricas cuantitativas desde diagramas

## Referencias

- [Artículo 003: Análisis independiente de tecnología](/extraDocs/003-rup-independencia-tecnologica/)
- [Artículo 004: Dashboard visual RUP](/extraDocs/004-dashboard-visual-rup-casos-uso/)
- [Artículo 007: Diagramas de contexto múltiples por tecnología](/extraDocs/007-diagramas-contexto-multiples-tecnologias/)
- [Artículo 015: Dashboards multi-stack y validación experimental](/extraDocs/015-dashboards-multistack-validacion-experimental/)
- [Artículo 016: CLI como validación](/extraDocs/016-validacion-cli/)
- [Artículo 017: Opinión cruzada entre LLMs](/extraDocs/017-opinion-cruzada-llms/)
- [C4 Model - Software Architecture Diagrams](https://c4model.com/)
- [Structurizr - Software architecture diagrams as code](https://structurizr.com/)
- [PlantUML - Open-source tool for UML diagrams](https://plantuml.com/)

---

<div align=right>

**Artículo 018** - Diagramas vivientes: gestión topológica de proceso
Fecha: 6 de enero de 2026
pySigHor - Sistema generador de horarios

</div>
