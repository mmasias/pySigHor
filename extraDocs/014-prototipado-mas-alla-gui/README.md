# Artículo 014: Prototipado Más Allá de GUI

## contexto del artículo

**Problema identificado en contexto educativo:**
Los estudiantes asocian fuertemente el concepto de "prototipado" con wireframes y mockups de interfaces gráficas, lo cual limita su comprensión de lo que realmente significa **validar los puntos de contacto del sistema**.

**Objetivo del artículo:**
Expandir el concepto de prototipado para incluir **todos los tipos de interfaces** que un sistema puede exponer: APIs REST, CLIs, formatos de archivos, esquemas de mensajería, etc.

## el problema: sesgo hacia GUI

### percepción común del estudiante

```
Prototipado = Wireframes + Mockups
Interfaz = Pantallas visuales
```

Esta percepción genera:
- ✗ Incapacidad de prototipar sistemas backend-only
- ✗ Falta de validación temprana de contratos API
- ✗ Confusión al enfrentar arquitecturas headless
- ✗ Prototipos incompletos en proyectos reales

### origen del sesgo

1. **Material didáctico**: La mayoría de ejemplos en libros muestran solo GUI
2. **Herramientas populares**: Figma, Sketch, Adobe XD son para interfaces visuales
3. **Terminología**: "Interfaz de usuario" se interpreta como "interfaz gráfica"
4. **Experiencia personal**: Los estudiantes interactúan principalmente con GUIs

## definición correcta de prototipado

### principio fundamental

> **Prototipado es la validación temprana de CUALQUIER punto de contacto entre el sistema y el exterior, antes de invertir en implementación completa.**

### puntos de contacto del sistema

Un sistema puede exponerse mediante:

|Tipo de interfaz|¿Qué se prototipa?|¿Quién consume?|
|-|-|-|
|**GUI (Graphical User Interface)**|Wireframes, mockups|Usuarios humanos|
|**API REST**|Especificaciones HTTP/JSON|Aplicaciones cliente|
|**API GraphQL**|Esquemas + queries|Aplicaciones cliente|
|**CLI (Command Line Interface)**|Sintaxis de comandos|Usuarios técnicos|
|**SDK/Biblioteca**|Firmas de funciones|Desarrolladores|
|**Archivos**|Formato de datos (CSV, JSON, XML)|Sistemas externos|
|**Mensajería**|Esquemas de eventos|Sistemas distribuidos|
|**Base de datos**|Esquema de tablas|Aplicaciones que persisten|
|**WebSockets**|Protocolo de mensajes|Clientes en tiempo real|

## ejemplo aplicado: pySigHor

### contexto del sistema
SigHor es un sistema de generación de horarios universitarios que **podría modernizarse** con diferentes arquitecturas.

### escenarios de modernización

#### escenario 1: aplicación web monolítica
**Interfaz principal:** GUI web
**Prototipos necesarios:**
- ✓ Wireframes de pantallas (gestión de aulas, profesores, cursos)
- ✓ Flujos de navegación entre pantallas

#### escenario 2: arquitectura headless (frontend-backend separados)
**Interfaces principales:** GUI web + API REST
**Prototipos necesarios:**
- ✓ Wireframes de pantallas
- ✓ **Especificaciones de API REST** (endpoints, requests, responses)
- ✓ Contratos de autenticación JWT

#### escenario 3: API pública para integraciones
**Interfaz principal:** API REST pública
**Prototipos necesarios:**
- ✓ **Especificación OpenAPI completa**
- ✓ Documentación de endpoints
- ✓ Ejemplos de requests/responses
- ✓ Rate limiting y políticas de autenticación

#### escenario 4: herramienta CLI para administradores
**Interfaz principal:** Command Line
**Prototipos necesarios:**
- ✓ **Sintaxis de comandos** (`sighor generate --semester=2024-1`)
- ✓ Flags y parámetros
- ✓ Formato de output (tabla, JSON, CSV)
- ✓ Mensajes de error y ayuda

#### escenario 5: servicio de exportación de datos
**Interfaz principal:** Archivos generados
**Prototipos necesarios:**
- ✓ **Estructura de archivos JSON** con horarios generados
- ✓ Formato CSV para importación a Excel
- ✓ Esquema de datos para validación

## caso de estudio: abrirAulas()

El caso de uso `abrirAulas()` del proyecto pySigHor ilustra perfectamente esta dualidad.

### prototipo GUI (tradicional)

<div align=center>

![](/images/RUP/00-casos-uso/02-detalle/abrirAulas/abrirAulas-wireframe.svg)

</div>

**Valida:**
- Disposición visual de información
- Acciones disponibles del usuario
- Flujo de navegación

### prototipo API REST (complementario)

```http
GET /api/aulas?filtro=101
Authorization: Bearer {token}

Response 200 OK:
{
  "aulas": [
    {
      "id": "001",
      "nombre": "Aula 101",
      "capacidad": 30,
      "edificio": {
        "id": "E01",
        "nombre": "Edificio Principal"
      }
    }
  ],
  "metadata": {
    "total": 42,
    "page": 1,
    "pageSize": 20
  }
}
```

**Valida:**
- Estructura de datos expuestos
- Contrato de comunicación cliente-servidor
- Códigos HTTP y manejo de errores
- Capacidades de filtrado y paginación

### complementariedad de prototipos

|Aspecto|Prototipo GUI|Prototipo API|
|-|-|-|
|**Qué valida**|Experiencia de usuario|Contrato de datos|
|**Con quién se valida**|Usuario final|Desarrollador frontend/cliente|
|**Feedback esperado**|"¿Es intuitivo?"|"¿Tiene los datos necesarios?"|
|**Momento de validación**|Requisitos|Requisitos + Diseño arquitectónico|
|**Herramienta**|Wireframe en PlantUML/Figma|Documento Markdown/OpenAPI|

**Ninguno de los dos es suficiente por sí solo en arquitecturas modernas.**

## ventajas del prototipado multi-interfaz

### 1. validación temprana de arquitectura

**Problema común:**
Desarrollar GUI completa y descubrir tarde que el backend no expone los datos necesarios.

**Solución con prototipo API:**
Validar el contrato de datos ANTES de implementar frontend.

### 2. desarrollo paralelo

**Con prototipo API REST:**
- Frontend puede trabajar con datos mock
- Backend puede desarrollarse contra tests de contrato
- Integración más suave al final

**Sin prototipo API REST:**
- Frontend espera a backend
- Backend descubre requisitos durante integración
- Múltiples ciclos de ajuste

### 3. documentación viva

**Prototipos API REST bien hechos se convierten en:**
- Documentación de referencia
- Base para tests de integración
- Especificación OpenAPI generada
- Postman Collections de ejemplo

### 4. validación con stakeholders técnicos

**Usuario final** valida GUI: "¿Puedo hacer mi trabajo?"
**Desarrollador cliente** valida API: "¿Puedo construir mi app con esto?"
**Arquitecto** valida ambos: "¿Es esto mantenible y escalable?"

## metodología de prototipado multi-interfaz

### paso 1: identificar puntos de contacto

Para cada caso de uso, preguntarse:
- ¿Quién/qué consumirá esta funcionalidad?
- ¿Cómo se comunicará con el sistema?
- ¿Qué tipo de interfaz necesita?

### paso 2: priorizar prototipos

No todos los prototipos tienen mismo valor:

|Prioridad|Cuándo prototipar|
|-|-|
|**Alta**|Interfaz principal del sistema|
|**Alta**|Contrato expuesto públicamente|
|**Media**|Interfaces internas entre componentes|
|**Baja**|Implementaciones internas sin exposición|

### paso 3: crear prototipos apropiados

|Tipo de interfaz|Artefacto de prototipo|Herramienta|
|-|-|-|
|GUI|Wireframes|PlantUML, Figma, papel|
|API REST|Especificación HTTP/JSON|Markdown, OpenAPI|
|CLI|Sintaxis + ejemplos|Markdown, man pages|
|Archivos|Esquemas + ejemplos|JSON Schema, XML Schema|
|Mensajería|Esquemas de eventos|AsyncAPI, JSON Schema|

### paso 4: validar con consumidores

|Interfaz|Validar con|Pregunta clave|
|-|-|-|
|GUI|Usuario final|¿Puedo completar mi tarea fácilmente?|
|API REST|Dev frontend|¿Tengo todos los datos que necesito?|
|CLI|Usuario técnico|¿Es intuitiva la sintaxis?|
|Archivos|Sistema consumidor|¿Puedo parsear/validar esto?|

### paso 5: iterar antes de implementar

El costo de cambiar:
- **Prototipo**: minutos a horas
- **Implementación**: horas a días
- **Producción**: días a semanas

**Objetivo: Maximizar cambios en fase de prototipo.**

## aplicación en RUP

### disciplina de requisitos

**Actividad:** Prototipar interfaces de usuario

**Extensión para arquitecturas modernas:**
→ Prototipar **todos** los puntos de contacto del sistema

### artefactos producidos

|Caso de uso|Artefactos de prototipo|
|-|-|
|`abrirAulas()`|`prototipo.puml` (GUI) + `prototipo-api.md` (REST)|
|`generarHorario()`|`prototipo.puml` (GUI) + `prototipo-api.md` (REST) + `formato-exportacion.json` (Archivo)|
|`importarDatos()`|`formato-importacion.csv` (Archivo) + `validacion.schema.json`|

### transición a fase de diseño

Los prototipos se convierten en:
- **Especificaciones formales** durante Diseño
- **Tests de contrato** durante Implementación
- **Documentación de usuario** durante Transición

## herramientas recomendadas

### para prototipos GUI
- **PlantUML**: Wireframes en texto plano (versionables)
- **Figma**: Mockups de alta fidelidad
- **Balsamiq**: Wireframes rápidos de baja fidelidad

### para prototipos API REST
- **Markdown**: Especificaciones legibles y versionables
- **OpenAPI/Swagger**: Especificaciones formales generables
- **Postman**: Colecciones de requests de ejemplo

### para prototipos CLI
- **Markdown**: Documentación de sintaxis y ejemplos
- **Docopt**: Especificaciones formales de comandos
- **Ejemplos ejecutables**: Scripts bash/PowerShell de muestra

### para prototipos de archivos
- **JSON Schema**: Especificaciones formales de estructura
- **Ejemplos reales**: Archivos de muestra con datos representativos
- **Validadores online**: Para que stakeholders prueben sus datos

## antipatrones a evitar

### ❌ antipatrón 1: solo prototipar GUI
**Problema:** Descubrir tarde que la arquitectura no soporta los requisitos
**Solución:** Prototipar API si hay separación frontend-backend

### ❌ antipatrón 2: prototipar implementación
**Problema:** Wireframe muestra "tabla SQL" o "llamada a API REST"
**Solución:** Prototipos muestran comportamiento desde perspectiva del consumidor

### ❌ antipatrón 3: prototipos demasiado detallados
**Problema:** Invertir días en mockup pixel-perfect antes de validar concepto
**Solución:** Empezar con baja fidelidad, aumentar detalle tras validación

### ❌ antipatrón 4: no validar prototipos
**Problema:** Crear prototipos pero no mostrarlos a consumidores
**Solución:** Sesiones de validación obligatorias con cada tipo de usuario

### ❌ antipatrón 5: prototipos desconectados de especificación
**Problema:** Wireframe muestra campos que no están en especificación del caso de uso
**Solución:** Tabla de correspondencia entre especificación y prototipo

## checklist de prototipado completo

Para cada caso de uso, verificar:

- [ ] Identificados todos los puntos de contacto del sistema
- [ ] Priorizados los prototipos según valor
- [ ] Creados prototipos apropiados para cada interfaz
- [ ] Cada prototipo tiene tabla de correspondencia con especificación
- [ ] Validados prototipos con consumidores reales
- [ ] Documentado feedback recibido
- [ ] Iterados prototipos según feedback
- [ ] Aprobación explícita de stakeholders antes de implementación

## aplicación en pySigHor

### estado actual del proyecto

El proyecto pySigHor está en **Fase de Elaboración (RUP)** con:
- ✓ 32 casos de uso especificados en detalle
- ✓ Prototipos GUI (wireframes) para todos los casos
- 🔄 **Prototipos API REST en desarrollo** (iniciado con `abrirAulas()`)

### plan de implementación

1. **Completar familia "abrir*"**: Prototipos API para listados
2. **Familia "crear*/editar*/eliminar*"**: Prototipos API CRUD completo
3. **Casos complejos**: `generarHorario()`, `consultarHorario()` con múltiples interfaces
4. **Consolidación**: Patrón arquitectónico completo antes de Fase de Construcción

### valor didáctico

Este proyecto sirve como:
- **Caso de estudio** de prototipado multi-interfaz en RUP
- **Material de referencia** para arquitecturas modernas
- **Plantilla replicable** para proyectos de estudiantes
- **Ejemplo real** de separación de responsabilidades

## referencias aplicadas en este proyecto

- [Prototipo API REST - abrirAulas()](/RUP/00-casos-uso/02-detalle/abrirAulas/prototipo-api.md)
- [Patrón de familia "abrir*"](patron-familia-abrir.md)
- [Artículo 003: RUP e Independencia Tecnológica](/extraDocs/003-rup-independencia-tecnologica/README.md)

## lecturas recomendadas

### sobre APIs y contratos
- **REST API Design Rulebook** (Mark Massé) - Convenciones RESTful
- **OpenAPI Specification** - Estándar de especificación de APIs
- **API Design Patterns** (JJ Geewax) - Patrones comunes

### sobre prototipado
- **The Design of Everyday Things** (Don Norman) - Principios de diseño de interfaces
- **Sketching User Experiences** (Bill Buxton) - Importancia del prototipado temprano
- **Lean UX** (Jeff Gothelf) - Prototipado rápido e iterativo

## conclusión

El prototipado es **independiente de la tecnología de interfaz**. Lo que importa es:
1. **Identificar puntos de contacto** del sistema con el exterior
2. **Crear prototipos apropiados** para cada tipo de interfaz
3. **Validar temprano** con consumidores reales
4. **Iterar barato** antes de implementar

Esta comprensión ampliada del prototipado es esencial para desarrolladores modernos que trabajan en arquitecturas distribuidas, APIs públicas, y sistemas headless.

---

**Este artículo es material didáctico vivo del proyecto pySigHor y se actualizará conforme se apliquen estos principios en el desarrollo real.**
