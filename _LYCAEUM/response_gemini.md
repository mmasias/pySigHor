# Respuesta Gemini — Ronda 1

## Análisis de valor pedagógico diferencial

| Grupo de CdU | Concepto nuevo que introduce | Valor didáctico |
| :--- | :--- | :--- |
| **Aulas (Completado)** | **Vertical Slice**: Estructura base (FastAPI, SQLModel, Inyección de dependencias). | **Alto** (Cimientos técnicos) |
| **Edificios** | **Jerarquía e Integridad**: Relaciones 1:N, borrados en cascada y navegación entre entidades vinculadas. | **Medio** (Estructura de datos) |
| **Cursos** | **Reglas de Dominio**: Mapeo de restricciones físicas (créditos/horas) a lógica de persistencia. | **Medio-Alto** (Lógica de negocio) |
| **Profesores** | **Preferencias Ponderadas**: Introducción de pesos (R1-R5) y relaciones M:N con Cursos. | **Alto** (Preparación algorítmica) |
| **Recursos** | **Optimización de Datos**: Implementación de `BitSets` o banderas para matching rápido (herencia del legacy). | **Medio** (Eficiencia) |
| **Horarios / Algoritmo** | **Optimización Combinatoria**: Gestión de estado global, transacciones complejas y validación de conflictos. | **Muy Alto** (El "Core") |

**Punto de aplanamiento de la curva:** Tras completar **Cursos**, la mecánica de "pantalla de mantenimiento" (CRUD) deja de enseñar arquitectura para convertirse en repetición. Para evitar esto, **Profesores** debe enfocarse no en el CRUD, sino en el modelado de las preferencias para el algoritmo.

## Momento óptimo para introducir pruebas (testing)

**Recomendación: Iniciar inmediatamente en la Iteración 2 (Edificios).**

**Justificación:**
Si se introducen en la Iteración 1, la carga cognitiva de aprender el stack (FastAPI/SQL) es excesiva. Introducirlas en la Iteración 2, sobre entidades simples como `Edificios`, permite aprender la mecánica de `Pytest` y *Testcontainers/Mocks* en un entorno controlado. Es vital tener esta red de seguridad **antes** de llegar a `Profesores` y `Horarios`, donde la lógica se vuelve difícil de trazar manualmente.

## Propuesta narrativa: "La Búsqueda del Horario Perfecto"

En lugar de una lista de tareas, propongo estructurar el desarrollo como una **historia de complejidad creciente**:

1.  **El Escenario (Aulas/Edificios):** Empezamos definiendo el "donde". El reto didáctico aquí es la consistencia: ¿Qué pasa con las aulas si demolemos un edificio?
2.  **Los Actores y sus Deseos (Cursos/Profesores):** Introducimos el conflicto. Los cursos tienen requisitos y los profesores tienen "caprichos" (las prioridades R1-R5). Aquí el alumno aprende que los datos no son planos; tienen "pesos" que afectarán el futuro.
3.  **El Oráculo (`generarHorario()`):** Introducir una versión "Alfa" del algoritmo antes de terminar todos los CRUDs de consulta. Los alumnos implementan la Fase 1 (Minimizar desperdicio de espacio) usando solo Aulas y Cursos. Esto genera un "momento WOW" temprano al ver al sistema tomar decisiones.
4.  **El Refinamiento (Recursos/Algoritmo completo):** Una vez que el sistema "decide", le añadimos complejidad (recursos, bitsets). El alumno vuelve atrás para refinar sus modelos de datos para que el oráculo sea más inteligente.

## Perspectivas adicionales

-   **Deuda Técnica Controlada:** Podría ser interesante permitir que los alumnos implementen `Edificios` sin tests, y luego "sufrir" un bug al implementar `Profesores` que los obligue a retroceder y aplicar testing como solución a un problema real, no como una imposición académica.
-   **El Factor Humano:** El algoritmo original fallaba por no considerar la fatiga. Una iteración final de "Consultas/Reportes" no debería ser solo visualización, sino una fase de "Crítica al Algoritmo" donde se ajusten pesos basados en el feedback de los reportes.

## Síntesis
La prioridad didáctica es romper el ciclo de CRUDs en la Iteración 3 para introducir una versión simplificada del algoritmo de optimización, usando el testing desde la Iteración 2 como la herramienta que permite esta transición hacia la complejidad.
