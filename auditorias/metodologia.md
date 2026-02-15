# Metodologia de Auditoria

Cada iteracion se audita en dos dimensiones:

## Tipos

### 1. Auditoria Tecnica

Evalua:

- Calidad de codigo (backend + frontend)
- Seguridad (autenticacion, autorizacion, validaciones)
- Arquitectura (patrones, separacion de responsabilidades)
- Configuracion (dependencies, environment, tooling)
- Testing (unit tests, integration tests)
- Documentacion (precision, completitud)

**Auditores**: Minimo 3 LLMs diferentes para triangulacion

### 2. Auditoria de Proceso RUP

Evalua:

- Trazabilidad Requisitos → Analisis
- Trazabilidad Analisis → Diseno
- Trazabilidad Diseno → Desarrollo
- Gaps (funcionalidad disenada no implementada)
- Drifts (funcionalidad implementada no disenada)
- Inconsistencias de nombres y terminologia

**Auditores**: Minimo 3 LLMs diferentes para triangulacion

## Notas

- **Commit de referencia**: Cada auditoria esta vinculada a un commit especifico para reproducibilidad
- **Version del codigo**: Las auditorias aplican al codigo en el momento del commit auditado
- **Actualizaciones**: Si el codigo cambia tras la auditoria, los hallazgos pueden quedar obsoletos
- **Triangulacion**: Se usan multiples LLMs para reducir sesgos y obtener vision completa
