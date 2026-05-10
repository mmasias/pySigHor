# pySigHor > consultarHorario > Diseño

## Información del artefacto
- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0
- **Fecha**: 2026-05-10
- **Autor**: Gemini

## Propósito
Definir la interacción entre los componentes del sistema para recuperar y visualizar el horario académico activo, gestionando tanto la existencia de datos como su ausencia mediante respuestas estándar de API.

## Diagrama de secuencia de diseño
![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/consultarHorario/secuencia.svg)
[Código PlantUML](secuencia.puml)

## Participantes
- **Administrador**: Actor que solicita la visualización del horario.
- **Frontend (React)**: Interfaz de usuario que gestiona el estado de la vista y la comunicación con la API.
- **API (FastAPI)**: Controlador que expone el endpoint y gestiona la seguridad (JWT).
- **HorarioService**: Capa de lógica de negocio que orquesta la obtención de datos y valida la existencia del recurso.
- **HorarioRepository**: Componente encargado del acceso a datos mediante SQLAlchemy async.
- **Base de Datos**: SQLite donde residen las tablas de horarios, sesiones académicas y sus relaciones.

## Decisiones de diseño
- **Endpoint GET /horario**: Se utiliza un endpoint singular ya que el sistema gestiona un único horario global activo.
- **Manejo de ausencia (404 Not Found)**: Si no se encuentra un horario generado, la API responde con un error 404, permitiendo al frontend distinguir entre "error de sistema" y "recurso no generado".
- **Estructura de respuesta SesionHorarioResponse**: Se entrega una lista plana donde cada objeto ya contiene los nombres resueltos de Curso, Profesor y Aula, optimizando la renderización de la tabla en React.
- **Seguridad JWT**: Se asume que el token JWT se envía en el encabezado de autorización para validar el acceso al recurso.
