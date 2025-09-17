# Fase de Diseño - pySigHor

<div align=right>

|[![](https://img.shields.io/badge/-Inicio-FFF?style=flat&logo=Emlakjet&logoColor=black)](../../README.md) [![](https://img.shields.io/badge/-RUP-FFF?style=flat&logo=Elsevier&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-Casos_de_Uso-FFF?style=flat&logo=typeorm&logoColor=black)](../00-casos-uso/README.md) [![](https://img.shields.io/badge/-Análisis-FFF?style=flat&logo=multisim&logoColor=black)](../01-analisis/README.md) [![](https://img.shields.io/badge/-Diseño-FFF?style=flat&logo=archlinux&logoColor=black)](README.md)|
|-:
|[![](https://img.shields.io/badge/-Estado-FFF?style=flat&logo=greensock&logoColor=black)](../README.md) [![](https://img.shields.io/badge/-Reflexiones-FFF?style=flat&logo=hootsuite&logoColor=black)](../../extraDocs/README.md) [![](https://img.shields.io/badge/-Log_de_conversación-FFF?style=flat&logo=gnometerminal&logoColor=black)](../../conversation-log.md)

</div>

## Información del artefacto

- **Proyecto**: pySigHor - Modernización del Sistema Generador de Horarios
- **Fase RUP**: Elaboration → Construction (Elaboración → Construcción)
- **Disciplina**: Análisis y Diseño
- **Versión**: 1.0
- **Fecha**: 2025-01-13
- **Autor**: Equipo de desarrollo

## Propósito de la Fase de Diseño

Esta fase marca la **transición crítica** del análisis independiente de tecnología hacia **decisiones arquitectónicas concretas** para la implementación de la versión web de pySigHor.

### Objetivos
- ✅ **Selección de stack tecnológico** basado en análisis RUP completado
- ✅ **Arquitectura del sistema** que preserve la independencia conceptual
- ✅ **Diseño de componentes** que implemente los patrones MVC identificados
- ✅ **Especificaciones técnicas** para la fase de construcción

## Estado del Proyecto - Transición Análisis → Diseño

### Fundamentos Completados (Análisis RUP 100%)
- ✅ **32 casos de uso** especificados y analizados con metodología "como comer pipas"
- ✅ **6 entidades del dominio** con modelo conceptual refinado
- ✅ **Arquitectura MVC** definida para todos los casos críticos
- ✅ **Algoritmo de optimización** completamente especificado (4 fases)
- ✅ **Independencia tecnológica** preservada según extraDocs/003

### Artefactos de Diseño a Crear
- [ ] **Stack tecnológico recomendado** (backend + frontend + datos)
- [ ] **Arquitectura del sistema** (diagrama de componentes + despliegue)
- [ ] **Diseño de base de datos** (modelo físico desde conceptual)
- [ ] **API REST** (especificación OpenAPI/Swagger)
- [ ] **Diseño de interfaz** (mockups de alta fidelidad)
- [ ] **Especificaciones técnicas** (configuración + despliegue)

## Metodología de Transición

### Principios RUP Aplicados
1. **Architecture-driven**: La arquitectura guía las decisiones tecnológicas
2. **Iterative development**: Refinamiento incremental del diseño
3. **Risk management**: Abordar primero decisiones arquitectónicas críticas
4. **Quality focus**: Mantener trazabilidad desde análisis hasta código

### Protocolos del Proyecto
- **LEY 004**: Trabajo en rama `xRevisar` para revisión antes de merge
- **Independencia tecnológica**: Decisiones justificadas desde análisis MVC
- **Trazabilidad**: Cada componente debe mapear a casos de uso analizados

## Contenido de la Fase

### 1. Stack Tecnológico
- [Propuesta de Stack Web](stack-tecnologico.md)
- [Justificación Arquitectónica](justificacion-arquitectonica.md)

### 2. Arquitectura del Sistema
- [Diagrama de Componentes](arquitectura-componentes.puml)
- [Arquitectura de Despliegue](arquitectura-despliegue.puml)

### 3. Diseño de Datos
- [Modelo Físico de Base de Datos](modelo-fisico-bd.puml)
- [Scripts de Creación](scripts-bd/)

### 4. API y Servicios
- [Especificación OpenAPI](api-rest.yaml)
- [Diseño de Servicios](servicios/)

### 5. Interfaz de Usuario
- [Mockups de Alta Fidelidad](ui-mockups/)
- [Sistema de Diseño](design-system.md)

## Referencias

- [Conversación 47](../../conversation-log.md) - Inicio de fase de diseño
- [extraDocs/003](../../extraDocs/003-rup-independencia-tecnologica/) - Independencia tecnológica RUP
- [Análisis completado](../01-analisis/) - Base para decisiones de diseño
- [Issue #16](https://github.com/mmasias/pySigHor/issues/16) - Diseño de la versión web