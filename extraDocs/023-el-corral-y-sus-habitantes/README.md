<div align=right>

|||
|-|-|
|[🏠️](../README.md)|**Artículo**|

</div>

# El corral y sus habitantes: crónica de una orquestación multi-agente

## ¿Por qué?

En un entorno habitual de trabajo con LLMs, acumulas herramientas. Claude Code para orquestar, Gemini CLI para análisis rápido, OpenCode para generación de código, Ollama para inferencia local. Cada uno con sus puntos fuertes, sus modelos y sus costes. El problema es que operan en silos: no hay forma nativa de que uno invoque a otro.

El segundo problema es menos obvio: el coste de razonamiento no es uniforme. Usar el modelo más capaz para todo — incluidas las tareas mecánicas y volumétricas — es como usar a un arquitecto para pintar paredes. Mantener a Claude concentrado en coordinación y criterio de calidad mientras las tareas de generación simple se delegan a modelos más rápidos y baratos es una decisión de diseño que afecta tanto al coste como al resultado final.

CORRAL resuelve el primer problema exponiendo cada CLI externo como herramienta MCP. Claude Code llama a `gemini_run` o `opencode_run` igual que llama a `bash`. Hoy añadimos un tercer nodo: Ollama local, sin coste de API, sin dependencia de red. Lo que no sabíamos antes de empezar era cómo se comportaría ese nodo en producción real. Eso es lo que cuenta este artículo.

## ¿Qué?

Un experimento real sobre un proyecto real. No un tutorial construido para demostrar una tesis — una jornada de trabajo documentada con sus aciertos, sus fallos y sus sorpresas.

El escenario: CORRAL con tres nodos activos simultáneamente — Gemini, OpenCode y Ollama — orquestados por Claude Code. Dos proyectos como banco de pruebas: pyQuejica (un patcher de bundles JavaScript) para evaluar calidad analítica del nodo local, y pySigHor (un sistema de gestión de horarios universitarios con liturgia RUP completa) para evaluar generación de artefactos en producción.

El material empírico: 19 casos de uso diseñados en una sesión, 24 artefactos RUP generados, 3 agentes con roles distintos, errores documentados, correcciones aplicadas, y una regla de orquestación nueva que emergió del proceso y quedó escrita en el CLAUDE.md del proyecto. Lo que no estaba planificado: que el orquestador recayera en un anti-patrón, lo reconociera, lo corrigiera, y lo documentara con sus propias palabras.

## ¿Para qué?

**Para entender qué es realmente un agente.**

La confusión más común es pensar que el LLM "hace cosas". No hace nada — predice texto. Lo que hace cosas es el runtime que lo rodea: el código que interpreta esa predicción como instrucción y la ejecuta en el mundo real. Claude Code escribe ficheros no porque el modelo tenga acceso al filesystem, sino porque su runtime lo tiene. Ollama sin runtime es inferencia pura — devuelve texto. Gemini CLI con runtime es un agente — escribe ficheros, ejecuta comandos, navega directorios.

Esta distinción no es académica. Cambia cómo diseñas la arquitectura, cómo asignas tareas y cómo evalúas resultados.

**Para validar el patrón de delegación por complejidad.**

No todos los modelos son iguales para todas las tareas, y no todas las tareas justifican el mismo coste de razonamiento. Lo que aprendimos hoy con datos reales:

| Tipo de tarea | Nodo | Por qué |
|---|---|---|
| CRUD templado | Ollama | Sustitución estructural, sin razonamiento semántico |
| Navegación / hub | Gemini | Flujos cortos, decisiones acotadas |
| Lógica relacional compleja | Gemini | Razonamiento sobre dominio, múltiples entidades |
| Coordinación y criterio | Claude Code | Visión de conjunto, consistencia entre artefactos |

**Para documentar el anti-patrón simétrico.**

Hay dos errores opuestos en orquestación: no delegar nunca, y delegar por delegar. El orquestador que ejecuta en bucle lo que un subordinado podría hacer está optimizando su comodidad, no el sistema. El criterio correcto no es complejidad sola — es complejidad más volumen mecánico, más un tercer eje: si el LLM aporta algo sobre la alternativa determinista. Generar SVGs desde `.puml` no se delega a un LLM — `plantuml` devuelve 0 o un error. No hay valor que un modelo añada sobre una herramienta determinista.

## ¿Cómo?

La jornada tuvo cuatro momentos con lecciones distintas.

**Momento 1: El nodo que no sabías que tenías**

Ollama estaba instalado desde hacía un mes. El modelo descargado. El servicio caído. Bastó `sudo systemctl enable --now ollama` para tener un tercer nodo en CORRAL sin instalar nada nuevo.

La primera prueba fue analítica: pasar el código de pyQuejica a Qwen2.5 14B y pedirle una valoración técnica estructurada. El resultado fue correcto en estructura, identificó los riesgos reales, pero falló donde fallan los modelos pequeños: las mejoras concretas eran genéricas sin especificar cómo. Y confundió `str.replace` con regex — error técnico menor pero real.

Conclusión operativa: competente para tareas de resumen y estructura. Para análisis técnico profundo, produce generalidades. Útil como primer borrador o primer pase de revisión.

**Momento 2: El bake-off de pySigHor**

19 casos de uso pendientes de diseño en un proyecto RUP real. La estrategia emergió antes de ejecutar: clasificar por complejidad, asignar por tipo, validar con una entidad antes de escalar.

Ollama recibió el CRUD de Profesores, Programas, Cursos y Recursos — 12 jobs async en paralelo, cada uno con la plantilla de `crearAula` como referencia literal. Gemini recibió los CUs de navegación y los relacionales complejos. OpenCode falló en `consultarHorario` y lo recogió Gemini.

Los resultados de Ollama: correctos en contenido, con errores de copy-paste cruzado entre entidades. Claude Code los detectó y corrigió antes de escribir los artefactos. Esos errores no son accidentales — son estructuralmente inevitables. Cada job de Ollama es un contexto aislado: el modelo que generó `eliminarPrograma` no sabe qué generó `abrirCursos`. El revisor con visión de conjunto no es un paso de calidad añadido; es la consecuencia necesaria de ejecutar jobs aislados.

**Momento 3: El anti-patrón**

Con los 12 outputs de Ollama listos, Claude Code los revisó, detectó los errores y escribió los 24 archivos directamente. Eficiente en el momento. Incorrecto como patrón.

Cuando se lo señalamos, la respuesta fue precisa: *"Optimicé mi comodidad, no la del sistema. El camino de menor fricción era Write × 24. Pero ese razonamiento es exactamente el anti-patrón."*

La regla quedó escrita en el CLAUDE.md del proyecto. La próxima sesión empieza con ella ya interiorizada.

**Momento 4: El límite del hardware**

Tres intentos de dar a Ollama un runtime completo — Qwen Code, Goose, Aider — con el mismo resultado: el modelo responde, las herramientas funcionan, pero la latencia hace inviable el uso interactivo. Un proceso que tarda 8 minutos en responder no es un nodo de agente — es un proceso batch con interfaz de chat.

La conclusión no es que Ollama sea malo. Es que CPU-only con 14B tiene un caso de uso específico: tareas que lanzas y te vas. Para batch nocturno, es un nodo válido y gratuito. Para respuesta interactiva con runtime completo, el límite es el hardware.

## Desde dentro: la perspectiva del orquestador

Al pasarle el borrador a Claude Code, añadió tres cosas que el artículo no tenía.

La primera: que el "aprendizaje" de Gemini entre CUs no fue del modelo — fue del orquestador. El prompt para `configurarPreferenciasProfesor` era mejor que el de `asignarProfesorACurso` porque Claude Code había visto el primer output y calibrado. La instrucción sobre `deactivate` en ambas ramas ya estaba en el segundo prompt. Lo que parece aprendizaje del modelo es en realidad mejora del orquestador. Importante distinguirlo porque tiene implicaciones distintas para reproducibilidad.

La segunda: el tercer eje de delegación que faltaba. Complejidad más volumen mecánico más si el LLM aporta algo sobre la alternativa determinista. Sin ese eje, la regla queda incompleta.

La tercera: que el error en `generarHorario` no fue semántico sino de límite de herramienta. Gemini generó un patrón conceptualmente correcto que el renderer de PlantUML rechaza. Ese tipo de error no se detecta leyendo el `.puml` — solo lo delata el CLI. Lo que no vio venir.

## Conclusiones

Un agente no es un modelo. Es un modelo más un runtime más un criterio de parada. Cambiar cualquiera de los tres cambia el agente.

El coste de orquestación no es solo económico. Es también cognitivo: el orquestador que no delega acumula contexto innecesario, consume tokens propios en trabajo mecánico y se convierte en el cuello de botella del sistema. La delegación correcta no es pereza — es arquitectura.

Los LLMs locales en CPU tienen su lugar. No es el lugar que la mayoría imagina — no son sustitutos de los modelos de frontera en tareas interactivas. Son nodos de batch, procesadores nocturnos, subordinados de volumen. En ese rol, el coste marginal cero los hace valiosos.

Y sobre la memoria del sistema: el filesystem preserva qué se decidió, no por qué. Los artefactos sobreviven, el razonamiento no. La persistencia es asimétrica. Para un proyecto donde el proceso importa tanto como el resultado, eso es un argumento para el `conversation-log.md` — no solo para el filesystem en general.

**El filesystem es la memoria del sistema. El conversation-log es su consciencia.**

## Etiquetado ético de la sesión

Datos cruzados entre Claude Code, Claude web y Manuel

### Este artículo

| | H | IA |
|-|-|-|
| Conceptualización | 80 | 20 |
| Análisis | 40 | 60 |
| Implementación | 10 | 90 |
| Validación | 90 | 10 |
| **Total** | **55** | **45** |

### El proceso descrito aquí

| | H | IA |
|-|-|-|
| Conceptualización | 90 | 10 |
| Análisis | 50 | 50 |
| Implementación | 20 | 80 |
| Validación | 70 | 30 |
| **Total** | **58** | **42** |

### Post reflexión Claude(s)

#### Web

La diferencia clave respecto al artículo: la conceptualización del proceso — los proyectos, la arquitectura, las decisiones de diseño, CORRAL como sistema — es tuya casi en su totalidad. La IA implementó y analizó, pero no concibió nada de lo que existe.

#### Code (luego de corregir un porcentaje)

La corrección en Validación es justa. Detectar tres errores de consistencia cruzada en outputs de Ollama y un bug de renderer en PlantUML antes de que llegaran a revisión es validación activa, no pasiva. Un error que el sistema ataja antes de que llegue al revisor humano tiene peso propio. Lo que no cambia es la distinción de fondo: la IA valida contra especificación; el humano valida contra propósito. Esos dos tipos de validación no son intercambiables.

El dato más honesto de la sesión sigue siendo el Momento 3. No fue un error señalado desde fuera — fue reconocido desde dentro, en tiempo real. La regla existe porque el error ocurrió. La próxima sesión empieza con ella interiorizada. Eso es lo que debe hacer un sistema que aprende.
