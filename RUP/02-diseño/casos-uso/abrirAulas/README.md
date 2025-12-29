# pySigHor > abrirAulas > Diseño

> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/main/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/abrirAulas/README.md)|[Análisis](/RUP/01-analisis/casos-uso/abrirAulas/README.md)|**Diseño**|Desarrollo|Pruebas|
> |-|-|-|-|-|-|-|

## Información del artefacto

- **Proyecto**: pySigHor
- **Fase RUP**: Elaboración
- **Disciplina**: Diseño
- **Versión**: 1.0 (Spring Boot + Angular)
- **Fecha**: 2025-12-29
- **Autor**: Manuel Masías + Claude Sonnet 4.5

## Propósito
Detallar el flujo de datos para recuperar y mostrar la lista paginada de aulas registradas en el sistema.

## Diagrama de secuencia de diseño

![Diagrama de Secuencia](/images/RUP/02-diseño/casos-uso/abrirAulas/secuencia.svg)

[Código PlantUML](secuencia.puml)

## Participantes
*   **Frontend (Angular)**: Componente `AulaListComponent` con servicio HTTP que consume la API.
*   **AulaController**: Endpoint REST `GET /api/aulas` protegido con JWT.
*   **AulaService**: Servicio que orquesta la lógica de negocio y mapea entidades a DTOs.
*   **AulaRepository**: Interface Spring Data JPA que ejecuta consultas paginadas.
*   **Base de Datos (H2)**: Persistencia de aulas.

## Decisiones de diseño
*   Endpoint protegido con filtro JWT (`JwtAuthenticationFilter`).
*   **Paginación nativa** con `Pageable` de Spring Data.
*   Retorno de `Page<AulaDTO>` con metadatos (total elements, pages, etc.).
*   Separación de DTOs de Entidades JPA para exponer solo datos necesarios.
*   Frontend usa `AuthGuard` de Angular para verificar autenticación antes de navegar.
