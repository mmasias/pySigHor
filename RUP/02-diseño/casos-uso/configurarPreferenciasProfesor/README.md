# pySigHor > configurarPreferenciasProfesor > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/README.md)|[Análisis](/RUP/01-analisis/casos-uso/configurarPreferenciasProfesor/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/configurarPreferenciasProfesor/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/configurarPreferenciasProfesor/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-11
- **Autor**: Gemini

## Propósito
Especificar el flujo para la configuración del orden de prioridad de recursos de un Profesor, utilizado por el algoritmo de generación de horarios para optimizar la asignación de aulas.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/configurarPreferenciasProfesor/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Componente `PreferenciasProfesor` con lista ordenable (drag & drop) de todos los recursos.
*   **API**: `GET /profesores/{id}/preferencias`, `PUT /profesores/{id}/preferencias`.
*   **PreferenciaService**: Inicializa preferencias por defecto si no existen; valida que el array de guardado contenga exactamente todos los recursos sin duplicados.
*   **PreferenciaRepository**: Reemplaza en bloque las filas de la tabla `preferencias` (DELETE + INSERT con prioridad = posición en el array).

## Decisiones de diseño
*   La lista incluye SIEMPRE todos los recursos del sistema — el admin reordena, no selecciona.
*   El body del PUT es un array ordenado de `recurso_ids`; la posición en el array define la prioridad (posición 0 = prioridad 1).
*   Si el profesor no tiene preferencias guardadas, el servicio inicializa con todos los recursos en orden por defecto antes de devolver la lista.
*   `422 Unprocessable Entity` si el array no contiene exactamente el conjunto completo de recursos disponibles (faltan, sobran o hay duplicados).
*   Retorno de `200 OK` con la lista actualizada ordenada por prioridad.
