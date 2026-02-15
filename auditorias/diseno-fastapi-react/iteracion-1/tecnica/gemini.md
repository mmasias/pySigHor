# AUDITORÍA TÉCNICA - Iteración 1 pySigHor

**Auditor**: Gemini (Google)
**Fecha de auditoría**: 2025-02-15
**Rama**: diseño-fastapi-react
**Commit auditado**: `a8894e2`
**Ver código en GitHub**: https://github.com/mmasias/pySigHor/commit/a8894e2

---

## RESUMEN EJECUTIVO
La Iteración 1 establece una base arquitectónica sólida con un stack moderno. Sin embargo, presenta issues críticos de seguridad y un bug bloqueante en el backend que impiden que la funcionalidad de login y el CRUD operen como se espera. La documentación, aunque estructuralmente excelente, es imprecisa respecto a la seguridad implementada.

## 🔴 ISSUES CRÍTICOS
- **[Seguridad Backend] Vulnerabilidad de Acesso No Autorizado en CRUD:** Todos los endpoints del CRUD de Aulas (`/api/v1/aulas/`) carecen de protección. Cualquier usuario anónimo puede crear, leer, actualizar y eliminar aulas. Se debe añadir `Depends(oauth2_scheme)` a cada endpoint en `routers/aulas.py`.
- **[Bug Backend] El Login está Roto:** El archivo `app/core/security.py` utiliza `Optional` sin importarlo de `typing`, lo que provoca un `NameError` al intentar llamar a `create_access_token`. Esto bloquea completamente el flujo de inicio de sesión.
- **[Documentación] Información de Seguridad Falsa:** Los archivos `SETUP-INICIAL.md` y la documentación RUP (`RUP/03-desarrollo/casos-uso/...`) afirman que los endpoints están protegidos y muestran ejemplos con `Authorization: Bearer <token>`. Esto es incorrecto y da una falsa sensación de seguridad.

## 🟡 ISSUES MEDIOS
- **[Seguridad Backend] Credenciales de Administrador Hardcodeadas:** `routers/auth.py` contiene un usuario "admin" con una contraseña débil ("admin") hardcodeada. Esto debe ser eliminado y reemplazado por un sistema de creación de usuarios en la base de datos.
- **[Arquitectura Backend] Violación del Patrón "Unit of Work":** Los repositorios (`aula_repository.py`) realizan `db.commit()` en cada operación. La responsabilidad de la transacción debe moverse al service layer para permitir operaciones atómicas más complejas y un rollback adecuado.
- **[Arquitectura Backend] Indicio de Dependencias Circulares:** El uso de importaciones locales dentro de los métodos de `aula_service.py` es un code smell que sugiere un problema en la estructura de dependencias. Debe refactorizarse para permitir importaciones a nivel de módulo.
- **[Bug Frontend] Configuración de Tema MUI Incorrecta:** `App.tsx` utiliza `colorScheme: { mode: 'light' }` para configurar el tema de Material-UI v5. La propiedad correcta es `palette: { mode: 'light' }`.
- **[Código Backend] Dependencia Innecesaria:** El endpoint de `login` depende de la sesión de base de datos (`get_db`) pero no la utiliza, ya que la validación se hace contra un diccionario en memoria.

## 🟢 ISSUES MENORES
- **[Rendimiento Backend] Instanciación Repetida:** Se crean nuevas instancias de `AulaService` y `AulaRepository` en cada llamada a los endpoints. Se recomienda usar un sistema de dependencias para instanciarlos una vez por request.
- **[Configuración Backend] Orígenes CORS Hardcodeados:** La lista de orígenes permitidos en `main.py` está hardcodeada. Debería obtenerse de variables de entorno para facilitar la configuración entre entornos.
- **[Frontend] Falta de Linter/Formatter:** El proyecto no incluye `ESLint` ni `Prettier`, lo que puede llevar a inconsistencias en el estilo del código.
- **[Organización Frontend] Ubicación de `ProtectedRoute`:** El componente `ProtectedRoute` debería extraerse de `App.tsx` a su propio archivo en la carpeta `components/` para mejorar la modularidad.
- **[Recomendación] Repositorio Genérico:** Implementar un `BaseRepository` genérico para reducir la duplicación de código en las operaciones CRUD.

## ⭐ ASPECTOS POSITIVOS
- **Arquitectura Limpia:** La separación en capas (Router, Service, Repository) en el backend está bien definida y es la correcta para este tipo de aplicación.
- **Stack Tecnológico Moderno:** La elección de FastAPI, React, Vite, Pydantic y SQLAlchemy es excelente y proporciona una base de alto rendimiento.
- **Scripts de Configuración Robustos:** Los scripts `setup.sh` son claros, automáticos y facilitan enormemente la puesta en marcha del entorno de desarrollo.
- **Estructura Frontend Sólida:** El uso de React Context para la autenticación, un cliente `axios` con interceptores y el enrutamiento protegido son implementaciones de libro.
- **Calidad de Documentación (Estructura):** La documentación RUP es excepcionalmente detallada, bien navegable y un gran ejemplo de cómo documentar el ciclo de vida de un caso de uso.
- **Foco en Calidad de Código:** La inclusión de `mypy`, `black`, `isort` y `TypeScript` desde el inicio demuestra un fuerte compromiso con la mantenibilidad y la calidad.

## 📊 EVALUACIÓN DE CALIDAD
- **Código Backend:** 4/10 *(La estructura es buena, pero la vulnerabilidad crítica y el bug bloqueante reducen drásticamente la puntuación.)*
- **Código Frontend:** 7/10 *(Bien estructurado y funcional, con algunos errores menores y oportunidades de mejora.)*
- **Documentación:** 5/10 *(Estructuralmente es un 10/10, pero la información crítica incorrecta sobre seguridad le resta la mitad de su valor.)*
- **Arquitectura:** 6/10 *(El patrón en capas es correcto, pero se ve afectado por la violación del "Unit of Work" y los indicios de dependencias circulares.)*
- **Configuración:** 8/10 *(Casi perfecta, gracias a los scripts de setup y la configuración de Vite. Pierde puntos por valores hardcodeados.)*

## 💡 RECOMENDACIONES
1.  **Prioridad Máxima:**
    -   **Corregir el bug de `Optional` en `security.py`** para habilitar el login.
    -   **Añadir protección de autenticación (`Depends`) a todos los endpoints de `aulas.py`** para cerrar la brecha de seguridad.
    -   **Actualizar toda la documentación** para reflejar el estado real de la seguridad.
2.  **Siguiente Iteración:**
    -   **Eliminar el usuario hardcodeado** y crear una tabla de usuarios con un endpoint para crearlos.
    -   **Refactorizar el manejo de transacciones,** moviendo el `db.commit()` del repositorio al servicio.
    -   **Resolver el problema de dependencias circulares** para eliminar las importaciones locales en los servicios.
3.  **Mejora Continua:**
    -   **Inyectar servicios y repositorios** usando el sistema de dependencias de FastAPI.
    -   **Añadir ESLint y Prettier** al workflow del frontend.
    -   **Mover la configuración de CORS a variables de entorno.**
