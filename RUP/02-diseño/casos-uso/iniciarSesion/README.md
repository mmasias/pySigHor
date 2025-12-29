# pySigHor > iniciarSesion > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/iniciarSesion/README.md)|[Análisis](/RUP/01-analisis/casos-uso/iniciarSesion/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (Spring Boot + Angular)
- **Fecha**: 2025-12-29
- **Autor**: Manuel Masías + Claude Sonnet 4.5

## Propósito
Detallar la interacción entre los componentes del sistema (Frontend Angular, Controller, Services, Repositories) para autenticar a un usuario y generar un token JWT.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/iniciarSesion/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend (Angular)**: Captura credenciales mediante formulario reactivo y gestiona el almacenamiento del token.
*   **AuthController**: Endpoint REST `/api/auth/login` que recibe `LoginRequest`.
*   **AuthService**: Lógica de negocio para verificar contraseñas con `PasswordEncoder` y delegar generación de tokens.
*   **UsuarioRepository**: Interface Spring Data JPA para acceso a datos de usuarios.
*   **JwtTokenProvider**: Componente de utilidad para generar y validar tokens JWT.
*   **Base de Datos (H2)**: Persistencia de usuarios y hashes de contraseñas.

## Decisiones de diseño
*   Uso de **JWT (JSON Web Tokens)** para autenticación stateless.
*   **Spring Security** con `PasswordEncoder` (BCrypt) para hashing seguro.
*   Separación de responsabilidades: `AuthService` para lógica de negocio, `JwtTokenProvider` para manejo de tokens.
*   Manejo de excepciones con `@ControllerAdvice` para respuestas 401 consistentes.
*   Token almacenado en `LocalStorage` del navegador (Angular Service).
