# 03-Desarrollo

Contiene la documentación de implementación de los casos de uso desarrollados en el proyecto.

## Estructura

```
03-desarrollo/
└── casos-uso/
    ├── iniciarSesion/
    │   └── README.md
    ├── abrirAulas/
    │   └── README.md
    ├── crearAula/
    │   └── README.md
    ├── editarAula/
    │   └── README.md
    └── eliminarAula/
        └── README.md
```

## Convención de Nombres

Los directorios siguen la convención de nombres de casos de uso en **camelCase**:
- `iniciarSesion` (no `iniciar_sesion`)
- `abrirAulas` (no `abrir_aulas`)
- `crearAula` (no `crear_aula`)

## Contenido de Cada README

Cada archivo `README.md` de caso de uso contiene:

### 1. Descripción
- Breve explicación del caso de uso
- Estado actual (✅ Completado, 🔧 En desarrollo, ⏸️ Pendiente)

### 2. Backend
- **Archivo**: Ruta del código backend
- **Rama**: Rama de Git donde está el código
- **Endpoints**: Lista de endpoints HTTP implementados
- **Implementación**: Detalles técnicos de la implementación
- **Archivos relacionados**: Otros archivos que componen la implementación

### 3. Frontend
- **Archivo**: Ruta del código frontend
- **Componentes**: Componentes React o páginas involucradas
- **Implementación**: Detalles técnicos de la implementación

### 4. Flujo de Datos
- Diagrama paso a paso del flujo de información

### 5. Notas de Implementación
- Problemas encontrados y soluciones
- Decisiones técnicas importantes
- Compatibility issues

### 6. Testing
- Comandos curl para probar backend
- Pasos manuales para probar frontend
- Casos de prueba automatizados

### 7. Casos de Prueba
- Lista de casos de prueba validados
- Resultados esperados

### 8. Relacionados
- Enlaces a otros casos de uso relacionados

## Relación con Otras Disciplinas

```
RUP/
├── 00-casos-uso/          # Especificación de requisitos
├── 01-analisis/           # Análisis MVC
├── 02-diseño/             # Diseño técnico (rama específica)
└── 03-desarrollo/         # Implementación (esta carpeta)
    └── casos-uso/
        └── <nombreCasoUso>/
            └── README.md
```

## Enlaces desde el Dashboard

Desde el diagrama de contexto (`RUP/99-seguimiento/diagrama-contexto-administrador.puml`):

```
[[...README.md <nombreCasoUso>()]]  # Especificación
[[...README.md A]]                    # Análisis
[[...README.md D]]                    # Diseño
[[...README.md dev]]                  # Desarrollo ← apunta aquí
```

El enlace `dev` apunta a:
```
https://github.com/mmasias/pySigHor/blob/<rama>/RUP/03-desarrollo/casos-uso/<nombreCasoUso>/README.md
```

## Casos de Uso Implementados

### Iteración 1 (Actual)

- ✅ `iniciarSesion` - Autenticación JWT
- ✅ `abrirAulas` - GET /api/v1/aulas/
- ✅ `crearAula` - POST /api/v1/aulas/
- ✅ `editarAula` - PATCH /api/v1/aulas/{id}
- ✅ `eliminarAula` - DELETE /api/v1/aulas/{id}

## Próximas Iteraciones

- Iteración 2: Edificios (abrirEdificios, crearEdificio, editarEdificio, eliminarEdificio)
- Iteración 3: Cursos
- Iteración 4: Profesores
- Iteración 5: Generación de Horarios
- Iteración 6: Consulta de Horarios
- Iteración 7: Reportes

## Notas

- Los archivos de desarrollo se crean en la rama de diseño actual (`diseño-fastapi-react`)
- Cada caso de uso tiene trazabilidad completa desde requisitos hasta implementación
- Los enlaces son permanentes y versionables
