# Patrón Replicable: Familia de Casos "abrir*"

## propósito

Establecer un patrón arquitectónico consistente para todos los casos de uso del tipo **"abrir*"** que representan operaciones de **listado y filtrado** de entidades maestras del sistema.

## casos de uso afectados

|Caso de uso|Endpoint API|Entidad|
|-|-|-|
|`abrirAulas()`|`GET /api/aulas`|Aula|
|`abrirProfesores()`|`GET /api/profesores`|Profesor|
|`abrirCursos()`|`GET /api/cursos`|Curso|
|`abrirEdificios()`|`GET /api/edificios`|Edificio|
|`abrirRecursos()`|`GET /api/recursos`|Recurso|

## patrón de endpoint REST

### estructura base

```http
GET /api/{entidad}
```

Donde `{entidad}` es el nombre del recurso en **plural** y **minúsculas**.

### query parameters estándar

Todos los endpoints de la familia **"abrir*"** deben soportar:

|Parámetro|Tipo|Obligatorio|Descripción|Valores permitidos|
|-|-|-|-|-|
|`filtro`|string|No|Búsqueda de texto libre|Cualquier string|
|`page`|integer|No|Número de página|≥ 1 (default: 1)|
|`pageSize`|integer|No|Resultados por página|1-100 (default: 20)|
|`sort`|string|No|Campo de ordenamiento|Depende de entidad|
|`order`|string|No|Dirección de orden|`asc`, `desc` (default: `asc`)|

### parámetros específicos por entidad

Cada endpoint puede agregar parámetros adicionales según su dominio:

```http
# abrirAulas: filtrado por edificio
GET /api/aulas?edificioId=E01

# abrirProfesores: filtrado por especialidad
GET /api/profesores?especialidad=Matemáticas

# abrirCursos: filtrado por programa académico
GET /api/cursos?programaId=P01
```

## patrón de response

### estructura JSON estándar

```json
{
  "{entidad}": [
    {
      // Objeto individual de la entidad
    }
  ],
  "metadata": {
    "total": 0,
    "page": 1,
    "pageSize": 20,
    "totalPages": 0
  }
}
```

### ejemplo: abrirAulas()

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
      }
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

### ejemplo: abrirProfesores()

```json
{
  "profesores": [
    {
      "id": "P001",
      "nombre": "Dr. Juan Pérez",
      "especialidad": "Matemáticas",
      "disponibilidad": {
        "horasPorSemana": 20,
        "horarioPreferido": "Mañanas"
      }
    }
  ],
  "metadata": {
    "total": 85,
    "page": 1,
    "pageSize": 20,
    "totalPages": 5
  }
}
```

## campos obligatorios por entidad

### estructura mínima de cada objeto

Cada entidad debe incluir **como mínimo**:

|Campo|Tipo|Descripción|
|-|-|-|
|`id`|string|Identificador único|
|`nombre`|string|Nombre descriptivo de la entidad|

### campos adicionales según dominio

Los campos adicionales dependen de la naturaleza de la entidad:

#### Aula
```json
{
  "id": "string",
  "nombre": "string",
  "capacidad": "integer",
  "edificio": "Edificio",
  "recursos": "string[]"
}
```

#### Profesor
```json
{
  "id": "string",
  "nombre": "string",
  "especialidad": "string",
  "disponibilidad": "Disponibilidad"
}
```

#### Curso
```json
{
  "id": "string",
  "nombre": "string",
  "programa": "Programa",
  "creditos": "integer",
  "requiereRecursos": "string[]"
}
```

## códigos HTTP estándar

|Código|Cuándo usar|Ejemplo|
|-|-|-|
|**200 OK**|Request válido con resultados|Listado devuelto correctamente|
|**200 OK** (array vacío)|Request válido sin resultados|Filtro no encuentra coincidencias|
|**400 Bad Request**|Parámetros inválidos|`pageSize=200` (excede límite)|
|**401 Unauthorized**|No autenticado|Token JWT ausente|
|**403 Forbidden**|Sin permisos|Usuario sin rol Administrador|
|**500 Internal Server Error**|Error interno|Conexión a BD falló|

## estructura de error estándar

Todos los errores deben seguir este formato:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Mensaje descriptivo para el usuario",
    "details": {
      // Información adicional del error
    }
  }
}
```

### ejemplo de error común

```json
{
  "error": {
    "code": "INVALID_PAGE_SIZE",
    "message": "El parámetro 'pageSize' debe estar entre 1 y 100",
    "details": {
      "parameter": "pageSize",
      "providedValue": 150,
      "minValue": 1,
      "maxValue": 100
    }
  }
}
```

## aplicación del filtro de texto

El parámetro `filtro` debe aplicarse a **todos los campos de texto principales** de la entidad:

### abrirAulas()
```
filtro="101" → Busca en: id, nombre, edificio.nombre
```

### abrirProfesores()
```
filtro="Juan" → Busca en: id, nombre, especialidad
```

### abrirCursos()
```
filtro="Matemáticas" → Busca en: id, nombre, programa.nombre
```

## ordenamiento por campos

Cada endpoint debe definir qué campos soportan ordenamiento:

### abrirAulas()
```
sort=capacidad → Ordena por capacidad numérica
sort=nombre → Ordena alfabéticamente por nombre
sort=edificio → Ordena por nombre de edificio
```

### abrirProfesores()
```
sort=nombre → Ordena alfabéticamente por nombre
sort=especialidad → Ordena por especialidad
```

## consideraciones de implementación

### rendimiento
- **Índices de BD**: Crear índices en campos usados en `filtro` y `sort`
- **Eager loading**: Cargar relaciones anidadas en una sola query
- **Caché**: Considerar caché de 60 segundos para listados sin filtros
- **Límites**: Validar `pageSize` máximo para proteger el servidor

### seguridad
- **Autenticación**: JWT obligatorio en header `Authorization: Bearer {token}`
- **Autorización**: Verificar rol de Administrador
- **Sanitización**: Limpiar parámetro `filtro` para prevenir SQL injection
- **Rate limiting**: Limitar requests por usuario/IP

### escalabilidad
- **Cursor pagination**: Para datasets muy grandes (>10k registros)
- **Campos selectivos**: Agregar parámetro `fields` para responses parciales
- **Compresión**: Habilitar gzip para reducir tamaño de respuesta

## navegación desde endpoints "abrir*"

Los responses de estos endpoints habilitan navegación a operaciones CRUD:

|Acción del usuario|Caso de uso destino|Información necesaria|
|-|-|-|
|Crear nueva entidad|`crear{Entidad}()`|Ninguna (botón "Nuevo")|
|Editar entidad existente|`editar{Entidad}()`|`id` de la fila seleccionada|
|Eliminar entidad|`eliminar{Entidad}()`|`id` de la fila seleccionada|
|Ver detalle|`ver{Entidad}()`|`id` de la fila seleccionada|

## checklist de implementación

Al implementar un nuevo endpoint de la familia "abrir*", verificar:

- [ ] Endpoint sigue convención `GET /api/{entidad}`
- [ ] Soporta query params estándar: `filtro`, `page`, `pageSize`, `sort`, `order`
- [ ] Response tiene estructura `{ "{entidad}": [], "metadata": {} }`
- [ ] Objeto entidad incluye mínimo `id` y `nombre`
- [ ] Códigos HTTP correctos: 200, 400, 401, 403, 500
- [ ] Estructura de error estandarizada
- [ ] Filtro de texto se aplica a todos los campos relevantes
- [ ] Índices de BD creados en campos de búsqueda/ordenamiento
- [ ] Validación de límites: `pageSize` máximo, `page` mínimo
- [ ] Autenticación JWT verificada
- [ ] Autorización de rol Administrador verificada
- [ ] Sanitización de parámetro `filtro` implementada
- [ ] Tests de contrato API creados
- [ ] Documentación OpenAPI generada

## evolución del patrón

Este patrón debe:
- **Mantenerse estable** para casos básicos de listado/filtrado
- **Extenderse** cuando se detecten necesidades comunes a múltiples endpoints
- **Documentarse** cualquier excepción justificada al patrón

### propuesta de cambio

Si se identifica necesidad de modificar el patrón:
1. Documentar el problema en issue de GitHub
2. Proponer solución aplicable a TODA la familia
3. Validar con casos de uso existentes
4. Actualizar este documento
5. Refactorizar endpoints existentes para mantener coherencia

## referencias

- [Prototipo API REST - abrirAulas()](/RUP/00-casos-uso/02-detalle/abrirAulas/prototipo-api.md)
- [Artículo: Prototipado más allá de GUI](/extraDocs/014-prototipado-mas-alla-gui/README.md)
- [Artículo: RUP e Independencia Tecnológica](/extraDocs/003-rup-independencia-tecnologica/README.md)
