# pySigHor > iniciarSesion > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/iniciarSesion/README.md)|[Análisis](/RUP/01-analisis/casos-uso/iniciarSesion/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (CLI HTTP)
- **Fecha**: 2026-01-02
- **Autor**: Equipo de desarrollo

## Propósito

Detallar la interacción entre los componentes del sistema (CLI, API HTTP, Servicios) para autenticar a un usuario desde la línea de comandos y almacenar el token de acceso localmente.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/iniciarSesion/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes

- **CLI (Click)**: Captura credenciales mediante prompts y gestiona almacenamiento local del token.
- **APIClient**: Cliente HTTP que consume endpoint `/token` del backend FastAPI.
- **API (FastAPI)**: Endpoint `/token` que recibe `OAuth2PasswordRequestForm` (reutilizado).
- **AuthService**: Lógica de negocio para verificar contraseñas y firmar JWTs (reutilizado).
- **UsuarioRepository**: Abstracción para acceso a datos de usuarios (reutilizado).
- **Base de Datos (SQLite)**: Persistencia de usuarios y hashes (compartida).

## Decisiones de diseño

- Uso de **JWT (JSON Web Tokens)** para autenticación stateless (heredado del backend).
- **Almacenamiento local** del token en archivo `~/.sighor/token` (específico de CLI).
- CLI como **cliente HTTP puro**: consume mismo endpoint `/token` que interfaz React.
- Manejo de errores HTTP explícito (401 → "Credenciales inválidas", ConnectionError → "Backend no disponible").
- **Reuso completo del backend**: AuthService, UsuarioRepository y DB sin modificaciones.
