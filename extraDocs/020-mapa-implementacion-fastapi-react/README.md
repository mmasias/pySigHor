# Mapa de Implementación - FastAPI + React

<div align=right>

||||||
|-|-|-|-|-|
|[🏠️](../README.md)|**Artículo 020**|[Contexto](contexto.md)|[Plan de Iteraciones](plan-iteraciones.md)|[Metodología](metodologia.md)|

</div>

## Resumen

Este artículo establece el mapa de implementación del sistema SigHor utilizando el stack tecnológico **FastAPI + React + TypeScript**, siguiendo una metodología de implementación por iteraciones con validación continua. El proyecto tiene naturaleza pedagógica: validar que **RUP permite construir sobre una base arquitectónica definida, ajustándose conforme se construye**.

**Objetivo central**: Construir la aplicación completa con trazabilidad de construcción, documentando los ajustes entre diseño e implementación como evidencia de la flexibilidad del proceso RUP.

## ¿Por qué?

### Naturaleza Pedagógica del Proyecto

Este no es un proyecto convencional de desarrollo de software. Es un **case study de RUP** con objetivos didácticos:

- ✅ Validar que un análisis RUP completo soporta implementación tecnológica
- ✅ Documentar cómo el diseño se ajusta durante la implementación
- ✅ Demostrar que RUP permite construir iterativamente sobre base arquitectónica
- ✅ Generar evidencia mediante commits bien descritos (no documentación forzada)

### Evidencia que Queremos Generar

**NO es**: "Diseñamos todo, luego implementamos todo sin errores"
- Esto no demostraría ajuste durante construcción
- No validaría la hipótesis de flexibilidad de RUP

**SÍ es**: "Diseñamos → Implementamos → Ajustamos → Documentamos"
- Muestra decisiones de diseño cambian con realidad de implementación
- Documenta ajustes reales (no teóricos)
- Valida que RUP permite construir ajustándose

## ¿Qué?

### Stack Tecnológico Seleccionado

<div align=center>

|Capa|Tecnología|Propósito|
|-|-|-|
|**Backend**|Python + FastAPI + Pydantic + SQLAlchemy|API REST con validación automática|
|**Frontend**|React + TypeScript + Vite|SPA moderna con type safety|
|**Base de Datos**|SQLite (desarrollo) → PostgreSQL (producción)|Zero-config para prototipado rápido|
|**Autenticación**|JWT (JSON Web Tokens)|Tokens stateless|
|**ORM**|SQLAlchemy|Mapeo objeto-relacional Python|

</div>

**Rationale de la selección**:
- **Rapidez de prototipado**: Python permite llegar al algoritmo principal más rápido
- **Stack moderno**: Demandado en el mercado actual
- **Zero-config**: SQLite para desarrollo sin overhead DevOps
- **Migración clara**: Esquema permite migrar a PostgreSQL posteriormente
- **Diseño completo**: 5/32 casos de uso ya diseñados (Iteración 1 lista)

### Estado Actual del Diseño

**Completados** (Iteración 1):
- ✅ `iniciarSesion()` - Autenticación JWT
- ✅ `abrirAulas()` - Listado paginado
- ✅ `crearAula()` - Creación con validación
- ✅ `editarAula()` - Edición con merge parcial
- ✅ `eliminarAula()` - Eliminación con confirmación

**Pendientes de diseño** (Iteraciones 2-7):
- Edificios, Recursos, Profesores, Programas, Cursos, GenerarHorario

## ¿Cómo?

### Metodología: Implementación por Iteraciones

<div align=center>

![Diagrama de flujo de iteraciones](/images/extraDocs/020-mapa-implementacion-fastapi-react/flujo-iteraciones.svg)
*Flujo de implementación por iteraciones ([flujo-iteraciones.puml](flujo-iteraciones.puml))*

</div>

#### Flujo de Trabajo por Iteración

```
1. Diseño (si no está listo)
   ↓
2. Implementación con commits descriptivos
   ↓
3. Ejecutable testeable en localhost
   ↓
4. Validación del ejecutable
   ↓
5. Documentación de ajustes
   ↓
6. Siguiente iteración
```

#### Criterio de Éxito por Iteración

- ✅ **Ejecutable funcional**: Backend + Frontend corriendo en localhost
- ✅ **Commits descriptivos**: Historia clara en mensajes de commit
- ✅ **Validación manual**: Tests ejecutados sobre el ejecutable
- ✅ **Ajustes documentados**: En conversation-log + casos de uso si pertinente

### Estrategia de Commits

Los commits son la **evidencia principal** del proceso. Deben ser descriptivos:

```bash
# Buen commit
git commit -m "feat(aulas): implementar abrirAulas con paginación de 20 elementos"

# Mal commit
git commit -m "implementar abrirAulas"

# Commit de ajuste
git commit -m "fix(aulas): corregir validación de capacidad para permitir aulas de 0-255"

# Commit de refactor
git commit -m "refactor(aulas): extraer lógica de filtrado a servicio FiltradoAulasService"
```

**Tipos de commits**:
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `refactor`: Reestructuración sin cambio de comportamiento
- `docs`: Cambios en documentación
- `test`: Agregar o modificar tests

## Plan de Iteraciones

### Resumen de Iteraciones

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

**Total**: 32 casos de uso en 7 iteraciones

### Iteración 1: Auth + CRUD Aulas ✅ DISEÑO COMPLETO

**Casos de uso** (5 casos):
1. `iniciarSesion()` - Autenticación con JWT
2. `abrirAulas()` - Listado paginado de aulas
3. `crearAula()` - Creación con validación de capacidad
4. `editarAula()` - Edición con merge parcial (PATCH)
5. `eliminarAula()` - Eliminación con confirmación

**Artefactos de diseño existentes**:
- Diagramas de secuencia con endpoints HTTP
- Clases de diseño (Pydantic schemas, SQLAlchemy models)
- Configuración de proyecto en `RUP/02-diseño/configuracion-proyecto.md`

**Próximo paso**: Implementar directamente desde diseño existente

### Iteración 2: CRUD Edificios

**Casos de uso** (4 casos):
1. `abrirEdificios()` - Listado de edificios
2. `crearEdificio()` - Creación de edificio
3. `editarEdificio()` - Edición de edificio
4. `eliminarEdificio()` - Eliminación de edificio

**Relaciones**:
- Edificio (1) ← (N) Aulas
- Eliminar en cascada ¿permitido o restringido?

### Iteración 3: CRUD Recursos

**Casos de uso** (4 casos):
1. `abrirRecursos()` - Listado de recursos
2. `crearRecurso()` - Creación de recurso
3. `editarRecurso()` - Edición de recurso
4. `eliminarRecurso()` - Eliminación de recurso

**Notas**:
- Recursos: Proyector, Laboratorio, Aires Acondicionados, etc.
- Bitmask de 5 bits en sistema legacy → Normalizar en diseño moderno
- Aulas ofrecen recursos, Profesores prefieren recursos

### Iteración 4: CRUD Profesores + Preferencias

**Casos de uso** (5 casos):
1. `abrirProfesores()` - Listado de profesores
2. `crearProfesor()` - Creación de profesor
3. `editarProfesor()` - Edición de profesor
4. `eliminarProfesor()` - Eliminación de profesor
5. `configurarPreferenciasProfesor()` - ¡R1-R5 del modelo de datos!

**Relaciones**:
- Profesor (1) ← (N) R_ProfesorCurso → (N) Curso
- Preferencias R1-R5 para algoritmo de optimización

### Iteración 5: CRUD Programas

**Casos de uso** (4 casos):
1. `abrirProgramas()` - Listado de programas académicos
2. `crearPrograma()` - Creación de programa
3. `editarPrograma()` - Edición de programa
4. `eliminarPrograma()` - Eliminación de programa

**Relaciones**:
- Programa (1) ← (N) Cursos
- Campo `Programa` embebido en M_Cursos en sistema legacy

### Iteración 6: CRUD Cursos (Complejo)

**Casos de uso** (5 casos):
1. `abrirCursos()` - Listado de cursos
2. `crearCurso()` - Creación con bloques horarios
3. `editarCurso()` - Edición de curso
4. `eliminarCurso()` - Eliminación de curso
5. `asignarProfesorACurso()` - Relación R_ProfesorCurso

**Notas**:
- Campo `H` (BloqueHorario) crítico para algoritmo
- Flags PI/PS/PC/PE para tipos de programa
- Ciclo, Créditos, Vacantes

### Iteración 7: Algoritmo Principal 🎯

**Casos de uso** (3-4 casos):
1. `generarHorario()` - ¡El corazón del sistema!
2. `abrirHorario()` - Ver resultado generado
3. `exportarHorario()` - PDF/Excel
4. ¿Validaciones/especiales?

**Algoritmo de 4 fases** (del sistema legacy):
1. `PrepararH()` - Resolución de conflictos
2. `GeneraPreHorario()` - Optimización dual (espacio + recursos)
3. `GeneraHorario()` - Materialización del horario final
4. `IngresoHE()/IngresoHV()` - Casos especiales

## Validación y Documentación de Ajustes

### Momento de Documentación

Al final de cada iteración (coincide con inicio de siguiente):

1. **Validar ejecutable**: Tests manuales en localhost
2. **Documentar ajustes** en:
   - `conversation-log.md` - Registro principal
   - Casos de uso específicos (si el ajuste es local)
   - Artículo 020 (actualización de este mapa)

3. **Tipos de ajustes a documentar**:
   - **Diseño → Implementación**: El diseño no funcionó como se pensó
   - **Restricciones técnicas**: Limitaciones del stack que forzaron cambio
   - **Mejoras de experiencia**: Implementación sugirió mejora al diseño
   - **Correcciones de bugs**: Errores que requirieron rediseño

### Plantilla de Documentación de Ajustes

```markdown
## Ajustes Iteración N - [Nombre Entidad]

### Ajuste 1: [Título corto]
- **Diseño original**: Lo que planeamos
- **Problema encontrado**: Qué no funcionó
- **Solución implementada**: Cómo lo ajustamos
- **Rationale**: Por qué esta solución es mejor
- **Impacto en diseño**: Si cambia algún artefacto de diseño

### Ajuste 2: [...]
```

## Métricas de Seguimiento

### Tabla de Progreso

<div align=center>

|Iteración|Entidad|Casos|Diseño|Implementación|Ejecutable|Ajustes|Commits|
|-|-|-|-|-|-|-|-|
|1|Auth + Aulas|5|✅|⏳|-|-|-|
|2|Edificios|4|⏳|-|-|-|-|
|3|Recursos|4|⏳|-|-|-|-|
|4|Profesores|5|⏳|-|-|-|-|
|5|Programas|4|⏳|-|-|-|-|
|6|Cursos|5|⏳|-|-|-|-|
|7|Generar Horario|3-4|⏳|-|-|-|-|

</div>

### Hitos de Validación

- **Hito 1**: Primer CRUD funcional (Iteración 1 completa)
- **Hito 2**: Tres CRUDs funcionando (Iteraciones 1-3 completas)
- **Hito 3**: CRUDs con relaciones complejas (Iteraciones 4-6 completas)
- **Hito 4**: Algoritmo generando horarios (Iteración 7 completa) 🎯

## Decisión Pendiente

### Motor de Base de Datos

Según **Artículo 019**: Extracción de BD Access 2.0

**Para fase de experimentación (actual)**:
- **SQLite** para desarrollo rápido
- Zero-config, archivo único
- Esquema idéntico permite migrar posteriormente

**Para fase de producción**:
- **PostgreSQL** como motor unificado
- Transversal a todos los stacks
- SQL estándar evita vendor lock-in

**Decisión**: Empezar con SQLite, migrar a PostgreSQL cuando el sistema esté validado.

## Conclusión

### Objetivo Final

Construir el sistema SigHor completo con:
- ✅ Trazabilidad completa en commits
- ✅ Ajustes documentados entre diseño e implementación
- ✅ Validación de que RUP permite construir ajustándose
- ✅ Evidencia pedagógica para comunidad de ingeniería de software

### Valor Didáctico

Este proyecto generará:
- **Case study auténtico** de aplicación RUP
- **Evidencia real** de ajustes entre diseño e implementación
- **Material educativo** sobre modernización de sistemas legacy
- **Validación metodológica** de RUP como proceso flexible

### Próximos Pasos

1. ✅ Artículo 020 creado (mapa de implementación)
2. ⏳ Cambiarse a rama `diseño-fastapi-react`
3. ⏾ Iniciar Iteración 1: Implementación de Auth + CRUD Aulas
4. ⏾ Validar ejecutable localhost
5. ⏾ Documentar ajustes de Iteración 1
6. ⏾ Continuar con Iteración 2

## Referencias

- [Artículo 015: Validación experimental de independencia tecnológica](/extraDocs/015-dashboards-multistack-validacion-experimental/)
- [Artículo 019: Extracción de BD Access 2.0](/extraDocs/019-extraccion-bd-access-coherencia-dominio/)
- [Diseño FastAPI+React](/RUP/02-diseño/) - Rama diseño-fastapi-react
- [Configuración de proyecto](/RUP/02-diseño/configuracion-proyecto.md)
- [Modelo del dominio](/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)
- [Estructura BD original](/src/DATOS/datosExportados/estructura-bd-original.md)

---

<div align=right>

**Artículo 020** - Mapa de Implementación FastAPI + React
Fecha: 15 de febrero de 2026
pySigHor - Sistema generador de horarios

</div>
