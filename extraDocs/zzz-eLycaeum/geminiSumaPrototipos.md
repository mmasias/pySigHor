# Reflexión: De los Prototipos de Casos de Uso a las Pantallas Finales

Este documento consolida la discusión sobre cómo se transita desde los prototipos de interfaz de usuario (UI) adjuntos a los casos de uso individuales, hacia las pantallas finales de la aplicación, que a menudo componen funcionalidades de múltiples casos de uso.

## La Pregunta Clave

¿Cómo se llega de forma sistemática desde los prototipos que ilustran un único caso de uso a las pantallas finales que un actor utiliza para realizar su trabajo, las cuales integran elementos de varios casos de uso?

## Explicación Inicial: La Diferencia de Propósito

La primera clave para entender la transición es la diferencia fundamental en el **propósito** de ambos artefactos:

1.  **Prototipo en un Caso de Uso:**
    *   **Propósito:** Validar y clarificar el flujo de **un único caso de uso**.
    *   **Audiencia:** Analistas y stakeholders (usuarios, clientes).
    *   **Naturaleza:** Herramienta de comunicación, de baja fidelidad, enfocada y aislada. Su objetivo es confirmar que "el flujo de interacción para esta tarea específica es correcto".

2.  **Pantalla Final (GUI):**
    *   **Propósito:** Proveer una **interfaz de trabajo eficiente y coherente** para un actor.
    *   **Audiencia:** El usuario final de la aplicación.
    *   **Naturaleza:** Herramienta de trabajo, de alta fidelidad, integradora. Su objetivo es permitir al actor cumplir sus objetivos globales, dándole acceso a múltiples funcionalidades (casos de uso) desde un mismo lugar.

La transición, por tanto, no es una conversión 1 a 1, sino un proceso de **diseño y síntesis** que busca optimizar el *workflow* del actor.

## El Método Sistemático según RUP

El Proceso Unificado de Rational (RUP) ofrece un camino formal y trazable que ocurre principalmente en la disciplina de **Análisis y Diseño**. Este método reemplaza el "salto" por una serie de pasos intermedios.

### Paso 1: Identificar las Abstracciones de la Interfaz (Análisis)

La actividad clave es el **Análisis de Casos de Uso**. Por cada caso de uso, se crea una "realización" que identifica clases de análisis con roles específicos (estereotipos):

*   `<<Boundary>>` (Límite/Frontera): Es la abstracción de lo que se necesita en la interfaz para que el actor interactúe con el sistema. Representa una pantalla, ventana o un componente de la GUI. **Este es el puente conceptual hacia la UI.**
*   `<<Control>>`: Modela la lógica de negocio y la orquestación del caso de uso.
*   `<<Entity>>`: Modela los objetos del dominio y los datos.

Al final de este paso, no tenemos un diseño de pantalla, sino una colección de "fragmentos de UI" conceptuales (objetos `<<Boundary>>`) necesarios para satisfacer todos los casos de uso.

### Paso 2: Sintetizar la Interfaz Final (Diseño)

Esta es una actividad de **Diseño Arquitectónico y de UI**. El diseñador o arquitecto toma todas las clases `<<Boundary>>` identificadas y las organiza en una interfaz coherente.

1.  **Agrupar y Fusionar:** Se identifican patrones. Por ejemplo, las clases `<<Boundary>>` para "Crear Usuario" y "Modificar Usuario" pueden ser tan similares que se fusionan en una única abstracción: `FormularioGestionUsuario`.
2.  **Componer y Organizar:** Se diseña la pantalla final como un contenedor de estas abstracciones. Una `PantallaGestionUsuarios` podría contener:
    *   Una `GridUsuarios` (que viene del C.U. "Listar Usuarios").
    *   Un botón "Nuevo" que abre el `FormularioGestionUsuario`.
    *   Botones "Editar" y "Eliminar" en cada fila de la `GridUsuarios`.
3.  **Refinar:** Se detalla el layout final, la navegación entre las pantallas y la interacción precisa entre los widgets de la UI y las clases de control.

### Conclusión del Método

El camino sistemático es:

**Requisitos -> Análisis -> Diseño**

1.  **[Análisis]** Por cada Caso de Uso, derivar las clases `<<Boundary>>` necesarias.
2.  **[Diseño]** Para cada Actor, estudiar el conjunto de clases `<<Boundary>>` con las que debe interactuar.
3.  **[Diseño]** **Sintetizar** esas clases `<<Boundary>>` en pantallas finales cohesivas que optimicen el flujo de trabajo del actor.

Este proceso garantiza la **trazabilidad**: cada elemento en la UI final puede ser rastreado hasta una clase `<<Boundary>>` que lo representa, y esa clase existe porque es necesaria para la realización de uno o más casos de uso.
