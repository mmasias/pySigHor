# pySigHor > abrirAulas > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirAulas/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirAulas/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar la interacción entre los componentes del sistema CLI Standalone para consultar y mostrar la lista de aulas, con soporte para formateo como tabla ASCII o JSON.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/abrirAulas/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (AulaCommand)**: Ejecuta comando de listado y gestiona opciones de formato.
- **TokenManager**: Verifica autenticación mediante token almacenado.
- **AulaService**: Lógica de negocio para obtener y transformar datos.
- **AulaRepository**: Abstracción para acceso a datos de aulas.
- **Base de Datos (SQLite)**: Persistencia local de aulas.
- **OutputFormatter**: Formatea salida en tabla ASCII (Rich) o JSON.

## Decisiones de diseño

- Verificación de autenticación obligatoria antes de ejecutar consulta.
- Acceso directo a SQLite mediante SQLAlchemy ORM.
- Uso de **Rich** para tablas ASCII con formato profesional.
- Opción `--format` para elegir entre tabla y JSON.
- Sin paginación (asumiendo volúmenes pequeños de datos).
- Conversión de objetos ORM a diccionarios en capa de servicio.
