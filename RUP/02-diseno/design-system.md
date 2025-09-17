# Sistema de Diseño - pySigHor Web

<div align=right>

|[![](https://img.shields.io/badge/-Diseño-FFF?style=flat&logo=archlinux&logoColor=black)](README.md) [![](https://img.shields.io/badge/-Sistema_de_Diseño-FFF?style=flat&logo=figma&logoColor=black)](design-system.md)|
|-:

</div>

## Información del artefacto

- **Proyecto**: pySigHor - Sistema de diseño para versión web
- **Fase RUP**: Elaboration (Elaboración) - Interfaz de Usuario
- **Versión**: 1.0
- **Fecha**: 2025-01-13
- **Autor**: Equipo de desarrollo

## Propósito

Define los **principios de diseño, componentes reutilizables y patrones de interfaz** para la implementación de la versión web de pySigHor, asegurando **consistencia visual** y **experiencia de usuario coherente** a través de los **32 casos de uso** especificados en el análisis RUP.

## Principios de Diseño

### 1. Mapeo Directo desde Wireframes RUP
**Principio**: Los mockups de alta fidelidad deben mantener **fidelidad conceptual** con los wireframes SALT especificados en el análisis.

**Aplicación**:
- ✅ **Estados visuales** corresponden a estados RUP del diagrama de contexto
- ✅ **Elementos de interfaz** mapean directamente a especificaciones de casos de uso
- ✅ **Flujos de navegación** respetan transiciones del análisis MVC

### 2. Filosofía C→U en Componentes
**Principio**: Implementar la filosofía "crear delgado → editar gordo" establecida en el análisis RUP.

**Aplicación**:
- 🔸 **Formularios de creación**: Campos mínimos, diseño simplificado, CTA hacia edición
- 🔹 **Formularios de edición**: Interfaz completa, sesión continua, todas las funcionalidades
- 🔄 **Transición automática**: De crear a editar sin fricción

### 3. Escalabilidad para 32 Casos de Uso
**Principio**: Componentes reutilizables que funcionen para múltiples entidades y operaciones.

**Aplicación**:
- 📋 **EntityTable**: Un componente para todas las listas (programas, cursos, profesores, etc.)
- 📝 **EntityForm**: Formularios configurables por tipo de entidad
- 🗂️ **EntityLayout**: Layout consistente para todas las páginas CRUD

## Paleta de Colores

### Colores Primarios (Derivados de RUP)
```css
/* Basados en los colores del dashboard RUP establecido */
:root {
  --primary-blue: #4A90E2;          /* Azul principal - casos de uso completados */
  --primary-green: #7ED321;         /* Verde - estados exitosos */
  --primary-orange: #F5A623;        /* Naranja - estados en progreso */
  --primary-red: #D0021B;           /* Rojo - errores y eliminaciones */
  
  /* Colores MVC del análisis */
  --mvc-view: #629EF9;              /* Azul - componentes de Vista */
  --mvc-controller: #B5BD68;        /* Verde oliva - lógica de Control */
  --mvc-model: #F2AC4E;             /* Naranja - entidades de Modelo */
  
  /* Colores de estado del sistema */
  --state-authenticated: #5CB85C;    /* Verde - usuario autenticado */
  --state-menu: #337AB7;             /* Azul - menú principal */
  --state-editing: #F0AD4E;          /* Amarillo - modo edición */
  --state-generating: #D9534F;       /* Rojo - generando horario */
}
```

### Colores Semánticos
```css
:root {
  /* Estados de datos */
  --success: #28A745;               /* Operaciones exitosas */
  --warning: #FFC107;               /* Advertencias */
  --danger: #DC3545;                /* Errores y eliminaciones */
  --info: #17A2B8;                  /* Información */
  
  /* Estados de entidades */
  --active: #28A745;                /* Entidades activas */
  --inactive: #6C757D;              /* Entidades inactivas */
  --draft: #FD7E14;                 /* Entidades en borrador */
  
  /* Algoritmo de horarios */
  --algorithm-phase1: #E83E8C;      /* PrepararH() */
  --algorithm-phase2: #6F42C1;      /* GeneraPreHorario() */
  --algorithm-phase3: #20C997;      /* GeneraHorario() */
  --algorithm-phase4: #FD7E14;      /* IngresoHE() */
}
```

### Colores Neutros
```css
:root {
  /* Grises */
  --gray-100: #F8F9FA;
  --gray-200: #E9ECEF;
  --gray-300: #DEE2E6;
  --gray-500: #6C757D;
  --gray-700: #495057;
  --gray-900: #212529;
  
  /* Backgrounds */
  --bg-primary: #FFFFFF;
  --bg-secondary: #F8F9FA;
  --bg-tertiary: #E9ECEF;
  
  /* Texto */
  --text-primary: #212529;
  --text-secondary: #6C757D;
  --text-muted: #ADB5BD;
}
```

## Tipografía

### Familias de Fuente
```css
:root {
  /* Fuente principal - optimizada para interfaces */
  --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
  
  /* Fuente para código y datos técnicos */
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;
  
  /* Fuente para títulos (opcional) */
  --font-display: 'Poppins', --font-primary;
}
```

### Escala Tipográfica
```css
:root {
  /* Títulos */
  --text-h1: 2.5rem;    /* 40px - Título de aplicación */
  --text-h2: 2rem;      /* 32px - Títulos de página */
  --text-h3: 1.5rem;    /* 24px - Títulos de sección */
  --text-h4: 1.25rem;   /* 20px - Subtítulos */
  
  /* Cuerpo */
  --text-body: 1rem;    /* 16px - Texto normal */
  --text-small: 0.875rem; /* 14px - Texto secundario */
  --text-xs: 0.75rem;   /* 12px - Texto mínimo */
  
  /* Peso */
  --weight-normal: 400;
  --weight-medium: 500;
  --weight-semibold: 600;
  --weight-bold: 700;
}
```

## Espaciado y Layout

### Sistema de Espaciado (8px grid)
```css
:root {
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
  --space-16: 4rem;     /* 64px */
}
```

### Breakpoints Responsive
```css
:root {
  --breakpoint-sm: 576px;    /* Teléfonos grandes */
  --breakpoint-md: 768px;    /* Tablets */
  --breakpoint-lg: 992px;    /* Laptops */
  --breakpoint-xl: 1200px;   /* Desktops */
  --breakpoint-xxl: 1400px;  /* Desktops grandes */
}
```

## Componentes Base

### 1. EntityTable Component
**Propósito**: Componente reutilizable para listar entidades (implementa casos `abrirX()`)

**Props Configurables**:
```typescript
interface EntityTableProps<T> {
  data: T[];
  columns: ColumnConfig<T>[];
  onEdit: (id: number) => void;      // Implementa editarX()
  onDelete: (id: number) => void;    // Implementa eliminarX()
  onCreate: () => void;              // Implementa crearX()
  loading?: boolean;
  emptyMessage?: string;
  searchable?: boolean;
  filterable?: boolean;
}
```

**Estados Visuales**:
- 🔄 **Loading**: Skeleton placeholders
- 📋 **Con Datos**: Tabla con acciones por fila
- 📭 **Vacío**: Empty state con CTA para crear
- 🔍 **Filtrando**: Indicadores de filtros activos

### 2. EntityForm Component  
**Propósito**: Formularios configurables para crear/editar entidades

**Variantes**:
- 🆕 **CrearForm**: "El delgado" - campos mínimos
- ✏️ **EditarForm**: "El gordo" - funcionalidad completa
- 👁️ **ViewForm**: Solo lectura para consultas

**Estados del Formulario**:
```typescript
type FormState = 
  | 'idle'           // Esperando interacción
  | 'editing'        // Usuario modificando
  | 'validating'     // Validando entrada
  | 'saving'         // Guardando cambios
  | 'success'        // Guardado exitoso
  | 'error';         // Error en validación/guardado
```

### 3. Navigation Component
**Propósito**: Navegación que refleja estados del diagrama de contexto RUP

**Estructura**:
```jsx
<Navigation currentState="PROGRAMAS_ABIERTO">
  <NavItem state="MENU_PRINCIPAL" icon="home">Dashboard</NavItem>
  <NavGroup label="Gestión Académica">
    <NavItem state="PROGRAMAS_ABIERTO" icon="graduation-cap">Programas</NavItem>
    <NavItem state="CURSOS_ABIERTO" icon="book">Cursos</NavItem>
    <NavItem state="PROFESORES_ABIERTO" icon="user">Profesores</NavItem>
  </NavGroup>
  <NavGroup label="Infraestructura">
    <NavItem state="EDIFICIOS_ABIERTO" icon="building">Edificios</NavItem>
    <NavItem state="AULAS_ABIERTO" icon="door">Aulas</NavItem>
    <NavItem state="RECURSOS_ABIERTO" icon="tool">Recursos</NavItem>
  </NavGroup>
  <NavGroup label="Horarios">
    <NavItem state="GENERANDO_HORARIO" icon="cog">Generar</NavItem>
    <NavItem state="CONSULTANDO_HORARIOS" icon="calendar">Consultar</NavItem>
  </NavGroup>
</Navigation>
```

### 4. Dashboard Layout
**Propósito**: Layout principal que implementa transiciones de estado RUP

**Estructura**:
```jsx
<DashboardLayout>
  <Sidebar>
    <Navigation />
  </Sidebar>
  <MainContent>
    <Header>
      <Breadcrumb />
      <UserMenu />
    </Header>
    <PageContent>
      {/* Contenido específico por estado */}
    </PageContent>
  </MainContent>
</DashboardLayout>
```

## Patrones de Interfaz

### 1. Patrón CRUD Completo
**Aplicación**: Todas las entidades del dominio (6 entidades × 4 operaciones)

**Estados de la Interfaz**:
```
Lista → [Crear] → Formulario Creación → [Guardar] → Formulario Edición
  ↓        ↑                                           ↓
[Editar] ←                                        [Cancelar/Guardar]
  ↓                                                     ↑
Formulario Edición ← [Eliminar + Confirmar] ← Lista ←
```

**Componentes**:
- 📋 **ListPage**: EntityTable + filtros + búsqueda
- 🆕 **CreatePage**: EntityForm (modo crear)
- ✏️ **EditPage**: EntityForm (modo editar)
- 🗑️ **DeleteModal**: Confirmación de eliminación

### 2. Patrón de Generación de Horarios
**Propósito**: Interfaz especializada para el algoritmo de 4 fases

**Flujo de Usuario**:
```
Dashboard → [Generar Horario] → Configuración → Ejecución → Resultados
                                      ↓             ↓          ↓
                                 [Cancelar]   [Progress]  [Consultar]
```

**Componentes Especializados**:
- ⚙️ **GenerateConfigForm**: Parámetros del algoritmo
- 🔄 **ProgressIndicator**: Fases del algoritmo en tiempo real
- 📊 **ResultsSummary**: Estadísticas de generación
- ⚠️ **ErrorHandler**: Manejo de errores algorítmicos

### 3. Patrón de Consulta de Horarios
**Propósito**: Visualización flexible de horarios generados

**Tipos de Vista**:
- 📅 **Vista Calendario**: Grid temporal por días/horas
- 📋 **Vista Tabla**: Lista detallada con filtros
- 👨‍🏫 **Vista Profesor**: Horario personal por docente
- 🏢 **Vista Aula**: Ocupación por espacio físico

## Micro-interacciones

### 1. Feedback de Acciones
```css
/* Botones con feedback inmediato */
.btn {
  transition: all 0.2s ease;
}

.btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.btn:active {
  transform: translateY(0);
}

/* Estados de carga */
.btn-loading {
  pointer-events: none;
}

.btn-loading::after {
  content: '';
  width: 16px;
  height: 16px;
  border: 2px solid transparent;
  border-top: 2px solid currentColor;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
```

### 2. Transiciones de Estado
```css
/* Transiciones entre páginas (estados RUP) */
.page-enter {
  opacity: 0;
  transform: translateX(20px);
}

.page-enter-active {
  opacity: 1;
  transform: translateX(0);
  transition: all 0.3s ease;
}

.page-exit {
  opacity: 1;
  transform: translateX(0);
}

.page-exit-active {
  opacity: 0;
  transform: translateX(-20px);
  transition: all 0.3s ease;
}
```

### 3. Indicadores de Progreso del Algoritmo
```css
/* Barra de progreso con fases del algoritmo */
.algorithm-progress {
  position: relative;
  background: var(--gray-200);
  border-radius: 8px;
  overflow: hidden;
}

.algorithm-progress-bar {
  height: 8px;
  background: linear-gradient(
    to right,
    var(--algorithm-phase1) 25%,
    var(--algorithm-phase2) 50%,
    var(--algorithm-phase3) 75%,
    var(--algorithm-phase4) 100%
  );
  transition: width 0.5s ease;
}

.algorithm-phase {
  position: absolute;
  top: -30px;
  font-size: 12px;
  font-weight: 500;
  color: var(--text-secondary);
  opacity: 0.7;
}

.algorithm-phase.active {
  opacity: 1;
  color: var(--text-primary);
}
```

## Accesibilidad

### 1. Contraste de Colores
- ✅ **WCAG AA**: Ratio mínimo 4.5:1 para texto normal
- ✅ **WCAG AAA**: Ratio mínimo 7:1 para texto importante
- ✅ **Estados de foco**: Outline visible en todos los elementos interactivos

### 2. Navegación por Teclado
```css
/* Foco visible para navegación por teclado */
.focusable:focus {
  outline: 2px solid var(--primary-blue);
  outline-offset: 2px;
}

/* Skip links para lectores de pantalla */
.skip-link {
  position: absolute;
  top: -40px;
  left: 6px;
  background: var(--bg-primary);
  color: var(--text-primary);
  padding: 8px;
  text-decoration: none;
  border-radius: 4px;
}

.skip-link:focus {
  top: 6px;
}
```

### 3. ARIA Labels
```jsx
// Ejemplo de tabla accesible
<table role="table" aria-label="Lista de programas académicos">
  <thead>
    <tr role="row">
      <th role="columnheader" aria-sort="ascending">Código</th>
      <th role="columnheader">Nombre</th>
      <th role="columnheader">Acciones</th>
    </tr>
  </thead>
  <tbody>
    <tr role="row" aria-rowindex="1">
      <td role="cell">PI</td>
      <td role="cell">Ingeniería de Sistemas</td>
      <td role="cell">
        <button aria-label="Editar programa PI">Editar</button>
        <button aria-label="Eliminar programa PI">Eliminar</button>
      </td>
    </tr>
  </tbody>
</table>
```

## Responsive Design

### 1. Mobile First
```css
/* Diseño base para móviles */
.entity-table {
  display: block;
}

.entity-table td {
  display: block;
  text-align: right;
  border: none;
  border-bottom: 1px solid var(--gray-200);
  padding: 0.5rem;
}

.entity-table td::before {
  content: attr(data-label) ": ";
  float: left;
  font-weight: 500;
}

/* Tablets y superiores */
@media (min-width: 768px) {
  .entity-table {
    display: table;
    width: 100%;
  }
  
  .entity-table td {
    display: table-cell;
    text-align: left;
    border: 1px solid var(--gray-200);
  }
  
  .entity-table td::before {
    display: none;
  }
}
```

### 2. Adaptación de Navegación
```css
/* Navegación móvil */
@media (max-width: 767px) {
  .sidebar {
    position: fixed;
    top: 0;
    left: -280px;
    width: 280px;
    height: 100vh;
    transition: left 0.3s ease;
    z-index: 1000;
  }
  
  .sidebar.open {
    left: 0;
  }
  
  .sidebar-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0,0,0,0.5);
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
  }
  
  .sidebar-overlay.visible {
    opacity: 1;
    pointer-events: auto;
  }
}
```

## Componentes Específicos del Dominio

### 1. HorarioGrid Component
**Propósito**: Visualización en grid del horario generado

```tsx
interface HorarioGridProps {
  horarios: Horario[];
  view: 'weekly' | 'daily' | 'professor' | 'room';
  onSlotClick?: (slot: TimeSlot) => void;
  filters?: {
    programaId?: number;
    profesorId?: number;
    aulaId?: number;
  };
}
```

### 2. AlgorithmMonitor Component
**Propósito**: Monitoreo en tiempo real del algoritmo de 4 fases

```tsx
interface AlgorithmMonitorProps {
  sessionId: string;
  onPhaseComplete: (phase: AlgorithmPhase) => void;
  onError: (error: AlgorithmError) => void;
  onComplete: (result: GenerarHorarioResponse) => void;
}
```

### 3. ConflictResolution Component
**Propósito**: Interfaz para resolver conflictos detectados por PrepararH()

```tsx
interface ConflictResolutionProps {
  conflicts: HorarioConflict[];
  onResolve: (conflictId: string, resolution: Resolution) => void;
  onSkip: (conflictId: string) => void;
}
```

## Implementación con Material-UI

### Tema Personalizado
```typescript
import { createTheme } from '@mui/material/styles';

export const pySigHorTheme = createTheme({
  palette: {
    primary: {
      main: '#4A90E2',      // primary-blue
      light: '#629EF9',     // mvc-view
      dark: '#337AB7',      // state-menu
    },
    secondary: {
      main: '#F5A623',      // primary-orange
      light: '#F2AC4E',     // mvc-model
      dark: '#D68910',
    },
    success: {
      main: '#28A745',      // success
    },
    warning: {
      main: '#FFC107',      // warning
    },
    error: {
      main: '#DC3545',      // danger
    },
    info: {
      main: '#17A2B8',      // info
    },
  },
  typography: {
    fontFamily: '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", sans-serif',
    h1: {
      fontSize: '2.5rem',
      fontWeight: 700,
    },
    h2: {
      fontSize: '2rem',
      fontWeight: 600,
    },
    // ... resto de configuración tipográfica
  },
  spacing: 8, // Base 8px grid
  shape: {
    borderRadius: 8,
  },
});
```

## Conclusiones

Este sistema de diseño proporciona una **base sólida y escalable** para la implementación de la versión web de pySigHor, asegurando:

1. ✅ **Consistencia visual** a través de todos los casos de uso
2. ✅ **Mapeo directo** desde wireframes RUP hasta componentes React
3. ✅ **Reutilización eficiente** con componentes configurables
4. ✅ **Experiencia responsive** optimizada para diferentes dispositivos
5. ✅ **Accesibilidad** cumpliendo estándares WCAG
6. ✅ **Escalabilidad** para futuras funcionalidades

El diseño mantiene **fidelidad conceptual** con el análisis RUP mientras optimiza la experiencia de usuario para la web moderna, creando un puente efectivo entre la metodología formal y la implementación práctica.

---

*Este sistema de diseño será refinado durante la implementación basándose en feedback de usuarios y pruebas de usabilidad*