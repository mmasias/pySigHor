# Contexto - Artículo 019

## Estado del proyecto

### Fecha
21 de enero de 2026

### Fase RUP actual
**Transición**: Diseño (02) → Desarrollo (03)

### Situación específica

El proyecto se encontraba en un punto crítico de transición hacia la fase de implementación:

1. **Fase de Análisis completada**: 32 casos de uso con análisis MVC completo
2. **Diseño multi-stack iniciado**: Casos de uso de aulas diseñados en Spring/Angular y FastAPI/React
3. **Modelo del dominio establecido**: Entidades y relaciones conceptuales validadas
4. **Pendiente**: Estructura física de base de datos para implementación

### Necesidad identificada

Antes de proceder con la implementación en cualquiera de los stacks tecnológicos, se requería:

- Documentar la estructura exacta de la base de datos original
- Validar coherencia entre modelo conceptual y estructura física
- Establecer criterios para selección del motor de base de datos transversal

## Artefactos relevantes previos

### Modelo del dominio
- **Ubicación**: `/RUP/00-casos-uso/00-modelo-del-dominio/`
- **Contenido**: Entidades conceptuales (Aula, Curso, Profesor, Horario, etc.)
- **Estado**: Completado y validado

### Documentación de ingeniería inversa
- **Ubicación**: `/extraDocs/000-ingenieria-inversa/reverseEngineering.md`
- **Contenido**: Análisis de alto nivel de estructura de datos
- **Limitación**: No incluye detalles de campos, tipos y relaciones

## Problema técnico encontrado

### Incompatibilidad de formato Access 2.0

Al intentar extraer la estructura de la base de datos `HOR_UDEP.MDB`:

```bash
$ mdb-tables HOR_UDEP.MDB
Error: Cannot open file format
```

**Causa**: Access 2.0 (formato de 1997) es anterior a Access 95/97 y no es soportado por herramientas modernas como `mdbtools`.

**Implicación**: No es posible documentar la estructura de la base de datos con herramientas contemporáneas.

## Solución aplicada

### Estrategia: VM Windows 98

El usuario decidió levantar una máquina virtual con Windows 98 y Access 2.0 nativo para realizar la extracción desde el entorno original.

**Artefactos generados**:

```
src/DATOS/datosExportados/
├── AAA-documentacion          # Documentación completa en formato .prn
├── M_Aulas.xls                # Exportación XLS de cada tabla
├── M_Cursos.xls
├── M_Profesores.xls
├── M_Horario.xls
├── M_DatosGenerales.xls
├── R_ProfesorCurso.xls
├── S_CursosHModificado.xls
├── S_AulaOcupada.xls
├── T_PreHorario.xls
├── T_AulaLibre.xls
├── T_Dias.xls
├── T_Horas.xls
├── SQLs.txt                   # Consultas SQL del sistema
└── ...
```

## Proceso de documentación

### 1. Extracción de información

Desde el archivo `AAA-documentacion` (formato .prn con control characters), se extrajo sistemáticamente:

- Nombres de tablas
- Campos con tipos y tamaños
- Relaciones y claves foráneas
- Índices

### 2. Estructuración de contenido

Se generaron tres artefactos principales:

|Artefacto|Propósito|Contenido|
|-|-|-|
|`estructura-bd-original.md`|Documentación completa|12 tablas con campos, tipos, relaciones|
|`er-diagram.puml`|DER completo|Entidades con atributos y relaciones|
|`er-diagram-simple.puml`|DER simplificado|Solo entidades y relaciones|

### 3. Validación de coherencia

Se comparó el modelo del dominio RUP con la estructura extraída:

|Concepto RUP|Tabla Access|Estado|
|-|-|-|
|Aula|M_Aulas|✅ Coherencia 1:1|
|Curso|M_Cursos|✅ Coherencia 1:1|
|Profesor|M_Profesores|✅ Coherencia 1:1|
|Horario|M_Horario|✅ Coherencia 1:1|
|BloqueHorario|Campo H en M_Cursos|✅ Embebido como atributo|
|Edificio|FK IDEdificio en M_Aulas|✅ Embebido como referencia|

## Conexión con artículos anteriores

### Artículo 000: Ingeniería inversa
Proporcionó el análisis inicial del sistema legacy, pero a nivel de algoritmo, no de estructura de base de datos detallada.

### Artículo 012: Fase de Análisis Completada
Estableció la base metodológica de modelos conceptuales ahora validados contra estructura física.

### Artículo 015: Dashboards multi-stack
Estableció la necesidad de una base de datos transversal a múltiples stacks tecnológicos.

## Decisión pendiente

Con la estructura documentada y la coherencia validada, la siguiente decisión crítica es:

**¿Qué motor de base de datos usar para todos los stacks?**

Opciones a evaluar:
- PostgreSQL (recomendado para producción)
- H2 (para Spring/Angular development)
- SQLite (para FastAPI/React y CLI development)

## Próximos pasos

1. Usuario genera SVGs desde archivos PlantUML
2. Decisión final sobre motor de base de datos
3. Creación de scripts de migración Access 2.0 → motor moderno
4. Validación de esquema en cada stack tecnológico
