# Extracción de BD Access 2.0 y validación de coherencia dominio-tablas

<div align=right>

|||||
|-|-|-|-|
|[🏠️](../README.md)|**Artículo**|[Contexto](contexto.md)|[Evidencia](evidencia.md)|

</div>

## Resumen

Este artículo documenta la extracción de la base de datos Access 2.0 del sistema legacy SigHor (1998), la validación de coherencia entre el modelo del dominio conceptual y la estructura física de tablas, y las implicaciones para la selección del motor de base de datos transversal a todos los stacks tecnológicos del proyecto pySigHor.

**Contexto del problema**: Para proceder con la fase de Implementación, se requiere documentar la estructura exacta de la base de datos original. Sin embargo, el formato Access 2.0 (1997) es incompatible con herramientas modernas de extracción.

**Solución aplicada**: Uso de máquina virtual Windows 98 para extracción nativa, generación de documentación estructurada y validación de coherencia modelo del dominio ↔ estructura de tablas.

## ¿Por qué?

### Necesidad de estructura física antes de implementación

La fase de Diseño había establecido las entidades y sus relaciones desde una perspectiva conceptual (modelo del dominio RUP). Para proceder a la implementación en cualquiera de los stacks tecnológicos (Spring/Angular, FastAPI/React, CLI variants), se requiere:

1. **Estructura exacta de campos**: Tipos, tamaños, restricciones
2. **Relaciones explícitas**: Claves foráneas y cardinalidades
3. **Índices y restricciones**: Consultas SQL originales y optimizaciones
4. **Validación de coherencia**: Confirmar que el modelo conceptual mapea correctamente a la estructura física

### Desafío técnico: Access 2.0 incompatible

**El problema**: `mdbtools` y otras herramientas modernas no pueden abrir archivos Access 2.0, un formato anterior a Access 95/97.

**Por qué importa**: Sin acceso a la estructura interna, cualquier implementación moderna sería una adivinanza basada en el código VB3.0, con riesgo de:
- Omisión de campos críticos
- Tipos de datos incorrectos
- Relaciones no identificadas
- Consultas mal optimizadas

## ¿Qué?

### Metodología de extracción

#### Paso 1: Máquina Virtual Windows 98

<div align=center>

|![Proceso de extracción](/images/extraDocs/019-extraccion-bd-access-coherencia-dominio/extraction-process.svg)|
|:-:|
|Proceso de extracción desde Access 2.0 ([extraction-process.puml](extraction-process.puml))|

</div>

**Archivos generados**:
- `AAA-documentacion` - Documentación completa en formato .prn (printer output)
- `M_Aulas.xls`, `M_Cursos.xls`, etc. - Exportación XLS de cada tabla
- `SQLs.txt` - Consultas SQL del sistema

#### Paso 2: Procesamiento de documentación .prn

El formato .prn contiene control characters legacy pero estructura tabular consistente:

```
Table: M_Aulas
Field Name     Type      Size      Description
─────────────  ──────    ──────    ──────────────
ID             Autoinc   4         Identificador único
Nombre         Text      50        Nombre del aula
Capacidad      Byte      1         Capacidad máxima
...
```

**Extracción sistemática**: Uso de `grep` y procesamiento de texto para generar:
- `estructura-bd-original.md` - Documentación estructurada completa
- `er-diagram.puml` - Diagrama Entidad-Relación con atributos
- `er-diagram-simple.puml` - Diagrama simplificado sin atributos

### Resultados de la extracción

#### Tablas identificadas

<div align=center>

|Tipo|Prefijo|Tablas|Propósito|
|-|-|-|-|
|**Maestras**|M_|M_Aulas, M_Cursos, M_Profesores, M_Horario, M_DatosGenerales|Entidades principales del dominio|
|**Relación**|R_|R_ProfesorCurso|Muchos-a-Muchos profesores↔cursos|
|**Secundarias**|S_|S_CursosHModificado, S_AulaOcupada|Control de modificaciones y ocupación|
|**Temporales**|T_|T_PreHorario, T_AulaLibre, T_Dias, T_Horas|Algoritmo de generación|

</div>

#### Campos críticos identificados

**M_Aulas**:
- `Propiedades` (Integer) - Bitmask de 5 bits para recursos
- `Capacidad` (Byte) - 0-255 estudiantes
- `Especial`, `Bloqueada` (Yes/No) - Flags de estado

**M_Profesores**:
- `R1, R2, R3, R4, R5` (Integer) - Prioridades de recursos para algoritmo de optimización

**M_Cursos**:
- `H` (Text, 2) - Bloque horario (1-8, E, V)
- `PI, PS, PC, PE` (Yes/No) - Flags de tipo de programa

## ¿Para qué?

### Validación de coherencia modelo del dominio ↔ estructura física

#### Insight metodológico clave

> **"El modelo del dominio casi que te da la estructura de tablas"**

En sistemas de 1998, no existía separación artificial entre análisis y persistencia. Las **entidades del análisis** identificadas mediante RUP **eran directamente las tablas de la base de datos**.

#### Correspondencia 1:1 validada

<div align=center>

|Concepto (Modelo del Dominio)|Tabla (BD Access 2.0)|Coherencia|
|-|-|-|
|Aula|M_Aulas|✅ 100%|
|Curso|M_Cursos|✅ 100%|
|Profesor|M_Profesores|✅ 100%|
|Horario|M_Horario|✅ 100%|
|BloqueHorario|Campo `H` en M_Cursos|✅ Embebido como atributo|
|Edificio|FK `IDEdificio` en M_Aulas|✅ Embebido como referencia|
|Programa|Campo `Programa` en M_Cursos|✅ Embebido como atributo|
|Recurso|Bitmask `Propiedades` en M_Aulas + `R1-R5` en M_Profesores|✅ Embebido como preferencias|

</div>

#### Diferencia importante: Entidades de análisis vs Tablas

<div align=center>

|![Evolución: Clases de análisis vs Tablas](/images/extraDocs/019-extraccion-bd-access-coherencia-dominio/evolucion-analisis-tablas.svg)|
|:-:|
|Evolución: Clases de análisis RUP ↔ Tablas BD ([evolucion-analisis-tablas.puml](evolucion-analisis-tablas.puml))|

</div>

**Implicación**: En modernización, debemos separar lo que estaba embebido:
- `BloqueHorario` como valor en `M_Cursos.H` → Entidad propia con lookup
- `Edificio` como FK en `M_Aulas.IDEdificio` → Entidad propia
- `Recurso` como bitmask → Sistema de preferencias normalizado

### Preparación para decisión de motor de base de datos

#### Requisito de transversalidad

<div align=center>

|![Base de datos transversal](/images/extraDocs/019-extraccion-bd-access-coherencia-dominio/bd-transversal-stacks.svg)|
|:-:|
|Base de datos transversal a todos los stacks ([bd-transversal-stacks.puml](bd-transversal-stacks.puml))|

</div>

**Criterios de selección**:

<div align=center>

|Criterio|Descripción|Importancia|
|-|-|-|
|Soporte multi-stack|Compatible con Java, Python, CLI|- ALTO|
|SQL estándar|Evitar vendor lock-in|- ALTO|
|Migración desde Access 2.0|Herramientas de conversión|- MEDIO|
|Despliegue simple|Docker, cloud, on-premise|- MEDIO|
|Costo|Open source preferido|- BAJO (si existe opción gratuita)|

</div>

## ¿Cómo?

### Proceso técnico de extracción

#### 1. Preparación de entorno

```bash
# VM Windows 98 con Access 2.0 instalado
# Montaje de HOR_UDEP.MBD desde host

# En Access 2.0:
Tools → Database Utilities → Documentor
→ Select All Tables
→ Output: Text File (AAA-documentacion.prn)

# Exportación individual de cada tabla:
File → Save As/Export → To External File
→ Format: Excel 3.0/4.0 (.xls)
```

#### 2. Procesamiento de archivos

```bash
# En host Linux moderno
cd src/DATOS/datosExportados

# Extracción de estructura desde .prn
grep -A 20 "Table: M_Aulas" AAA-documentacion

# Generación de documentación estructurada
# (proceso manual de parseo a formato Markdown)

# Generación de diagramas PlantUML
# (manual, basado en relaciones extraídas)
```

#### 3. Validación de coherencia

```bash
# Comparación modelo del dominio vs BD
diff RUP/00-casos-uso/00-modelo-del-dominio/ \
     src/DATOS/datosExportados/estructura-bd-original.md

# Resultado: Correspondencia 1:1 confirmada
```

### Lecciones aprendidas

#### Sobre Access 2.0

- **Formato propietario obsoleto**: Herramientas modernas no lo soportan
- **VM con SO nativo**: Única solución viable para extracción fidedigna
- **Documentación interna**: Access incluía herramienta de documentación útil

#### Sobre sistemas legacy

- **Modelo del dominio ≡ Estructura BD**: Correspondencia directa en 1998
- **Embebimiento de conceptos**: BloqueHorario, Edificio como campos FK, no entidades
- **Optimizaciones específicas**: Bitmask para recursos (ahorro de espacio en 1998)

#### Sobre modernización con RUP

- **Normalización necesaria**: Lo que estaba embebido debe separarse
- **Flexibilidad vs fidelidad**: Decidir qué patrones legacy preservar vs modernizar
- **Transversalidad de BD**: Una sola BD para todos los stacks
- **Análisis RUP intacto**: Nuestras clases de análisis ya nos habían dado la estructura

## Decisión pendiente: Motor de base de datos

### Opciones evaluadas

<div align=center>

|Motor|Ventajas|Desventajas|Stacks compatibles|
|-|-|-|-|
|**PostgreSQL**|Open source, SQL estándar, maduro|Requiere setup|Todos|
|**H2**|Embeddable, Java native|No para multi-stack|Spring/Angular solo|
|**SQLite**|Archivo único, zero-config|Concurrencia limitada|CLI / desarrollo|
|**MySQL/MariaDB**|Muy popular|Licensing histórico|Todos|
|**HSQLDB**|Java puro, embeddable|No para multi-stack|Spring/Angular solo|

</div>

### Recomendación metodológica

**Para fase de experimentación (Diseño → Implementación)**:
- **H2 (Spring/Angular)** + **SQLite (FastAPI/React)** + **SQLite (CLI)**

**Ventajas**:
- Zero-config para desarrollo rápido
- Cada stack usa lo nativo de su ecosistema
- Esquema idéntico permite migrar posteriormente

**Para fase de producción**:
- **PostgreSQL** como motor unificado

**Ventajas**:
- Transversal real a todos los stacks
- SQL estándar evita vendor lock-in
- Herramientas de migración maduras
- Soporte empresarial

## Conclusión

### Resultados obtenidos

1. **Estructura completa documentada**: 12 tablas con campos, tipos, relaciones
2. **Coherencia validada**: Modelo del dominio ↔ estructura BD Access 2.0 confirmada
3. **Artefactos generados**: Documentación estructurada + DERs PlantUML
4. **Insight metodológico**: En sistemas legacy 1998, entidad ≡ tabla

### Próximos pasos

1. **Decisión de motor**: Seleccionar PostgreSQL para fase de producción
2. **Migración de esquema**: Convertir tipos Access 2.0 → tipos modernos
3. **Normalización**: Separar conceptos embebidos (BloqueHorario, Edificio)
4. **Implementación paralela**: Validar que schema funciona en todos los stacks

### Lección transferible

**Para proyectos de modernización legacy con RUP**:

> La estructura de la base de datos original es el **eslabón perdido** entre el análisis de objetos y la implementación moderna. Sin ella, cualquier diseño es una adivinanza. Con ella, validamos que nuestras **clases de análisis RUP** son correctas y podemos proceder con confianza a la implementación multi-stack.

**El patrón "entidades de análisis ≡ tablas"** es típico de sistemas desktop legacy previos a la proliferación de ORMs. Reconocer este patrón acelera significativamente la modernización, pues el análisis RUP ya nos había dado la estructura de persistencia sin necesidad de capas adicionales.

## Referencias

- [Artículo 000: Ingeniería inversa del sistema SigHor](/extraDocs/000-ingenieria-inversa/)
- [Modelo del dominio](/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md)
- [Estructura BD original](/src/DATOS/datosExportados/estructura-bd-original.md)
- [DER completo](/src/DATOS/datosExportados/er-diagram.puml)
- [DER simplificado](/src/DATOS/datosExportados/er-diagram-simple.puml)
- [Documentación Access 2.0](/src/DATOS/datosExportados/AAA-documentacion)

---

<div align=right>

**Artículo 019** - Extracción de BD Access 2.0 y validación de coherencia
Fecha: 21 de enero de 2026
pySigHor - Sistema generador de horarios

</div>
