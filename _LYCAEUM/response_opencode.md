# Respuesta Opencode — Ronda 1

## Análisis de la deuda técnica de la Iteración 1

### Tabla de problemas identificados

| Problema | Severidad | Justificación |
|----------|-----------|---------------|
| **Credenciales hardcodeadas** (`admin:admin`) | Bloqueante | Expone vulnerabilidad crítica de seguridad que podría propagarse a producción. Impide implementación real de usuarios múltiples. |
| **Usuario único sin base de datos** | Bloqueante | Bloquea toda funcionalidad de gestión de usuarios (roles, permisos, auditoría). Fundamental para sistema multiusuario. |
| **CORS permisivo sin configuración específica** | Diferible | Problema de seguridad pero no bloquea funcionalidad. Puede configurarse en iteraciones posteriores sin afectar desarrollo actual. |
| **Ausencia de tests automatizados** | Diferible | Aunque ideal, no bloquea el desarrollo de nuevas funcionalidades. Los patrones actuales son suficientemente consistentes. |

### Análisis de arquitectura para escalabilidad

La arquitectura establecida en `configuracion-proyecto.md` **ES suficientemente genérica para soportar ~26 casos de uso** sin refactorización mayor. Los patrones Router → Service → Repository → Model son consistentes y reutilizables.

**Piezas específicas que añadir para Iteración 2 (Edificios):**

1. **Nuevo modelo**: `backend/app/models/edificio.py` (ya existe)
2. **Schema**: `backend/app/schemas/edificio.py` (pendiente)
3. **Repository**: `backend/app/repositories/edificio_repository.py` (pendiente)
4. **Service**: `backend/app/services/edificio_service.py` (pendiente)
5. **Router**: `backend/app/routers/edificios.py` (pendiente)
6. **Frontend**: `frontend/src/pages/EdificiosPage.tsx` (pendiente)
7. **Relación aula-edificio**: Ya implementada en `aula.py:17`

La estructura actual soporta perfectamente este crecimiento sin modificaciones.

### Evaluación de la secuencia de iteraciones

**✅ La secuencia actual es CORRECTA desde perspectiva técnica:**

**Edificios → Cursos → Profesores → Generación de Horarios → Consulta → Reportes**

**Justificación:**

1. **Dependencias de datos**: Los edificios son prerequisito de aulas (relación FK existente). Cursos y profesores son independientes entre sí pero necesarios antes del algoritmo.

2. **Complejidad creciente**: La secuencia va de lo simple (CRUD básico) a lo complejo (algoritmo de optimización), permitiendo construir bases sólidas.

3. **Reutilización de patrones**: Los primeros 3 CdU (Edificios, Cursos, Profesores) reutilizan exactamente los mismos patrones CRUD, maximizando eficiencia.

4. **Validación incremental**: Cada iteración valida la anterior antes de abordar el complejo algoritmo de horarios.

## Consideraciones técnicas

### Bloqueantes críticos a resolver ANTES de Iteración 2:

1. **Implementar persistencia de usuarios**: Migrar de `FAKE_USERS_DB` a tabla SQLAlchemy real
2. **Configurar SECRET_KEY seguro**: Cambiar valor hardcodeado en producción
3. **Establecer manejo de roles**: Preparar para múltiples tipos de usuarios

### Recomendación de implementación prioritaria:

Resolver el bloqueante de usuarios mediante:
- Crear modelo `Usuario` con migración Alembic
- Implementar `UsuarioRepository` y `UsuarioService`
- Modificar `auth.py` para usar base de datos real
- Configurar variables de entorno apropiadas

La deuda técnica restante (CORS, tests) puede abordarse en paralelo sin bloquear el avance.

## Recomendación

**Avanzar a Iteración 2 PERO después de resolver los bloqueantes de autenticación**. La arquitectura está lista para escalar y la secuencia planeada es técnicamente sólida.