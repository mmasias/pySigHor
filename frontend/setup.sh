#!/bin/bash

###############################################################################
# pySigHor Frontend - Script de Inicialización
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
echo -e "${BLUE}║       pySigHor Frontend - Configuración Inicial           ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

###############################################################################
# 1. Verificar Node.js
###############################################################################
echo -e "${YELLOW}► Verificando Node.js...${NC}"
if ! command -v node &> /dev/null; then
    echo -e "${RED}✗ Node.js no está instalado${NC}"
    echo "Instala Node.js con: sudo dnf install nodejs npm  (Fedora)"
    echo "                    o visita https://nodejs.org/"
    exit 1
fi
NODE_VERSION=$(node --version)
echo -e "${GREEN}✓${NC} Node.js instalado: ${NODE_VERSION}"

# Verificar npm
if ! command -v npm &> /dev/null; then
    echo -e "${RED}✗ npm no está instalado${NC}"
    exit 1
fi
NPM_VERSION=$(npm --version)
echo -e "${GREEN}✓${NC} npm instalado: ${NPM_VERSION}"
echo ""

###############################################################################
# 2. Verificar que el backend está corriendo
###############################################################################
echo -e "${YELLOW}► Verificando backend...${NC}"
if curl -s http://localhost:8000/health > /dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} Backend corriendo en http://localhost:8000"
else
    echo -e "${YELLOW}⚠${NC} Backend no detectado en http://localhost:8000"
    echo "   Asegúrate de levantar el backend primero:"
    echo "   cd ../backend && poetry run uvicorn app.main:app --reload --port 8000"
fi
echo ""

###############################################################################
# 3. Instalar dependencias
###############################################################################
echo -e "${YELLOW}► Instalando dependencias de Node...${NC}"
if [ -d "node_modules" ]; then
    echo -e "${YELLOW}⚠${NC} node_modules ya existe. ¿Reinstalar? (s/N)"
    read -r response
    if [[ "$response" =~ ^([sS][yY][sS]|[sS])$ ]]; then
        rm -rf node_modules package-lock.json
        npm install
        echo -e "${GREEN}✓${NC} Dependencias reinstaladas"
    else
        echo -e "${GREEN}✓${NC} Manteniendo dependencias existentes"
    fi
else
    npm install
    echo -e "${GREEN}✓${NC} Dependencias instaladas correctamente"
fi
echo ""

###############################################################################
# 4. Resumen
###############################################################################
echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║                   ✓ Configuración Completada               ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${GREEN}Frontend listo para usar${NC}"
echo ""
echo "Comandos útiles:"
echo "  • Levantar servidor desarrollo:"
echo -e "    ${YELLOW}npm run dev${NC}"
echo ""
echo "  • Build para producción:"
echo -e "    ${YELLOW}npm run build${NC}"
echo ""
echo "  • Verificar tipos TypeScript:"
echo -e "    ${YELLOW}npm run type-check${NC}"
echo ""
echo "  • Acceder a la aplicación:"
echo -e "    ${YELLOW}http://localhost:5173${NC}"
echo ""
echo "Credenciales de prueba:"
echo -e "  • Usuario: ${YELLOW}admin${NC}"
echo -e "  • Contraseña: ${YELLOW}admin${NC}"
echo ""
echo -e "${GREEN}¡Listo para comenzar! 🚀${NC}"
