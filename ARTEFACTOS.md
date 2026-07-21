# Artefactos

**pySigHor**: proyecto de un constructor de Horarios

## Modelo del dominio

<div align=center>

|![](/images/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.svg)
|-:
<sup>[*Código fuente*](/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.puml)</sup>

</div>

### Glosario

[Ver glosario completo](/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md#glosario)

### Diagrama de estados de entidades

<div align=center>

|![](/images/modelosUML/curso-estados.svg)<br><sup>[*Código fuente*](/modelosUML/curso-estados.puml)</sup>|![](/images/modelosUML/aula-estados.svg)<br><sup>[*Código fuente*](/modelosUML/aula-estados.puml)</sup>
|-|-

</div>

## Requisitos

### Actores y Casos de uso

<div align=center>

|![](/images/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-001.svg)
|-:
<sup>[*Código fuente*](/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-001.puml)</sup>

|![](/images/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-002.svg)
|-:
<sup>[*Código fuente*](/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-002.puml)</sup>

|![](/images/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-003.svg)
|-:
<sup>[*Código fuente*](/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-003.puml)</sup>

</div>

### Diagrama de contexto

<div align=center>

|![](/images/RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.svg)
|-:
<sup>[*Código fuente*](/RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.puml)</sup>

</div>

### Detalle de casos de uso

#### CdU 1: crearAula()

<div align=center>

|Detalle|Prototipo|
|:-:|:-:|
|![](/images/RUP/00-casos-uso/02-detalle/crearAula/crearAula.svg)<br><sup>[*Código fuente*](/RUP/00-casos-uso/02-detalle/crearAula/especificacion.puml)</sup>|![](/images/RUP/00-casos-uso/02-detalle/crearAula/crearAula-wireframe.svg)<br><sup>[*Código fuente*](/RUP/00-casos-uso/02-detalle/crearAula/wireframes.puml)</sup>|

</div>

#### CdU 2: configurarPreferenciasProfesor()

<div align=center>

|Detalle|Prototipo|
|:-:|:-:|
|![](/images/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/configurarPreferenciasProfesor.svg)<br><sup>[*Código fuente*](/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/especificacion.puml)</sup>|![](/images/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/configurarPreferenciasProfesor-wireframe.svg)<br><sup>[*Código fuente*](/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/wireframes.puml)</sup>|

</div>

#### CdU 3: editarAula()

<div align=center>

|Detalle|Prototipo|
|:-:|:-:|
|![](/images/RUP/00-casos-uso/02-detalle/editarAula/editarAula.svg)<br><sup>[*Código fuente*](/RUP/00-casos-uso/02-detalle/editarAula/especificacion.puml)</sup>|![](/images/RUP/00-casos-uso/02-detalle/editarAula/editarAula-wireframe.svg)<br><sup>[*Código fuente*](/RUP/00-casos-uso/02-detalle/editarAula/wireframes.puml)</sup>|

</div>

#### CdU 4: abrirAulas()

<div align=center>

|Detalle|Prototipo (GUI)|Prototipo (API REST)|
|:-:|:-:|:-:|
|![](/images/RUP/00-casos-uso/02-detalle/abrirAulas/abrirAulas.svg)<br><sup>[*Código fuente*](/RUP/00-casos-uso/02-detalle/abrirAulas/especificacion.puml)</sup>|![](/images/RUP/00-casos-uso/02-detalle/abrirAulas/abrirAulas-wireframe.svg)<br><sup>[*Código fuente*](/RUP/00-casos-uso/02-detalle/abrirAulas/prototipo.puml)</sup>|[Ver contrato REST](/RUP/00-casos-uso/02-detalle/abrirAulas/prototipo-api.md#endpoint-principal)|

</div>

## Análisis

### Analisis de casos de uso

#### CdU 1: crearAula()

<div align=center>

|![](/images/RUP/01-analisis/casos-uso/crearAula/crearAula-analisis.svg)
|-:
<sup>[*Código fuente*](/RUP/01-analisis/casos-uso/crearAula/colaboracion.puml)</sup>

</div>

#### CdU 2: configurarPreferenciasProfesor()

<div align=center>

|![](/images/RUP/01-analisis/casos-uso/configurarPreferenciasProfesor/configurarPreferenciasProfesor-analisis.svg)
|-:
<sup>[*Código fuente*](/RUP/01-analisis/casos-uso/configurarPreferenciasProfesor/colaboracion.puml)</sup>

</div>

#### CdU 3: editarAula()

<div align=center>

|![](/images/RUP/01-analisis/casos-uso/editarAula/editarAula-analisis.svg)
|-:
<sup>[*Código fuente*](/RUP/01-analisis/casos-uso/editarAula/colaboracion.puml)</sup>

</div>

#### CdU 4: abrirAulas()

<div align=center>

|![](/images/RUP/01-analisis/casos-uso/abrirAulas/abrirAulas-analisis.svg)
|-:
<sup>[*Código fuente*](/RUP/01-analisis/casos-uso/abrirAulas/colaboracion.puml)</sup>

</div>

### Diagrama de clases de análisis

<div align=center>

|Inventario (solo nombres)|Inventario + métodos|
|:-:|:-:|
|![](/images/RUP/01-analisis/clases-analisis.svg)<br><sup>[*Código fuente*](/RUP/01-analisis/clases-analisis.puml)</sup>|![](/images/RUP/01-analisis/clases-analisis-metodos.svg)<br><sup>[*Código fuente*](/RUP/01-analisis/clases-analisis-metodos.puml)</sup>|
|**Diagrama de clases** (+ relaciones)|**Diagrama de clases** + métodos|
|![](/images/RUP/01-analisis/clases-analisis-relaciones.svg)<br><sup>[*Código fuente*](/RUP/01-analisis/clases-analisis-relaciones.puml)</sup>|![](/images/RUP/01-analisis/clases-analisis-metodos-relaciones.svg)<br><sup>[*Código fuente*](/RUP/01-analisis/clases-analisis-metodos-relaciones.puml)</sup>|

</div>

## Diseño

> Stack de ejemplo: FastAPI + React (rama [`diseño-fastapi-react`](https://github.com/mmasias/pySigHor/tree/diseño-fastapi-react)).

### Diseño de casos de uso

#### CdU 1: crearAula()

<div align=center>

|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/casos-uso/crearAula/secuencia.svg)
|-:
<sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/casos-uso/crearAula/secuencia.puml)</sup>

</div>

#### CdU 2: configurarPreferenciasProfesor()

<div align=center>

|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/casos-uso/configurarPreferenciasProfesor/secuencia.svg)
|-:
<sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/casos-uso/configurarPreferenciasProfesor/secuencia.puml)</sup>

</div>

#### CdU 3: editarAula()

<div align=center>

|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/casos-uso/editarAula/secuencia.svg)
|-:
<sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/casos-uso/editarAula/secuencia.puml)</sup>

</div>

#### CdU 4: abrirAulas()

<div align=center>

|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/casos-uso/abrirAulas/secuencia.svg)
|-:
<sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/casos-uso/abrirAulas/secuencia.puml)</sup>

</div>

### Diagrama de clases de diseño

<div align=center>

|Inventario (solo nombres)|Inventario + atributos/métodos|
|:-:|:-:|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/clases-diseño.svg)<br><sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/clases-diseño.puml)</sup>|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/clases-diseño-metodos.svg)<br><sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/clases-diseño-metodos.puml)</sup>|
|**Diagrama de clases** (+ relaciones)|**Diagrama de clases** + atributos/métodos|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/clases-diseño-relaciones.svg)<br><sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/clases-diseño-relaciones.puml)</sup>|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/clases-diseño-metodos-relaciones.svg)<br><sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/clases-diseño-metodos-relaciones.puml)</sup>|

</div>

### Diagrama Entidad-Relación (DER)

<div align=center>

|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/DER.svg)
|-:
<sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/DER.puml)</sup>

</div>

### Diagrama de despliegue

<div align=center>

|Estado actual (desarrollo local)|
|:-:|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/despliegue-actual.svg)<br><sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/despliegue-actual.puml)</sup>|

</div>

<div align=center>

|Objetivo (un servidor, Docker)|Objetivo distribuido (dos servidores)|
|:-:|:-:|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/despliegue-objetivo.svg)<br><sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/despliegue-objetivo.puml)</sup>|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/despliegue-objetivo-distribuido.svg)<br><sup>[*Código fuente*](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/02-diseño/despliegue-objetivo-distribuido.puml)</sup>|

</div>

## Desarrollo

#### CdU 1: crearAula()

[Ver artefactos de código](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/03-desarrollo/casos-uso/crearAula/README.md)

#### CdU 2: configurarPreferenciasProfesor()

[Ver artefactos de código](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/03-desarrollo/casos-uso/configurarPreferenciasProfesor/README.md)

#### CdU 3: editarAula()

[Ver artefactos de código](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/03-desarrollo/casos-uso/editarAula/README.md)

#### CdU 4: abrirAulas()

[Ver artefactos de código](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/03-desarrollo/casos-uso/abrirAulas/README.md)
