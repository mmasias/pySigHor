# pySigHor > crearAula > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/crearAula/README.md)|[Análisis](/RUP/01-analisis/casos-uso/crearAula/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Propósito
Especificar el flujo para la creación de una nueva entidad Aula, incluyendo validaciones y persistencia.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/crearAula/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend**: Formulario `AulaForm` (modo creación).
*   **API**: Endpoint `POST /aulas`.
*   **AulaService**: Lógica de creación.
*   **AulaRepository**: `INSERT` en base de datos.

## Decisiones de diseño
*   Uso de `AulaCreate` schema para validación de entrada (tipos, obligatoriedad).
*   Retorno de código HTTP `201 Created` con el objeto creado.
