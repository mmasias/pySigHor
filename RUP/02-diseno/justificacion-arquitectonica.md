# Justificación Arquitectónica - pySigHor Web

<div align=right>

|[![](https://img.shields.io/badge/-Diseño-FFF?style=flat&logo=archlinux&logoColor=black)](README.md) [![](https://img.shields.io/badge/-Justificación-FFF?style=flat&logo=reason&logoColor=black)](justificacion-arquitectonica.md)|
|-:

</div>

## Información del artefacto

- **Proyecto**: pySigHor - Justificación arquitectónica
- **Fase RUP**: Elaboration (Elaboración) - Architecture-driven
- **Versión**: 1.0
- **Fecha**: 2025-01-13
- **Autor**: Equipo de desarrollo

## Propósito

Este documento justifica las **decisiones arquitectónicas clave** del stack tecnológico propuesto, demostrando cómo cada decisión se deriva directamente del **análisis RUP completado** y respeta los principios de **independencia tecnológica** establecidos.

## Principios Arquitectónicos RUP

### 1. Architecture-driven Development
**Principio**: La arquitectura debe emerger del análisis, no precederlo.

**Aplicación en pySigHor**:
- ✅ **32 casos de uso analizados** → Decisiones de API REST
- ✅ **6 entidades del dominio** → Modelo de datos físico
- ✅ **Patrones MVC identificados** → Separación frontend/backend
- ✅ **Algoritmo de 4 fases especificado** → Selección JVM para performance

### 2. Preservación de Independencia Tecnológica
**Principio**: El análisis debe ser válido independientemente de la implementación tecnológica.

**Validación**:
- ✅ **Vocabulario RUP puro**: "Actor solicita, Sistema presenta" → Mapeable a cualquier UI
- ✅ **Estados sin sesgo tecnológico**: `PROGRAMAS_ABIERTO` → Implementable en web/desktop/mobile
- ✅ **Colaboraciones MVC abstractas** → Traducibles a Spring, Django, Express, etc.

### 3. Risk-driven Iteration
**Principio**: Abordar primero los riesgos arquitectónicos más críticos.

**Riesgos identificados y mitigados**:
1. **Algoritmo complejo de optimización** → JVM + Spring Boot
2. **32 casos CRUD sistemáticos** → React + componentes reutilizables
3. **Navegación compleja entre estados** → React Router + Context API
4. **Consultas intensivas de BD** → PostgreSQL + índices optimizados

## Mapeo Análisis → Arquitectura

### Del Modelo del Dominio al Modelo de Datos

#### Entidades Conceptuales (RUP) → Tablas Físicas (PostgreSQL)

| Entidad RUP | Tabla PostgreSQL | Justificación |
|-------------|------------------|---------------|
| **Programa** | `programas` | Entidad independiente, cardinalidad 1:N con cursos |
| **Curso** | `cursos` | Entidad central, múltiples relaciones |
| **Profesor** | `profesores` | Entidad independiente con preferencias complejas |
| **Aula** | `aulas` | Entidad con capacidad y recursos |
| **Edificio** | `edificios` | Agregación 1:N con aulas |
| **Recurso** | `recursos` | Entidad de configuración |
| **Horario** | `horarios` | **Tabla integradora** - resultado del algoritmo |

#### Relaciones Conceptuales → Constraints SQL

```sql
-- Agregación: Horario referencia entidades (análisis RUP)
ALTER TABLE horarios 
  ADD CONSTRAINT fk_horario_profesor FOREIGN KEY (profesor_id) REFERENCES profesores(id),
  ADD CONSTRAINT fk_horario_curso FOREIGN KEY (curso_id) REFERENCES cursos(id),
  ADD CONSTRAINT fk_horario_aula FOREIGN KEY (aula_id) REFERENCES aulas(id);

-- Preferencias (análisis MVC): Profesor → Recursos
CREATE TABLE profesor_recursos (
  profesor_id INTEGER REFERENCES profesores(id),
  recurso_id INTEGER REFERENCES recursos(id),
  PRIMARY KEY (profesor_id, recurso_id)
);
```

### Del Análisis MVC a la Arquitectura Spring Boot

#### Patrón Identificado en Análisis → Implementación Tecnológica

**Ejemplo: `editarCurso()` MVC Collaboration**

**Análisis RUP** (independiente de tecnología):
```
EditarCursoView → CursoController → CursoRepository → Curso
```

**Implementación Spring Boot** (tecnología específica):
```java
@RestController  // ← EditarCursoView (API REST)
public class CursoController {
    
    @Autowired
    private CursoService cursoService;  // ← CursoController (lógica negocio)
    
    @PutMapping("/api/cursos/{id}")
    public ResponseEntity<Curso> editarCurso(@PathVariable Long id, @RequestBody Curso curso) {
        return ResponseEntity.ok(cursoService.actualizar(id, curso));
    }
}

@Service  // ← CursoController (análisis)
public class CursoService {
    
    @Autowired
    private CursoRepository cursoRepository;  // ← CursoRepository (análisis)
    
    public Curso actualizar(Long id, Curso curso) {
        // Lógica de negocio derivada del caso de uso
    }
}

@Repository  // ← CursoRepository (análisis)
public interface CursoRepository extends JpaRepository<Curso, Long> {
    // Acceso a datos como especificado en análisis
}

@Entity  // ← Curso (modelo del dominio)
public class Curso {
    // Atributos derivados del modelo conceptual RUP
}
```

### De los Estados del Sistema a la Navegación React

#### Diagrama de Contexto → React Router

**Estados RUP** (independientes de tecnología):
```
NO_AUTENTICADO → iniciarSesion() → MENU_PRINCIPAL
MENU_PRINCIPAL → abrirProgramas() → PROGRAMAS_ABIERTO  
PROGRAMAS_ABIERTO → crearPrograma() → PROGRAMA_ABIERTO
```

**Implementación React** (tecnología específica):
```javascript
// App.jsx - Navegación derivada del diagrama de contexto
const App = () => (
  <Router>
    <Routes>
      <Route path="/login" element={<LoginPage />} />        {/* NO_AUTENTICADO */}
      <Route path="/dashboard" element={<Dashboard />} />    {/* MENU_PRINCIPAL */}
      <Route path="/programas" element={<ProgramasPage />} /> {/* PROGRAMAS_ABIERTO */}
      <Route path="/programas/:id" element={<ProgramaEditPage />} /> {/* PROGRAMA_ABIERTO */}
    </Routes>
  </Router>
);

// Estados RUP → React Context
const SystemStateContext = createContext();

const useSystemState = () => {
  const [currentState, setCurrentState] = useState('NO_AUTENTICADO');
  
  const transition = (action, params) => {
    // Transiciones basadas en diagrama de contexto RUP
    switch (currentState) {
      case 'NO_AUTENTICADO':
        if (action === 'iniciarSesion') setCurrentState('MENU_PRINCIPAL');
        break;
      case 'MENU_PRINCIPAL':
        if (action === 'abrirProgramas') setCurrentState('PROGRAMAS_ABIERTO');
        break;
      // ... más transiciones del análisis RUP
    }
  };
};
```

## Decisiones Arquitectónicas Críticas

### Decisión 1: Separación Frontend/Backend

**Análisis RUP que la justifica**:
- **Independencia tecnológica**: Análisis no asume interfaz específica
- **Múltiples clientes potenciales**: Preparado para web + mobile futuro
- **Casos de "consulta"**: `consultarHorario()` consumible por diferentes interfaces

**Implementación**:
```
React Client ←→ REST API ←→ Spring Boot Backend
```

**Beneficios**:
- ✅ Análisis MVC se mantiene válido
- ✅ Misma API sirve web + futuras implementaciones mobile
- ✅ Testing independiente de frontend y backend

### Decisión 2: PostgreSQL para Algoritmo Complejo

**Análisis RUP que la justifica**:

**Del caso `generarHorario()`**:
```
Sistema ejecuta algoritmo de optimización:
1. PrepararH() - Resolución de conflictos
2. GeneraPreHorario() - Optimización dual  
3. GeneraHorario() - Materialización
4. IngresoHE() - Casos especiales
```

**Requisitos identificados**:
- **Consultas complejas**: JOINs múltiples entre 6+ tablas
- **Transacciones ACID**: Integridad durante generación de horarios
- **Optimizaciones**: Índices para búsquedas por bloque horario, profesor, aula
- **Restricciones de integridad**: Validación automática de conflictos

**Implementación SQL derivada**:
```sql
-- Consulta optimizada derivada del algoritmo PrepararH()
CREATE INDEX idx_cursos_bloque_programa ON cursos(bloque_horario, programa_id);
CREATE INDEX idx_aulas_capacidad_recursos ON aulas(capacidad) INCLUDE (recursos);

-- Función PostgreSQL para el algoritmo de optimización
CREATE OR REPLACE FUNCTION generar_prehorario(bloque_h INTEGER)
RETURNS TABLE(curso_id INTEGER, aula_id INTEGER, puntuacion DECIMAL)
AS $$
BEGIN
  -- Implementación de optimización dual derivada del análisis
  RETURN QUERY
  SELECT c.id, a.id, calcular_puntuacion_compatibilidad(c.id, a.id)
  FROM cursos c
  CROSS JOIN aulas a  
  WHERE c.bloque_horario = bloque_h
    AND a.capacidad >= c.vacantes
    AND NOT EXISTS (SELECT 1 FROM horarios h WHERE h.aula_id = a.id AND h.bloque_horario = bloque_h)
  ORDER BY calcular_puntuacion_compatibilidad(c.id, a.id) DESC;
END;
$$ LANGUAGE plpgsql;
```

### Decisión 3: React para 32 Casos de Uso

**Análisis RUP que la justifica**:

**Complejidad de navegación identificada**:
- **11 estados del sistema** en diagrama de contexto
- **32 casos de uso** con transiciones específicas
- **Filosofía C→U**: Componentes reutilizables para crear/editar
- **Patrones de navegación**: `<<include>>` relationships en eliminaciones

**Implementación React derivada**:
```javascript
// Hook derivado de la filosofía C→U del análisis
const useEntityCRUD = (entityType) => {
  const crear = async (datosMinimos) => {
    // "El delgado" - crearPrograma()
    const entity = await api.post(`/api/${entityType}`, datosMinimos);
    navigate(`/${entityType}/${entity.id}/editar`); // → "El gordo"
  };
  
  const editar = (id) => {
    // "El gordo" - editarPrograma()
    navigate(`/${entityType}/${id}/editar`);
  };
  
  const eliminar = async (id) => {
    // Patrón <<include>> del análisis
    await api.delete(`/api/${entityType}/${id}`);
    navigate(`/${entityType}`); // <<include>> abrirProgramas()
  };
};

// Componente reutilizable derivado del patrón CRUD
const EntityListPage = ({ entityType }) => {
  const { crear, editar, eliminar } = useEntityCRUD(entityType);
  
  // Interfaz que implementa estados CRUD del análisis RUP
  return (
    <div>
      <EntityTable onEdit={editar} onDelete={eliminar} />
      <CreateButton onClick={crear} />
    </div>
  );
};
```

## Validación de Independencia Tecnológica

### Test de Migración Conceptual

**Pregunta clave**: ¿El análisis RUP sigue siendo válido si cambio la tecnología?

#### Ejemplo: Migración React → Angular

**Análisis RUP** (inmutable):
```
Estado: PROGRAMAS_ABIERTO
Caso de uso: abrirProgramas()
Transición: editarPrograma() → PROGRAMA_ABIERTO
```

**React** (implementación actual):
```javascript
const ProgramasPage = () => {
  const navigate = useNavigate();
  return <EntityList onEdit={(id) => navigate(`/programas/${id}`)} />;
};
```

**Angular** (implementación alternativa):
```typescript
@Component({ template: '<entity-list (edit)="onEdit($event)"></entity-list>' })
export class ProgramasComponent {
  onEdit(id: string) {
    this.router.navigate(['/programas', id]); // Misma lógica de transición
  }
}
```

**Resultado**: ✅ El análisis se mantiene válido, solo cambia la sintaxis.

#### Ejemplo: Migración Spring Boot → Django

**Análisis MVC** (inmutable):
```
EditarCursoView → CursoController → CursoRepository → Curso
```

**Spring Boot** (actual):
```java
@RestController
public class CursoController {
    @PutMapping("/api/cursos/{id}")
    public Curso editarCurso(@PathVariable Long id, @RequestBody Curso curso) {
        return cursoService.actualizar(id, curso);
    }
}
```

**Django** (alternativo):
```python
class CursoViewSet(viewsets.ModelViewSet):
    def update(self, request, pk=None):
        curso = self.curso_service.actualizar(pk, request.data)
        return Response(CursoSerializer(curso).data)
```

**Resultado**: ✅ Misma separación MVC, diferente sintaxis.

## Riesgos Arquitectónicos y Mitigaciones

### Riesgo 1: Complejidad del Algoritmo de Optimización

**Descripción**: El algoritmo de 4 fases puede ser computacionalmente intensivo.

**Mitigación**: 
- **JVM optimizada**: Spring Boot + Java 17 con GC optimizado
- **Procesamiento asíncrono**: CompletableFuture para operaciones largas
- **Cacheable**: Spring Cache para resultados frecuentes
- **Monitoreo**: Spring Actuator para métricas de rendimiento

```java
@Service
public class GenerarHorarioService {
    
    @Async
    @Cacheable(value = "horarios", key = "#parametros.hashCode()")
    public CompletableFuture<Horario> generarHorarioAsync(ParametrosGeneracion parametros) {
        // Implementación de las 4 fases con métricas
        return CompletableFuture.completedFuture(horario);
    }
}
```

### Riesgo 2: Escalabilidad de 32 Casos CRUD

**Descripción**: Mantener 32 casos de uso puede generar código repetitivo.

**Mitigación**:
- **Componentes genéricos**: React components reutilizables
- **Spring Data**: Repository patterns automáticos
- **Patrones establecidos**: Metodología "como comer pipas" del análisis

```javascript
// Componente genérico derivado del análisis CRUD
const EntityCRUDPage = ({ entityConfig }) => {
  // Una implementación sirve para las 6 entidades
  return (
    <div>
      <EntityTable config={entityConfig} />
      <EntityForm config={entityConfig} />
    </div>
  );
};

// Configuración derivada del modelo del dominio
const ENTITY_CONFIGS = {
  programas: { fields: ['codigo', 'nombre'], endpoint: '/api/programas' },
  cursos: { fields: ['codigo', 'nombre', 'creditos'], endpoint: '/api/cursos' },
  // ... configuración para las 6 entidades
};
```

### Riesgo 3: Sincronización Estado Frontend/Backend

**Descripción**: Estados del diagrama de contexto deben mantenerse sincronizados.

**Mitigación**:
- **Single source of truth**: Estado en backend, cache en frontend
- **React Query**: Sincronización automática con invalidación
- **Optimistic updates**: UX responsiva con rollback automático

```javascript
// Hook derivado del diagrama de contexto RUP
const useSystemState = () => {
  const queryClient = useQueryClient();
  
  const transition = useMutation(
    ({ from, action, params }) => api.post('/api/system/transition', { from, action, params }),
    {
      onSuccess: (newState) => {
        queryClient.setQueryData(['systemState'], newState);
        navigate(getRouteForState(newState)); // Navegación automática
      }
    }
  );
};
```

## Conclusiones Arquitectónicas

### Validación de Principios RUP

1. ✅ **Architecture-driven**: Stack emerge del análisis, no lo precede
2. ✅ **Independence preserved**: Análisis válido para múltiples tecnologías
3. ✅ **Risk-driven**: Decisiones mitigan riesgos arquitectónicos identificados
4. ✅ **Iterative refinement**: Arquitectura puede evolucionar sin romper análisis

### Trazabilidad Completa

| Artefacto RUP | Decisión Tecnológica | Justificación |
|---------------|---------------------|---------------|
| **Modelo del dominio** | PostgreSQL schema | Relaciones complejas requieren BD relacional |
| **Casos de uso MVC** | Spring Boot architecture | Separación View/Controller/Repository natural |
| **Estados del sistema** | React Router + Context | Navegación compleja entre 11 estados |
| **Algoritmo 4 fases** | Java + JVM optimization | Performance crítico para optimización |
| **32 casos CRUD** | React components + Spring Data | Reutilización y generación automática |

### Preparación para Evolución

**La arquitectura propuesta permite**:
- ✅ **Múltiples implementaciones**: Web actual → Mobile futuro → Desktop eventual
- ✅ **Migración tecnológica**: Cambio de stack sin re-análisis
- ✅ **Escalabilidad**: Microservicios futuros desde monolito actual
- ✅ **Extensibilidad**: Nuevos casos de uso sin refactoring arquitectónico

---

*Esta justificación será validada durante la implementación y actualizada según se refine la arquitectura*