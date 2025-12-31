# Comparativa de Stacks: FastAPI/React vs Spring/Angular

<div align=right>

||||||
|-|-|-|-|-|
|[🏠️](../README.md)|[Artículo](README.md)|[Contexto](contexto.md)|[Evidencia](evidencia.md)|**Comparativa**|

</div>

## Introducción

Esta comparativa analiza cómo el mismo análisis RUP se materializa en dos stacks tecnológicos diferentes, evidenciando la independencia tecnológica de la metodología.

## Comparación de filosofías

<table>
<tr><th>FastAPI/React<br>Filosofía minimalista</th><th>Spring/Angular<br>Filosofía enterprise</th></tr>
<tr><td valign=top>

**Servidor: FastAPI (Python)**

- Marco de trabajo moderno, asíncrono por defecto
- Tipado nativo (Python 3.6+)
- Documentación automática con OpenAPI/Swagger
- Validación automática con Pydantic
- Rendimiento comparable a Node.js y Go

</td><td valign=top>

**Servidor: Spring Boot (Java)**

- Marco de trabajo maduro, ecosistema completo
- Inyección de dependencias nativa
- Transaccionalidad, seguridad, pruebas integradas
- Escalabilidad probada en producción
- Comunidad masiva, documentación exhaustiva

</td></tr>
<tr><td valign=top>

**Cliente: React (TypeScript)**

- Biblioteca compositiva, no marco de trabajo
- Arquitectura basada en componentes
- DOM virtual para rendimiento
- Ecosistema flexible (eliges tus herramientas)
- Ganchos para gestión de estado

</td><td valign=top>

**Cliente: Angular (TypeScript)**

- Marco de trabajo completo, con opinión marcada
- Enlace de datos bidireccional
- Inyección de dependencias en cliente
- RxJS para programación reactiva
- Interfaz de línea de comandos completa, pruebas integradas

</td></tr>
<tr><td valign=top>

**Filosofía general:**

- **Minimalismo:** Solo lo necesario, nada más
- **Flexibilidad:** Eliges arquitectura y herramientas
- **Velocidad:** Rápido de desarrollar, rápido de ejecutar
- **Modernidad:** Técnicas asíncronas, seguridad de tipos, experiencia de desarrollo optimizada

</td><td valign=top>

**Filosofía general:**

- **Estructura:** Todo tiene su lugar, convenciones fuertes
- **Completitud:** Batería incluida, soluciones oficiales
- **Escalabilidad:** Diseñado para equipos grandes, proyectos complejos
- **Robustez:** Seguridad de tipos, pruebas, patrones probados

</td></tr>
<tr><td valign=top>

**Público objetivo:**

- Empresas emergentes, productos mínimos viables, prototipos rápidos
- APIs modernas, microservicios
- Equipos pequeños a medianos
- Proyectos donde velocidad de desarrollo importa

</td><td valign=top>

**Público objetivo:**

- Corporaciones, sistemas críticos
- Aplicaciones empresariales de larga vida
- Equipos grandes, múltiples equipos
- Proyectos donde mantenibilidad y robustez importan

</td></tr>
</table>


## Mapeo desde análisis MVC

### Caso de estudio: `iniciarSesion()`

**Análisis RUP (tecnológicamente neutro):**
```
Clases de análisis:
- PantallaLogin (boundary)
- ControladorAutenticacion (control)
- Usuario (entity)
- BaseDatosUsuarios (entity)
```

**Responsabilidades definidas en análisis:**

- **PantallaLogin:** Recoger credenciales, mostrar resultado
- **ControladorAutenticacion:** Validar credenciales, crear sesión
- **Usuario:** Representar datos del usuario
- **BaseDatosUsuarios:** Persistir y recuperar usuarios

### Mapeo en FastAPI/React

**Clases de diseño (backend - FastAPI):**
```python
# Boundary → Controller
class AuthController:
    @router.post("/api/auth/login")
    async def login(credentials: LoginRequest) -> TokenResponse:
        # Delega en control

# Control → Service
class AuthService:
    async def authenticate(username: str, password: str) -> User:
        # Lógica de autenticación

# Entity → Repository + Model
class UserRepository:
    async def find_by_username(username: str) -> Optional[User]:
        # Acceso a datos

class User(BaseModel):
    id: int
    username: str
    # ... (Pydantic model)
```

**Clases de diseño (frontend - React):**
```typescript
// Boundary → Component
const LoginForm: React.FC = () => {
    const [credentials, setCredentials] = useState({...})
    const handleSubmit = async () => {
        // Delega en service
    }
}

// Control → Service
class AuthService {
    async login(username: string, password: string): Promise<AuthResponse> {
        // Llamada a API backend
    }
}

// Entity → Interface/Type
interface User {
    id: number
    username: string
    // ...
}
```

**Tecnologías específicas:**

- **Asíncrono/esperar:** FastAPI asíncrono, ganchos de React con funciones asíncronas
- **Validación:** Pydantic en servidor, bibliotecas de validación de formularios en cliente
- **Estado:** API de Contexto de React o Zustand para estado global
- **HTTP:** Puntos finales FastAPI, Axios/Fetch en React

### Mapeo en Spring/Angular

**Clases de diseño (backend - Spring Boot):**
```java
// Boundary → Controller
@RestController
@RequestMapping("/api/auth")
public class AuthController {
    @PostMapping("/login")
    public ResponseEntity<TokenResponse> login(@RequestBody LoginRequest credentials) {
        // Delega en control
    }
}

// Control → Service
@Service
public class AuthService {
    public User authenticate(String username, String password) {
        // Lógica de autenticación
    }
}

// Entity → Repository + Entity
@Repository
public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
}

@Entity
public class User {
    @Id @GeneratedValue
    private Long id;
    private String username;
    // ... (JPA entity)
}
```

**Clases de diseño (frontend - Angular):**
```typescript
// Boundary → Component
@Component({
    selector: 'app-login',
    templateUrl: './login.component.html'
})
export class LoginComponent {
    credentials = { username: '', password: '' }

    onSubmit(): void {
        // Delega en service
    }
}

// Control → Service
@Injectable({ providedIn: 'root' })
export class AuthService {
    login(username: string, password: string): Observable<AuthResponse> {
        // Llamada a API backend (RxJS Observable)
    }
}

// Entity → Interface/Model
export interface User {
    id: number
    username: string
    // ...
}
```

**Tecnologías específicas:**

- **Inyección de dependencias:** Spring DI en servidor, Angular DI en cliente
- **Validación:** Validación de Beans en servidor, formularios basados en plantillas/reactivos en cliente
- **Estado:** Servicios Angular con BehaviorSubjects de RxJS
- **HTTP:** RestController de Spring, HttpClient de Angular con Observables

## Comparativa técnica detallada

### Arquitectura backend

<div align=center>

| Aspecto | FastAPI/React | Spring/Angular |
|-|-|-|
| **Lenguaje** | Python 3.11+ | Java 17+ |
| **Paradigma** | Asíncrono/esperar, funcional | POO, imperativo |
| **Seguridad de tipos** | Sugerencias de tipo (ejecución opcional) | Sistema de tipos completo (compilación) |
| **Inyección de dependencias** | No nativo (puede usar bibliotecas) | Nativo (Spring Core) |
| **ORM** | SQLAlchemy (asíncrono), Tortoise ORM | JPA/Hibernate |
| **Validación** | Pydantic (declarativa) | Validación de Beans (anotaciones) |
| **Pruebas** | pytest, unittest | JUnit 5, Spring Test |
| **Rendimiento** | ~20k pet/s (uvicorn) | ~15k pet/s (Tomcat) |
| **Tiempo de inicio** | <1s | ~3-5s |
| **Memoria base** | ~50MB | ~200MB |

</div>

### Arquitectura frontend

<div align=center>

| Aspecto | FastAPI/React | Spring/Angular |
|-|-|-|
| **Tipo** | Biblioteca | Marco de trabajo completo |
| **Paradigma** | Compositivo, funcional | Con opinión, estructurado |
| **Enlace de datos** | Unidireccional | Bidireccional |
| **Gestión de estado** | API de Contexto, Redux, Zustand | Servicios + RxJS |
| **Programación reactiva** | Ganchos, no nativo | RxJS nativo |
| **Inyección de dependencias** | No nativo (props, contexto) | Nativo (Angular DI) |
| **Enrutamiento** | React Router (biblioteca) | Angular Router (nativo) |
| **Formularios** | Componentes controlados, bibliotecas | Basados en plantillas, Reactivos |
| **Pruebas** | Jest, React Testing Library | Jasmine, Karma, Angular Testing |
| **Tamaño de paquete (mín)** | ~40KB (núcleo React) | ~150KB (núcleo Angular) |
| **Curva de aprendizaje** | Baja-Media | Media-Alta |

</div>

### Decisiones arquitectónicas derivadas del análisis

#### Autenticación (`iniciarSesion()`)

**Análisis RUP especifica:**

- Validar credenciales contra base de datos
- Crear sesión persistente
- Manejar errores de credenciales inválidas

**FastAPI/React implementa:**

- Tokens JWT (sin estado)
- Token almacenado en almacenamiento local/cookies
- Contexto de React para estado de autenticación global
- Inyección de dependencias FastAPI para validar tokens

**Spring/Angular implementa:**

- Tokens JWT (sin estado) O Spring Session (con estado)
- Token almacenado en almacenamiento local/cookies
- Servicio Angular con BehaviorSubject para estado global
- Spring Security con filtros para validar tokens

**Observación:** Ambos conjuntos tecnológicos llegaron a la misma decisión (JWT) porque el análisis especificó "sesión persistente" sin dictar tecnología.

#### CRUD de Aulas (`crearAula()`, `editarAula()`, `eliminarAula()`)

**Análisis RUP especifica:**

- Patrones "el delgado" (Crear → Usar) y "el gordo" (Editar continua)
- Validación de datos antes de persistir
- Confirmación para eliminación
- Navegación de vuelta a lista después de operación

**FastAPI/React implementa:**

- Componentes separados: FormularioAula (crear/editar), ListaAulas (lista)
- Formulario con Gancho de React para validación declarativa
- Modal de confirmación con estado local
- Enrutador de React para navegación programática

**Spring/Angular implementa:**

- Componentes separados: ComponenteFormularioAula, ComponenteListaAulas
- Formularios Reactivos con validadores para validación
- Modal de confirmación (Diálogo de Angular Material)
- Enrutador de Angular para navegación programática

**Observación:** La estructura de componentes es casi idéntica porque el análisis MVC ya definió las responsabilidades de boundary.

## Consistencia arquitectónica entre stacks

### Responsabilidades MVC preservadas

<div align=center>

| Clase de análisis | FastAPI/React | Spring/Angular | Consistencia |
|-|-|-|-|
| **Boundary** | Controller (API) + Component (UI) | Controller (API) + Component (UI) | 100% |
| **Control** | Service (backend) + Service (frontend) | Service (backend) + Service (frontend) | 100% |
| **Entity** | Model (Pydantic) + Repository (SQLAlchemy) | Entity (JPA) + Repository (JPA) | 100% |

</div>

### Patrones de diseño convergentes

**Ambos conjuntos tecnológicos implementan:**

- **Separación servidor/cliente:** API REST como contrato
- **Arquitectura en capas:** Controlador → Servicio → Repositorio
- **Patrón DTO:** Objetos de transferencia separados de entidades
- **Inyección de dependencias:** Explícita (Spring/Angular) o implícita (FastAPI/React)
- **Programación asíncrona:** Nativa en ambos (Python async, Java CompletableFuture/RxJS)

**Divergencias tecnológicas (esperadas):**

- **Momento de seguridad de tipos:** Tiempo de compilación (Java/TypeScript en Angular) vs tiempo de ejecución (sugerencias de tipo Python)
- **Enfoque de ID:** Dirigido por marco de trabajo (Spring/Angular) vs dirigido por biblioteca/patrón (FastAPI/React)
- **Programación reactiva:** RxJS en todas partes (Angular) vs asíncrono/esperar selectivo (React)

## Velocidad de desarrollo

### Tiempo de implementación

<div align=center>

| Caso de uso | FastAPI/React | Spring/Angular | Diferencia |
|-|-|-|-|
| `iniciarSesion()` | ~1h | ~1.5h | +50% Spring/Angular |
| `abrirAulas()` | ~30min | ~45min | +50% Spring/Angular |
| `crearAula()` | ~1h | ~1h | Igual |
| `editarAula()` | ~1h | ~1h | Igual |
| `eliminarAula()` | ~30min | ~30min | Igual |
| **Total conjunto completo** | ~4h | ~5h | +25% Spring/Angular |

</div>

**Factores que explican diferencia:**

- **Configuración inicial:** FastAPI más rápido (menos código repetitivo)
- **Configuración:** Spring Boot requiere más configuración inicial (aunque Spring Initializr ayuda)
- **Aprendizaje:** React más simple para casos básicos
- **Convergencia:** Casos complejos (CRUD) toman tiempo similar porque la complejidad está en lógica de negocio

### Curva de aprendizaje

<div align=center>

|FastAPI/React|Spring/Angular|
|-|-|
|✅ Rápido de empezar (menos conceptos iniciales)|⚠️ Curva inicial más pronunciada (muchos conceptos)|
|✅ Flexible (eliges tu camino)|⚠️ Más código ceremonial inicial|
|⚠️ Requiere decisiones arquitectónicas (sin convenciones fuertes)|✅ Convenciones fuertes (menos decisiones arquitectónicas)|
|⚠️ Ecosistema fragmentado (muchas opciones para cada problema)|✅ Ecosistema cohesivo (soluciones oficiales para todo)|

</div>

## Escalabilidad y mantenibilidad

### Escalabilidad técnica

<div align=center>

| Aspecto | FastAPI/React | Spring/Angular | Ganador |
|-|-|-|-|
| **Rendimiento bruto** | ~20k pet/s | ~15k pet/s | FastAPI |
| **Tiempo de inicio** | <1s | ~3-5s | FastAPI |
| **Memoria base** | ~50MB | ~200MB | FastAPI |
| **Escalabilidad horizontal** | Excelente (sin estado) | Excelente (sin estado) | Empate |
| **Caché, optimización** | Manual (Redis, etc) | Caché Spring (nativo) | Spring |
| **Microservicios** | Excelente (ligero) | Excelente (Spring Cloud) | Empate |

</div>

### Mantenibilidad a largo plazo

<div align=center>

| Aspecto | FastAPI/React | Spring/Angular | Ganador |
|-|-|-|-|
| **Seguridad de tipos** | Tiempo de ejecución (Pydantic) | Tiempo de compilación (Java) | Spring |
| **Herramientas de refactorización** | Medio (IDEs Python) | Excelente (IDEs Java) | Spring |
| **Cobertura de pruebas** | Depende de disciplina | Marcos de trabajo integrados | Spring |
| **Documentación automática** | Excelente (OpenAPI) | Buena (Swagger) | Empate |
| **Convenciones** | Débiles (libertad) | Fuertes (estructura) | Spring |
| **Escalado de equipo** | Bueno (hasta ~10 devs) | Excelente (100+ devs) | Spring |

</div>

## Conclusiones de la comparativa

### RUP cumple su promesa

**Evidencia:**

- 100% de artefactos de análisis sin modificación
- Responsabilidades MVC mapearon directamente a ambos stacks
- Tiempo de diseño comparable (lógica de negocio ya resuelta en análisis)
- Arquitecturas convergentes (patrones similares en ambos stacks)

**Implicación:** Un análisis RUP riguroso SÍ es tecnológicamente independiente.

### Diferencias son tecnológicas, no conceptuales

<div align=center>

|FastAPI/React es mejor para:|Spring/Angular es mejor para:|
|-|-|
Prototipos rápidos, MVPs, startups|Sistemas enterprise, aplicaciones críticas
Equipos pequeños (~2-10 desarrolladores)|Equipos grandes (~10-100+ desarrolladores)
Proyectos donde velocidad de desarrollo es crítica|Proyectos de larga vida (5-10+ años)
APIs modernas, microservicios ligeros|Aplicaciones complejas con muchos módulos

</div>

**Pero ambos implementan el mismo análisis sin modificarlo.**

### Lecciones para metodología RUP

1. **El análisis MVC es el MVP metodológico:** Sin análisis riguroso, la independencia tecnológica no funciona
2. **La separación de responsabilidades paga dividendos:** Boundary/Control/Entity mapearon perfectamente a ambos stacks
3. **Las especificaciones detalladas son reutilizables:** Diagramas de estado, wireframes, flujos se aplicaron sin cambios
4. **La disciplina metodológica reduce el tiempo total:** Aunque el análisis tomó tiempo, el diseño fue rápido en ambos stacks

### Próximos experimentos

**Pregunta pendiente:** ¿La independencia se mantiene con algoritmos complejos?

- **Caso de prueba:** `generarHorario()` (4 fases de optimización)
- **Hipótesis:** El análisis permanecerá inalterado
- **Validación:** Diseñar en ambos stacks y medir ajustes al análisis

**Pregunta adicional:** ¿Podemos agregar más stacks?

- **Candidatos:** Electron/Tauri (desktop), React Native/Flutter (mobile)
- **Hipótesis:** El análisis soportará tantos stacks como necesitemos
- **Validación:** Crear tercera y cuarta rama de diseño

## Referencias

- [Artículo principal](README.md)
- [Contexto del experimento](contexto.md)
- [Evidencia técnica](evidencia.md)
- [Análisis de casos de uso](https://github.com/mmasias/pySigHor/tree/main/RUP/01-analisis/casos-uso)
- [Diseño FastAPI/React](https://github.com/mmasias/pySigHor/tree/diseño-fastapi-react/RUP/02-diseño/casos-uso)
- [Diseño Spring/Angular](https://github.com/mmasias/pySigHor/tree/diseño-spring-angular/RUP/02-diseño/casos-uso)
