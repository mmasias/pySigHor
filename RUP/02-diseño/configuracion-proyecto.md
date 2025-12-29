# Configuración y estructura del proyecto

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración → Construcción
- **Disciplina**: Diseño
- **Versión**: 1.0 (Spring Boot + Angular)
- **Fecha**: 2025-12-29
- **Autor**: Claude Sonnet 4.5

## Propósito

Este documento define la estructura de directorios, configuraciones iniciales y decisiones técnicas necesarias para materializar la arquitectura diseñada en código ejecutable usando **Spring Boot + Angular**. Sirve como puente entre el diseño abstracto y la implementación concreta.

## Filosofía de organización

### Principios aplicados

1. **Separación de responsabilidades**: Backend Java y Frontend Angular en módulos independientes
2. **Escalabilidad**: Estructura que permite crecer sin reestructurar
3. **Convenciones sobre configuración**: Seguir estándares de Spring Boot y Angular CLI
4. **Trazabilidad**: Mapeo directo entre artefactos de diseño y código

## Estructura de directorios

### Vista general

```
pySigHor/
├── backend/                           # Aplicación Spring Boot
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/pysighor/
│   │   │   │   ├── config/           # Configuración (Security, JPA)
│   │   │   │   ├── entity/           # Entidades JPA
│   │   │   │   ├── dto/              # Data Transfer Objects
│   │   │   │   ├── repository/       # Repositorios Spring Data JPA
│   │   │   │   ├── service/          # Lógica de negocio
│   │   │   │   ├── controller/       # Controladores REST
│   │   │   │   ├── security/         # JWT, Filters, UserDetails
│   │   │   │   ├── exception/        # Manejo global de excepciones
│   │   │   │   └── PySighorApplication.java
│   │   │   └── resources/
│   │   │       ├── application.properties    # Configuración principal
│   │   │       ├── application-dev.properties
│   │   │       ├── application-prod.properties
│   │   │       └── data.sql          # Datos iniciales (seed)
│   │   └── test/                     # Tests unitarios e integración
│   ├── pom.xml                       # Dependencias Maven
│   └── .env.example                  # Plantilla variables de entorno
│
├── frontend/                          # Aplicación Angular
│   ├── src/
│   │   ├── app/
│   │   │   ├── core/                 # Servicios singleton, guards, interceptors
│   │   │   │   ├── services/         # AuthService, ApiService
│   │   │   │   ├── guards/           # AuthGuard
│   │   │   │   ├── interceptors/     # JwtInterceptor, ErrorInterceptor
│   │   │   │   └── models/           # Interfaces TypeScript
│   │   │   ├── shared/               # Componentes, directivas, pipes compartidos
│   │   │   ├── features/             # Módulos de funcionalidad
│   │   │   │   ├── auth/             # Login
│   │   │   │   ├── aulas/            # CRUD Aulas
│   │   │   │   └── dashboard/        # Dashboard principal
│   │   │   ├── app.component.ts      # Componente raíz
│   │   │   ├── app.routes.ts         # Configuración de rutas
│   │   │   └── app.config.ts         # Configuración de la app
│   │   ├── assets/                   # Recursos estáticos
│   │   ├── environments/             # Configuración por entorno
│   │   └── main.ts                   # Punto de entrada
│   ├── angular.json                  # Configuración Angular CLI
│   ├── package.json                  # Dependencias npm
│   ├── tsconfig.json                 # Configuración TypeScript
│   └── tsconfig.app.json
│
├── docs/                              # Documentación adicional
├── RUP/                               # Artefactos metodológicos
└── README.md                          # Documentación principal
```

### Justificación de la estructura

#### Backend: Arquitectura por capas (Spring Boot)

```
com.pysighor/
├── config/         → Configuración (SecurityConfig, JpaConfig)
├── entity/         → Entidades JPA (@Entity)
├── dto/            → Contratos de API (DTOs)
├── repository/     → Interfaces Spring Data JPA
├── service/        → Orquestación de lógica de negocio (@Service)
├── controller/     → Definición de endpoints REST (@RestController)
├── security/       → JWT, Filters, UserDetailsService
└── exception/      → Manejo global con @ControllerAdvice
```

**Flujo de una petición**:
```
Controller → Service → Repository → Entity → Database
   ↓             ↓
  DTO (input)   DTO (output)
```

Esta separación permite:
- **Testabilidad**: Cada capa puede probarse independientemente con Mockito
- **Mantenibilidad**: Cambios en BD no afectan lógica de negocio
- **Reutilización**: Servicios pueden llamarse desde múltiples controllers
- **Inyección de dependencias**: Spring gestiona el ciclo de vida de beans

#### Frontend: Organización por responsabilidad (Angular)

```
app/
├── core/         → Servicios singleton (providedIn: 'root')
├── shared/       → Componentes reutilizables (botones, modals)
├── features/     → Módulos de funcionalidad (auth, aulas)
└── app.routes.ts → Configuración de rutas standalone
```

**Flujo de una acción del usuario**:
```
Component → Service → HttpClient → API Backend
    ↓          ↓
  Template   RxJS Observable (estado)
```

## Configuraciones iniciales

### Backend: Spring Boot 3.x + JPA

#### 1. Dependencias (`backend/pom.xml`)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.1</version>
        <relativePath/>
    </parent>

    <groupId>com.pysighor</groupId>
    <artifactId>pysighor-backend</artifactId>
    <version>0.1.0</version>
    <name>pySigHor Backend</name>
    <description>API REST para sistema de generación de horarios universitarios</description>

    <properties>
        <java.version>17</java.version>
        <jjwt.version>0.12.3</jjwt.version>
    </properties>

    <dependencies>
        <!-- Spring Boot Starters -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>

        <!-- Database -->
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <scope>runtime</scope>
        </dependency>

        <!-- JWT -->
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-api</artifactId>
            <version>${jjwt.version}</version>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-impl</artifactId>
            <version>${jjwt.version}</version>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt-jackson</artifactId>
            <version>${jjwt.version}</version>
            <scope>runtime</scope>
        </dependency>

        <!-- Lombok (opcional, reduce boilerplate) -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
        </dependency>

        <!-- Testing -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>org.springframework.security</groupId>
            <artifactId>spring-security-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

**Justificación de dependencias clave**:
- `spring-boot-starter-web`: Framework REST con servidor Tomcat embebido
- `spring-boot-starter-data-jpa`: ORM JPA con Hibernate
- `spring-boot-starter-security`: Autenticación y autorización
- `h2`: Base de datos en memoria/fichero para desarrollo
- `jjwt`: Librería JWT para tokens de autenticación
- `lombok`: Reduce boilerplate (getters, setters, constructores)

#### 2. Configuración de aplicación (`backend/src/main/resources/application.properties`)

```properties
# Nombre de la aplicación
spring.application.name=pySigHor

# Puerto del servidor
server.port=8080

# Configuración de la base de datos H2
spring.datasource.url=jdbc:h2:file:./data/pysighor
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

# Configuración JPA/Hibernate
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
spring.jpa.hibernate.ddl-auto=update
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true

# Consola H2 (solo desarrollo)
spring.h2.console.enabled=true
spring.h2.console.path=/h2-console

# Configuración JWT
jwt.secret=${JWT_SECRET:mySecretKeyForDevelopmentPleaseChangeInProduction}
jwt.expiration=86400000

# Configuración de logging
logging.level.com.pysighor=DEBUG
logging.level.org.springframework.security=DEBUG
logging.level.org.hibernate.SQL=DEBUG
```

#### 3. Configuración de desarrollo (`application-dev.properties`)

```properties
# Perfil de desarrollo
spring.config.activate.on-profile=dev

# Consola H2 habilitada
spring.h2.console.enabled=true

# Inicialización de datos
spring.jpa.defer-datasource-initialization=true
spring.sql.init.mode=always

# CORS permitido para desarrollo local
cors.allowed-origins=http://localhost:4200
```

#### 4. Configuración de producción (`application-prod.properties`)

```properties
# Perfil de producción
spring.config.activate.on-profile=prod

# Desactivar consola H2
spring.h2.console.enabled=false

# No mostrar SQL
spring.jpa.show-sql=false

# Logging reducido
logging.level.com.pysighor=INFO
logging.level.org.springframework=WARN
```

### Frontend: Angular 17+

#### 1. Dependencias (`frontend/package.json`)

```json
{
  "name": "pysighor-frontend",
  "version": "0.1.0",
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "watch": "ng build --watch --configuration development",
    "test": "ng test",
    "lint": "ng lint"
  },
  "private": true,
  "dependencies": {
    "@angular/animations": "^17.0.0",
    "@angular/common": "^17.0.0",
    "@angular/compiler": "^17.0.0",
    "@angular/core": "^17.0.0",
    "@angular/forms": "^17.0.0",
    "@angular/platform-browser": "^17.0.0",
    "@angular/platform-browser-dynamic": "^17.0.0",
    "@angular/router": "^17.0.0",
    "@angular/material": "^17.0.0",
    "rxjs": "~7.8.0",
    "tslib": "^2.6.0",
    "zone.js": "~0.14.2"
  },
  "devDependencies": {
    "@angular-devkit/build-angular": "^17.0.0",
    "@angular/cli": "^17.0.0",
    "@angular/compiler-cli": "^17.0.0",
    "@types/jasmine": "~5.1.0",
    "jasmine-core": "~5.1.0",
    "karma": "~6.4.0",
    "karma-chrome-launcher": "~3.2.0",
    "karma-coverage": "~2.2.0",
    "karma-jasmine": "~5.1.0",
    "karma-jasmine-html-reporter": "~2.1.0",
    "typescript": "~5.2.2"
  }
}
```

**Justificación de dependencias clave**:
- `@angular/core`, `@angular/common`: Framework base de Angular
- `@angular/forms`: Formularios reactivos
- `@angular/router`: Enrutamiento SPA
- `@angular/material`: Librería de componentes UI (opcional: Bootstrap)
- `rxjs`: Programación reactiva con Observables

#### 2. Configuración de entorno (`frontend/src/environments/environment.ts`)

```typescript
export const environment = {
  production: false,
  apiUrl: 'http://localhost:8080/api'
};
```

#### 3. Configuración de entorno producción (`frontend/src/environments/environment.prod.ts`)

```typescript
export const environment = {
  production: true,
  apiUrl: 'https://api.pysighor.com/api'
};
```

## Esquema de base de datos

### Script de inicialización (`backend/src/main/resources/data.sql`)

```sql
-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    rol VARCHAR(20) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Tabla de aulas
CREATE TABLE IF NOT EXISTS aulas (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    capacidad INTEGER NOT NULL,
    edificio VARCHAR(50) NOT NULL
);

-- Datos iniciales (seed)
INSERT INTO usuarios (username, password_hash, rol, is_active)
VALUES ('admin', '$2a$10$N9qo8UiLU8m1I7J1d8vKS.QnKnH8LqZ1i6J8x8vKS.QnKnH8LqZ1i', 'ADMIN', TRUE);

INSERT INTO aulas (nombre, capacidad, edificio)
VALUES
  ('Aula 101', 30, 'Edificio A'),
  ('Aula 102', 25, 'Edificio A'),
  ('Aula 201', 40, 'Edificio B');
```

**Nota**: El hash de password es para la contraseña `admin123` usando BCrypt.

## Mapeo entre artefactos de diseño y código

### Diagrama de clases de diseño → Código Java

| Artefacto de Diseño | Clase Java | Paquete |
|---------------------|------------|---------|
| Usuario (Entidad) | `Usuario.java` | `com.pysighor.entity` |
| Aula (Entidad) | `Aula.java` | `com.pysighor.entity` |
| AulaDTO | `AulaDTO.java` | `com.pysighor.dto` |
| AulaCreateDTO | `AulaCreateDTO.java` | `com.pysighor.dto` |
| AulaUpdateDTO | `AulaUpdateDTO.java` | `com.pysighor.dto` |
| JwtResponse | `JwtResponse.java` | `com.pysighor.dto` |
| LoginRequest | `LoginRequest.java` | `com.pysighor.dto` |
| UsuarioRepository | `UsuarioRepository.java` | `com.pysighor.repository` |
| AulaRepository | `AulaRepository.java` | `com.pysighor.repository` |
| AuthService | `AuthService.java` | `com.pysighor.service` |
| AulaService | `AulaService.java` | `com.pysighor.service` |
| AuthController | `AuthController.java` | `com.pysighor.controller` |
| AulaController | `AulaController.java` | `com.pysighor.controller` |
| JwtTokenProvider | `JwtTokenProvider.java` | `com.pysighor.security` |
| JwtAuthenticationFilter | `JwtAuthenticationFilter.java` | `com.pysighor.security` |

### Diagrama de secuencia → Endpoints REST

| Caso de Uso | Método HTTP | Endpoint | Controller | Método |
|-------------|-------------|----------|------------|--------|
| iniciarSesion | POST | `/api/auth/login` | `AuthController` | `login()` |
| abrirAulas | GET | `/api/aulas` | `AulaController` | `listar()` |
| crearAula | POST | `/api/aulas` | `AulaController` | `crear()` |
| editarAula | PUT | `/api/aulas/{id}` | `AulaController` | `editar()` |
| eliminarAula | DELETE | `/api/aulas/{id}` | `AulaController` | `eliminar()` |

## Comandos de desarrollo

### Backend (Spring Boot)

```bash
# Instalar dependencias y compilar
mvn clean install

# Ejecutar aplicación (perfil dev)
mvn spring-boot:run -Dspring-boot.run.profiles=dev

# Ejecutar tests
mvn test

# Empaquetar JAR
mvn package

# Ejecutar JAR empaquetado
java -jar target/pysighor-backend-0.1.0.jar
```

### Frontend (Angular)

```bash
# Instalar dependencias
npm install

# Ejecutar servidor de desarrollo (http://localhost:4200)
npm start

# Compilar para producción
npm run build

# Ejecutar tests unitarios
npm test

# Ejecutar linter
npm run lint
```

### Desarrollo full-stack local

1. **Terminal 1 - Backend**:
   ```bash
   cd backend
   mvn spring-boot:run -Dspring-boot.run.profiles=dev
   ```
   API disponible en `http://localhost:8080`

2. **Terminal 2 - Frontend**:
   ```bash
   cd frontend
   npm start
   ```
   App disponible en `http://localhost:4200`

3. **Acceso a consola H2**: `http://localhost:8080/h2-console`
   - JDBC URL: `jdbc:h2:file:./data/pysighor`
   - Usuario: `sa`
   - Password: (vacío)

## Notas de implementación

### Seguridad

1. **JWT Secret**: En producción, usar variable de entorno `JWT_SECRET` con valor seguro
2. **CORS**: Configurar `cors.allowed-origins` según dominio de producción
3. **Passwords**: Todos los passwords se hashean con BCrypt (costo 10)

### Performance

1. **Paginación**: Usar `Pageable` de Spring Data para listas grandes
2. **DTOs**: Siempre exponer DTOs, nunca entidades JPA directamente
3. **Lazy Loading**: Configurar relaciones JPA como `LAZY` por defecto

### Testing

1. **Backend**: Tests con `@SpringBootTest`, `@WebMvcTest`, Mockito
2. **Frontend**: Tests con Jasmine/Karma para componentes y servicios

## Próximos pasos

1. Implementar clases de entidad JPA (`Usuario`, `Aula`)
2. Crear repositorios Spring Data JPA
3. Implementar servicios de negocio
4. Crear controladores REST
5. Configurar Spring Security + JWT
6. Desarrollar componentes Angular
7. Integrar frontend-backend
8. Tests de integración
