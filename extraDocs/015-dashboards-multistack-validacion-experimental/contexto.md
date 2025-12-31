# Contexto: Dashboards multi-stack y validación experimental

<div align=right>

||||||
|-|-|-|-|-|
|[🏠️](../README.md)|[Artículo](README.md)|**Contexto**|[Evidencia](evidencia.md)|[Comparativa](comparativa-stacks.md)|

</div>

## Antecedentes del experimento

### Artículo 003: La promesa de RUP bajo examen

En el [artículo 003](/extraDocs/003-rup-independencia-tecnologica/) se documentó una decisión estratégica clave:

> "Estoy pensando que en este primer empujón lo dejaré todo con el análisis hecho y lo de tecnología lo abordaré(mos) luego, y en varias ramas. Si RUP es cierto, debería poder avanzar el análisis y, ante cambios de tecnología, todos los artefactos hasta ese punto no deberían verse afectados."

Esta decisión marcó el inicio de un **experimento metodológico en tiempo real** para validar la promesa fundamental de RUP sobre independencia tecnológica.

**Hipótesis del experimento:**
Un análisis RUP completo y riguroso puede soportar múltiples implementaciones tecnológicas sin modificaciones sustanciales a los artefactos de análisis.

**Estructura experimental propuesta:**
```
main/analisis-completo
├── rama-web-spa        # React/Vue/Angular
├── rama-desktop        # Electron/Tauri
├── rama-mobile         # React Native/Flutter
├── rama-api-rest       # Express/FastAPI/Spring
└── rama-legacy-port    # VB.NET/Java (port directo)
```

### Artículo 004: Dashboard visual como herramienta de gestión

El [artículo 004](/extraDocs/004-dashboard-visual-rup-casos-uso/) introdujo una innovación metodológica: usar el diagrama de contexto RUP como dashboard visual mediante codificación por colores.

**Sistema de codificación desarrollado:**
- **Líneas punteadas** (grosor 1): Casos de uso identificados, no iniciados
- **Líneas continuas** (grosor 2): Casos de uso en trabajo activo
- **Colores por disciplina RUP:**
  - 🔘 Gris punteado: Identificado
  - 🔴 Rojo: Detalle/Prototipado
  - 🟫 Amarillo oscuro: Análisis
  - 🟢 Verde: Diseño
  - 🔵 Celeste: Desarrollo
  - 🔵 Azul: Pruebas
  - ⚫ Negro continuo: Completado

**Valor de la innovación:**
- Visibilidad instantánea del estado del proyecto
- El dashboard ES parte de la metodología RUP
- No requiere herramientas externas
- Evoluciona naturalmente con el proyecto

## Materialización del experimento

### Completitud del análisis

**Estado del proyecto antes del experimento:**
- ✅ 32 casos de uso con especificación detallada completa
- ✅ 32 casos de uso con análisis MVC completo
- ✅ Diagramas de colaboración para todos los casos
- ✅ Diagramas de secuencia para casos complejos
- ✅ Modelo del dominio refinado
- ✅ 100% del análisis RUP completado

Este nivel de completitud permitió iniciar el experimento con una base sólida y verificable.

### Selección de casos de uso para validación inicial

**Criterio de selección:** Vertical slice del módulo de aulas
- Cubre operaciones CRUD completas
- Incluye autenticación y navegación
- Representa complejidad real sin ser excesivo
- 5 casos de uso: cantidad manejable para primera validación

**Casos seleccionados:**
1. `iniciarSesion()` - Autenticación de usuarios
2. `abrirAulas()` - Apertura de gestión de aulas
3. `crearAula()` - Creación de aulas ("el delgado" C→U)
4. `editarAula()` - Edición de aulas ("el gordo" con edición continua)
5. `eliminarAula()` - Eliminación segura con confirmación

### Selección de stacks tecnológicos

**Stack 1: FastAPI/React**
- **Backend:** FastAPI (Python) - framework moderno, async, type hints
- **Frontend:** React + TypeScript - biblioteca compositiva, flexible
- **Filosofía:** Minimalista, rápido, pragmático
- **Target:** Startups, MVPs, APIs modernas

**Stack 2: Spring/Angular**
- **Backend:** Spring Boot (Java) - framework enterprise, maduro, robusto
- **Frontend:** Angular + TypeScript - framework opinionado, full-featured
- **Filosofía:** Enterprise, estructurado, escalable
- **Target:** Corporaciones, sistemas críticos, equipos grandes

**Razón de esta combinación:**
- Representan **dos filosofías distintas** de desarrollo (Python vs Java)
- **Frameworks con diferente nivel de opinión** (React minimalista vs Angular completo)
- **Paradigmas diferentes** (biblioteca vs framework)
- **Culturas de desarrollo diferentes** (startup vs enterprise)
- **Maximiza la validación** de independencia tecnológica

## Desafío arquitectónico: navegación multi-stack

### El problema de la duplicación

**Escenario inicial:**
- Dashboard en `/main/` con todos los casos analizados
- Ramas de diseño necesitan mostrar progreso específico
- Navegación debe ser coherente dentro de cada contexto

**Pregunta crítica:**
¿Cómo enlazar artefactos de análisis (compartidos) con artefactos de diseño (específicos por stack) sin duplicar documentación?

### Solución: arquitectura de navegación jerárquica

**Principios establecidos:**
1. **Single Source of Truth:** Análisis y Detalle SIEMPRE en `/main/`
2. **Especialización por rama:** Solo artefactos de Diseño en ramas tecnológicas
3. **Enlaces contextuales:** `[D]` apunta a rama específica, `[A]` y nombre de caso apuntan a `/main/`
4. **Dashboard por contexto:** Cada rama tiene su propia vista del progreso

**Implementación técnica:**
```plantuml
# En main: sin enlaces [D]
NoAuth -[#darkgoldenrod,thickness=2]-> Menu: [[.../detalle/iniciarSesion/README.md iniciarSesion()]] [[.../analisis/.../README.md A]]

# En diseño-fastapi-react: con [D] apuntando a su rama
NoAuth -[#green,thickness=2]-> Menu: [[.../main/.../detalle/iniciarSesion/README.md iniciarSesion()]] [[.../main/.../analisis/.../README.md A]] [[.../diseño-fastapi-react/.../diseño/.../README.md D]]

# En diseño-spring-angular: con [D] apuntando a su rama
NoAuth -[#green,thickness=2]-> Menu: [[.../main/.../detalle/iniciarSesion/README.md iniciarSesion()]] [[.../main/.../analisis/.../README.md A]] [[.../diseño-spring-angular/.../diseño/.../README.md D]]
```

**Ventajas de esta arquitectura:**
- ✅ Cero duplicación de artefactos de análisis
- ✅ Cero propagación de cambios entre ramas
- ✅ Navegación coherente dentro de cada stack
- ✅ Switching fácil entre tecnologías vía leyenda del dashboard

## Evolución del concepto de dashboard

### Dashboard simple (Artículo 004)

**Características originales:**
- Un solo dashboard en `/main/`
- Progreso lineal: Identificado → Análisis → Diseño → ...
- Sin consideración de múltiples implementaciones

### Dashboard multi-stack (Este artículo)

**Nuevas características:**
- **Tres dashboards independientes:**
  - Main: Base tecnológicamente neutra (análisis completo)
  - FastAPI/React: Vista del progreso en este stack
  - Spring/Angular: Vista del progreso en este stack

- **Navegación entre dashboards:**
  - Leyenda en main: Enlaces a ambos dashboards de diseño
  - Leyenda en cada diseño: Enlace a stack alternativo + indicación de stack actual

- **Color coding diferencial:**
  - Main: Todo en 🟫 Amarillo oscuro (Analizado)
  - Diseños: 🟢 Verde (Diseñado) + 🟫 Amarillo oscuro (Pendiente)

**Complejidad adicional manejada:**
- Coherencia de enlaces entre ramas
- Switching entre contextos tecnológicos
- Representación visual de progreso paralelo

## Timeline del experimento

**Fase 1: Análisis (Completada)**
- Duración: Varios meses
- Resultado: 32 casos de uso completamente analizados
- Artefacto clave: Dashboard main con todo en amarillo oscuro

**Fase 2: Diseño paralelo (En curso)**
- Inicio: Creación de ramas `diseño-fastapi-react` y `diseño-spring-angular`
- Primera validación: 5 casos de uso (vertical slice de aulas)
- Resultado: Dashboards de diseño con casos en verde
- Estado actual: Validación exitosa, expansión pendiente

**Fase 3: Expansión (Próxima)**
- Objetivo: Diseñar más casos de uso en ambos stacks
- Prioridad: `generarHorario()` - algoritmo complejo
- Meta: Validar independencia con lógica de negocio sofisticada

## Conexión con el proyecto pySigHor

### Algoritmo original (1998)

**SigHor original:**
- Desarrollado en Visual Basic 3.0
- Implementa algoritmo sofisticado de investigación de operaciones
- 4 fases de optimización de horarios
- Representa excelencia técnica de su época

### Modernización metodológica (2024-2025)

**Estrategia de dos fases:**
1. **Réplica fiel:** Port directo a tecnología moderna
2. **Reingeniería:** Mejoras considerando factores humanos

**Experimento multi-stack valida:**
- Que el análisis del algoritmo es tecnológicamente neutro
- Que la complejidad del dominio (horarios) puede diseñarse en múltiples stacks
- Que RUP escala desde algoritmos legacy hasta arquitecturas modernas

## Valor didáctico del experimento

### Para estudiantes

**Aprendizajes concretos:**
- Ven metodología RUP aplicada rigurosamente en proyecto real
- Comprenden la separación entre análisis y diseño
- Experimentan el valor de la independencia tecnológica
- Observan evolución de dashboards como herramienta de gestión

### Para profesionales

**Aplicabilidad práctica:**
- Técnica replicable en proyectos de modernización
- Estrategia probada para validación de metodologías
- Arquitectura de navegación multi-stack reutilizable
- Sistema de dashboards visuales adaptable a otros contextos

### Para la comunidad RUP

**Contribución metodológica:**
- Primera validación experimental documentada de independencia tecnológica
- Evidencia de que RUP es viable en desarrollo moderno
- Innovación en herramientas de gestión usando artefactos RUP nativos
- Demostración de adaptabilidad metodológica

## Próximos hitos

**Validación técnica:**
- Diseñar `generarHorario()` en ambos stacks
- Medir resistencia de análisis ante algoritmos complejos
- Documentar ajustes necesarios (esperados: mínimos o cero)

**Validación de escalabilidad:**
- Expandir a 10+ casos de uso por stack
- Evaluar velocidad de diseño comparativa
- Medir consistencia arquitectónica

**Expansión de stacks:**
- Considerar tercera rama: Electron/Tauri (desktop)
- Evaluar React Native/Flutter (mobile)
- Explorar port directo desde VB original

---

## Referencias

- [Artículo 003: Análisis independiente de tecnología](/extraDocs/003-rup-independencia-tecnologica/)
- [Artículo 004: Dashboard visual RUP](/extraDocs/004-dashboard-visual-rup-casos-uso/)
- [Conversation Log: Registro completo del proyecto](/conversation-log.md)
