# Codex Suma – Prototipos y Pantallas Consolidadas

## Contexto inmediato
- Repositorio `pySigHor`: reingeniería del generador de horarios SIGHOR, con código Visual Basic 3.0 y fuerte documentación RUP.
- Uso docente actual: soporte para explicar RUP a estudiantes de Ingeniería de Software; foco presente en la disciplina de requisitos.

## Duda guía
¿Cómo explicar sistemáticamente el salto entre los prototipos de interfaz que aparecen acoplados a cada caso de uso y las pantallas finales que combinan elementos disparadores de múltiples casos?

## Línea de razonamiento
1. **Vista escenario**: cada caso de uso se prototipa de forma atómica para capturar el diálogo usuario-sistema mínimo. Sirve para validar el flujo sin contaminación de navegación global.
2. **Vista interfaz consolidada**: dentro de requisitos se arma un catálogo de componentes (formularios, listados, widgets) nacidos de los prototipos atómicos y se describe cómo se ensamblan cuando los casos colaboran. Aquí aparece la trazabilidad entre acciones compartidas, actores comunes y dependencias de datos.
3. **Vista navegación/arquitectura UI**: al pasar a diseño se modelan estados de interfaz, menús y elementos que disparan varios casos. Las interacciones globales son combinaciones explícitas de los flujos ya descritos, manteniendo la relación caso-botón/menú/acción.

Esta secuencia deja ver que las pantallas finales no son “nuevas”: reutilizan componentes validados en los casos de uso y los agrupan según las colaboraciones identificadas.

## Qué dice la teoría RUP
- **Modelo de casos de uso y especificaciones**: documenta prototipos centrados en cada flujo, pero no prescribe su consolidación.
- **Requisitos suplementarios**: incluyen lineamientos globales de usabilidad/interfaz, sin detallar la mecánica de ensamblaje.
- **Prototipos de interfaz**: la disciplina permite prototipos simples o globales, pero deja abierto el método para derivar pantallas completas.

Conclusión: la teoría legítima los prototipos aislados y autoriza prototipos integrados, pero no dicta un procedimiento formal para pasar de uno a otro. Esto abre el espacio para definir un artefacto propio (por ejemplo, catálogos de componentes, matrices caso→pantalla o mapas de navegación) que aseguren la trazabilidad desde los prototipos atómicos hasta las pantallas finales.
