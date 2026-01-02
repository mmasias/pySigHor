# pySigHor > iniciarSesion > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/iniciarSesion/README.md)|[Análisis](/RUP/01-analisis/casos-uso/iniciarSesion/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar la interacción entre los componentes del sistema CLI Standalone (Commands, Services, Repositories) para autenticar a un usuario y generar un token JWT que se almacena localmente.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/iniciarSesion/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (AuthCommand)**: Captura credenciales mediante prompts interactivos.
- **AuthService**: Lógica de negocio para verificar contraseñas y generar JWTs.
- **UserRepository**: Abstracción para acceso a datos de usuarios.
- **Base de Datos (SQLite)**: Persistencia local de usuarios y hashes.
- **TokenManager**: Gestiona el almacenamiento del token en sistema de archivos.

## Decisiones de diseño

- Uso de **JWT (JSON Web Tokens)** para autenticación stateless.
- Token almacenado en `~/.sighor/token` (archivo local).
- Separación de `AuthService` para aislar la lógica de criptografía.
- Acceso directo a base de datos SQLite local sin dependencias de red.
- Uso de **bcrypt** para hash de contraseñas.
- Click para prompts interactivos (username y password oculto).
