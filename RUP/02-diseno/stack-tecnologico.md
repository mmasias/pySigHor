# Stack Tecnológico Recomendado - pySigHor Web

<div align=right>

|[![](https://img.shields.io/badge/-Diseño-FFF?style=flat&logo=archlinux&logoColor=black)](README.md) [![](https://img.shields.io/badge/-Stack_Tecnológico-FFF?style=flat&logo=stackshare&logoColor=black)](stack-tecnologico.md)|
|-:

</div>

## Información del artefacto

- **Proyecto**: pySigHor - Stack tecnológico para versión web
- **Fase RUP**: Elaboration (Elaboración) - Arquitectura
- **Versión**: 1.0
- **Fecha**: 2025-01-13
- **Autor**: Equipo de desarrollo

## Resumen Ejecutivo

**Stack recomendado**: **React + Spring Boot + PostgreSQL** con arquitectura REST API, basado en análisis de 32 casos de uso RUP completados y algoritmo de optimización de 4 fases especificado.

### Decisión Arquitectónica Principal
**Separación Frontend/Backend**: Arquitectura desacoplada que permite múltiples clientes (web, mobile futuro) consumiendo la misma API REST.

## Análisis de Requisitos desde RUP

### Complejidad Algorítmica Identificada
- **Algoritmo de 4 fases**: PrepararH() → GeneraPreHorario() → GeneraHorario() → IngresoHE()
- **Optimización dual**: Minimización Z + maximización compatibilidad aula-profesor
- **Procesamiento intensivo**: Hasta 8 bloques horarios × múltiples cursos × resolución de conflictos

### Patrones Arquitectónicos del Análisis
- **MVC establecido**: 32 casos con separación View/Controller/Repository
- **CRUD sistemático**: Patrón "C→U" (crear delgado → editar gordo) implementado
- **Include relationships**: Casos de eliminación incluyen navegación automática

### Entidades del Dominio
- **6 entidades principales**: Programa, Curso, Profesor, Aula, Edificio, Recurso
- **1 entidad integradora**: Horario (resultado del algoritmo)
- **Relaciones complejas**: Agregación + preferencias + restricciones temporales

## Stack Tecnológico Recomendado

### 🎯 **Backend: Spring Boot 3.2 + Java 17**

#### Justificación técnica
- **Algoritmo complejo**: JVM optimizada para procesamiento intensivo del algoritmo de horarios
- **Arquitectura MVC**: Spring MVC mapea perfectamente a análisis realizado
- **Ecosistema maduro**: Spring Data JPA, Spring Security, Spring Boot Actuator
- **Escalabilidad**: Preparado para múltiples usuarios simultáneos generando horarios

#### Características clave
- **Spring Data JPA**: Implementación directa de repositories analizados
- **Spring Security**: Manejo robusto del caso `iniciarSesion()`
- **Spring Boot Actuator**: Monitoreo del algoritmo de optimización
- **Validation**: Implementación directa de validaciones especificadas

### 🎯 **Frontend: React 18 + TypeScript**

#### Justificación técnica
- **32 casos de uso**: React maneja eficientemente navegación compleja entre estados
- **Wireframes SALT**: Componentes React mapean directamente a prototipos especificados
- **Estados del sistema**: React State + Context API para navegación entre vistas
- **Reutilización**: Filosofía C→U implementable con componentes reutilizables

#### Tecnologías complementarias
- **React Router**: Navegación entre estados del diagrama de contexto
- **React Hook Form**: Formularios de edición complejos (editarCurso, editarProfesor)
- **Axios**: Cliente HTTP para consumir API REST
- **Material-UI**: Sistema de componentes que acelera desarrollo de CRUD

### 🎯 **Base de Datos: PostgreSQL 15**

#### Justificación técnica
- **Algoritmo de optimización**: Consultas complejas optimizadas (JOINs, subconsultas)
- **Integridad referencial**: Restricciones del dominio implementadas a nivel BD
- **ACID**: Transacciones para generación de horarios sin corrupción de datos
- **Índices avanzados**: Optimización para consultas del algoritmo

#### Modelo físico derivado
- **6 tablas principales**: programas, cursos, profesores, aulas, edificios, recursos
- **Tablas de relación**: profesor_recursos (preferencias), curso_programas
- **Tabla de resultados**: horarios (salida del algoritmo)
- **Tablas temporales**: Para fases intermedias del algoritmo

### 🔧 **Herramientas de Desarrollo**

#### Control de versiones y CI/CD
- **Git**: Ya establecido en el proyecto
- **GitHub Actions**: CI/CD para builds automáticos
- **Docker**: Contenedorización para despliegue

#### Testing
- **JUnit 5**: Testing unitario del algoritmo backend
- **React Testing Library**: Testing de componentes frontend
- **Testcontainers**: Testing de integración con PostgreSQL

#### Documentación API
- **OpenAPI 3.0/Swagger**: Especificación de API REST derivada de casos de uso
- **Postman**: Testing manual de endpoints

## Mapeo Análisis RUP → Tecnología

### Casos de Uso → Endpoints REST

| Caso de Uso RUP | Método HTTP | Endpoint | Justificación |
|------------------|-------------|----------|---------------|
| `crearPrograma()` | POST | `/api/programas` | Creación de recurso |
| `editarPrograma()` | PUT | `/api/programas/{id}` | Actualización completa |
| `eliminarPrograma()` | DELETE | `/api/programas/{id}` | Eliminación con confirmación |
| `abrirProgramas()` | GET | `/api/programas` | Listado con filtros |
| `generarHorario()` | POST | `/api/horarios/generar` | Algoritmo de optimización |
| `consultarHorario()` | GET | `/api/horarios` | Consulta de resultados |

### Análisis MVC → Arquitectura Spring

| Elemento RUP | Tecnología Spring | Implementación |
|--------------|-------------------|----------------|
| **View** (análisis) | **@RestController** | Endpoints REST JSON |
| **Controller** (análisis) | **@Service** | Lógica de negocio |
| **Repository** (análisis) | **@Repository + JPA** | Acceso a datos |
| **Model** (dominio) | **@Entity** | Entidades JPA |

### Estados del Sistema → Navegación React

| Estado RUP | Componente React | Navegación |
|------------|------------------|------------|
| `NO_AUTENTICADO` | `LoginPage` | `/login` |
| `MENU_PRINCIPAL` | `Dashboard` | `/dashboard` |
| `PROGRAMAS_ABIERTO` | `ProgramasListPage` | `/programas` |
| `PROGRAMA_ABIERTO` | `ProgramaEditPage` | `/programas/{id}` |

## Arquitectura del Sistema

### Separación de Responsabilidades

```
┌─────────────────┐    HTTP/REST    ┌─────────────────┐    JPA/SQL    ┌─────────────────┐
│   React Client  │ ◄──────────────► │  Spring Boot    │ ◄────────────► │   PostgreSQL    │
│                 │      JSON       │     Backend     │    Entities   │    Database     │
│  - Components   │                 │  - Controllers  │               │  - Tables       │
│  - State Mgmt   │                 │  - Services     │               │  - Indexes      │
│  - Navigation   │                 │  - Repositories │               │  - Constraints  │
└─────────────────┘                 └─────────────────┘               └─────────────────┘
```

### Flujo de Datos Típico

1. **Usuario interactúa** → Componente React
2. **Estado actualizado** → React State/Context
3. **HTTP Request** → Axios → Spring Controller
4. **Lógica de negocio** → Spring Service (implementa casos de uso)
5. **Acceso datos** → Spring Repository → PostgreSQL
6. **Respuesta JSON** → React Component → UI Update

## Consideraciones de Implementación

### Algoritmo de Generación de Horarios

#### Implementación Backend (Spring)
```java
@Service
public class GenerarHorarioService {
    // Fase 1: PrepararH() - Resolución de conflictos
    public void prepararHorarios(List<Curso> cursos) { ... }
    
    // Fase 2: GeneraPreHorario() - Optimización dual
    public PreHorario generarPreHorario(int bloqueH) { ... }
    
    // Fase 3: GeneraHorario() - Materialización
    public Horario generarHorario(PreHorario preHorario) { ... }
    
    // Fase 4: IngresoHE() - Casos especiales
    public void procesarHorariosEspeciales() { ... }
}
```

#### Consumo Frontend (React)
```javascript
// Hook para generación de horarios
const useGenerarHorario = () => {
  const [estado, setEstado] = useState('inicial');
  const [progreso, setProgreso] = useState(0);
  
  const generar = async () => {
    setEstado('preparando'); // PrepararH()
    setEstado('optimizando'); // GeneraPreHorario()
    setEstado('materializando'); // GeneraHorario()
    setEstado('completado'); // Resultado final
  };
};
```

### Casos CRUD - Filosofía C→U

#### Implementación de "El Delgado" + "El Gordo"
```javascript
// crearPrograma() - "El delgado"
const CrearPrograma = () => {
  const crear = async (datosMinimos) => {
    const programa = await api.post('/programas', datosMinimos);
    navigate(`/programas/${programa.id}/editar`); // → "El gordo"
  };
};

// editarPrograma() - "El gordo"  
const EditarPrograma = () => {
  // Formulario completo con todas las funcionalidades
  // Recibe tanto programas nuevos como existentes
};
```

## Cronograma de Implementación Sugerido

### Fase 1: Infraestructura Base (2-3 semanas)
- [ ] Configuración Spring Boot + PostgreSQL
- [ ] Modelo de datos físico
- [ ] Configuración React + TypeScript
- [ ] CI/CD básico

### Fase 2: API Core (3-4 semanas)
- [ ] Endpoints CRUD básicos (6 entidades)
- [ ] Autenticación y autorización
- [ ] Validaciones de dominio
- [ ] Testing unitario

### Fase 3: Algoritmo de Optimización (4-5 semanas)
- [ ] Implementación de las 4 fases
- [ ] Optimización de consultas
- [ ] Manejo de casos especiales
- [ ] Testing del algoritmo

### Fase 4: Frontend Completo (4-5 semanas)
- [ ] Componentes CRUD reutilizables
- [ ] Navegación completa entre estados
- [ ] Formularios de edición complejos
- [ ] Interfaz de generación de horarios

### Fase 5: Integración y Despliegue (2-3 semanas)
- [ ] Testing de integración completo
- [ ] Optimización de rendimiento
- [ ] Documentación técnica
- [ ] Despliegue en producción

## Alternativas Consideradas

### Backend Alternativo: Django + Python
- **Pros**: Sintaxis más cercana al algoritmo original, ORM robusto
- **Contras**: Rendimiento inferior para algoritmo intensivo, menos tipado
- **Decisión**: Spring Boot seleccionado por optimización JVM

### Frontend Alternativo: Angular
- **Pros**: Framework completo, TypeScript nativo
- **Contras**: Mayor curva de aprendizaje, más opinionado
- **Decisión**: React seleccionado por flexibilidad y ecosistema

### Base de Datos Alternativa: MongoDB
- **Pros**: Esquema flexible, JSON nativo
- **Contras**: Consultas complejas menos eficientes, sin integridad referencial
- **Decisión**: PostgreSQL por naturaleza relacional del dominio

## Conclusiones

### Beneficios del Stack Seleccionado
1. **Mapeo directo**: Tecnologías alineadas con análisis RUP
2. **Rendimiento**: Optimizado para algoritmo computacionalmente intensivo
3. **Escalabilidad**: Arquitectura preparada para crecimiento
4. **Mantenibilidad**: Separación clara de responsabilidades
5. **Ecosistema**: Herramientas maduras y bien documentadas

### Riesgos Identificados
1. **Complejidad del algoritmo**: Requiere optimización cuidadosa
2. **Curva de aprendizaje**: Stack completo requiere conocimiento amplio
3. **Integración**: Coordinación entre múltiples tecnologías

### Próximos Pasos
1. **Validación con stakeholders**: Confirmar decisiones arquitectónicas
2. **Prototipo técnico**: Implementar caso de uso crítico end-to-end
3. **Arquitectura detallada**: Diagramas de componentes y despliegue
4. **Planificación iterativa**: División en incrementos de desarrollo

---

*Este documento será actualizado conforme se refine la arquitectura durante la implementación*