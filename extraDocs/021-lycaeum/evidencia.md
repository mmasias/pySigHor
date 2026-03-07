# Evidencia y Enlaces - Artículo 021

<div align=right>

|||||
|-|-|-|-|
|[🏠️](../README.md)|[Artículo](README.md)|[Contexto](contexto.md)|**Evidencia**

</div>

## Commits de la Sesión

### Commit 1 — Ronda 1 LYCAEUM
```
LYCAEUM: ronda 1 completa - análisis estado pySigHor
```
Primer ciclo completo del sistema: objetivo → delegación → respuestas → síntesis. Incluye `_LYCAEUM/` con todos los artefactos de la ronda: tasks, responses, blackboard y síntesis final.

### Commit 2 — Acciones 0-A y 0-B
```
LYCAEUM 0-A/0-B: dashboard actualizado + diseño mínimo Edificios (pre-it2)
```
Ejecutado directamente por el orquestador sin delegación. Incluye:
- `RUP/README.md` actualizado con estado real de 5 CdU
- `RUP/02-diseño/casos-uso/edificio/` — 4 diagramas de secuencia (abrirEdificios, crearEdificio, editarEdificio, eliminarEdificio)

### Commit 3 — Acción 1
```
LYCAEUM Acción 1: migrar auth hardcodeada a BD real - prereq Iteración 2
```
Migración completa de autenticación. Archivos creados:
- `backend/app/models/usuario.py`
- `backend/app/schemas/usuario.py`
- `backend/app/repositories/usuario_repository.py`
- `backend/app/services/usuario_service.py`

Archivos modificados:
- `backend/app/models/__init__.py` — registra Usuario
- `backend/app/routers/auth.py` — elimina FAKE_USERS_DB
- `backend/init_db.py` — seed idempotente del admin
- `backend/.env` — SECRET_KEY segura (256 bits)

---

## Artefactos LYCAEUM generados

### CLAUDE.md — instrucciones del orquestador
Define el rol, el directorio de trabajo, el protocolo de ronda y el formato de síntesis final. Regla crítica: máximo 5 rondas por objetivo.

### contexto_*.md — instrucciones de los subordinados
Tres ficheros, uno por agente, con rol asignado, protocolo de lectura/escritura de archivos y formato de respuesta esperado.

### blackboard.md — estado global
Actualizado por el orquestador al inicio y al cierre de cada ronda. Registra el estado de cada agente y el veredicto de la ronda.

### sintesis_ronda1.md — síntesis final
Documento completo con conclusión, fundamento por agente, disensos relevantes y tabla de próximos pasos ordenados. Persistido en el repo para referencia futura del orquestador.

---

## Verificación de la migración de autenticación

Comandos ejecutados por el orquestador para verificar la Acción 1:

```bash
# Recrear BD
cd backend && rm -f pySigHor.db && poetry run python init_db.py
# Output:
# ✅ Usuario admin creado
# ✅ Base de datos creada exitosamente
# ✅ Tablas creadas: ['aulas', 'edificios', 'usuarios']

# Verificar contenido de BD
poetry run python -c "
from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///./pySigHor.db')
with engine.connect() as conn:
    print('Tablas:', engine.dialect.get_table_names(conn))
    result = conn.execute(text('SELECT id, username, activo FROM usuarios'))
    print('Usuarios:', result.fetchall())
"
# Output:
# Tablas: ['edificios', 'usuarios', 'aulas']
# Usuarios: [(1, 'admin', 1)]

# Login correcto
curl -X POST 'http://localhost:8000/api/v1/auth/login' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=admin&password=admin'
# Output: {"access_token": "eyJ...", "token_type": "bearer"}

# verify-token
# Output: {"username": "admin"}

# Login incorrecto
curl -X POST 'http://localhost:8000/api/v1/auth/login' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=admin&password=wrong'
# Output: {"detail": "Usuario o contraseña incorrectos"}
```

---

## Observación sobre el auto-compact

Durante la Acción 1, Claude Code activó compactación automática tras alcanzar ~48.7k tokens de contexto (301 tool uses en la fase de exploración). El plan sobrevivió porque ya estaba escrito antes de la compactación, pero representa un vector de fallo documentado para tareas de alta densidad.

**Indicador:** `Compacting conversation... (3m 20s · ↑ 9.0k tokens · thought for 26s)`

La compactación ocurrió en el momento de transición de exploración a redacción del plan, no durante la ejecución de cambios — el riesgo real fue bajo en este caso específico.

---

**Esta evidencia proporciona trazabilidad de los tres commits de la sesión, los artefactos generados por el sistema, y la verificación técnica de la migración ejecutada.**