# Relación entre Prototipos de Casos de Uso y Pantallas Finales: Análisis Didáctico

## Introducción

Este documento resume el análisis realizado sobre la relación entre los prototipos de casos de uso y las pantallas finales en el contexto de la disciplina de requisitos RUP, aplicado al proyecto pySigHor.

## El Problema Original

El problema original planteado fue: ¿cómo se llega, a partir de los prototipos que se presentan en los casos de uso (atómicos) a las pantallas finales que involucran muchas veces elementos que llaman a varios casos de uso?

## Análisis de la Relación entre Casos de Uso y Pantallas

### 1. El Patrón de Arquitectura Basado en Estados

En el sistema SigHor, cada pantalla representa un **estado** del sistema, y cada acción del usuario genera una **transición** que ejecuta un caso de uso:

```
[ESTADO A: Menu Principal] 
        ↓ (completarGestion())
[ESTADO B: Menu con botones] 
        ↓ (abrirProfesores())  
[ESTADO C: Lista de Profesores] 
        ↓ (editarProfesor())
[ESTADO D: Formulario de Edición]
```

### 2. Tipos de Relaciones entre Casos de Uso y Pantallas

#### A. Relación 1:1 Directa
- **Un solo caso de uso** → **Una pantalla específica**
- Ejemplo: `generarHorario()` → Pantalla con proceso de generación

#### B. Relación 1:N Multiplexada
- **Un caso de uso base** → **Una pantalla con múltiples funcionalidades**
- Ejemplo: `abrirProfesores()` → Pantalla con botones para crear, editar, eliminar, filtrar

#### C. Relación N:1 Consolidada  
- **Varios casos de uso** → **Una pantalla de menú**
- Ejemplo: `abrirProgramas()`, `abrirCursos()`, `abrirProfesores()` → Pantalla `completarGestion()`

## Patrones Metodológicos del Proyecto

### 1. Diagrama de Contexto como Máquina de Estados

**Innovación metodológica del proyecto**: Usar diagramas de estados para representar la navegación completa del usuario.
- Cada **estado** = pantalla o vista
- Cada **transición** = ejecución de caso de uso
- Cada **caso de uso** = etiqueta de la transición

### 2. Patrón "Delgado vs Gordo" (C→U)

**Creación mínima seguida de edición completa**:
- **Casos de Uso "Delgados"** (Ej: crearProfesor()):
  - Objetivo: Minimizar fricción en la creación inicial
  - Flujo: Creación mínima → Transferencia inmediata a edición
  - Pantalla: Formulario simple que se convierte rápidamente en edición completa

- **Casos de Uso "Gordos"** (Ej: editarProfesor()):
  - Objetivo: Edición completa con todos los campos disponibles
  - Flujo: Presentación de todos los campos → Modificación continua → Guardado
  - Pantalla: Formulario con todos los datos editables

### 3. Consolidación de Funcionalidades en Estados

- El **caso de uso primario** define el **estado base** de la pantalla
- Los **casos de uso secundarios** se **integran como acciones** dentro de ese estado
- La **navegación** entre estados se define por las **transiciones posibles**

## ¿Qué dice la teoría RUP formal?

### Lo que sí dice:

1. **Relación fundamental**: La interfaz de usuario se puede relacionar con los casos de uso porque "cada caso de uso describe una funcionalidad del sistema y la interfaz de usuario es el medio por el cual el usuario interactúa con el sistema para realizar dicha funcionalidad".

2. **Relación no 1:1**: "Una misma pantalla o interfaz puede estar relacionada con varios casos de uso, ya que puede ser utilizada por diferentes usuarios para realizar diferentes tareas".

### Lo que no dice:

- **No** proporciona un patrón específico o algoritmo para determinar exactamente qué casos de uso deben coexistir en una pantalla
- **No** especifica reglas formales para la agrupación de funcionalidades en interfaces
- **No** detalla una metodología explícita para pasar de casos de uso atómicos a interfaces integradas
- **No** aborda el manejo de la complejidad cuando muchos casos de uso se integran en una sola pantalla

## La Innovación Metodológica del Proyecto

El proyecto pySigHor ha desarrollado una **extensión práctica** de RUP que va más allá de la teoría formal:

### 1. Diagramas de contexto como máquinas de estados
- Cada estado = pantalla o vista
- Cada transición = ejecución de caso de uso
- Representación dinámica del comportamiento del sistema

### 2. Patrones de transición entre estados
- Basados en casos de uso
- Consideran la experiencia de usuario
- Implementan flujos lógicos de navegación

### 3. Agrupación lógica de funcionalidades
- En pantallas según experiencia de usuario
- Basada en relaciones conceptuales entre funcionalidades
- Considerando la eficiencia del trabajo del usuario

### 4. Diseño incremental de interfaces
- Basado en casos de uso atómicos
- Evolución progresiva de funcionalidades
- Validación continua con el usuario

## Lección Didáctica para Alumnos

> "La teoría RUP dice que los casos de uso deben guiar el diseño de interfaces, y que una interfaz puede relacionarse con múltiples casos de uso. Pero **no dice explícitamente cómo** hacer esa relación en la práctica. La metodología del proyecto pySigHor demuestra que **los equipos de desarrollo deben crear sus propios patrones prácticos** que extiendan la teoría formal, como los patrones de máquina de estados, el patrón delgado/gordo, y otros mecanismos para integrar casos de uso en interfaces."

### La Relación no es Directa

- **Casos de uso atómicos** definen el **comportamiento esencial** del sistema
- **Pantallas finales** son la **expresión integrada** de múltiples casos de uso que trabajan juntos
- **El diagrama de contexto como máquina de estados** es la clave que conecta ambos niveles de abstracción

## Ejercicio Didáctico para Alumnos

Dado el caso de uso `abrirCursos()`:
1. Identificar el **estado del sistema** que representa
2. Describir qué **botones/acciones** puede tener la pantalla final
3. Identificar qué **casos de uso secundarios** pueden iniciarse desde esa pantalla
4. Explicar cómo se **integran** los casos de uso `crearCurso()`, `editarCurso()`, `eliminarCurso()` en la misma pantalla

## Conclusión

La relación entre prototipos de casos de uso y pantallas finales representa un **paso metodológico de síntesis** que no está completamente especificado en la teoría formal de RUP. El proyecto pySigHor ha desarrollado patrones prácticos que extienden la metodología, demostrando que la ingeniería de software requiere no solo seguir teorías establecidas, sino también desarrollar soluciones contextuales que enriquezcan la práctica profesional.