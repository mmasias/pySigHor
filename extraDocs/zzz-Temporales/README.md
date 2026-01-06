# Análisis del dashboard propuesto

Este documento analiza la propuesta del dashboard implementado en el proyecto, contrastándolo con herramientas existentes y definiendo su valor.

## ¿Por qué?

La gestión de proyectos guiados por RUP tradicionalmente adolece de dos problemas opuestos:

1. **Opacidad**: Es difícil saber el estado real de avance en una estructura compleja de casos de uso interdependientes.
1. **Sobrecarga**: Las herramientas clásicas (como la antigua Rational Suite) eran pesadas, caras y separaban la gestión de la arquitectura.

Las herramientas ágiles modernas (Jira, Trello, Kanban) son **lineales**: tratan el desarrollo como una lista de tareas (To Do -> Doing -> Done), perdiendo la perspectiva **topológica** (cómo afecta el avance de una pieza al sistema completo).

## ¿Qué?

El Dashboard Visual es una implementación de ***"Diagramas vivientes"*** orientada a la gestión del proceso, no solo a la documentación de la estructura.

Es un "hack" metodológico que consiste en reutilizar un artefacto de análisis estándar (el **Diagrama de contexto de casos de uso**) y superponerle una capa de metadatos de gestión mediante un código de colores semántico. Transforma un mapa estático de "qué hace el sistema" en un mapa dinámico de "cómo va la construcción del sistema".

### Diferencia con C4 Model (PlantUML)

<div align=center>

|Característica|Dashboard|C4 Model / Structurizr|
|-|-|-|
|**Propósito**|Gestión de proceso (Dinámico)|Documentación de estructura (Estático)|
|**Pregunta clave**|¿Cómo vamos?|¿Qué es esto?|
|**Enfoque**|Minimalista / Topológico|Formal / Descriptivo|

</div>

## ¿Para qué?

|||
|-|-|
Visibilidad topológica|Permite ver el estado del proyecto proyectado sobre la propia arquitectura, identificando qué áreas funcionales están maduras y cuáles verdes.
Economía de herramientas|Elimina la necesidad de software de gestión externo. El diagrama *es* el reporte de estado.
Trazabilidad histórica|Al estar versionado en Git, el historial del archivo genera automáticamente una "película" de la evolución del proyecto sin esfuerzo adicional.
Valor didáctico|Enseña a visualizar el software como un todo orgánico en evolución, en lugar de tickets aislados en un backlog.

## ¿Cómo?

La implementación se basa en la **Ley del Mínimo Esfuerzo Tecnológico**:

1. **Artefacto base**: Se utiliza el archivo fuente PlantUML (`.puml`) del diagrama de contexto de casos de uso.
2. **Semántica de color**: Se define una leyenda estandarizada que vincula colores a fases RUP (ver `extraDocs/004-dashboard-visual-rup-casos-uso/`).
   - 🔘 Gris: Identificado
   - 🟫 Amarillo: Análisis
   - 🟢 Verde: Diseño
   - 🔵 Azul: Implementación
3. **Actualización continua**: Cuando un ingeniero avanza en un caso de uso, edita el color en el archivo `.puml` como parte de su trabajo técnico.
4. **Renderizado automático**: El sistema de control de versiones o el IDE renderiza el nuevo estado visualmente.

### Ejemplo de evolución: de análisis a diseño

El siguiente ejemplo ilustra cómo el dashboard refleja el progreso del proyecto al comparar el estado en la rama principal (`main`) frente a una rama de trabajo específica (por ejemplo, `diseño-cli-python-http`).

|Estado A: Rama `main` (Hito de Análisis Completado)|Estado B: Rama `diseño-cli-python-http` (Trabajo en Curso)|
|-|-|
![](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|![](https://raw.githubusercontent.com/mmasias/pySigHor/dise%C3%B1o-cli-python-http/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)
<sub>Todos los casos de uso han superado la fase de análisis. El color predominante es el amarillo/marrón.|<sub>Al comenzar el diseño técnico de un subconjunto de casos de uso, estos cambian a verde. El dashboard muestra instantáneamente qué partes del sistema están evolucionando tecnológicamente mientras el resto permanece en estado de análisis.

Esta técnica convierte la actualización del estado del proyecto en una operación de código (`git commit`), integrando perfectamente la gestión en el flujo de trabajo del desarrollador.