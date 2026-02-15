#!/bin/bash

###############################################################################
# pySigHor Backend - Script de Inicialización
# Este script configura el entorno de desarrollo automáticamente
###############################################################################

set -e  # Detener ejecución si hay algún error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║        pySigHor Backend - Configuración Inicial           ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

###############################################################################
# 1. Verificar Poetry
###############################################################################
echo -e "${YELLOW}► Verificando Poetry...${NC}"
if ! command -v poetry &> /dev/null; then
    echo -e "${RED}✗ Poetry no está instalado${NC}"
    echo "Instala Poetry con: curl -sSL https://install.python-poetry.org | python3 -"
    exit 1
fi
POETRY_VERSION=$(poetry --version)
echo -e "${GREEN}✓${NC} Poetry instalado: ${POETRY_VERSION}"
echo ""

###############################################################################
# 2. Verificar versión de Python
###############################################################################
echo -e "${YELLOW}► Verificando versión de Python...${NC}"
PYTHON_VERSION=$(python3 --version | awk '{print $2}')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 11 ]); then
    echo -e "${RED}✗ Python 3.11+ requerido (detectado: ${PYTHON_VERSION})${NC}"
    exit 1
fi
echo -e "${GREEN}✓${NC} Python ${PYTHON_VERSION} compatible"
echo ""

###############################################################################
# 3. Crear archivo .env
###############################################################################
echo -e "${YELLOW}► Configurando variables de entorno...${NC}"
if [ ! -f .env ]; then
    if [ -f .env.example ]; then
        cp .env.example .env
        echo -e "${GREEN}✓${NC} Archivo .env creado desde .env.example"
    else
        echo -e "${YELLOW}⚠${NC} No existe .env.example, creando .env con valores por defecto"
        cat > .env << EOF
# Database
DATABASE_URL=sqlite:///./pySigHor.db

# Security
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# API
API_V1_STR=/api/v1
PROJECT_NAME=pySigHor
EOF
        echo -e "${GREEN}✓${NC} Archivo .env creado con valores por defecto"
    fi
else
    echo -e "${GREEN}✓${NC} Archivo .env ya existe"
fi
echo ""

###############################################################################
# 4. Instalar dependencias
###############################################################################
echo -e "${YELLOW}► Instalando dependencias de Python...${NC}"
poetry install --no-root
echo -e "${GREEN}✓${NC} Dependencias instaladas correctamente"
echo ""

###############################################################################
# 5. Inicializar base de datos
###############################################################################
echo -e "${YELLOW}► Inicializando base de datos...${NC}"
poetry run python init_db.py

# Verificar que se creó el archivo
if [ -f pySigHor.db ]; then
    echo -e "${GREEN}✓${NC} Base de datos creada: pySigHor.db"
else
    echo -e "${RED}✗ Error: No se pudo crear la base de datos${NC}"
    exit 1
fi

# Verificar tablas
TABLES=$(poetry run python -c "
from sqlalchemy import inspect
from app.core.database import engine
inspector = inspect(engine)
tables = inspector.get_table_names()
print(','.join(tables))
" 2>/dev/null)

if [[ "$TABLES" == *"aulas"* ]] && [[ "$TABLES" == *"edificios"* ]]; then
    echo -e "${GREEN}✓${NC} Tablas verificadas: ${TABLES}"
else
    echo -e "${RED}✗ Error: No se pudieron crear todas las tablas${NC}"
    exit 1
fi
echo ""

###############################################################################
# 6. Resumen
###############################################################################
echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                   ✓ Configuración Completada               ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}Backend listo para usar${NC}"
echo ""
echo "Comandos útiles:"
echo "  • Levantar servidor:"
echo -e "    ${YELLOW}poetry run uvicorn app.main:app --reload --port 8000${NC}"
echo ""
echo "  • Probar health check:"
echo -e "    ${YELLOW}curl http://localhost:8000/health${NC}"
echo ""
echo "  • Ver documentación API:"
echo -e "    ${YELLOW}http://localhost:8000/docs${NC}"
echo ""
echo "  • Login (usuario: admin, contraseña: admin):"
echo -e "    ${YELLOW}curl -X POST 'http://localhost:8000/api/v1/auth/login' \\\${NC}"
echo -e "      ${YELLOW}-H 'Content-Type: application/x-www-form-urlencoded' \\\${NC}"
echo -e "      ${YELLOW}-d 'username=admin&password=admin'${NC}"
echo ""
echo -e "${GREEN}¡Listo para comenzar! 🚀${NC}"
