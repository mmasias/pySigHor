# Setup Inicial - pySigHor Backend

## Método Rápido: Script Automatizado

Ejecuta el script de configuración que hace todo por ti:

```bash
cd backend
./setup.sh
```

Este script verifica e instala automáticamente:
- ✅ Poetry (si no está instalado)
- ✅ Python 3.11+
- ✅ Dependencias del proyecto
- ✅ Base de datos SQLite
- ✅ Configuración de entorno

## Método Manual (si prefieres control total)

1. **Instalar Poetry** (si no lo tienes)
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Instalar dependencias**
   ```bash
   cd backend
   poetry install --no-root
   ```

3. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env si necesitas cambiar algo
   ```

4. **Inicializar base de datos**
   ```bash
   poetry run python init_db.py
   ```
   Esto creará el archivo `pySigHor.db` con las tablas necesarias.

## Levantar el Servidor

```bash
poetry run uvicorn app.main:app --reload --port 8000
```

## Verificar que Funciona

- Health check: http://localhost:8000/health
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Credenciales de Prueba

- Usuario: `admin`
- Contraseña: `admin`

## Próximos Pasos

Una vez que el backend esté corriendo, continúa con el frontend:
```bash
cd ../frontend
npm install
npm run dev
```
