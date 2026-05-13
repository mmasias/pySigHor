# Artículo 025: Post-auditoría - Refactoring alineado a diseño

## ¿Por qué?

El artículo 024 documentó la detección de 20 desviaciones entre el diseño y la implementación. Este artículo cierra el ciclo: registra cómo se resolvió, qué se aprendió y cómo queda el proyecto después del refactoring.

## ¿Qué?

Se ejecutó un refactoring por capas en la rama `diseño-fastapi-react`, con **12 commits atómicos** que recorren la pila completa del backend y el frontend, alineando cada línea de código con lo que el diseño especifica.

### Tags de referencia

| Tag | Commit | Significado |
|---|---|---|
| [`pre-auditoria-diseno-codigo`](https://github.com/mmasias/pySigHor/tree/pre-auditoria-diseno-codigo) | `40af49d` | Estado del código divergente (equipo malo) |
| [`post-auditoria-diseno-codigo`](https://github.com/mmasias/pySigHor/tree/post-auditoria-diseno-codigo) | `fff93aa` | Estado del código alineado al diseño (equipo bueno) |

### Secuencia de refactoring

```
R01  Dependencias     pyproject.toml: pydantic v1 -> v2, async, pydantic-settings
R02  Config           config.py: BaseSettings v2, SECRET_KEY sin default, CORS configurable
R03  Database         database.py: create_engine -> create_async_engine, AsyncSession
R04  Security         security.py: Optional bug fix, decode_access_token
R05  Models           usuario.py: +rol, +timestamps en todos los modelos
R06  Schemas          schemas/*.py: orm_mode -> ConfigDict(from_attributes=True)
R07  Repositories     repositories/*.py: sync -> async, deferred imports eliminados
R08  Services         services/*.py: sync -> async, repo en __init__
R09  Routers          routers/*.py: async + Depends(get_current_user) en todos los endpoints
R10  Infraestructura  alembic.ini + migrations/async + tests/ (auth + aulas)
R11  Frontend bugs    theme MUI, token verification, 401 interceptor
R12  Navegacion       Layout sidebar, components/, public/
```

### Resultado: 18/20 desviaciones resueltas

| Desviación | Descripción | Estado |
|---|---|---|
| D01 | Motor sync vs async | Resuelta (R03+R04+R07+R08+R09) |
| D02 | Pydantic v1 vs v2 | Resuelta (R01+R02+R06) |
| D03 | SECRET_KEY con default | Resuelta (R02) |
| D04 | CORS hardcodeado | Resuelta (R02+R09) |
| D05 | Endpoints sin auth | Resuelta (R09) |
| D06 | Usuario sin rol | Resuelta (R05) |
| D07 | Sin timestamps | Resuelta (R05) |
| D08 | Sin Alembic | Resuelta (R10) |
| D09 | Sin tests | Resuelta (R10) |
| D10 | Optional sin importar | Resuelta (R04) |
| D11 | Sin navegacion | Resuelta (R12) |
| D12 | Sin selectores FK | **Pendiente** |
| D13 | Theme MUI incorrecto | Resuelta (R11) |
| D14 | Sin interceptor 401 | Resuelta (R11) |
| D15 | Token sin verificar | Resuelta (R11) |
| D16 | EmailStr sin usar | Resuelta (R06) |
| D17 | Imports diferidos | Resuelta (R07) |
| D18 | Sin components/ | Resuelta (R12) |
| D19 | Sin utils/ | **Pendiente** |
| D20 | Sin public/ | Resuelta (R12) |

## ¿Para qué?

| Lección metodológica | Aplicación |
|---|---|
| El código que no cumple el diseño es código equivocado | El diseño es el artefacto autoritativo en RUP |
| La auditoría formal detecta lo que la revisión informal no ve | 20 desviaciones acumuladas inadvertidamente |
| El refactoring por capas permite trazabilidad granular | Cada commit resuelve desviaciones específicas y documentadas |
| LEY 004 (xRevisar) era apropiada para requisitos/analisis/diseño | En construcción, se push directo a la rama de desarrollo |
| "Echar al equipo malo y contratar al bueno" funciona | El tag pre/post preserva ambos estados para comparación |

## ¿Cómo?

### Metodología aplicada

1. **Auditoría formal**: Documento con referencias exactas (diseño:línea vs código:línea)
2. **Tag pre-auditoría**: Preservación inmutable del estado divergente
3. **Refactoring por capas**: Un commit por capa de la arquitectura
4. **Trazabilidad en commit messages**: Cada commit referencia desviaciones resueltas y línea del diseño
5. **Seguimiento documental**: `seguimiento.md` actualizado con hashes reales
6. **Tag post-auditoría**: Estado final alineado

### Evolución del flujo de trabajo

El proyecto ha madurado de fase a fase:

| Fase | Flujo de integración |
|---|---|
| Requisitos / Análisis / Diseño | LEY 004: xRevisar -> PR -> main |
| Construcción | Push directo a rama de desarrollo (`diseño-fastapi-react`) |

LEY 004 queda obsoleta en su forma original. La revisión ahora se hace sobre la rama de construcción, no sobre main.

## ¿Y ahora qué?

- **D12 (selectores FK)**: Próximo objetivo al retomar el frontend
- **D19 (utils/)**: Se llenará cuando haya utilidades que extraer
- **El proyecto está alineado**: Código fiel al diseño, listo para continuar la construcción del dominio core (generarHorario, consultarHorario)

## Referencias

- **Auditoría completa**: [Artículo 024](../024-auditoria-diseno-vs-implementacion/articulo.md)
- **Código pre-auditoría**: [tag `pre-auditoria-diseno-codigo`](https://github.com/mmasias/pySigHor/tree/pre-auditoria-diseno-codigo)
- **Código post-auditoría**: [tag `post-auditoria-diseno-codigo`](https://github.com/mmasias/pySigHor/tree/post-auditoria-diseno-codigo)
- **Diff completo**: `git diff pre-auditoria-diseno-codigo..post-auditoria-diseno-codigo`
- **Diseño de referencia**: `RUP/02-diseño/configuracion-proyecto.md` (rama `diseño-fastapi-react`)
