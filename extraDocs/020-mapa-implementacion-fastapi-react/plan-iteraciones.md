# Plan de Iteraciones - FastAPI + React

<div align=right>

||||||
|-|-|-|-|
|[🏠️](../README.md)|**Artículo 020**|[Contexto](contexto.md)|[Plan de Iteraciones](plan-iteraciones.md)|[Metodología](metodologia.md)|

</div>

## Información del Artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Construcción (Construction)
- **Disciplina**: Implementación
- **Versión**: 1.0
- **Fecha**: 15 de febrero de 2026

## Resumen del Plan

Total de **32 casos de uso** organizados en **7 iteraciones** de ~5 casos cada una.

Cada iteración produce un **ejecutable testeable** en localhost con commits descriptivos que documentan el proceso de construcción.

<div align=center>

|Iteración|Entidad|Casos|Estado Diseño|Estado Implementación|
|-|-|-|-|-|
|**1**|Auth + Aulas|5|✅ Completo|⏳ Pendiente|
|**2**|Edificios|4|⏳ Pendiente|-|
|**3**|Recursos|4|⏳ Pendiente|-|
|**4**|Profesores + Preferencias|5|⏳ Pendiente|-|
|**5**|Programas|4|⏳ Pendiente|-|
|**6**|Cursos (Complejo)|5|⏳ Pendiente|-|
|**7**|Algoritmo Principal|3-4|⏳ Pendiente|-|

</div>

---

## Iteración 1: Auth + CRUD Aulas ✅ DISEÑO COMPLETO

### Casos de Uso (5 casos)

1. **iniciarSesion()** - Autenticación con JWT
2. **abrirAulas()** - Listado paginado de aulas
3. **crearAula()** - Creación con validación
4. **editarAula()** - Edición con merge parcial
5. **eliminarAula()** - Eliminación con confirmación

**Próximo paso**: Implementar directamente desde diseño existente

---

## Iteración 2: CRUD Edificios

**Casos de uso** (4 casos):
1. `abrirEdificios()` - Listado
2. `crearEdificio()` - Creación
3. `editarEdificio()` - Edición
4. `eliminarEdificio()` - Eliminación

**Relaciones**: Edificio (1) ← (N) Aulas

---

## Iteración 3: CRUD Recursos

**Casos de uso** (4 casos):
1. `abrirRecursos()` - Listado
2. `crearRecurso()` - Creación
3. `editarRecurso()` - Edición
4. `eliminarRecurso()` - Eliminación

**Notas**: Normalización desde bitmask de sistema legacy

---

## Iteración 4: CRUD Profesores + Preferencias

**Casos de uso** (5 casos):
1. `abrirProfesores()` - Listado
2. `crearProfesor()` - Creación
3. `editarProfesor()` - Edición
4. `eliminarProfesor()` - Eliminación
5. `configurarPreferenciasProfesor()` - R1-R5 del modelo de datos

**Relaciones**: Profesor (1) ← (N) R_ProfesorCurso → (N) Curso

---

## Iteración 5: CRUD Programas

**Casos de uso** (4 casos):
1. `abrirProgramas()` - Listado
2. `crearPrograma()` - Creación
3. `editarPrograma()` - Edición
4. `eliminarPrograma()` - Eliminación

**Relaciones**: Programa (1) ← (N) Cursos

---

## Iteración 6: CRUD Cursos (Complejo)

**Casos de uso** (5 casos):
1. `abrirCursos()` - Listado
2. `crearCurso()` - Creación con bloques horarios
3. `editarCurso()` - Edición
4. `eliminarCurso()` - Eliminación
5. `asignarProfesorACurso()` - Relación R_ProfesorCurso

**Notas**: Campo H (BloqueHorario), flags PI/PS/PC/PE

---

## Iteración 7: Algoritmo Principal 🎯

**Casos de uso** (3-4 casos):
1. `generarHorario()` - ¡El corazón del sistema!
2. `abrirHorario()` - Ver resultado generado
3. `exportarHorario()` - PDF/Excel
4. ¿Validaciones/especiales?

**Algoritmo de 4 fases**: PrepararH() → GeneraPreHorario() → GeneraHorario() → IngresoHE()/IngresoHV()

---

## Cronograma Estimado

<div align=center>

|Iteración|Duración Estimada|Complejidad|Dependencias|
|-|-|-|-|
|1|2-3 sesiones|Baja|Ninguna|
|2|1-2 sesiones|Baja|Iteración 1|
|3|1-2 sesiones|Media|Iteración 2|
|4|2-3 sesiones|Media|Iteración 3|
|5|1-2 sesiones|Baja|Iteración 4|
|6|3-4 sesiones|Alta|Iteraciones 4-5|
|7|4-5 sesiones|Muy Alta|Todas las anteriores|

</div>

**Total estimado**: 14-22 sesiones (~2-3 meses de trabajo esporádico)

---

## Hitos de Validación

- **Hito 1**: Primer CRUD funcional (Iteración 1 completa)
- **Hito 2**: Tres CRUDs funcionando (Iteraciones 1-3 completas)
- **Hito 3**: CRUDs con relaciones complejas (Iteraciones 4-6 completas)
- **Hito 4**: Algoritmo generando horarios (Iteración 7 completa) 🎯

---

**Plan de Iteraciones** - Artículo 020
Fecha: 15 de febrero de 2026
pySigHor - Sistema generador de horarios
