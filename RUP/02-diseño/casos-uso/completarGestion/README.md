# pySigHor > completarGestion > Diseño

## Información del artefacto
- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Gemini

## Propósito
Definir la interacción entre los componentes del sistema para presentar el panel central de gestión al usuario tras una autenticación exitosa.

## Diagrama de secuencia de diseño
![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/completarGestion/secuencia.svg)
[Código PlantUML](secuencia.puml)

## Participantes
- **Administrador**: Actor que interactúa con la interfaz.
- **Frontend (React)**: SPA que gestiona el estado de la sesión, la navegación y el renderizado del dashboard.
- **API (FastAPI)**: Punto de entrada REST que provee la información del perfil del usuario autenticado.
- **AuthService**: Lógica de negocio encargada de validar la integridad y vigencia del JWT.
- **UsuarioRepository**: Abstracción de acceso a datos para recuperar la información del usuario de la base de datos.
- **Base de Datos**: Persistencia (SQLite) donde se almacenan las credenciales y perfiles.

## Decisiones de diseño
- **Arquitectura desacoplada**: El frontend asume la responsabilidad de la navegación interna mediante React Router, reduciendo la carga del servidor y mejorando la respuesta de la UI.
- **Validación continua**: Cada acceso al dashboard dispara una verificación del token (`/auth/me`) para garantizar que la sesión sigue siendo válida antes de mostrar las opciones de gestión.
- **Simplificación de Permisos**: Para este sprint, se asume un modelo de acceso total para usuarios con rol administrador, centralizando la lógica en la existencia de un token válido vinculado a un usuario existente.
