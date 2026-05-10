# pySigHor > cerrarSesion > Diseño
## Información del artefacto
- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Gemini
## Propósito
Definir la interacción entre los componentes del sistema para finalizar de forma segura la sesión del usuario y limpiar el estado de autenticación en el cliente.
## Diagrama de secuencia de diseño
![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/cerrarSesion/secuencia.svg)
[Código PlantUML](secuencia.puml)
## Participantes
- **Administrador (Actor)**: Inicia la solicitud de cierre y confirma la acción.
- **Frontend (React)**: Gestiona la interfaz de usuario, solicita confirmación, elimina el token JWT y redirige al login.
- **API (FastAPI)**: Expone el endpoint de logout para coordinar la terminación lógica de la sesión.
- **AuthService (Servicio)**: Implementa la lógica de negocio asociada a la finalización de la autenticación.
## Decisiones de diseño
- **JWT Stateless**: El cierre de sesión se delega principalmente al frontend mediante la eliminación del token, manteniendo el backend simple y sin estado (sin blacklist en este sprint).
- **Confirmación de Usuario**: Se implementa un flujo de confirmación antes de proceder con el logout para evitar cierres de sesión accidentales.
- **Endpoint Explícito**: Se utiliza un endpoint `POST /auth/logout` para permitir que el backend realice tareas de limpieza o auditoría futuras, siguiendo estándares REST.
