# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) cuando trabaja con código en este repositorio.

## IMPORTANTE: Inicio de Sesión

**Antes que nada, identifica en qué rol arrancas.** Este repositorio tiene dos narrativas independientes de "Conversación N", en ramas distintas, sobre temas que no tienen relación entre sí:

- **pySigHor construyendo su propio port RUP/FastAPI+React** (rol nativo del repo): ramas `main`/`diseño-fastapi-react`. Sigue el protocolo de abajo tal cual, con `conversation-log.md` de la rama en la que estés.
- **pySigHor oficiando de orquestador/revisor de los proyectos hermanos pyCelda y pySesion** (rol de "consultor"): **cambia primero a la rama `leConsultor`** (`git checkout leConsultor` -- parte de `main`, así que hereda los artículos completos de `extraDocs/`) antes de seguir. Ahí el historial real es `conversation-log-orquestacion.md`, no `conversation-log.md` (que en `leConsultor` sigue siendo el heredado de `main`, de la otra narrativa -- no lo confundas). Detalle completo del onboarding de ese rol en `~/misRepos/_ASIGNATURAS/mmasias_private/AGENTES/inputAgenteGestor.md`.

Si no sabes cuál de los dos toca, pregúntale a Manuel antes de asumirlo -- son dos historias sin relación temática, mezclarlas fue precisamente el problema que motivó separar `leConsultor` el 2026-08-30.

**SIEMPRE que inicies una nueva sesión de trabajo en este repositorio, DEBES leer los siguientes archivos para obtener el contexto completo (ajustando el nombre del log al de la rama en la que estés, según lo de arriba):**

1. **`conversation-log.md`** (o `conversation-log-orquestacion.md` en `leConsultor`) - Historial completo de conversaciones, decisiones tomadas, y estado actual del proyecto
2. **`extraDocs/999-leyes-proyecto/`** - Reglas discretas y principios específicos que deben seguirse durante el desarrollo

Estos archivos contienen la trazabilidad completa del proyecto RUP y las reglas establecidas, siendo esenciales para mantener continuidad y coherencia entre sesiones.

## PROTOCOLO DE GESTIÓN DE CONTEXTO

### Regla de Estado Actual
**La última conversación numerada en `conversation-log.md` marca SIEMPRE el estado actual del proyecto.**

### Obligaciones de Claude
- **Inicio de sesión**: Leer `conversation-log.md` + `extraDocs/999-leyes-proyecto/`
- **Identificar estado**: Localizar la última conversación numerada para el contexto actual
- **Exigir protocolo**: Si el Usuario no cumple sus obligaciones, EXIGIR su cumplimiento

### Obligaciones del Usuario
- **Fin de sesión**: SIEMPRE avisar cuando termine la sesión
- **Actualización obligatoria**: Permitir que Claude actualice `conversation-log.md` al terminar
- **Incumplimiento**: Si no avisa el fin de sesión, Claude DEBE exigirlo

### Protocolo de Cierre
1. **Usuario declara**: "Terminamos por hoy" / "Fin de sesión"
2. **Claude actualiza**: Crea nueva conversación numerada en `conversation-log.md`
3. **Estado preservado**: Próxima sesión inicia con contexto exacto

## LEY 004: Rama de Revisión Obligatoria

**TODO trabajo producto de la iteración Manuel-Claude DEBE ir primero a la rama `xRevisar` antes de incorporarse a `main`.**

### Flujo Obligatorio para Claude
1. **Proponer artefactos**: "Artefactos listos, necesito que generes los SVG"
2. **Esperar SVG**: Manuel convierte archivos .puml a imágenes .svg
3. **Rama xRevisar**: SIEMPRE `git checkout -b xRevisar` o `git checkout xRevisar` 
4. **Push completo**: `git add [archivos + SVG]` → `git commit` → `git push -u origin xRevisar`
5. **Comunicar**: "Trabajo completado en rama xRevisar, listo para revisión"
6. **Esperar OK**: NO proceder sin aprobación explícita de Manuel
7. **Pull Request**: Solo después de recibir "OK para PR" de Manuel

### Casos que REQUIEREN xRevisar
- ✅ Nuevos casos de uso RUP, modificaciones a especificaciones
- ✅ Documentación técnica nueva, cambios en estructura del proyecto  
- ✅ Implementación de nuevas funcionalidades

### Casos que NO requieren xRevisar
- ❌ Correcciones menores de typos, ajustes de formato
- ❌ Actualizaciones del conversation-log.md, cambios cosméticos

**Referencia completa**: `/extraDocs/999-leyes-proyecto/ley-rama-revision.md`

## IMPORTANTE: Idioma Vehicular del Proyecto

**ESPAÑOL como idioma obligatorio en TODO el proyecto:**

- **Documentación**: Todos los archivos .md, comentarios y especificaciones en español
- **Commits**: Mensajes de commit obligatoriamente en español
- **Código**: Comentarios, nombres de variables y funciones en español cuando sea posible
- **Comunicación**: Toda interacción con Claude Code debe ser en español
- **Artefactos RUP**: Diagramas, especificaciones y análisis en español

**Excepción**: Código fuente legacy original (Visual Basic 3.0) se mantiene tal como está para preservar integridad histórica.

## Resumen del Proyecto

**pySigHor** es un proyecto de arqueología de software histórico centrado en el análisis y documentación de SigHor (Sistema Generador de Horarios), un sistema de programación de horarios universitarios desarrollado en Visual Basic 3.0 en 1998 para la Universidad de Piura. El proyecto demuestra algoritmos avanzados de investigación de operaciones aplicados a problemas de programación de horarios académicos.

## Estructura del Repositorio

```text
pySigHor/
├── src/                    # Código fuente original de Visual Basic 3.0
│   ├── Horario.bas        # Implementación del algoritmo principal de horarios
│   ├── MODULO.BAS         # Utilidades globales y configuración
│   ├── *.FRM              # Formularios de interfaz de usuario
│   ├── DATOS/             # Archivos de base de datos Microsoft Access
│   └── Reporte/           # Archivos de Crystal Reports
├── RUP/                   # Estructura del proyecto RUP
│   ├── 00-casos-uso/      # Casos de uso (requisitos)
│   │   ├── 00-modelo-del-dominio/
│   │   ├── 01-actores-casos-uso/
│   │   └── 02-detalle/
│   ├── 01-analisis/       # Análisis y diseño
│   │   └── casos-uso/
│   └── 99-seguimiento/    # Dashboard y seguimiento
├── images/                # Capturas de pantalla y assets de documentación
│   ├── RUP/              # Imágenes generadas de diagramas RUP
│   └── extraDocs/        # Imágenes de documentación adicional
├── extraDocs/             # Documentación adicional y análisis
│   ├── 000-ingenieria-inversa/
│   ├── 001-saltarse-pasos-desarrollo/
│   ├── 002-coherencia-estructural-readme/
│   ├── 003-rup-independencia-tecnologica/
│   ├── 004-dashboard-visual-rup-casos-uso/
│   ├── 005-etiquetado-etico-colaboracion-humano-ia/
│   ├── 006-reflexion-alcance-casos-uso-colaboracion/
│   ├── 007-diagramas-contexto-multiples-tecnologias/
│   └── 999-leyes-proyecto/
├── extraFiles/            # Archivos de licencias y configuración legacy
├── drafts-temp/          # Borradores y archivos temporales
├── conversation-log.md   # Registro completo de conversaciones del proyecto
├── *.md                  # Archivos de documentación y análisis
└── README.md             # Resumen del proyecto
```

## Componentes Clave

### Archivos del Algoritmo Principal

- **`src/Horario.bas`** - Algoritmo principal de horarios con proceso de optimización de 4 fases
- **`src/MODULO.BAS`** - Variables globales, configuración de base de datos y funciones utilitarias
- **`src/frmMenuP.frm`** - Interfaz principal de generación de horarios

### Estructura de Base de Datos

- **Base de Datos Principal**: `src/DATOS/HOR_UDEP.MDB` (Microsoft Access)
- **Tablas Clave**: M_Aulas (aulas), M_Cursos (cursos), M_Profesores (profesores), M_Horario (horario final)

### Documentación

- **`reverseEngineering.md`** - Documentación técnica completa del sistema
- **`reflexiones.md`** - Análisis de resultados del algoritmo y factores humanos
- **`reflexionesAlgoritmo.md`** - Análisis detallado del algoritmo y lecciones aprendidas

## Arquitectura del Algoritmo de Horarios

El sistema implementa un proceso de optimización de 4 fases:

1. **PrepararH()** - Resolución de conflictos y preparación de ubicación de cursos
2. **GeneraPreHorario()** - Optimización dual (minimización de espacio + coincidencia de recursos)
3. **GeneraHorario()** - Materialización del horario final
4. **IngresoHE()/IngresoHV()** - Manejo de casos especiales

### Técnicas Clave de Optimización

- **Minimización Z**: Minimiza la capacidad no utilizada del aula
- **Puntuación binaria ponderada**: Coincide las preferencias del profesor con los recursos del aula
- **Resolución de conflictos**: Maneja conflictos de horarios mediante reasignación sistemática de cursos

## Tareas Comunes

### Análisis del Algoritmo

```bash
# Ver la lógica principal de horarios
cat src/Horario.bas

# Examinar documentación de estructura de base de datos
cat reverseEngineering.md

# Revisar análisis del algoritmo
cat reflexionesAlgoritmo.md
```

### Trabajo con Documentación

- Todos los archivos de análisis están en formato Markdown
- Diagramas UML están en formato PlantUML en `modelosUML/`
- Capturas de pantalla y documentación visual en `images/`

### Comprensión del Modelo de Datos

El sistema utiliza una base de datos Access con tres tipos principales de entidades:

- **Tablas maestras (M_*)**: Entidades principales (aulas, cursos, profesores)
- **Tablas secundarias (S_*)**: Datos de apoyo (edificios, recursos)
- **Tablas temporales (T_*)**: Datos de trabajo del algoritmo
- **Tablas de relación (R_*)**: Relaciones muchos a muchos

## Notas Importantes

### Contexto Histórico

- Desarrollado en 1998 usando Visual Basic 3.0
- Representa aplicación avanzada de investigación de operaciones para su época
- Demuestra tanto excelencia técnica como limitaciones prácticas

### Percepciones del Algoritmo

- El sistema produce soluciones matemáticamente óptimas que pueden ser impracticables para uso humano
- Concentra clases en horas tempranas de la mañana y primeros días de la semana
- Demuestra la importancia de equilibrar optimización matemática con factores humanos

### Codificación de Archivos

- Los archivos originales de Visual Basic usan codificación Windows-1252
- Algunos archivos pueden contener caracteres de control legacy o formateo

## Entorno de Desarrollo

Este es un proyecto de investigación y documentación. El código original de Visual Basic se conserva para análisis histórico pero no está destinado para desarrollo activo. Cualquier esfuerzo de modernización debe enfocarse en:

1. Análisis y documentación del algoritmo
2. Reconstrucción del modelo de datos
3. Estudios de implementación moderna
4. Desarrollo de material educativo

## Especificaciones Técnicas

- **Plataforma Original**: Windows 95/98, Visual Basic 3.0
- **Base de Datos**: Microsoft Access (Motor Jet)
- **Arquitectura**: Aplicación de escritorio de una sola capa
- **Componentes de Terceros**: Crystal Reports, controles 3D, grillas de datos

El sistema representa una aplicación sofisticada de técnicas de satisfacción de restricciones y optimización para resolver el complejo problema de programación de horarios universitarios dentro de las limitaciones tecnológicas de finales de los años 1990.

## Proyecto de Modernización con RUP

### Objetivo del Proyecto

Este repositorio ahora incluye un proyecto de modernización del sistema SigHor utilizando la metodología RUP (Rational Unified Process) como herramienta didáctica y práctica profesional.

### Estrategia de Modernización

**Enfoque de Dos Fases:**
1. **Fase 1: Réplica Fiel** - Port directo del sistema legacy a tecnología moderna
2. **Fase 2: Reingeniería** - Mejoras sobre la base modernizada (considerando factores humanos)

### Metodología RUP

**Fases del Proyecto:**
- **Inicio (Inception)** - Análisis del sistema legacy, visión del proyecto
- **Elaboración (Elaboration)** - Arquitectura, requisitos detallados, casos de uso
- **Construcción (Construction)** - Desarrollo iterativo e incremental
- **Transición (Transition)** - Despliegue, documentación, mantenimiento

**Disciplinas Cubiertas:**
- Modelado de Negocio
- Requisitos
- Análisis y Diseño
- Implementación
- Pruebas
- Despliegue
- Gestión de Configuración
- Gestión de Proyectos
- Entorno

### Estructura del Proyecto RUP

```text
pySigHor-RUP/
├── 00-Legacy-Analysis/          # Análisis del sistema original
├── 01-Inception/                # Fase de Inicio
├── 02-Elaboration/              # Fase de Elaboración
├── 03-Construction/             # Fase de Construcción
├── 04-Transition/               # Fase de Transición
└── artifacts/                   # Artefactos transversales
```

### Herramientas y Formatos

- **Diagramas UML**: PlantUML (texto plano, versionable)
- **Documentación**: Markdown
- **Selección Tecnológica**: Se definirá en la fase de Elaboración (Architecture-driven)

### Registro de Conversaciones

El archivo `conversation-log.md` mantiene un registro detallado de todas las decisiones, discusiones y evolución del proyecto para propósitos didácticos y de trazabilidad.

### Valor Didáctico

Este proyecto sirve como:
- **Caso de estudio** de aplicación completa de RUP
- **Ejemplo práctico** de modernización de sistemas legacy
- **Referencia** de ingeniería de software aplicada
- **Plantilla** para proyectos similares