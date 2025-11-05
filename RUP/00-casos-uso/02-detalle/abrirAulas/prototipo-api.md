# pySigHor > abrirAulas > Prototipo API REST

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirAulas/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirAulas/README.md)|Diseño|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Inception (Inicio)
- **Disciplina**: Requisitos
- **Tipo de prototipo**: API REST
- **Versión**: 1.0
- **Fecha**: 2025-11-05
- **Autor**: Equipo de desarrollo

## propósito del prototipo API

**Objetivo:** Validar el contrato de comunicación entre cliente y servidor para el caso de uso `abrirAulas()` antes de invertir en implementación.

Este prototipo especifica:
- Endpoints HTTP necesarios
- Estructura de requests y responses
- Códigos de estado HTTP
- Esquemas de datos JSON

## endpoint principal

### listar y filtrar aulas

```http
GET /api/aulas
```

#### query parameters

|Parámetro|Tipo|Obligatorio|Descripción|Ejemplo|
|-|-|-|-|-|
|`filtro`|string|No|Texto de búsqueda aplicado a ID, nombre y edificio|`filtro=101`|
|`edificioId`|string|No|Filtrado específico por ID de edificio|`edificioId=E01`|
|`page`|integer|No|Número de página para paginación (por defecto: 1)|`page=2`|
|`pageSize`|integer|No|Cantidad de resultados por página (por defecto: 20)|`pageSize=50`|
|`sort`|string|No|Campo por el que ordenar (id, nombre, capacidad)|`sort=capacidad`|
|`order`|string|No|Dirección de ordenamiento (asc, desc)|`order=desc`|

#### ejemplos de requests

##### listar todas las aulas
```http
GET /api/aulas
```

##### filtrar por texto
```http
GET /api/aulas?filtro=101
```

##### filtrar por edificio
```http
GET /api/aulas?edificioId=E01
```

##### filtrar y ordenar
```http
GET /api/aulas?filtro=Aula&sort=capacidad&order=desc
```

##### paginación
```http
GET /api/aulas?page=2&pageSize=10
```

#### response exitoso (200 OK)

```json
{
  "aulas": [
    {
      "id": "001",
      "nombre": "Aula 101",
      "capacidad": 30,
      "edificio": {
        "id": "E01",
        "nombre": "Edificio Principal"
      },
      "recursos": ["Proyector", "Pizarra digital"]
    },
    {
      "id": "002",
      "nombre": "Aula 102",
      "capacidad": 45,
      "edificio": {
        "id": "E01",
        "nombre": "Edificio Principal"
      },
      "recursos": ["Proyector", "Sistema de audio"]
    }
  ],
  "metadata": {
    "total": 42,
    "page": 1,
    "pageSize": 20,
    "totalPages": 3
  }
}
```

#### estructura del response

##### objeto principal

|Campo|Tipo|Descripción|
|-|-|-|
|`aulas`|Array\<Aula\>|Lista de aulas que cumplen los criterios|
|`metadata`|Metadata|Información de paginación y totales|

##### objeto Aula

|Campo|Tipo|Obligatorio|Descripción|
|-|-|-|-|
|`id`|string|Sí|Identificador único del aula|
|`nombre`|string|Sí|Nombre descriptivo del aula|
|`capacidad`|integer|Sí|Número máximo de estudiantes|
|`edificio`|Edificio|Sí|Objeto con información del edificio|
|`recursos`|Array\<string\>|No|Lista de recursos disponibles en el aula|

##### objeto Edificio

|Campo|Tipo|Obligatorio|Descripción|
|-|-|-|-|
|`id`|string|Sí|Identificador único del edificio|
|`nombre`|string|Sí|Nombre del edificio|

##### objeto Metadata

|Campo|Tipo|Descripción|
|-|-|-|
|`total`|integer|Cantidad total de aulas que cumplen el criterio|
|`page`|integer|Página actual|
|`pageSize`|integer|Cantidad de resultados por página|
|`totalPages`|integer|Cantidad total de páginas disponibles|

#### códigos de estado HTTP

|Código|Descripción|Cuándo ocurre|
|-|-|-|
|**200 OK**|Solicitud exitosa|Siempre que los parámetros sean válidos|
|**400 Bad Request**|Parámetros inválidos|pageSize > 100, page < 1, sort con campo inválido|
|**401 Unauthorized**|No autenticado|Token JWT ausente o inválido|
|**403 Forbidden**|Sin permisos|Usuario autenticado pero no es Administrador|
|**500 Internal Server Error**|Error del servidor|Problemas de conexión a base de datos u otros errores internos|

#### ejemplo de error (400 Bad Request)

```json
{
  "error": {
    "code": "INVALID_PARAMETER",
    "message": "El parámetro 'pageSize' no puede ser mayor a 100",
    "details": {
      "parameter": "pageSize",
      "providedValue": 150,
      "maxValue": 100
    }
  }
}
```

## correspondencia con especificación

### conversación actor-sistema

|Especificación|Implementación API|
|-|-|
|**Actor solicita listar aulas**|`GET /api/aulas`|
|**Sistema presenta lista de aulas**|Response 200 con array `aulas[]`|
|**Sistema permite solicitar filtrar lista**|Query params: `filtro`, `edificioId`|
|**Actor solicita filtrar lista**|`GET /api/aulas?filtro=...`|
|**Sistema presenta lista filtrada**|Response 200 con aulas filtradas|

### estados del caso de uso

|Estado|Endpoint|Observación|
|-|-|-|
|**MostrandoLista**|`GET /api/aulas`|Sin parámetros de filtro|
|**FiltrandoLista**|`GET /api/aulas?filtro=...`|Con parámetros de filtro aplicados|

## navegación a otros casos de uso

El cliente (frontend) usará la información del response para habilitar navegación a:

|Caso de uso destino|Información necesaria del response|Próximo endpoint|
|-|-|-|
|`crearAula()`|N/A - botón "Crear nueva aula"|`POST /api/aulas`|
|`editarAula()`|`aula.id` de la fila seleccionada|`GET /api/aulas/{id}` + `PUT /api/aulas/{id}`|
|`eliminarAula()`|`aula.id` de la fila seleccionada|`DELETE /api/aulas/{id}`|
|`completarGestion()`|N/A - botón "Volver"|Navegación de cliente|

## validaciones del prototipo

### preguntas de validación

#### funcionalidad
- ¿La estructura del response contiene toda la información necesaria?
- ¿Los parámetros de filtrado cubren los casos de uso esperados?
- ¿La paginación es suficientemente flexible?
- ¿Falta algún campo en el objeto Aula?

#### arquitectura
- ¿El endpoint sigue convenciones RESTful?
- ¿Los códigos HTTP están correctamente asignados?
- ¿El anidamiento del objeto Edificio es apropiado o debería ser solo el ID?
- ¿Debería incluirse información de recursos en el listado o solo en detalle?

#### rendimiento
- ¿El pageSize máximo de 100 es apropiado?
- ¿Debería incluirse información de caché en los headers?
- ¿El anidamiento de Edificio genera queries N+1?

#### usabilidad
- ¿La estructura de error es suficientemente descriptiva?
- ¿Los nombres de campos son intuitivos?
- ¿La metadata de paginación es completa?

## consideraciones de implementación

### seguridad
- **Autenticación**: JWT Bearer token obligatorio
- **Autorización**: Verificar rol de Administrador
- **SQL Injection**: Sanitizar parámetros `filtro`
- **Rate limiting**: Considerar límite de requests por usuario

### rendimiento
- **Caché**: Considerar caché de 60 segundos para listados sin filtro
- **Índices de BD**: Índices en campos `nombre`, `edificioId`, `capacidad`
- **Eager loading**: Cargar relación `edificio` en una sola query
- **Límites**: Validar `pageSize` máximo para evitar queries pesadas

### escalabilidad
- **Cursor pagination**: Considerar cursor-based pagination para datasets grandes
- **Campos parciales**: Considerar parámetro `fields` para devolver solo campos necesarios
- **Compresión**: Habilitar compresión gzip para responses

## relación con otros prototipos

### coherencia arquitectónica
Este prototipo establece el patrón para la familia de casos **"abrir*"**:
- `abrirProfesores()` → `GET /api/profesores`
- `abrirCursos()` → `GET /api/cursos`
- `abrirEdificios()` → `GET /api/edificios`
- `abrirRecursos()` → `GET /api/recursos`

Todos seguirán la misma estructura:
- Query params: `filtro`, paginación, ordenamiento
- Response: `{ items: [], metadata: {} }`
- Códigos HTTP consistentes
- Estructura de error estandarizada

## próximos pasos

### completar la familia CRUD
1. **Prototipo API para `crearAula()`**: `POST /api/aulas`
2. **Prototipo API para `editarAula()`**: `GET /api/aulas/{id}` + `PUT /api/aulas/{id}`
3. **Prototipo API para `eliminarAula()`**: `DELETE /api/aulas/{id}`

### documentación complementaria
- **OpenAPI Specification**: Generar spec completo en formato YAML
- **Postman Collection**: Colección de requests de ejemplo
- **Tests de contrato**: Definir tests que validen el contrato API

## referencias

- [Especificación detallada - abrirAulas()](README.md)
- [Prototipo GUI - Wireframes](prototipo.puml)
- [Análisis MVC - abrirAulas()](/RUP/01-analisis/casos-uso/abrirAulas/README.md)
- [Artículo: Prototipado más allá de GUI](/extraDocs/014-prototipado-mas-alla-gui/README.md)
