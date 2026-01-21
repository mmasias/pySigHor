# Estructura de Base de Datos - HOR_UDEP.MDB (Access 2.0)

## Información del Artefacto

- **Sistema**: SigHor - Sistema Generador de Horarios (1998)
- **Motor**: Microsoft Access 2.0
- **Archivo**: `HOR_UDEP.MDB`
- **Fecha creación**: 20/11/1997 10:49:13
- **Última actualización**: 11/07/1998 04:24:15
- **Extracción**: 21/01/2026 desde Windows 98 VM

## Propósito

Este documento documenta la estructura completa de la base de datos original del sistema SigHor, extraída directamente del archivo Access mediante la herramienta de documentación de Access 2.0.

---

## Tablas de la Base de Datos

### Tablas Maestras (M_)

#### M_Aulas - Recursos físicos de aulas

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **ID** | Autoincremental (Long) | 4 | Identificador único (PK) |
| **Nombre** | Text | 50 | Nombre del aula |
| **Capacidad** | Numérico (Byte) | 1 | Capacidad máxima de estudiantes |
| **Propiedades** | Numérico (Integer) | 2 | Bitmask de recursos (5 bits) |
| **Especial** | Yes/No | 1 | Aula de uso especial |
| **Bloqueada** | Yes/No | 1 | Aula temporalmente no disponible |
| **IDEdificio** | Numérico (Long) | 4 | FK al edificio |

**Índices**:
- `NOMBRE` sobre campo Nombre

**Relaciones**:
- Uno a Muchos con `M_Horario` (IDAula)
- Uno a Muchos con `S_AulaOcupada` (IDAula)
- Uno a Muchos con `T_PreHorario` (IDAula)

---

#### M_Cursos - Asignaturas académicas

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **ID** | Autoincremental (Long) | 4 | Identificador único (PK) |
| **Nombre** | Text | 50 | Nombre de la asignatura |
| **Sigla** | Text | 4 | Código abreviado |
| **Programa** | Text | 10 | Programa académico |
| **Ciclo** | Numérico (Double) | 8 | Ciclo académico |
| **Creditos** | Numérico (Integer) | 2 | Créditos del curso |
| **H** | Text | 2 | Bloque horario (1-8, E, V) |
| **Vacantes** | Numérico (Integer) | 2 | Número de estudiantes |
| **Activo** | Yes/No | 1 | Curso activo en plan de estudios |
| **Laboratorio** | Yes/No | 1 | Requiere laboratorio |
| **PI** | Yes/No | 1 | Programa Inicial |
| **PS** | Yes/No | 1 | Programa Semi-Inicial |
| **PC** | Yes/No | 1 | Programa Completo |
| **PE** | Yes/No | 1 | Programa Especial |
| **ProfesorVisitante** | Yes/No | 1 | Asignado a profesor visitante |

**Relaciones**:
- Uno a Muchos con `M_Horario` (IDCurso)
- Uno a Muchos con `S_CursosHModificado` (IDCurso)
- Uno a Muchos con `R_ProfesorCurso` (IDCurso)

---

#### M_DatosGenerales - Configuración del sistema

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **IDClase** | Numérico (Byte) | 1 | Agrupador de configuración |
| **IDCorrelativo** | Numérico (Byte) | 1 | Orden dentro de la clase |
| **Elemento** | Text | 50 | Nombre del parámetro |
| **Descripcion** | Text | 200 | Valor/descripción |

**Índices**:
- Primary Key sobre `IDClase`, `IDCorrelativo`

---

#### M_Horario - Resultado final de horarios

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **ID** | Autoincremental (Long) | 4 | Identificador único (PK) |
| **Dia** | Text | 50 | Día de semana (L,M,X,J,V,S) |
| **Hora** | Numérico (Double) | 8 | Hora del día (7-12) |
| **IDAula** | Numérico (Long) | 4 | FK a M_Aulas |
| **IDCurso** | Numérico (Long) | 4 | FK a M_Cursos |

**Índices**:
- Primary Key sobre `ID`
- Índices sobre Dia, Hora, IDAula, IDCurso

**Relaciones**:
- Muchos a Uno con `M_Aulas` (IDAula)
- Muchos a Uno con `M_Cursos` (IDCurso)

---

#### M_Profesores - Docentes del sistema

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **ID** | Autoincremental (Long) | 4 | Identificador único (PK) |
| **Nombre** | Text | 50 | Nombre completo |
| **Oficina** | Text | 50 | Ubicación de oficina |
| **R1** | Numérico (Integer) | 2 | Prioridad recurso 1 |
| **R2** | Numérico (Integer) | 2 | Prioridad recurso 2 |
| **R3** | Numérico (Integer) | 2 | Prioridad recurso 3 |
| **R4** | Numérico (Integer) | 2 | Prioridad recurso 4 |
| **R5** | Numérico (Integer) | 2 | Prioridad recurso 5 |

**Notas**:
- R1-R5 representan las preferencias de recursos del profesor (pesos para optimización)
- Algoritmo usa: `EnteroDelAula = Σ Propiedad(i) * 2^Ri`

**Relaciones**:
- Uno a Muchos con `R_ProfesorCurso` (IDProfesor)

---

### Tablas de Relación (R_)

#### R_ProfesorCurso - Asignación profesor-curso

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **IDProfesor** | Numérico (Long) | 4 | FK a M_Profesores |
| **IDCurso** | Numérico (Long) | 4 | FK a M_Cursos |

**Relaciones**:
- Muchos a Uno con `M_Profesores`
- Muchos a Uno con `M_Cursos`

---

### Tablas Secundarias (S_)

#### S_AulaOcupada - Control de ocupación

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **ID** | Numérico (Long) | 4 | FK a M_Aulas (IDAula) |

---

#### S_CursosHModificado - Cambios de bloque horario

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **IDCurso** | Numérico (Long) | 4 | FK a M_Cursos |
| **NuevoH** | Text | 2 | Nuevo bloque horario |

---

### Tablas Temporales (T_)

#### T_PreHorario - Asignaciones preliminares

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **IDAula** | Numérico (Long) | 4 | FK a M_Aulas |
| **IDCurso** | Numérico (Long) | 4 | FK a M_Cursos |
| **H** | Text | 2 | Bloque horario asignado |

---

#### T_AulaLibre - Cálculo de optimización

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **ID** | Numérico (Long) | 4 | FK a M_Aulas |
| **Z** | Numérico (Integer) | 2 | Desperdicio de capacidad |

---

#### T_AulaOcupada - Control temporal

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **ID** | Numérico (Long) | 4 | Identificador |

---

#### T_Dias - Tabla de referencia de días

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **Dia** | Text | 50 | Nombre del día |
| **DiaCorto** | Text | 1 | Código corto (L,M,X,J,V,S) |
| **ID** | Numérico (Long) | 4 | Orden numérico |

---

#### T_Horas - Tabla de referencia de horas

| Campo | Tipo | Tamaño | Descripción |
|-------|------|--------|-------------|
| **Hora** | Numérico (Double) | 8 | Valor de hora |
| **ID** | Numérico (Long) | 4 | Orden numérico |

---

#### T_HorarioParaImprimir - Formato para reportes

Contiene los datos formateados para impresión de horarios.

---

## Consultas SQL del Sistema

El archivo `SQLs.txt` contiene las consultas principales:

| Consulta | Propósito |
|----------|-----------|
| `C_CursosIgualH` | Cursos filtrados por bloque H con modificaciones |
| `C_CursosIgualHIgualC` | Cursos por H y Ciclo |
| `C_CursosPorPartir` | Cursos con >145 vacantes (requieren dividirse) |
| `C_HMaximo` | Máximo bloque H usado |
| `C_ProfesorCurso` | Obtiene preferencias R1-R5 del profesor de un curso |
| `Horario Final` | Reporte principal del horario generado |

---

## Relaciones Entre Tablas (ER)

```
M_Profesores (1) ----< (N) R_ProfesorCurso >---- (1) M_Cursos
                                |
                                v
                           (1) M_Horario (N)
                                |
                                v
                           (1) M_Aulas

M_Cursos (1) ----< (N) S_CursosHModificado
M_Cursos (1) ----< (N) T_PreHorario
M_Aulas (1) ----< (N) S_AulaOcupada
```

---

## Notas Técnicas

1. **Access 2.0 (1997)**: Formato anterior a Access 95/97
2. **Codificación**: Windows-1252 (ANSI)
3. **Tamaños de campos**: Compactos para la época (Byte = 0-255)
4. **Relaciones**: Enforced con Cascade Updates/Deletes
5. **Índices**: Indexación sobre campos de búsqueda frecuente

---

## Mapeo a Tecnologías Modernas

| Access 2.0 | Spring Boot/JPA | TypeScript |
|------------|-----------------|------------|
| Autoincremental (Long) | `@GeneratedValue @Id Long` | `number` |
| Text (50) | `@Column(length=50) String` | `string` |
| Numérico (Byte) | `@Column Integer` | `number` |
| Numérico (Integer) | `@Column Integer` | `number` |
| Yes/No | `@Column Boolean` | `boolean` |
| Double | `@Column Double` | `number` |

---

## Fuente

- **Archivo original**: `src/DATOS/HOR_UDEP.MDB`
- **Documentación Access**: `datosExportados/AAA-documentacion`
- **SQLs del sistema**: `datosExportados/SQLs.txt`
- **Tablas exportadas**: `datosExportados/*.xls`
