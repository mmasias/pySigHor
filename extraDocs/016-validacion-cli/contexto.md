# Contexto: CLI como validación

<div align=right>

|||||||
|-|-|-|-|-|-|
|[🏠️](../README.md)|[Artículo](README.md)|**Contexto**|[Evidencia](evidencia.md)|[Comparativa](comparativa-arquitecturas-cli.md)|[Reutilización](reutilizacion-vs-reimplementacion.md)|

</div>

## Antecedentes: La serie de validaciones de independencia tecnológica

### Artículo 003: La hipótesis original

El [artículo 003](/extraDocs/003-rup-independencia-tecnologica/) estableció la siguiente hipótesis:

> "Un análisis RUP completo y riguroso puede soportar múltiples implementaciones tecnológicas sin modificaciones sustanciales a los artefactos de análisis."

Esta decisión estratégica de completar todo el análisis antes de abordar tecnología específica marcó el inicio de un experimento metodológico en tiempo real.

### Artículo 004: Dashboard visual como herramienta

El [artículo 004](/extraDocs/004-dashboard-visual-rup-casos-uso/) introdujo el sistema de codificación por colores en el diagrama de contexto:

- 🔘 Gris punteado: Identificado
- 🔴 Rojo: Detalle/Prototipado
- 🟫 Amarillo oscuro: Análisis
- 🟢 Verde: Diseño
- 🔵 Celeste: Desarrollo
- 🔵 Azul: Pruebas
- ⚫ Negro continuo: Completado

Este dashboard permitió visualizar el progreso del experimento de independencia tecnológica.

### Artículo 014: Prototipado más allá de GUI

El [artículo 014](/extraDocs/014-prototipado-mas-alla-gui/) expandió el concepto de prototipado:

> "El prototipado RUP no se trata solo de mockups visuales. También debería incluir validación de APIs REST, CLIs y/o cualquier punto de contacto del sistema."

**Afirmaciones clave:**

- Los wireframes SALT son abstracciones de interacción, no solo GUI
- El prototipado valida contratos de interfaz, no tecnologías específicas
- Múltiples puntos de contacto (GUI, API, CLI) pueden compartir el mismo análisis

**Este artículo 016 valida empíricamente esas afirmaciones.**

### Artículo 015: Validación entre "primos tecnológicos"

El [artículo 015](/extraDocs/015-dashboards-multistack-validacion-experimental/) materializó el experimento:

**Stacks validados:**

- FastAPI/React (minimalista, Python, biblioteca compositiva)
- Spring/Angular (enterprise, Java, framework con opinión)

**Resultados:**

- 5 casos de uso diseñados en ambos stacks
- 100% de artefactos de análisis sin modificación
- Consistencia arquitectónica alta entre implementaciones

**Similitudes entre ambos stacks:**

- Ambos son arquitecturas cliente/servidor web
- Ambos usan GUI en navegador
- Ambos usan HTTP/REST para comunicación
- Ambos comparten paradigma de interacción visual

**Pregunta pendiente:** ¿Qué pasa si eliminamos completamente la interfaz gráfica?

## Motivación para validación con CLI

### La limitación del experimento 015

Aunque el artículo 015 validó independencia tecnológica entre stacks muy diferentes, todos compartían características fundamentales:

**Familia tecnológica compartida:**

- Todos son aplicaciones web
- Todos tienen interfaz gráfica
- Todos usan navegador
- Todos dependen de HTTP para UI

**Esto dejó una pregunta sin responder:**

> ¿La independencia tecnológica de RUP es real o está limitada a tecnologías de la misma familia (web con GUI)?

### CLI como caso extremo

CLI representa un paradigma radicalmente diferente:

**Diferencias fundamentales con GUI web:**

<div align=center>

| Aspecto | GUI Web (React/Angular) | CLI (Terminal) |
|-|-|-|
| Entorno de ejecución | Navegador | Terminal/consola |
| Paradigma de interacción | Visual, apuntar y hacer click | Textual, comandos imperativos |
| Estado de interfaz | DOM en memoria | Variables, archivos, salida de texto |
| Navegación | Clicks, enlaces, botones | Comandos secuenciales |
| Formularios | Inputs visuales, validación en tiempo real | Prompts secuenciales |
| Feedback | Visual (colores, animaciones) | Textual (mensajes, códigos salida) |
| Dependencia de HTTP | Sí (para UI) | No (opcional) |

</div>

**Si el análisis RUP funciona con este cambio de paradigma, valida su independencia tecnológica.**

## Estado del proyecto antes del experimento CLI

### Análisis RUP completado al 100%

**Estado en rama `main`:**

- 32 casos de uso con especificación detallada completa
- 32 casos de uso con análisis MVC completo
- Diagramas de colaboración para todos los casos
- Diagramas de secuencia para casos complejos
- Modelo del dominio refinado
- Wireframes SALT para interfaces críticas

### Diseños web existentes

**Rama `diseño-fastapi-react`:**

- 5 casos de uso diseñados (verde en dashboard)
- API REST endpoints implementados
- Componentes React mapeados desde análisis

**Rama `diseño-spring-angular`:**

- 5 casos de uso diseñados (verde en dashboard)
- API REST endpoints implementados
- Componentes Angular mapeados desde análisis

**Oportunidad clave:** Los endpoints REST de FastAPI ya están diseñados y pueden reutilizarse.

## La pregunta de las dos arquitecturas CLI

### Descubrimiento durante planificación

Al planificar la validación CLI, surgió una pregunta arquitectónica interesante:

**¿Cómo debe CLI interactuar con la base de datos?**

<div align=center>

|Opción 1 - Cliente HTTP|Opción 2 - Monolítico|
|-|-|
`CLI → HTTP REST → FastAPI → PostgreSQL`|`CLI → Services → Repositories → PostgreSQL`
Reutiliza backend existente|Sin dependencias de servidor HTTP
Consume mismos endpoints que React|Acceso directo a base de datos
Requiere servidor corriendo|Standalone, portable

</div>

Esta decisión arquitectónica NO debería afectar el análisis RUP. Si afecta, entonces RUP no es realmente independiente de tecnología.

**Este experimento valida dos dimensiones:**

1. Independencia de paradigma de interfaz (GUI → CLI)
2. Invariancia ante decisiones arquitectónicas (cliente HTTP vs monolítico)

## Selección de casos de uso para validación

### Criterio de selección: reutilización del mismo conjunto de casos

**Casos seleccionados (mismos que artículo 015):**

1. `iniciarSesion()` - Autenticación de usuarios
2. `abrirAulas()` - Apertura de gestión de aulas
3. `crearAula()` - Creación de aulas
4. `editarAula()` - Edición de aulas
5. `eliminarAula()` - Eliminación segura con confirmación

**Razones:**

- Ya diseñados en FastAPI/React y Spring/Angular
- Cubre CRUD completo + autenticación
- Permite comparación directa entre tres paradigmas (React, Angular, CLI)
- Conjunto representativo sin ser excesivo

### Complejidad de mapeo GUI → CLI

**Casos triviales para CLI:**

- `iniciarSesion()` - Prompt usuario/password es natural en CLI
- `crearAula()` - Formulario secuencial con prompts
- `eliminarAula()` - Confirmación y/n es estándar en CLI

**Casos con adaptación:**

- `abrirAulas()` - Listado largo requiere paginación o formato tabla
- `editarAula()` - Edición continua no es natural en CLI (requiere rediseño de interacción)

**Hipótesis:** La adaptación es de presentación, no de análisis.

## Tecnologías seleccionadas para CLI

### Stack tecnológico: Python

**Razones de la elección:**

1. **Coherencia con FastAPI:** Mismo lenguaje que backend existente
2. **Librerías maduras:** `click` o `typer` para CLIs modernos
3. **Reutilización potencial:** Si implementamos monolítico, podemos compartir lógica con FastAPI
4. **Simplicidad:** Python es ideal para prototipado rápido de CLIs

### Librería CLI: Click

**Características:**

- Decoradores para definir comandos
- Prompts interactivos nativos
- Formateo de salida (colores, tablas)
- Manejo de opciones y argumentos
- Composición de comandos

**Ejemplo mínimo:**
```python
import click

@click.command()
def login():
    username = click.prompt('Username')
    password = click.prompt('Password', hide_input=True)
    click.echo('✓ Sesión iniciada')
```

### Cliente HTTP: Requests

Para arquitectura cliente HTTP:
```python
import requests

response = requests.post('http://localhost:8000/api/login',
                        json={'username': username, 'password': password})
```

### ORM (solo para monolítico): SQLAlchemy

Para arquitectura monolítica (acceso directo a DB):
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://...')
Session = sessionmaker(bind=engine)
```

## Timeline del experimento

### Fase 1: Diseño conceptual (Actual)

**Objetivo:** Documentar experimento y validar independencia de análisis

**Artefactos a crear:**

- Artículo 016 con descripción completa del experimento
- Comparativas de arquitecturas CLI
- Análisis de reutilización vs reimplementación
- Diagramas de mapeo MVC para CLI

**Estado:** En progreso (este artículo)

### Fase 2: Implementación arquitectura cliente HTTP (Próxima)

**Objetivo:** Validar reutilización máxima de backend existente

**Tareas:**

- Crear rama `diseño-cli-python-http`
- Diseñar 5 comandos CLI consumiendo API FastAPI
- Actualizar dashboard con casos CLI en verde
- Medir tiempo de diseño vs React/Angular

**Tiempo estimado:** ~2 horas

### Fase 3: Implementación arquitectura monolítica (Opcional)

**Objetivo:** Validar independencia total de stack web

**Tareas:**

- Crear rama `diseño-cli-python-standalone`
- Diseñar 5 comandos + services + repositories
- Comparar esfuerzo con arquitectura HTTP
- Validar que análisis permanece inalterado

**Tiempo estimado:** ~6 horas

### Fase 4: Documentación de resultados

**Objetivo:** Cerrar el ciclo de validación

**Tareas:**

- Actualizar artículo 016 con evidencia real
- Agregar commits específicos a evidencia.md
- Generar dashboard CLI con casos en verde
- Documentar lecciones aprendidas

## Conexión con el proyecto pySigHor

### Algoritmo original (1998)

**SigHor original:**

- Visual Basic 3.0 con GUI Windows
- Interfaz gráfica para todas las operaciones
- Algoritmo de horarios ejecutado desde UI

### Modernización metodológica (2024-2025)

**Estrategia de validación:**

1. **Análisis independiente** de tecnología (completado)
2. **Diseño web** en dos stacks (FastAPI/React, Spring/Angular)
3. **Diseño CLI** validando paradigma diferente
4. **Futuro:** Desktop (Electron), Mobile (React Native), etc.

**Valor para la comunidad:**

- Demuestra que algoritmo de 1998 puede modernizarse con múltiples paradigmas
- Valida RUP con proyecto real y complejo
- Material didáctico excepcional

## Valor didáctico del experimento CLI

### Para estudiantes

**Aprendizajes concretos:**

- Ven que el análisis MVC captura responsabilidades, no tecnologías
- Comprenden que decisiones arquitectónicas son ortogonales al análisis
- Experimentan la separación entre qué (análisis) y cómo (diseño)

### Para profesionales

**Aplicabilidad práctica:**

- Técnica para modernizar sistemas legacy sin rehacer análisis
- Estrategia para ofrecer múltiples interfaces (GUI, CLI, API) desde mismo backend
- Validación de que inversión en análisis riguroso paga dividendos

### Para la comunidad RUP

**Contribución metodológica:**

- Validación documentada de independencia de paradigma de interfaz
- Evidencia de que RUP escala más allá de aplicaciones web
- Demostración de invariancia del análisis ante decisiones arquitectónicas

## Próximos hitos del experimento

**Validación técnica:**

- Diseñar comandos CLI en ambas arquitecturas (HTTP y monolítico)
- Medir resistencia de análisis ante cambio de paradigma de interfaz
- Documentar ajustes necesarios (esperados: mínimos o cero)

**Validación de escalabilidad:**

- Comparar tiempo de diseño CLI vs React vs Angular
- Evaluar facilidad de mapeo MVC → CLI
- Medir consistencia entre tres paradigmas

**Expansión futura:**

- Considerar TUI (Terminal UI con curses)
- Evaluar interfaz de voz (Alexa/Google Assistant)
- Explorar API GraphQL pura sin interfaz

## Referencias

- [Artículo 003: Análisis independiente de tecnología](/extraDocs/003-rup-independencia-tecnologica/)
- [Artículo 004: Dashboard visual RUP](/extraDocs/004-dashboard-visual-rup-casos-uso/)
- [Artículo 014: Prototipado más allá de GUI](/extraDocs/014-prototipado-mas-alla-gui/)
- [Artículo 015: Dashboards multi-stack](/extraDocs/015-dashboards-multistack-validacion-experimental/)
- [Análisis completo de casos de uso](https://github.com/mmasias/pySigHor/tree/main/RUP/01-analisis/casos-uso)
