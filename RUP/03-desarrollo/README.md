<div align=right>

|[![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../01-analisis/casos-uso/README.md) [![](https://img.shields.io/badge/-Diseño-FFF?style=flat&logo=draw.io&logoColor=black)](../02-diseño/README.md) [![](https://img.shields.io/badge/-Desarrollo-FFF?style=flat&logo=github&logoColor=black)](README.md)|
|-|

</div>

# Fase de desarrollo - Hoja de ruta

## Contexto

Este documento define el camino desde el diseño completo hasta el software funcional. Es el **puente entre el "qué" (análisis), el "cómo" (diseño) y el "hacer" (implementación)**.

### De dónde venimos

<div align=center>

|Fase|Estado|Artefactos|
|-|-|-|
|**00 - Requisitos**|✅ Completado|32 casos de uso especificados|
|**01 - Análisis**|✅ Completado|32 diagramas MVC tecnológicamente neutros|
|**02 - Diseño**|✅ Completado (5 CdU)|Arquitectura Spring/Angular + 5 diagramas de secuencia|

</div>

### Hito metodológico

> Vamos a validar que el análisis RUP riguroso se materializa correctamente en código funcional.
>
> Si RUP cumple su promesa, el código será coherente con el análisis y el diseño sin necesidad de revisar artefactos previos.

## Infraestructura necesaria (PREVIA a desarrollo de casos de uso)

Estos componentes deben implementarse **antes** de cualquier caso de uso funcional. Son los cimientos sobre los que se construirá el resto del sistema.

### Backend: Spring Boot

<div align=center>

|Componente|Diseño|Archivo|Estado|
|-|:-:|-|-|
|Proyecto Maven|✅|`backend/pom.xml`|⏳ Pendiente|
|Configuración principal|✅|`application.properties`|⏳ Pendiente|
|Configuración desarrollo|✅|`application-dev.properties`|⏳ Pendiente|
|Clase principal|✅|`Sighor.java`|⏳ Pendiente|
|Configuración JPA|✅|`JpaConfig.java`|⏳ Pendiente|
|Configuración Security|✅|`SecurityConfig.java`|⏳ Pendiente|
|JWT Token Provider|✅|`JwtTokenProvider.java`|⏳ Pendiente|
|JWT Filter|✅|`JwtAuthenticationFilter.java`|⏳ Pendiente|
|Excepciones globales|✅|`GlobalExceptionHandler.java`|⏳ Pendiente|
|Configuración CORS|✅|`CorsConfig.java`|⏳ Pendiente|

</div>

### Frontend: Angular

<div align=center>

|Componente|Diseño|Archivo|Estado|
|-|:-:|-|-|
|Proyecto Angular|✅|`frontend/package.json`|⏳ Pendiente|
|Configuración entorno|✅|`environments/environment.ts`|⏳ Pendiente|
|Configuración rutas|✅|`app.routes.ts`|⏳ Pendiente|
|Configuración aplicación|✅|`app.config.ts`|⏳ Pendiente|
|Interceptor JWT|✅|`jwt.interceptor.ts`|⏳ Pendiente|
|Interceptor errores|✅|`error.interceptor.ts`|⏳ Pendiente|
|Guard de autenticación|✅|`auth.guard.ts`|⏳ Pendiente|
|Servicio API base|✅|`api.service.ts`|⏳ Pendiente|

</div>

### Base de datos

<div align=center>

|Componente|Diseño|Script|Estado|
|-|:-:|-|-|
|Esquema inicial|✅|`data.sql`|⏳ Pendiente|
|Datos de prueba|✅|`data.sql`|⏳ Pendiente|

</div>

## Casos de uso a implementar

Los 5 casos de uso diseñados en orden de dependencia:

### Orden de implementación recomendado

```
1. iniciarSesion() ────┐
                       ├──→ Dependen de auth
2. abrirAulas() ───────┘
                       ├──→ Dependen de aulas base
3. crearAula()
4. editarAula()
5. eliminarAula()
```

### Matriz de implementación

<div align=center>

|#|Caso de Uso|Backend (Controller)|Frontend (Component)|Tests|Estado|
|-|-|-|-|-|-|
|1|[`iniciarSesion()`](01-iniciarSesion/README.md)|`AuthController.login()`|`LoginComponent`|`AuthTests`|⏳ Pendiente|
|2|[`abrirAulas()`](02-abrirAulas/README.md)|`AulaController.listar()`|`AulasListComponent`|`AulaTests`|⏳ Pendiente|
|3|[`crearAula()`](03-crearAula/README.md)|`AulaController.crear()`|`AulaFormComponent`|`AulaTests`|⏳ Pendiente|
|4|[`editarAula()`](04-editarAula/README.md)|`AulaController.editar()`|`AulaFormComponent`|`AulaTests`|⏳ Pendiente|
|5|[`eliminarAula()`](05-eliminarAula/README.md)|`AulaController.eliminar()`|`AulasListComponent`|`AulaTests`|⏳ Pendiente|

</div>

## Mapeo: de diseño a código

> **Nota metodológica**: La arquitectura y estructura del sistema ya están definidas en la fase de [Diseño](../02-diseño/README.md). Esta sección muestra cómo se materializan en código Spring/Angular.

### Backend: materialización del diseño

La arquitectura por capas está definida en [Diseño → Diagrama de clases](../02-diseño/clases-diseño.puml).

<div align=center>

|![Diagrama de clases de diseño](/images/RUP/02-diseño/clases-diseño.svg)|
|:-:|
|[Ver diagrama completo en Diseño](../02-diseño/clases-diseño.puml)|

| Capa (Diseño) | Anotación Spring | Paquete | Responsabilidad |
|-|-|-|-|
| Controller | `@RestController` | `controller/` | Endpoints REST, manejo HTTP |
| Service | `@Service` | `service/` | Lógica de negocio, orquestación |
| Repository | `JpaRepository` | `repository/` | Acceso a datos (Spring Data JPA) |
| Entity | `@Entity` | `entity/` | Entidades JPA, mapeo BD |
| DTO | (ninguna) | `dto/` | Contratos de API |
| Security | `@Component` | `security/` | JWT, filtros, autenticación |

</div>

### Frontend: materialización del diseño

La organización de componentes está definida en [Diseño → Configuración del proyecto](../02-diseño/configuracion-proyecto.md).

<div align=center>

| Tipo | Ubicación Angular | Propósito |
|-|-|-|
| **Servicios core** | `core/services/` | Singleton inyectables en toda la app |
| **Guards** | `core/guards/` | Protección de rutas |
| **Interceptors** | `core/interceptors/` | JWT inyección, manejo de errores |
| **Features** | `features/*/` | Módulos funcionales lazy-loaded |
| **Shared** | `shared/` | Componentes reutilizables |

</div>

## Checklist de inicio de sesión de desarrollo

Antes de implementar cualquier caso de uso, verificar:

- [ ] **JDK 17+ instalado** (`java -version`)
- [ ] **Maven 3.6+ instalado** (`mvn -version`)
- [ ] **Node.js 18+ instalado** (`node -v`)
- [ ] **npm 9+ instalado** (`npm -v`)
- [ ] **IDE configurado** (IntelliJ IDEA recomendado para Spring/Angular)
- [ ] **Git configurado** para esta rama
- [ ] **Base de datos H2** seleccionada (ya viene en dependencias Maven)

## Referencia de comandos

### Backend

```bash
# Crear proyecto Spring Boot inicial
mvn archetype:generate -DgroupId=com.pysighor -DartifactId=pysighor-backend \
  -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

# Ejecutar backend (desde backend/)
mvn spring-boot:run -Dspring-boot.run.profiles=dev

# Compilar y ejecutar tests
mvn clean install && mvn test

# Empaquetar para producción
mvn clean package -DskipTests
```

### Frontend

```bash
# Crear proyecto Angular (standalone)
ng new pysighor-frontend --standalone --routing --style=css

# Ejecutar frontend (desde frontend/)
npm start

# Compilar para producción
npm run build

# Ejecutar tests
npm test
```

## Estrategia de Testing

### Backend

<div align=center>

|Tipo|Herramienta|Qué prueba|
|-|-|-|
|Unitario|JUnit 5 + Mockito|Clases individuales (Service, Repository)|
|Integración|`@SpringBootTest`|Flujo completo Controller→Service→Repository|
|Contract|RestAssured|Endpoints REST contra especificación|

</div>

### Frontend

<div align=center>

|Tipo|Herramienta|Qué prueba|
|-|-|-|
|Unitario|Jasmine + Karma|Componentes y Services aislados|
|Integración|Angular Testing Utilities|Componente con sus dependencias|
|E2E|Playwright/Cypress|Flujos completos de usuario|

</div>

## Seguimiento de progreso

Esta tabla se actualizará conforme avancemos. Cada casilla marcada representa un componente funcional y probado.

### Infraestructura Backend

- [ ] Proyecto Maven creado
- [ ] `application.properties` configurado
- [ ] `JpaConfig` implementado
- [ ] `SecurityConfig` implementado
- [ ] `JwtTokenProvider` implementado
- [ ] `GlobalExceptionHandler` implementado

### Infraestructura Frontend

- [ ] Proyecto Angular creado
- [ ] Rutas configuradas
- [ ] `AuthService` implementado
- [ ] `ApiService` implementado
- [ ] `AuthGuard` implementado
- [ ] Interceptores configurados

### Casos de Uso

<div align=center>

|#|Caso|Backend|Frontend|Tests|Integración|
|-|-|:-:|:-:|:-:|:-:|
|1|iniciarSesion|⏳|⏳|⏳|⏳|
|2|abrirAulas|⏳|⏳|⏳|⏳|
|3|crearAula|⏳|⏳|⏳|⏳|
|4|editarAula|⏳|⏳|⏳|⏳|
|5|eliminarAula|⏳|⏳|⏳|⏳|

</div>

## Próximo paso inmediato

**[01 - Infraestructura Backend](00-infraestructura/README.md)** → Configurar proyecto Spring Boot desde cero.

> **Nota**: Esta fase de desarrollo demuestra la **validez práctica de RUP**. Si el análisis y el diseño fueron bien hechos, la implementación debería ser directa - solo traducir decisiones ya tomadas a código. Si encontramos problemas, es señal de que debemos revisar el diseño (o el análisis).
