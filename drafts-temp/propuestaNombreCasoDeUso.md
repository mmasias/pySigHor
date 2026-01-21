# Propuesta de Implementación para el Caso de Uso "abrirAulas"

## 1. Descripción del Caso de Uso

El caso de uso **abrirAulas()** permite al Administrador visualizar una lista de aulas registradas en el sistema con capacidad de filtrado, búsqueda y navegación a operaciones CRUD (Crear, Leer, Editar, Eliminar). Este caso de uso actúa como punto de entrada para la gestión de aulas en el sistema pySigHor.

## 2. Requisitos Funcionales

### 2.1 Flujo Principal
1. El Administrador solicita listar aulas desde el estado SISTEMA_DISPONIBLE
2. El sistema presenta una lista de aulas con:
   - ID del aula
   - Nombre del aula
   - Capacidad
   - Edificio al que pertenece
   - Recursos disponibles (opcional)
3. El sistema permite filtrar la lista por:
   - Texto general (ID, nombre, edificio)
   - Edificio específico
4. El sistema permite navegar a operaciones CRUD:
   - Crear nueva aula
   - Editar aula seleccionada
   - Eliminar aula seleccionada
   - Volver al menú principal

### 2.2 Requisitos Técnicos
- Autenticación JWT obligatoria
- Autorización de rol Administrador
- Paginación nativa con Spring Data
- API RESTful con endpoints estandarizados
- Frontend con Angular y protección de rutas

## 3. Arquitectura Propuesta

### 3.1 Stack Tecnológico
- **Backend**: Spring Boot con Spring Security, Spring Data JPA
- **Frontend**: Angular con Angular Router y HttpClient
- **Base de Datos**: H2 (desarrollo) / PostgreSQL (producción)
- **Seguridad**: JWT (JSON Web Tokens)

### 3.2 Componentes del Backend

#### 3.2.1 Controlador (AulaController)
```java
@RestController
@RequestMapping("/api/aulas")
@PreAuthorize("hasRole('ADMIN')")
public class AulaController {
    
    @GetMapping
    public ResponseEntity<Page<AulaDTO>> listarAulas(
        @RequestParam(required = false) String filtro,
        @RequestParam(required = false) String edificioId,
        @RequestParam(defaultValue = "0") int page,
        @RequestParam(defaultValue = "20") int pageSize,
        @RequestParam(defaultValue = "id") String sort,
        @RequestParam(defaultValue = "asc") String order) {
        // Implementación
    }
}
```

#### 3.2.2 Servicio (AulaService)
- Responsable de la lógica de negocio
- Orquesta la obtención y filtrado de aulas
- Mapea entidades a DTOs

#### 3.2.3 Repositorio (AulaRepository)
- Interface Spring Data JPA
- Consultas paginadas y con filtros
- Soporte para búsqueda por texto y por edificio

#### 3.2.4 Entidad (Aula)
- Representa la información del aula
- Relación con Edificio
- Validaciones de dominio

### 3.3 Componentes del Frontend

#### 3.3.1 Componente Angular (AulaListComponent)
- Presenta la lista de aulas en una tabla
- Implementa controles de paginación
- Maneja filtros y búsqueda
- Proporciona botones para operaciones CRUD

#### 3.3.2 Servicio Angular (AulaService)
- Cliente HTTP para consumir la API REST
- Manejo de errores y estado de carga
- Interceptors para tokens JWT

#### 3.3.3 Guardas (AuthGuard)
- Protección de rutas
- Verificación de autenticación y autorización

## 4. Diseño de la API

### 4.1 Endpoint Principal
```
GET /api/aulas
```

### 4.2 Parámetros de Consulta
- `filtro` (opcional): Texto para búsqueda general
- `edificioId` (opcional): ID del edificio para filtrar
- `page` (opcional, default: 0): Número de página (0-indexed)
- `pageSize` (opcional, default: 20): Tamaño de página
- `sort` (opcional, default: id): Campo para ordenar
- `order` (opcional, default: asc): Dirección de orden (asc/desc)

### 4.3 Estructura de la Respuesta
```json
{
  "content": [
    {
      "id": "001",
      "nombre": "Aula 101",
      "capacidad": 30,
      "edificio": {
        "id": "E01",
        "nombre": "Edificio Principal"
      },
      "recursos": ["Proyector", "Pizarra digital"]
    }
  ],
  "pageable": {
    "pageNumber": 0,
    "pageSize": 20,
    "sort": {
      "sorted": true,
      "empty": false,
      "unsorted": false
    },
    "offset": 0,
    "paged": true,
    "unpaged": false
  },
  "totalElements": 42,
  "totalPages": 3,
  "last": false,
  "first": true,
  "sort": {
    "sorted": true,
    "empty": false,
    "unsorted": false
  },
  "numberOfElements": 20,
  "size": 20,
  "number": 0,
  "empty": false
}
```

## 5. Consideraciones de Seguridad

- **Autenticación JWT**: Todos los endpoints requieren token válido en header
- **Autorización**: Verificación de rol de Administrador
- **Protección contra inyección SQL**: Parámetros sanitizados
- **Rate limiting**: Límites de peticiones por usuario

## 6. Consideraciones de Rendimiento

- **Caché**: Caché de 60 segundos para listados sin filtro
- **Índices**: Índices en campos `nombre`, `edificioId`, `capacidad`
- **Eager loading**: Carga eficiente de relación con Edificio
- **Límites**: Validación de `pageSize` máximo (100 elementos)

## 7. Flujo de Navegación

```
SISTEMA_DISPONIBLE → abrirAulas() → AULAS_ABIERTO
    ↓
AULAS_ABIERTO → crearAula() → AULA_ABIERTO
AULAS_ABIERTO → editarAula() → AULA_ABIERTO
AULAS_ABIERTO → eliminarAula() → AULAS_ABIERTO
AULAS_ABIERTO → completarGestion() → SISTEMA_DISPONIBLE
```

## 8. Validaciones del Prototipo

- [x] La estructura del response contiene toda la información necesaria
- [x] Los parámetros de filtrado cubren los casos de uso esperados
- [x] La paginación es suficientemente flexible
- [x] El endpoint sigue convenciones RESTful
- [x] Los códigos HTTP están correctamente asignados

## 9. Próximos Pasos

1. **Implementación Backend**:
   - Crear entidad Aula con relaciones
   - Implementar repositorio con métodos de búsqueda
   - Desarrollar servicio con lógica de negocio
   - Crear controlador con endpoints protegidos

2. **Implementación Frontend**:
   - Componente Angular para mostrar lista
   - Servicio HTTP para consumir API
   - Formulario de filtrado y paginación
   - Rutas protegidas y guardas

3. **Pruebas**:
   - Pruebas unitarias para el backend
   - Pruebas de integración API
   - Pruebas de componentes Angular
   - Pruebas de seguridad y autorización

4. **Documentación**:
   - Actualizar OpenAPI specification
   - Crear colección de Postman
   - Documentar endpoints en el README

Esta propuesta sigue el patrón establecido en el proyecto para casos de uso "abrir*" y mantiene coherencia con el análisis MVC y el diseño de secuencia ya definidos.