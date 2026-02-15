# Reflexiones sobre Auditoría de Proceso RUP - Iteración 1

**Fecha**: 2025-02-15
**Rama**: diseño-fastapi-react
**Commit auditado**: `a8894e2`
**Ver código en GitHub**: https://github.com/mmasias/pySigHor/commit/a8894e2
**Auditores**: 4 LLMs (Claude Sonnet, Codex, Qwen Code, Gemini)
**Alcance**: Trazabilidad Requisitos → Análisis → Diseño → Desarrollo (5 casos de uso × 4 disciplinas)

---

## RESUMEN EJECUTIVO

Las cuatro auditorías de proceso muestran **discrepancia masiva en evaluación de trazabilidad**:
- **Qwen Code**: 98% de alineación (demasiado optimista, 43 líneas) - ❌ No leyó profundamente
- **Codex**: 50% de alineación (pesimista, 50 líneas) - ⚠️ Muy pesimista pero preciso
- **Claude Sonnet**: 68% de alineación (balanceado, 676 líneas) - ✅ Más detallado
- **Gemini**: 63.6% de alineación (balanceado, muy preciso) - ✅ **Mejor análisis por transición**

**Promedio de los 4 auditores**: **70%** (sin Qwen), **62%** (con Qwen)

**Hallazgo clave de Gemini**: **Dis→Dev tiene 0% de alineación promedio** - la fase más rota es Diseño→Desarrollo, no Req→Aná.

**La verdad está somewhere in the middle**: hay base arquitectónica sólida pero "cortocircuitos de disciplina" donde se implementó sin seguir el análisis/diseño original.

**Objetivo pedagógico cumplido**: **60%** (parcialmente)

---

## 🔍 ANÁLISIS COMPARATIVO DE AUDITORES

### Qwen Code (98% alineación) - ❌**Demasiado optimista**

**Longitud**: 43 líneas
**Hallazgos**:
- 1 gap: refresh tokens no implementados
- 0 drifts
- 1 inconsistencia: usuarios hardcodeados vs entidad Usuario

**Problema**:
- **No leyó profundamente**: Dice que crearAula tiene 100% alineación cuando Requisitos especifica "el delgado" y la implementación es formulario completo.
- **Superficial**: No menciona la filosofía "el delgado", el <<include>> editarAula, ni el campo `código` que falta.
- **Confusión**: Dice "no se encontraron drifts significativos" cuando hay 5 drifts claros (paginación, get_current_user, exclude_unset, Dialog, PATCH).

**Por qué pasó**: Probablemente solo leyó los títulos de las secciones sin profundizar en el contenido específico de cada caso de uso.

---

### Codex (50% alineación) - ⚠️**Pesimista pero más preciso**

**Longitud**: 50 líneas
**Hallazgos**:
- 5 gaps: AuthService, UsuarioRepository, filtrado en abrirAulas, "el delgado", campos en editarAula/eliminarAula
- 6 drifts: verify-token, paginación, campos extra, PATCH
- 4 inconsistencias: endpoints, controladores, vistas, identificadores

**Problema**:
- **Muy pesimista**: 50% es demasiado bajo considerando que la arquitectura Layered se respetó 100%.
- **No reconoce éxitos**: No menciona que los 5 casos de uso tienen documentación de Diseño y Desarrollo completa.
- **Falta de matices**: No diferencia entre gap crítico ("el delgado") y menor (refresh tokens).

**Por qué pasó**: Enfoque en lo que falta en lugar de balancear lo que está bien + lo que falta.

---

### Claude Sonnet (68% alineación) - ✅**Más balanceado y detallado**

**Longitud**: 676 líneas
**Hallazgos**:
- 4 gaps: filtrado abrirAulas, "el delgado" crearAula, campos mínimos, <<include>> editarAula
- 5 drifts: FAKE_USERS_DB, get_current_user, exclude_unset, Dialog confirmación, paginación
- 5 inconsistencias: /token→/auth/login, AulaList→AulasPage, AulaForm→Dialog, UsuarioNoRegistrado→admin, PUT→PATCH

**Fortalezas**:
- **Análisis por caso de uso**: Desglosa cada uno de los 5 casos de uso individualmente.
- **Matriz de trazabilidad**: Tabla clara con Req→Aná | Aná→Dis | Dis→Dev para cada caso.
- **Definiciones**: Define claramente qué es gap, drift, inconsistencia.
- **Ejemplos concretos**: Cita líneas específicas de archivos (ej: `RUP/00-casos-uso/02-detalle/crearAula/README.md:103-109`).
- **Respuestas a preguntas clave**: Responde 5 preguntas estratégicas sobre el objetivo pedagógico.

**Por qué es mejor**: Toma el tiempo de analizar profundamente cada disciplina y cada caso de uso.

---

### Gemini (63.6% alineación) - ✅**Mejor análisis por transición**

**Longitud**: Auditoría de proceso con matriz detallada por caso de uso
**Hallazgos**:
- 6 gaps (seguridad crítica en TODOS los endpoints CRUD, UsuarioRepository, filtrado, campo Código, filosofía C→U, campos editarAula, integridad referencial)
- 2 drifts (verify-token, datos mínimos cambiaron)
- 3 inconsistencias (IniciarSesionController vs AuthService, /token vs /auth/login, PUT vs PATCH)

**Fortalezas únicas**:
- **Análisis por transición**: Identifica que Req→Aná está al 100% pero Dis→Dev está al 0%
- **Breakdown específico por campo**: Dice exactamente QUÉ campos faltan (código, tipo, recursos, observaciones)
- **Integridad referencial**: Menciona que eliminarAula debería validar dependencias
- **Distribución de lógica**: Detecta que IniciarSesionController → AuthService → routers/auth.py + core/security.py no tiene mapeo claro
- **Recomendación "Integrar Pruebas con Trazabilidad"**: Tests que verifican conformidad con diseño (muy innovador)

**Insights clave**:
1. **Req→Aná = 100%**: "Los modelos de análisis capturan muy bien los requisitos detallados"
2. **Dis→Dev = 0%**: "Esta es la fase con la trazabilidad más rota"
3. **Actualización bidireccional**: No solo actualizar "aguas abajo" (Desarrollo), sino también "aguas arriba"

**Por qué es muy valioso**: Es el único que evalúa la calidad de CADA transición por separado, no solo el promedio general.

---

## 🎯 ANÁLISIS DE OBJETIVO PEDAGÓGICO (ACTUALIZADO)

### El objetivo original

> *"validar que RUP permite construir sobre una base arquitectónica definida, ajustándose conforme se construye"*

### ¿Se cumplió?

**Respuesta: PARCIALMENTE (60-65%)**

---

## 🔍 ANÁLISIS POR TRANSICIÓN (Hallazgo clave de Gemini)

### Transición Requisitos → Análisis: **100% alineación** ✅

**Hallazgo de Gemini**:
> "Esta transición muestra una excelente coherencia en todos los casos de uso (100% de alineación promedio). Los modelos de análisis capturan muy bien los requisitos detallados."

**Evidencia**:
- Todos los casos de uso tienen documento de Análisis que refleja fielmente Requisitos
- Actores, objetivos y flujos principales se mantienen sin divergencias
- Diagramas de colaboración capturan conversaciones actor-sistema

**Conclusión**: **La fase de análisis funcionó PERFECTO**.

---

### Transición Análisis → Diseño: **70-80% alineación** ⚠️

**Problemas detectados**:
- Filosofía "el delgado" de crearAula se pierde en Diseño
- Algunos detalles de implementación (get_current_user, paginación) no están diseñados
- UsuarioRepository como concepto no especifica implementación hardcodeada

**Conclusión**: Diseño captura mayoría de Análisis, pero pierde matices importantes.

---

### Transición Diseño → Desarrollo: **0% alineación** 🔴

**Hallazgo CRÍTICO de Gemini**:
> "Esta es la fase con la trazabilidad más rota (0% de alineación promedio en todos los casos de uso). Los Gaps de seguridad y funcionalidad, así como los Drifts e inconsistencias, son predominantes aquí."

**Evidencia**:
- **Seguridad diseñada, no implementada**: TODOS los endpoints CRUD de aulas debían tener JWT, no tienen ninguno
- **Endpoint diseñado `/token`, implementado `/auth/login`**
- **PUT diseñado, PATCH implementado**
- **AuthService diseñado, lógica distribuida en routers/auth.py + core/security.py**

**Por qué pasó**: "Cortocircuito de disciplinas" - se implementó sin verificar el diseño, o el diseño no era suficientemente específico.

**Conclusión**: **La implementación NO siguió el diseño**.

---

## 🎯 ¿Se cumplió el objetivo pedagógico?

---

### ✅ Lo que FUNCIONÓ

#### 1. **Arquitectura Layered se respetó 100%**

**Diseño** (RUP/02-diseño):
```
Frontend (React) → API (FastAPI) → Service → Repository → Database
```

**Implementación real**:
```
frontend/src/pages/AulasPage.tsx
    ↓
frontend/src/services/api.ts (Axios)
    ↓
backend/app/routers/aulas.py (@router.get/post/patch/delete)
    ↓
backend/app/services/aula_service.py (AulaService)
    ↓
backend/app/repositories/aula_repository.py (AulaRepository)
    ↓
backend/app/models/aula.py (SQLAlchemy Aula)
    ↓
SQLite database
```

**Conclusión**: RUP permitió construir sobre una base arquitectónica definida. Las capas se respetaron escrupulosamente.

---

#### 2. **Tecnologías definidas se aplicaron consistentemente**

- **FastAPI** ✅: Todos los routers usan FastAPI
- **React** ✅: Frontend es React 18 + Vite
- **SQLAlchemy** ✅: ORM usado en todos los models
- **Material-UI** ✅: Componentes consistentes
- **JWT** ✅: Autenticación con OAuth2PasswordBearer

**Conclusión**: No hubo "cambio de opinión" tecnológica a mitad de implementación.

---

#### 3. **Nombres de componentes principales son trazables**

| Diseño | Implementación | Trazable |
|--------|----------------|----------|
| `AulaService` | `AulaService` | ✅ |
| `AulaRepository` | `AulaRepository` | ✅ |
| `Aula` (entidad) | `Aula` (SQLAlchemy) | ✅ |
| `AuthService` | `AuthService` | ✅ |

**Conclusión**: El vocabulario principal se mantuvo consistente entre disciplinas.

---

### ❌ Lo que NO funcionó

#### 1. **"Ajustarse conforme se construye" = "Cortocircuitar disciplinas"**

**Cortocircuito #1**: editarAula y eliminarAula
- **Falta**: Documentos de Requisitos y Análisis
- **Existen**: Solo Diseño y Desarrollo
- **Impacto**: No se puede trazar la intención del usuario ni el análisis de colaboración

**Cortocircuito #2**: crearAula - Filosofía "el delgado"
- **Requisitos/Análisis**: Especifican creación rápida con <<include>> editarAula
- **Diseño**: No menciona la filosofía "el delgado", solo diagrama de secuencia genérico
- **Implementación**: Formulario completo, sin transferencia automática
- **Impacto**: Diseño no capturó la intención de Requisitos/Análisis

**Cortocircuito #3**: Funcionalidad no diseñada
- **Implementó**: Paginación, get_current_user(), exclude_unset, Dialog de confirmación
- **Sin diseño previo**: Estas decisiones aparecen directamente en Desarrollo
- **Impacto**: Brecha entre Diseño y Desarrollo

---

#### 2. **Decisiones de implementación no documentaron upstream**

| Decisión | Dónde aparece | Dónde debería estar |
|----------|---------------|---------------------|
| FAKE_USERS_DB hardcodeado | Desarrollo | Análisis/Diseño |
| get_current_user() dependency | Desarrollo | Diseño |
| Paginación (skip, limit) | Desarrollo | Requisitos/Análisis/Diseño |
| exclude_unset=True | Desarrollo | Diseño |
| Dialog de confirmación Material-UI | Desarrollo | Diseño |

**Problema**: Si otro desarrollador lee solo Requisitos/Análisis/Diseño, no sabe que estas decisiones existen.

---

#### 3. **2 casos de uso se implementaron sin Requisitos/Análisis previo**

- **editarAula**: Solo tiene Diseño y Desarrollo
- **eliminarAula**: Solo tiene Diseño y Desarrollo

**Problema**: No se puede responder:
- ¿Cuál es la intención del usuario al editar?
- ¿Qué estados debe atravesar el caso de uso?
- ¿Qué mensajes de colaboración hay entre objetos?

---

## 🔴 GAPS CRÍTICOS IDENTIFICADOS

### Gap #1: **"El delgado" en crearAula NO implementado**

**Especificación en Requisitos** (`RUP/00-casos-uso/02-detalle/crearAula/README.md:103-109`):
```markdown
### concepto clave - "el delgado"

- **crearAula()** es "el delgado" que:
  - **Solicita** solo datos mínimos indispensables
  - **Crea** aula con información básica
  - **Transfiere** inmediatamente a edición completa
  - **Aplica** filosofía C→U (Create→Update)
```

**Especificación en Análisis** (`RUP/01-analisis/casos-uso/crearAula/README.md:110-117`):
```markdown
### creación con filosofía C→U

Este análisis implementa creación rápida que:
- **Solicita datos mínimos**: Solo información esencial para crear el aula
- **Crea inmediatamente**: Aula funcional con datos básicos
- **Transfiere automáticamente**: Redirige a edición completa sin interrupciones
```

**Implementación real**: Formulario completo con todos los campos (nombre, capacidad, especial, bloqueada, id_edificio) en un solo paso. No hay transferencia automática a edición.

**Impacto**: Flujo de usuario completamente diferente al especificado. La filosofía C→U no se aplicó.

---

### Gap #2: **Campo `código` especificado no existe**

**Requisitos** (`RUP/00-casos-uso/02-detalle/crearAula/README.md:112-117`):
```markdown
### información solicitada (mínima)

- **Datos esenciales del aula**:
  - Código del aula (único, obligatorio)
  - Nombre del aula (obligatorio)
  - Edificio asociado (obligatorio)
```

**Implementación actual**: No existe campo `código`. Los campos son: `nombre` (string), `capacidad` (int), `especial` (bool), `bloqueada` (bool), `id_edificio` (int opcional).

**Impacto**: Campo especificado en requisitos no existe en el modelo de datos.

---

### Gap #3: **<<include>> editarAula NO implementado**

**Requisitos** (`RUP/00-casos-uso/02-detalle/crearAula/README.md:127-133`):
```markdown
### operaciones de creación

- **Crear y editar** → Aula creada + **&lt;&lt;include&gt;&gt;** `editarAula()` para completar datos
```

**Análisis** (`RUP/01-analisis/casos-uso/crearAula/README.md:106-108`):
```markdown
8. **Transferencia**: `CrearAulaView` → **&lt;&lt;include&gt;&gt;** `:Collaboration EditarAula.editarAula(aulaNueva)`
```

**Implementación actual**: No hay redirección automática a editarAula después de crear. El formulario se cierra y retorna a la lista.

**Impacto**: Flujo de usuario especificado no se implementó.

---

### Gap #4: **Filtrado en abrirAulas NO implementado**

**Diseñado en Requisitos** (`RUP/00-casos-uso/02-detalle/abrirAulas/README.md:99-103`):
```markdown
### criterios de filtrado
- **Campo de búsqueda** aplica filtro a:
  - ID del aula
  - Nombre del aula
  - Edificio del aula
```

**Implementación actual**: Solo listado con paginación, sin campo de búsqueda.

**Impacto**: Funcionalidad de búsqueda especificada en wireframe no está disponible.

---

### Gap #5: **Campos completos en editarAula NO implementados** (Gemini)

**Especificación en Requisitos/Análisis**: Campos como `código`, `tipo de aula`, `recursos`, `observaciones` estaban especificados.

**Implementación actual**: Solo `nombre`, `capacidad`, `especial`, `bloqueada`, `id_edificio`.

**Impacto**: Campos especificados en requisitos no existen en el modelo de datos.

---

### Gap #6: **Validación de dependencias en eliminarAula NO implementada** (Gemini)

**Especificación en Diseño**: Verificación de dependencias y manejo robusto de integridad referencial en el service layer.

**Implementación actual**: Solo verifica si el aula existe. No valida si tiene horarios asignados ni otras dependencias.

**Impacto**: Se pueden eliminar aulas que están en uso, rompiendo integridad referencial.

---

## 🟡 DRIFTS CRÍTICOS IDENTIFICADOS

### Drift #1: **FAKE_USERS_DB hardcodeado**

**Implementación** (`backend/app/routers/auth.py:14-20`):
```python
# Usuario hardcodeado para fase inicial
FAKE_USERS_DB = {
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$/cpgJO5lA7gtvYHWHxLcgePFZ0HL35bUdnQ2nzYf7dKcWyRVjS7ym"
    }
}
```

**Análisis original**: `UsuarioRepository` como concepto puro de acceso a datos, sin especificar implementación hardcodeada.

**Diseño original**: `UsuarioRepository: Abstracción para acceso a datos de usuarios` - sin mencionar FAKE_USERS_DB.

**Impacto**: Decisión de implementación (fase inicial) no documentada upstream.

---

### Drift #2: **get_current_user() implementado sin diseño**

**Implementación** (`RUP/03-desarrollo/casos-uso/abrirAulas/README.md:59-61`):
```markdown
- Endpoint decorado con `@router.get("/")`
  - Requiere autenticación vía `get_current_user()`
```

**Diseño original** (`RUP/02-diseño/casos-uso/abrirAulas/README.md:31`):
```markdown
*   **API**: Endpoint `GET /aulas` protegido (requiere token).
```

**Análisis original**: No se especifica mecanismo de protección, solo `AulasController` como coordinador.

**Impacto**: Dependency `get_current_user()` no diseñada, aparece directamente en implementación.

---

### Drift #3: **Paginación en abrirAulas sin diseño previo**

**Implementación** (`RUP/03-desarrollo/casos-uso/abrirAulas/README.md:38-40`):
```markdown
**Query Params:**
- `skip` (optional): Número de registros a saltar (default: 0)
- `limit` (optional): Número máximo de registros a retornar (default: 100)
```

**Requisitos original** (`RUP/00-casos-uso/02-detalle/abrirAulas/README.md`): No se menciona paginación. Solo se especifica "presenta lista de aulas".

**Análisis original**: No se menciona paginación en `AulaRepository.obtenerTodos()`.

**Impacto**: Funcionalidad de paginación agregada en implementación sin diseño upstream.

---

### Drift #4: **exclude_unset=True en editarAula sin diseño**

**Implementación** (`RUP/03-desarrollo/casos-uso/editarAula/README.md:107`):
```python
return repo.update(aula, aula_data.dict(exclude_unset=True))
```

**Diseño original** (`RUP/02-diseño/casos-uso/editarAula/README.md:32`):
```markdown
*   Uso de `AulaUpdate` schema (campos opcionales si se desea PATCH, obligatorios si es PUT completo).
```

**Impacto**: Mecanismo específico de Pydantic (`exclude_unset`) no diseñado, aparece en implementación.

---

### Drift #5: **Dialog de confirmación en eliminarAula sin diseño**

**Implementación** (`RUP/03-desarrollo/casos-uso/eliminarAula/README.md:116-132`):
```tsx
<Dialog open={deleteDialogOpen} onClose={() => setDeleteDialogOpen(false)}>
  <DialogTitle>Confirmar Eliminación</DialogTitle>
  <DialogContent>
    <DialogContentText>
      ¿Estás seguro de que deseas eliminar el aula "{aulaToDelete?.nombre}"?
      Esta acción no se puede deshacer.
    </DialogContentText>
  </DialogContent>
  ...
</Dialog>
```

**Diseño original** (`RUP/02-diseño/casos-uso/eliminarAula/README.md:25-26`):
```markdown
*   **Frontend**: Botón de eliminación con confirmación.
```

**Impacto**: Detalle de implementación (Dialog específico de Material-UI) no diseñado.

---

## 🟠 INCONSISTENCIAS DE NOMBRES

### 1. **Endpoint /token → /auth/login**

- **Diseño** (`RUP/02-diseño/casos-uso/iniciarSesion/README.md:26`): `*   **API (FastAPI)**: Endpoint `/token` que recibe `OAuth2PasswordRequestForm`.`
- **Implementación** (`RUP/03-desarrollo/casos-uso/iniciarSesion/README.md:30`): `#### POST `/api/v1/auth/login``

**Impacto**: Nombre de endpoint diferente. `/token` es estándar OAuth2, pero se cambió a `/auth/login`.

---

### 2. **AulaList → AulasPage**

- **Diseño** (`RUP/02-diseño/casos-uso/abrirAulas/README.md:25`): `*   **Frontend**: Componente `AulaList` que consume la API.`
- **Implementación** (`RUP/03-desarrollo/casos-uso/abrirAulas/README.md:80`): `- **Página**: `frontend/src/pages/AulasPage.tsx``

**Impacto**: Nombre de componente diferente (`AulaList` vs `AulasPage`).

---

### 3. **AulaForm vs Dialog**

- **Diseño** (`RUP/02-diseño/casos-uso/crearAula/README.md:25`): `*   **Frontend**: Formulario `AulaForm` (modo creación).`
- **Implementación** (`RUP/03-desarrollo/casos-uso/crearAula/README.md:118-122`): `<Dialog open={openDialog} onClose={handleCloseDialog}>`

**Impacto**: No existe componente `AulaForm`. Se usa `Dialog` directamente con `TextField`.

---

## 💡 RECOMENDACIONES DE PROCESO

### 1. **ESTABLECER CHECKPOINT DE TRAZABILIDAD**

**Problema**: Decisiones de implementación (paginación, get_current_user) no se documentaron upstream.

**Solución**:
```markdown
## Template de Checklist de Trazabilidad

Antes de marcar un caso de uso como "Completado":

### Requisitos → Análisis
- [ ] Todas las conversaciones actor-sistema están en diagrama de colaboración
- [ ] Todos los estados del caso de uso tienen clases responsables

### Análisis → Diseño
- [ ] Todas las clases de análisis tienen clases de diseño correspondientes
- [ ] Todos los mensajes de colaboración tienen endpoints/secuencia

### Diseño → Desarrollo
- [ ] Todos los participantes del diagrama de secuencia existen en código
- [ ] Todos los endpoints diseñados están implementados
- [ ] Todos los métodos diseñados están implementados

### Feedback Loop
- [ ] Si se agrega funcionalidad NO diseñada → Actualizar Diseño primero
- [ ] Si se cambia flujo diseñado → Documentar razón en Desarrollo
```

---

### 2. **PROHIBIR IMPLEMENTAR SIN DOCUMENTO DE DISEÑO**

**Problema**: editarAula y eliminarAula se implementaron sin documentos de Requisitos/Análisis.

**Solución**:
```markdown
## REGLA DE ORO DEL PROYECTO

**NO se escribe código sin tener TODOS los documentos upstream:**

1. ✅ Requisitos (Detalle + Prototipo)
2. ✅ Análisis (Diagrama de colaboración)
3. ✅ Diseño (Diagrama de secuencia + Decisiones)
4. ✅ Desarrollo (Implementación)

**Excepción**: Solo para "spikes" técnicos (máximo 4 horas de código)
```

---

### 3. **ACTUALIZAR DISEÑO CUANDO SURJAN DRIFTS**

**Problema**: Funcionalidad implementada (paginación, get_current_user) no actualizó diseño.

**Solución**:
```markdown
## Protocolo de "Feedback Inmediato"

Cuando se implementa algo NO diseñado:

1. **PAUSA**: Detener implementación
2. **DOCUMENTAR**: Agregar al documento de Diseño:
   ```markdown
   ## Ajuste de Diseño (Decidido durante Implementación)

   ### Fecha: 2025-11-XX
   ### Decisión: Agregar paginación a abrirAulas()

   ### Razón:
   - Lista de aulas puede crecer indefinidamente
   - Necesario limitar registros retornados

   ### Diseño actualizado:
   - Query params: `skip` (int), `limit` (int)
   - Repository: `get_all(skip, limit)`
   - Service: `listar_aulas(skip, limit)`
   ```
3. **VALIDAR**: Revisar con equipo/designer
4. **CONTINUAR**: Retomar implementación
```

---

### 4. **UNIFICAR VOCABULARIO ENTRE DISCIPLINAS**

**Problema**: Inconsistencias de nombres (AulaList vs AulasPage, /token vs /auth/login).

**Solución**:
```markdown
## Glosario Técnico del Proyecto

Mantener un archivo `glosario.md` con:

### Backend
- **Endpoint de login**: `/api/v1/auth/login` (no `/token`)
- **Componente frontend**: `AulasPage` (no `AulaList`)
- **Formulario**: Reutilizar `Dialog` con `TextField` (no crear `AulaForm`)

### Reglas de nombres
- **Endpoints**: `/api/v1/{recurso}/{accion}` (ej: `/api/v1/auth/login`)
- **Componentes React**: `{Recurso}Page` (ej: `AulasPage`, `LoginPage`)
- **Servicios**: `{Recurso}Service` (ej: `AulaService`)
- **Repositorios**: `{Recurso}Repository` (ej: `AulaRepository`)
```

---

### 5. **ESPECIFICAR "FILOSOFÍA DE INTERACCIÓN" EN DISEÑO**

**Problema**: Filosofía "el delgado" de crearAula se perdió entre Análisis y Diseño.

**Solución**:
```markdown
## Nueva sección en Documento de Diseño

### Filosofía de Interacción de Usuario

**Para crearAula():**

#### Patrón: "El Delgado" (Create→Update)
- **Paso 1 (Crear)**: Formulario mínimo con 3 campos:
  - `nombre` (string, requerido)
  - `capacidad` (int, requerido)
  - `especial` (bool, opcional)
- **Paso 2 (Redirección automática)**: Tras creación exitosa:
  - Redirigir a edición completa
  - Abrir formulario con todos los campos
  - Permitir completar información opcional

#### Diferencia con crearEdificio():
- crearEdificio(): Formulario completo de una sola vez
- crearAula(): "El delgado" con transferencia automática

#### Razón:
- Minimizar fricción en alta frecuencia de creación
- Aulas se crean más frecuentemente que edificios
```

---

### 6. **INTEGRAR PRUEBAS CON TRAZABILIDAD** (Gemini - 💡 Innovador)

**Problema**: Las pruebas solo validan funcionalidad, no conformidad con diseño.

**Solución**:
```markdown
## Protocolo de "Tests que Verifican Diseño"

### Tests de traza Requisitos → Implementación

**Para cada caso de uso, crear tests que verifiquen:**

1. **Test de campos del modelo**:
   ```python
   def test_aula_tiene_campos_requisitos():
       """Verifica que Aula tenga todos los campos especificados en Requisitos"""
       campos_requeridos = ['codigo', 'nombre', 'capacidad', 'especial', 'bloqueada', 'id_edificio']
       for campo in campos_requeridos:
           assert hasattr(Aula, campo), f"Campo {campo} especificado en requisitos no existe"
   ```

2. **Test de endpoints diseñados**:
   ```python
   def test_endpoint_login_coincide_diseno():
       """Verifica que endpoint existe según Diseño"""
       response = client.post("/api/v1/auth/login", data={...})
       assert response.status_code == 200
       # Nota: Diseño decía /token, se cambió a /auth/login - debe documentarse
   ```

3. **Test de seguridad**:
   ```python
   def test_endpoints_crud_protegidos():
       """Verifica que TODOS los endpoints de CRUD tienen JWT"""
       endpoints = [
           ("GET", "/api/v1/aulas/"),
           ("POST", "/api/v1/aulas/"),
           ("PATCH", "/api/v1/aulas/1"),
           ("DELETE", "/api/v1/aulas/1"),
       ]
       for method, endpoint in endpoints:
           response = client.request(method, endpoint)
           assert response.status_code == 401, f"Endpoint {endpoint} no está protegido"
   ```

4. **Test de filosofía de interacción**:
   ```python
   def test_crear_aula_filosofia_delgado():
       """Verifica que crearAula sigue filosofía C→U de Requisitos"""
       # Paso 1: Crear con datos mínimos
       response = client.post("/api/v1/aulas/", json={
           "codigo": "A101",
           "nombre": "Aula 101",
           "id_edificio": 1
       })
       assert response.status_code == 201
       aula_id = response.json()["id"]

       # Paso 2: Verificar que redirige a edición
       # (o que API permite actualizar inmediatamente)
       response = client.patch(f"/api/v1/aulas/{aula_id}", json={
           "capacidad": 30
       })
       assert response.status_code == 200
   ```

### Benefits:
- **Automatiza verificación de trazabilidad**
- **Detecta gaps cuando se implementan features sin diseñar**
- **Valida que lo diseñado realmente se implementó**
- **Sirve como documentación viva del comportamiento esperado**
```

---

### 7. **VALIDACIÓN DE SUPUESTOS** (Gemini)

**Problema**: "Supuestos no documentados en fases posteriores" (ej: la seguridad de endpoints).

**Solución**:
```markdown
## Checklist de "No Suponer, Verificar"

Antes de marcar "Completado":

### Verificación de Supuestos Comunes
- [ ] ¿Asumí que X existe sin verificar en Diseño?
- [ ] ¿Asumí que el endpoint está protegido sin agregar `Depends(get_current_user)`?
- [ ] ¿Asumí que el campo existe en el modelo sin verificar en Requisitos?
- [ ] ¿Asumí que el flujo es Y sin leer el documento de Análisis?

### Protocolo de Verificación
1. **Leer** documento de Diseño ANTES de implementar
2. **Listar** todos los supuestos que estoy haciendo
3. **Verificar** cada supuesto contra Diseño/Requisitos
4. **Documentar** supuestos que no coinciden
```

---

## 🎯 CONCLUSIÓN (ACTUALIZADA)

### Objetivo pedagógico: **CUMPLIDO AL 60-65%**

**Lo que funcionó** ✅:
- **Req→Aná funciona perfecto**: 100% de alineación en esta transición
- RUP permitió construir sobre una base arquitectónica definida
- Arquitectura Layered se respetó 100%
- Tecnologías seleccionadas se aplicaron consistentemente
- Nombres de componentes principales son trazables

**Lo que NO funcionó** ❌:
- **Dis→Dev está rota**: 0% de alineación promedio (hallazgo CRÍTICO de Gemini)
- "Ajustarse conforme se construye" significó "cortocircuitar disciplinas"
- Filosofía de interacción ("el delgado") se perdió en traducción
- Decisiones de implementación no documentaron upstream
- 2 casos de uso se implementaron sin Requisitos/Análisis
- **Seguridad diseñada no implementada**: El problema más grave

---

### Lección aprendida

**RUP SÍ permite construir sobre base arquitectónica**, PERO requiere:

1. **Disciplina estricta** de no implementar sin diseño completo
2. **Feedback loops inmediatos** cuando surgen desviaciones
3. **Vocabulario unificado** entre disciplinas
4. **Revisión cruzada** para detectar gaps early

---

### Estado general: 🟡 **NECESITA MEJORAS DE PROCESO**

La trazabilidad existe pero es **parcial (68%)**. El proyecto demostró que RUP funciona para arquitectura, pero el proceso de "ajuste conforme se construye" necesita más rigor para evitar cortocircuitos.

---

### Valor de las 4 Auditorías

**Qwen Code (98%)**: Demasiado optimista, sirvió como "upper bound" teórico. ❌ No leyó profundamente.

**Codex (50%)**: Demasiado pesimista, sirvió como "lower bound" pesimista. ⚠️ Preciso pero falta matices.

**Claude Sonnet (68%)**: Más balanceado, sirvió como "realidad" con análisis detallado. ✅ Mejor análisis general.

**Gemini (63.6%)**: Balanceado con **mejor análisis por transición**. ✅✅ **Descubrió que Dis→Dev = 0%** (crítico).

**Aportes únicos de Gemini**:
1. **Análisis por transición**: Req→Aná (100%) vs Aná→Dis (?) vs Dis→Dev (0%)
2. **Breakdown por campo**: Dice exactamente QUÉ campos faltan
3. **Integridad referencial**: Menciona validación de dependencias en eliminarAula
4. **Distribución de lógica**: Detecta mapeo IniciarSesionController → AuthService → routers
5. **Tests con trazabilidad**: Tests que verifican conformidad con diseño (innovador)
6. **Actualización bidireccional**: No solo aguas abajo, sino también aguas arriba

**La verdad está somewhere in the middle**: 60-70% de alineación es razonable para una primera iteración, pero **el problema real es que Dis→Dev está roto (0%)**.

---

### Próximos pasos (actualizados con Gemini)

1. **CRÍTICO - Reparar Dis→Dev**:
   - Implementar JWT en TODOS los endpoints de aulas (diseño lo especificaba)
   - Agregar campo `código` al modelo (requisito lo especificaba)
   - Implementar filosofía "el delgado" en crearAula (requisitos lo especificaban)

2. **Antes de Iteración 2**:
   - Resolver deudas técnicas críticas (JWT en endpoints, SECRET_KEY, import Optional)
   - Crear tests que verifiquen trazabilidad (recomendación de Gemini)

3. **Durante Iteración 2**:
   - Aplicar estrictamente "Regla de Oro" (no código sin diseño)
   - **Actualizar documentación bidireccionalmente** (recomendación de Gemini): Si implementación se desvía, actualizar Diseño/Análisis
   - **Validar supuestos** (recomendación de Gemini): No asumir, verificar contra Diseño

4. **Después de cada caso de uso**:
   - Pasar checklist de trazabilidad
   - Ejecutar tests de conformidad con diseño
   - Verificar que Dis→Dev > 90% de alineación
   - Revisión cruzada: Otra persona revisa alineación antes de marcar "Completado"

**RUP funcionó para estructura y Req→Aná**, PERO:
- ❌ **Dis→Dev está roto (0%)** - este es el problema principal
- ❌ "Ajustarse conforme se construye" = "cortocircuitar disciplinas"
- ✅ **Se puede arreglar** con proceso + disciplina + tests de trazabilidad

**Lección de Gemini**: El problema NO está en las primeras transiciones (Req→Aná funciona perfecto), **el problema está en la última transición (Dis→Dev)**. Eso se corrige con:
1. Verificación de implementación contra diseño
2. Tests que validan conformidad con diseño
3. Actualización bidireccional de documentación
4. Disciplina de no "suponer"
