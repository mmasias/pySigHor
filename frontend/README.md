# Frontend - pySigHor

Frontend React + Vite + TypeScript + Material-UI para el Sistema Generador de Horarios.

## Tecnologías

- **React 18** - Framework UI
- **TypeScript 5** - Tipado estático
- **Vite 5** - Build tool ultrarrápido
- **Material-UI v5** - Componentes UI
- **React Router v6** - Enrutamiento
- **Axios** - Cliente HTTP

## Método Rápido: Script Automatizado

Ejecuta el script de configuración:

```bash
cd frontend
./setup.sh
```

## Método Manual

### 1. Instalar dependencias

```bash
npm install
```

### 2. Levantar servidor de desarrollo

```bash
npm run dev
```

La aplicación estará disponible en **http://localhost:5173**

## Comandos Disponibles

```bash
npm run dev          # Servidor de desarrollo (Vite)
npm run build        # Build para producción
npm run preview      # Previsualizar build de producción
npm run type-check   # Verificar tipos TypeScript
```

## Estructura del Proyecto

```
frontend/
├── src/
│   ├── pages/           # Páginas de la aplicación
│   │   ├── LoginPage.tsx
│   │   └── AulasPage.tsx
│   ├── services/        # Cliente API
│   │   └── api.ts
│   ├── context/         # Contextos React
│   │   └── AuthContext.tsx
│   ├── types/           # Tipos TypeScript
│   │   └── index.ts
│   ├── App.tsx          # Componente principal
│   └── main.tsx         # Punto de entrada
├── public/              # Archivos estáticos
├── index.html           # HTML template
├── vite.config.ts       # Configuración Vite
└── package.json         # Dependencias
```

## Configuración del Backend

El frontend se conecta al backend en **http://localhost:8000** por defecto.

Para cambiar la URL del backend, modifica:

```typescript
// src/services/api.ts
const API_BASE_URL = 'http://localhost:8000';
```

## Credenciales de Prueba

- **Usuario**: `admin`
- **Contraseña**: `admin`

## Funcionalidades

### Iteración 1 (Actual)

- ✅ Login con JWT
- ✅ CRUD completo de Aulas
  - Crear aulas
  - Listar aulas
  - Editar aulas
  - Eliminar aulas
- ✅ Autenticación con token Bearer
- ✅ Manejo de errores con alertas
- ✅ Validación de formularios

## Próximas Iteraciones

- Iteración 2: Edificios
- Iteración 3: Cursos
- Iteración 4: Profesores
- Iteración 5: Algoritmo de Horarios
- Iteración 6: Reportes
- Iteración 7: Pulimiento y UX

## Troubleshooting

### El frontend no se conecta al backend

Verifica que el backend esté corriendo:
```bash
curl http://localhost:8000/health
```

### Error de CORS

El backend debe tener configurado el CORS para http://localhost:5173.
Revisa `app/main.py` en el backend.

### Typescript errors

Ejecuta:
```bash
npm run type-check
```
