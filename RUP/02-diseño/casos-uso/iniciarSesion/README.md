# pySigHor > iniciarSesion > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/iniciarSesion/README.md)|[Análisis](/RUP/01-analisis/casos-uso/iniciarSesion/README.md)|**Diseño**|[Desarrollo](/RUP/03-desarrollo/casos-uso/iniciarSesion/README.md)|[Pruebas](/RUP/04-pruebas/casos-uso/iniciarSesion/README.md)|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2025-11-19
- **Autor**: Gemini

## Propósito
Detallar la interacción entre los componentes del sistema (Frontend, API, Servicios) para autenticar a un usuario y generar un token de acceso.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/iniciarSesion/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend (React)**: Captura credenciales y gestiona el almacenamiento del token.
*   **API (FastAPI)**: Endpoint `/token` que recibe `OAuth2PasswordRequestForm`.
*   **AuthService**: Lógica de negocio para verificar contraseñas y firmar JWTs.
*   **UsuarioRepository**: Abstracción para acceso a datos de usuarios.
*   **Base de Datos (SQLite)**: Persistencia de usuarios y hashes.

## Decisiones de diseño
*   Uso de **JWT (JSON Web Tokens)** para autenticación stateless.
*   Separación de `AuthService` para aislar la lógica de criptografía.
*   Manejo de errores 401 explícito para feedback al usuario.
