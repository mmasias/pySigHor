<div align=right>

|||
|-|-|
|[🏠️](../README.md)|**Artículo**|

</div>

# bundungún -> LYCAEUM -> CORRAL: anatomía de una evolución

## La constante

Tres sistemas distintos. Una arquitectura que no cambió.

En los tres, el output de cada agente son ficheros. En los tres, el orquestador lee esos ficheros con sus propias herramientas. En los tres, el estado del sistema vive en el filesystem, no en la memoria de ningún proceso. Eso no es inercia — es una decisión de diseño que sobrevivió tres iteraciones porque funciona: los ficheros son verificables, persistentes, independientes del runtime que los produjo, y accesibles por cualquier herramienta sin intermediario.

Lo que cambió en cada salto no fue la arquitectura. Fue quién mueve los datos entre nodos.

## bundungún: cuatro voces, un humano decisor

bundungún era un script bash. Lanzaba cuatro CLIs de IA en un grid de Terminator — Claude, Gemini, Opencode, Qwen — con el mismo prompt. Los cuatro respondían en paralelo. El humano leía las cuatro respuestas, sintetizaba, decidía.

Era un pipeline, no un agente. El único nodo con capacidad de decisión era el humano. La topología era fija. No había delegación — había consulta múltiple.

El problema no era técnico: era cognitivo. Leer cuatro respuestas largas, identificar los puntos de divergencia, sintetizar sin perder los matices de cada perspectiva — eso es trabajo intelectual que el humano hacía entero, cada ronda.

**Lo que faltaba**: un nodo que decidiera, no solo consultara.

## LYCAEUM: un orquestador, un mensajero humano

LYCAEUM introdujo el blackboard pattern. Un directorio compartido. Un orquestador — Claude Code — que descompone el objetivo, escribe tareas diferenciadas para cada agente, lee las respuestas y sintetiza.

La arquitectura de separación control/datos apareció aquí por primera vez en su forma explícita: Claude Code como control plane, los subordinados como data plane. Cada agente con un rol distinto, una pregunta distinta, un ángulo distinto. La triangulación de perspectivas produjo hallazgos que ningún agente individual habría generado solo.

Pero el transporte seguía siendo manual. Manuel llevaba los `task_*.md` a cada agente. Manuel traía los `response_*.md` de vuelta. El orquestador no podía invocar a los subordinados — solo podía escribir instrucciones y esperar a que el mensajero las entregara.

El sistema funcionaba. Era incómodo.

**Lo que faltaba**: eliminar al mensajero.

## CORRAL: el mensajero desaparece

CORRAL no inventó una arquitectura nueva. Tomó la de LYCAEUM y resolvió el único problema que quedaba: el transporte.

Cada CLI externo se expone como herramienta MCP. Claude Code llama a `gemini_run` o `opencode_run` igual que llama a `bash`. El filesystem sigue siendo el bus de datos — los agentes escriben en workdirs, el orquestador lee con sus propias herramientas. La separación control/datos es idéntica.

Lo que cambió: el orquestador decide en tiempo de ejecución a quién delegar, con qué instrucción, en qué momento recoger. Sin intervención humana en el transporte. Sin mensajero.

La consecuencia directa: el paralelismo real. En LYCAEUM, lanzar tres agentes en paralelo requería que el humano entregara tres tareas manualmente y recogiera tres respuestas. En CORRAL, Claude Code lanza `gemini_run_async`, `opencode_run_async` y `ollama_run_async` en la misma operación y recoge cuando están listos. El tiempo total se aproxima al del agente más lento, no a la suma de todos.

## La fuerza que condujo cada salto

No fue la tecnología disponible — MCP existía antes de CORRAL, los CLIs existían antes de LYCAEUM. Fue la fricción.

bundungún era incómodo porque el humano sintetizaba. LYCAEUM resolvió eso pero era incómodo porque el humano transportaba. CORRAL resolvió eso.

Cada salto eliminó exactamente una fuente de fricción, sin cambiar lo que funcionaba. Esa es la señal de que la arquitectura base era correcta desde el principio.

## Lo que no cambió y por qué importa

El filesystem como fuente de verdad. Los artefactos como ficheros. La verificación determinista sobre el output final.

Esto no es una limitación técnica — es una decisión. Los flujos de texto volátiles entre procesos no son verificables. Un fichero sí. Puedes leerlo, diffarlo, commitearlo, auditarlo, pasárselo a otro agente en otra sesión. El filesystem no tiene estado de sesión — tiene historia.

En los tres sistemas, cuando algo falla, la pregunta es siempre la misma: ¿qué hay en el fichero? No ¿qué dijo el agente? — ¿qué escribió?

## La trilogía como unidad

El artículo 021 documenta LYCAEUM en su sesión fundacional — la primera vez que el blackboard pattern funcionó sobre un proyecto real. El artículo 023 documenta CORRAL en producción — la primera vez que el transporte fue completamente autónomo. Este artículo es el tejido conectivo: la misma arquitectura vista en tres momentos de su evolución.

bundungún era cuatro voces al mismo tiempo. LYCAEUM era un panel con un presidente. CORRAL es un panel donde el presidente convoca a los ponentes sin que nadie tenga que hacer de recadero.
