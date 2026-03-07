# Contexto del Proyecto - Artículo 021

<div align=right>

|||||
|-|-|-|-|
|[🏠️](../README.md)|[Artículo](README.md)|**Contexto**|[Evidencia](evidencia.md)

</div>

## Estado del Proyecto en el Momento del Análisis

**Fecha**: 7 de marzo de 2026  
**Fase RUP**: Construcción — Iteración 1 completa  
**Colaboradores activos**: Manuel (operador/mensajero), Claude Code (orquestador), Opencode/GLM-4.6 (análisis técnico), Gemini (análisis pedagógico), Qwen (contrargumentación)

---

## Situación Técnica

### Iteración 1 completada
- ✅ Backend FastAPI + SQLAlchemy: 5 CdU implementados (iniciarSesion, abrirAulas, crearAula, editarAula, eliminarAula)
- ✅ Frontend React 18 + TypeScript + Material-UI
- ✅ Autenticación JWT con bcrypt
- ⚠️ Usuario hardcodeado en memoria (`admin/admin` en `FAKE_USERS_DB`)
- ⚠️ Dashboard `RUP/README.md` no reflejaba el estado real de desarrollo

### Documentación RUP
- ✅ 26 CdU identificados con detalle y análisis
- ✅ 5 CdU con diseño técnico completo (diagramas de secuencia)
- ✅ 5 CdU con implementación y documentación de desarrollo
- ❌ 21 CdU sin diseño técnico
- ❌ Testing: columna Pruebas vacía en todos los CdU

### Stack tecnológico
```
Backend:  FastAPI + SQLAlchemy (sync) + JWT/bcrypt + SQLite
Frontend: React 18 + TypeScript + Material-UI + Axios
Repo:     ~/misRepos/pySigHor — rama diseño-fastapi-react
```

### Patrón arquitectónico establecido
```
Router (español) → Service (español) → Repository (inglés) → ORM Model
```
Naming convention documentada en `RUP/02-diseño/configuracion-proyecto.md`.

---

## Situación Metodológica

### Deuda técnica conocida antes de LYCAEUM
| Problema | Severidad estimada |
|---|---|
| Credenciales hardcodeadas | Alta |
| Usuario sin BD | Alta |
| CORS permisivo | Media |
| Sin tests automatizados | Media |
| Dashboard inconsistente | Media |

### Próximas iteraciones planificadas (ruta original)
Edificios → Cursos → Profesores → GenerarHorario → Consulta → Reportes

La ruta asumía que `generarHorario()` era la última iteración — supuesto que el sistema cuestionaría durante la sesión.

---

## Contexto de bundungún

El sistema multi-agente previo de Manuel era un script bash que lanzaba cuatro CLIs (Claude, Qwen, Gemini, z.ai/OpenCode) en un grid de Terminator. Características:

- Flujo rígido: los cuatro recibían el mismo prompt
- Sin roles diferenciados
- Sin estado compartido entre sesiones
- El humano era el único nodo decisor

LYCAEUM surgió de una discusión conceptual sobre la diferencia entre un **pipeline** y un **agente**, y de la pregunta: *¿qué pasaría si uno de los nodos fuera el jefe?*

---

## Entorno de trabajo

```
OS:        Fedora / KDE (Wayland)
Terminal:  Terminator con grid de 4 paneles
Agentes:   Claude Code v2.1.70 (Sonnet 4.6 + Opus 4.6)
           OpenCode v1.2.20 (GLM-4.6 / Z.AI)
           Gemini CLI (Gemini 3 Auto)
           Qwen CLI
Directorio: ~/misRepos/pySigHor/_LYCAEUM/
```