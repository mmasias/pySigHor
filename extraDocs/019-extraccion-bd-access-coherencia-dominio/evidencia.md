# Evidencia - Artículo 019

## Artefactos creados

### Documentación de estructura de base de datos

|Artefacto|Ubicación|Descripción|
|-|-|-|
|Estructura BD|[`estructura-bd-original.md`](/src/DATOS/datosExportados/estructura-bd-original.md)|Documentación completa de 12 tablas con campos, tipos, relaciones|
|DER completo|[`er-diagram.puml`](/src/DATOS/datosExportados/er-diagram.puml)|Diagrama Entidad-Relación con atributos completos|
|DER simplificado|[`er-diagram-simple.puml`](/src/DATOS/datosExportados/er-diagram-simple.puml)|DER simplificado sin atributos|

### Archivos fuente extraídos

|Archivo|Ubicación|Origen|
|-|-|-|
|AAA-documentacion|[`/src/DATOS/datosExportados/AAA-documentacion`](/src/DATOS/datosExportados/AAA-documentacion)|Documentación nativa de Access 2.0 (.prn)|
|SQLs.txt|[`/src/DATOS/datosExportados/SQLs.txt`](/src/DATOS/datosExportados/SQLs.txt)|Consultas SQL del sistema|
|*.xls|[`/src/DATOS/datosExportados/*.xls`](/src/DATOS/datosExportados/)|Exportación XLS de cada tabla|

## Tablas documentadas

### Tablas Maestras (M_)

|Tabla|Campos|Propósito|
|-|-|-|
|M_Aulas|7 campos|Recursos físicos de aulas|
|M_Cursos|14 campos|Asignaturas académicas|
|M_Profesores|7 campos|Docentes del sistema|
|M_Horario|5 campos|Resultado final de horarios|
|M_DatosGenerales|4 campos|Configuración del sistema|

### Tablas de Relación (R_)

|Tabla|Campos|Propósito|
|-|-|-|
|R_ProfesorCurso|2 campos|Asignación profesor-curso (M:N)|

### Tablas Secundarias (S_)

|Tabla|Campos|Propósito|
|-|-|-|
|S_CursosHModificado|2 campos|Cambios de bloque horario|
|S_AulaOcupada|1 campo|Control de ocupación|

### Tablas Temporales (T_)

|Tabla|Campos|Propósito|
|-|-|-|
|T_PreHorario|3 campos|Asignaciones preliminares|
|T_AulaLibre|2 campos|Cálculo de optimización|
|T_Dias|3 campos|Tabla de referencia de días|
|T_Horas|2 campos|Tabla de referencia de horas|

## Campos críticos identificados

### M_Aulas - Bitmask de recursos

```
Propiedades (Integer, 2 bytes)
├── Bit 0: Recurso 1
├── Bit 1: Recurso 2
├── Bit 2: Recurso 3
├── Bit 3: Recurso 4
└── Bit 4: Recurso 5
```

**Uso en algoritmo**: `EnteroDelAula = Σ Propiedad(i) * 2^Ri`

### M_Profesores - Prioridades de recursos

```
R1, R2, R3, R4, R5 (Integer, 2 bytes cada uno)
```

**Función**: Pesos para cálculo de coincidencia de recursos

### M_Cursos - Bloque horario

```
H (Text, 2 caracteres)
Valores: "1", "2", "3", "4", "5", "6", "7", "8", "E", "V"
```

**Correspondencia**: H1-H8 bloques principales, HE especiales, HV varios

## Validación de coherencia

### Modelo del dominio ↔ Estructura BD

```
┌─────────────────────┐         ┌─────────────────────┐
│ Modelo del Dominio  │         │ Estructura BD       │
│ (RUP conceptual)    │         │ (Access 2.0 física) │
├─────────────────────┤         ├─────────────────────┤
│ Aula                │   ↔     │ M_Aulas             │
│ Curso               │   ↔     │ M_Cursos            │
│ Profesor            │   ↔     │ M_Profesores        │
│ Horario             │   ↔     │ M_Horario           │
│ BloqueHorario       │   ↔     │ Campo H en M_Cursos │
│ Edificio            │   ↔     │ FK IDEdificio       │
│ Programa            │   ↔     │ Campo Programa      │
│ Recurso             │   ↔     │ Bitmask + R1-R5     │
└─────────────────────┘         └─────────────────────┘
```

**Resultado**: ✅ Coherencia 1:1 validada

## Mapeo de tipos Access 2.0 → Tecnologías modernas

|Access 2.0|Spring Boot/JPA|TypeScript|Python|
|-|-|-|-|
|Autoincremental (Long)|`@GeneratedValue @Id Long`|`number`|`int` (autoincrement)|
|Text (50)|`@Column(length=50) String`|`string`|`String(max_length=50)`|
|Numérico (Byte)|`@Column Integer`|`number`|`SmallInteger`|
|Numérico (Integer)|`@Column Integer`|`number`|`Integer`|
|Yes/No|`@Column Boolean`|`boolean`|`Boolean`|
|Double|`@Column Double`|`number`|`Float`|

## Consultas SQL originales

|Consulta|Propósito|
|-|-|
|C_CursosIgualH|Cursos filtrados por bloque H con modificaciones|
|C_CursosIgualHIgualC|Cursos por H y Ciclo|
|C_CursosPorPartir|Cursos con >145 vacantes (requieren dividirse)|
|C_HMaximo|Máximo bloque H usado|
|C_ProfesorCurso|Obtiene preferencias R1-R5 del profesor de un curso|
|Horario Final|Reporte principal del horario generado|

## Diagramas generados

### DER completo (er-diagram.puml)
- Entidades con todos los atributos
- Relaciones con cardinalidades
- Leyenda de tipos de datos Access 2.0
- Color coding por tipo de tabla

### DER simplificado (er-diagram-simple.puml)
- Solo entidades y relaciones
- Validación visual de estructura
- Comparación con modelo del dominio

## Criterios para decisión de motor BD

### Requisitos identificados

1. **Transversalidad**: Debe funcionar con Java, Python, CLI
2. **SQL estándar**: Evitar vendor lock-in
3. **Migración**: Herramientas desde Access 2.0
4. **Despliegue**: Docker, cloud, on-premise

### Opciones evaluadas

|Motor|Multi-stack|SQL estándar|Migración|Recomendación|
|-|-|-|-|-|
|PostgreSQL|✅|✅|✅|Producción|
|H2|❌ (Java only)|✅|N/A|Desarrollo Spring|
|SQLite|✅|Limitado|✅|Desarrollo FastAPI/CLI|
|MySQL/MariaDB|✅|Casi estándar|✅|Alternativa|

## Referencias a commits

**Estado actual**: Commit pendiente
Los artefactos de documentación y diagramas están listos para ser commiteados a la rama `main` o `xRevisar` según protocolo del proyecto.
