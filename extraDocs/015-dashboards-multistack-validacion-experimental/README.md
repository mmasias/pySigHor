# Dashboards multi-stack y validación experimental: RUP con FastAPI/React y Spring/Angular

<div align=right>

||||||
|-|-|-|-|-|
|[🏠️](../README.md)|**Artículo**|[Contexto](contexto.md)|[Evidencia](evidencia.md)|[Comparativa](comparativa-stacks.md)|

</div>

## Resumen ejecutivo

Este artículo documenta la materialización del experimento de independencia tecnológica propuesto en el [artículo 003](/extraDocs/003-rup-independencia-tecnologica/) y la evolución del sistema de dashboards visuales del [artículo 004](/extraDocs/004-dashboard-visual-rup-casos-uso/). Se presenta la primera validación práctica de la promesa fundamental de RUP: que un análisis riguroso puede soportar múltiples implementaciones tecnológicas sin modificaciones.

**Resultado experimental:** El mismo conjunto de casos de uso analizados ha sido diseñado exitosamente en dos stacks tecnológicos diferentes (FastAPI/React y Spring/Angular), manteniendo intactos todos los artefactos de análisis.

## Del experimento teórico a la práctica

### La hipótesis original (Artículo 003)

> "Un análisis RUP completo y riguroso puede soportar múltiples implementaciones tecnológicas sin modificaciones sustanciales a los artefactos de análisis"

Hace varios meses se tomó la decisión estratégica de completar todo el análisis RUP antes de abordar cualquier tecnología específica. Esta decisión representaba una apuesta consciente por validar si RUP cumple su promesa de independencia tecnológica.

### El momento de la verdad

Después de completar 32 casos de uso con análisis MVC completo, llegó el momento de poner a prueba la hipótesis. La estrategia: implementar el mismo subconjunto de casos de uso (aulas/classrooms) en dos stacks tecnológicos radicalmente diferentes.

**Casos de uso del experimento:**
- `iniciarSesion()` - Autenticación de usuarios
- `abrirAulas()` - Apertura de gestión de aulas
- `crearAula()` - Creación de aulas
- `editarAula()` - Edición de aulas
- `eliminarAula()` - Eliminación de aulas

## Innovación en dashboards multi-stack

### Evolución del concepto (Artículo 004)

El [artículo 004](/extraDocs/004-dashboard-visual-rup-casos-uso/) introdujo la innovación de usar el diagrama de contexto como dashboard visual mediante codificación por colores:

- 🔘 Gris punteado: Identificado (no iniciado)
- 🔴 Rojo: Detalle/Prototipado
- 🟫 Amarillo oscuro: Análisis
- 🟢 Verde: Diseño
- 🔵 Celeste: Desarrollo
- 🔵 Azul: Pruebas
- ⚫ Negro continuo: Completado

### Desafío arquitectónico: navegación multi-stack

La implementación paralela en múltiples tecnologías presentó un nuevo desafío: **¿cómo permitir navegación coherente entre artefactos de análisis compartidos y diseños específicos de cada stack?**

#### Problema de propagación

**Enfoque con posible complicación:** Duplicar artefactos de análisis en cada rama tecnológica

- Resultado: Cualquier cambio requiere actualizar 3 ramas (main + 2 diseños)
- Consecuencia: Violación del principio DRY (Don't Repeat Yourself)
- Riesgo: Divergencia entre versiones

#### Solución: punto central con enlaces contextuales

**Estrategia de navegación implementada:**

1. **Detalle y Análisis:** SIEMPRE apuntan a `/main/` (punto central)
2. **Diseño:** Enlaces `[D]` apuntan a rama específica del stack tecnológico
3. **Dashboard:** Cada stack tiene su propia vista con navegación a stack alternativo

**Ventajas:**

- Punto central para artefactos de análisis
- Cero propagación de cambios entre ramas
- Navegación coherente dentro de cada stack
- Cambio fácil entre tecnologías

## Validación experimental

### Stacks tecnológicos seleccionados

**Stack 1: FastAPI/React**

- Backend: FastAPI (Python)
- Frontend: React + TypeScript
- Paradigma: API REST + SPA moderna
- Rama: `diseño-fastapi-react`

**Stack 2: Spring/Angular**

- Backend: Spring Boot (Java)
- Frontend: Angular + TypeScript
- Paradigma: Enterprise + Framework full-featured
- Rama: `diseño-spring-angular`

**Razón de la selección:** Representan dos filosofías distintas (Python vs Java, React vs Angular) maximizando la validación de independencia tecnológica.

### Metodología de validación

**Proceso aplicado:**

1. Tomar casos de uso completamente analizados de `/main/`
2. Crear diseño específico en rama `diseño-fastapi-react`
3. Crear diseño específico en rama `diseño-spring-angular`
4. Verificar que análisis permanece inalterado
5. Documentar diferencias y similitudes

**Métricas de validación:**

- Porcentaje de artefactos de análisis sin modificación: **100%**
- Número de casos de uso diseñados en ambos stacks: **5**
- Consistencia arquitectónica entre implementaciones: **Alta**

## Evidencia técnica: tres dashboards coherentes

<div align=center>

|Spring/Angular|Main (Análisis)|FastAPI/React|
|:-:|:-:|:-:|
|![Dashboard Spring/Angular](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|![Dashboard Main](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|![Dashboard FastAPI/React](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|[Ver dashboard Spring/Angular](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Ver dashboard Main](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Ver dashboard FastAPI/React](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|
|Casos en verde: diseñados|Casos en amarillo oscuro: analizados|Casos en verde: diseñados|

</div>

### Interpretación visual

**Dashboard Main (centro):**

- Todos los casos de uso en **amarillo oscuro** (🟫 Analizado)
- Sin enlaces `[D]` (diseño disponible en ramas específicas)
- Leyenda incluye enlaces a ambos dashboards de diseño
- Representa la **base tecnológicamente neutra**

**Dashboards de diseño (laterales):**

- 5 casos de uso en **verde** (🟢 Diseñado): `iniciarSesion()`, `abrirAulas()`, `crearAula()`, `editarAula()`, `eliminarAula()`
- Resto de casos en **amarillo oscuro** (🟫 Analizado): pendientes de diseño
- Enlaces `[D]` apuntan a diseño específico del stack
- Leyenda incluye enlace al stack alternativo
- Cada uno representa una **materialización tecnológica específica**

## Lecciones aprendidas

### Lo que funcionó perfectamente

**1. Independencia de análisis MVC**

- Las clases de análisis (boundary, control, entity) mapearon directamente a componentes de diseño
- Ningún diagrama de colaboración MVC requirió modificación
- Las responsabilidades identificadas en análisis se mantuvieron en ambos stacks

**2. Reutilización de especificaciones**

- Todas las especificaciones detalladas permanecieron válidas
- Los diagramas de estado se aplicaron sin cambios a ambas implementaciones
- Los wireframes SALT sirvieron como base para ambos frontends

**3. Arquitectura de navegación**

- La estrategia de "punto central" eliminó duplicación
- El switching entre stacks resultó intuitivo y coherente
- Cero conflictos de merge entre ramas

### Matices y refinamientos descubiertos

**1. Nomenclatura de stacks**

- Decisión: Usar "FastAPI/React" y "Spring/Angular" en lugar de acrónimos
- Razón: TypeScript es estándar en 2025, no necesita mención explícita
- Aprendizaje: La claridad supera la brevedad en navegación

**2. Placement de enlaces de switching**

- Iteración inicial: Footer con texto largo "Stack tecnológico: X | Cambiar a Y"
- Refinamiento: Leyenda con líneas separadas para stack actual y enlace a alternativo
- Resultado: Más limpio y coherente con el diseño del dashboard

**3. Granularidad de validación**

- Decisión: Validar con vertical slice (módulo completo de aulas)
- Razón: Cubre CRUD completo + autenticación + navegación
- Aprendizaje: 5 casos de uso fueron suficientes para validación sin ser excesivos

## Próximos pasos

### Expansión del experimento

**Fase siguiente:** Diseñar casos de uso adicionales en ambos stacks

- Prioridad: `generarHorario()` - el caso más complejo algorítmicamente
- Objetivo: Validar que la independencia tecnológica se mantiene con lógica de negocio compleja

**Métricas a seguir:**

- Número de casos diseñados en cada stack
- Tiempo de diseño comparativo (FastAPI/React vs Spring/Angular)
- Número de ajustes al análisis (esperado: cero)

### Potencial para más stacks

**Candidatos adicionales:**

- Desktop: Electron/Tauri (validación de mismo backend, diferentes frontends)
- Mobile: React Native/Flutter (validación de adaptación a restricciones móviles)
- Legacy port: Java/VB.NET (validación de port directo desde código original)

### Integración con desarrollo

**Siguiente hito:** Transición de Diseño a Implementación

- Crear ramas de desarrollo desde ramas de diseño
- Mantener coherencia de navegación en fase de implementación
- Evolucionar dashboard para incluir estados de Desarrollo y Pruebas

## Impacto metodológico

### Para RUP como metodología

**Validación empírica:**

- Primera demostración práctica documentada de independencia tecnológica de RUP
- Evidencia verificable mediante commits de Git
- Medición cuantitativa: 100% de artefactos de análisis sin modificación

**Refinamiento de expectativas:**

- RUP cumple su promesa cuando el análisis MVC es riguroso
- La separación disciplinaria (Requisitos → Análisis → Diseño) es clave
- La calidad del análisis determina la facilidad del diseño multi-stack

### Para el proyecto pySigHor

**Logro metodológico:**

- Demostración de que algoritmo de 1998 puede modernizarse con múltiples tecnologías
- Base sólida para comparación de paradigmas tecnológicos
- Material didáctico excepcional de aplicación práctica de RUP

**Valor académico:**

- Caso de estudio real de metodología aplicada
- Trazabilidad completa desde análisis hasta diseño en dos tecnologías
- Proceso replicable para otros proyectos de modernización

### Para estudiantes y profesionales

**Lecciones transferibles:**

1. **El análisis riguroso es inversión, no gasto:** Las horas dedicadas a análisis MVC se multiplican en velocidad de diseño
2. **La independencia tecnológica requiere disciplina:** No mezclar decisiones de implementación en fase de análisis
3. **La arquitectura de navegación importa:** Diseñar para múltiples contextos desde el inicio evita refactoring posterior
4. **Los dashboards visuales funcionan:** El diagrama de contexto como herramienta de gestión demostró su valor práctico

## Conclusión

Este artículo documenta más que una implementación técnica: representa la **validación experimental de una promesa metodológica fundamental**.

**Lo que se ha demostrado:**

- RUP cumple su promesa de independencia tecnológica con análisis riguroso
- Un mismo conjunto de artefactos de análisis puede soportar múltiples diseños tecnológicos
- La innovación de dashboards visuales escala a contextos multi-stack
- La arquitectura de navegación basada en punto central elimina duplicación

**Lo que esto significa:**

- Las metodologías formales **sí importan** cuando se aplican con rigor
- RUP es **viable y práctico** en contextos modernos de desarrollo
- La separación de responsabilidades entre disciplinas **tiene valor real medible**
- Las decisiones arquitectónicas tempranas **se validan con el tiempo**

**El siguiente capítulo:**

Con la validación exitosa del experimento, el proyecto pySigHor entra en una nueva fase: la expansión del diseño multi-stack hacia casos de uso más complejos, especialmente `generarHorario()`, que pondrá a prueba si la independencia tecnológica se mantiene ante algoritmos sofisticados de investigación de operaciones.

## Referencias

- [Artículo 003: Análisis independiente de tecnología](/extraDocs/003-rup-independencia-tecnologica/)
- [Artículo 004: Dashboard visual RUP](/extraDocs/004-dashboard-visual-rup-casos-uso/)
- [Dashboard Main](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)
- [Dashboard FastAPI/React](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)
- [Dashboard Spring/Angular](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-spring-angular/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)
