# Artefactos

**pySigHor**: proyecto de un constructor de Horarios

## Modelo del dominio

<div align=center>

|![](/images/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.svg)
|-

</div>

### Diagrama de estados de entidades

<div align=center>

|![](/images/modelosUML/curso-estados.svg)|![](/images/modelosUML/aula-estados.svg)
|-|-

</div>

### Glosario

[Ver glosario completo](/RUP/00-casos-uso/00-modelo-del-dominio/modelo-dominio.md#glosario)

## Requisitos

### Actores y Casos de uso

<div align=center>

|![](/images/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-001.svg)
|-
|![](/images/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-002.svg)
|-
|![](/images/RUP/00-casos-uso/01-actores-casos-uso/actores-casos-uso-003.svg)
|-

</div>

### Diagrama de contexto

<div align=center>

|![](/images/RUP/00-casos-uso/01-actores-casos-uso/diagrama-contexto-administrador.svg)
|-

</div>

### Detalle de casos de uso

#### CdU 1: crearAula()

<div align=center>

|![](/images/RUP/00-casos-uso/02-detalle/crearAula/crearAula.svg)|![](/images/RUP/00-casos-uso/02-detalle/crearAula/crearAula-wireframe.svg)
|-|-

</div>

#### CdU 2: configurarPreferenciasProfesor()

<div align=center>

|![](/images/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/configurarPreferenciasProfesor.svg)|![](/images/RUP/00-casos-uso/02-detalle/configurarPreferenciasProfesor/configurarPreferenciasProfesor-wireframe.svg)
|-|-

</div>

#### CdU 3: editarAula()

<div align=center>

|![](/images/RUP/00-casos-uso/02-detalle/editarAula/editarAula.svg)|![](/images/RUP/00-casos-uso/02-detalle/editarAula/editarAula-wireframe.svg)
|-|-

</div>

## Análisis

### Analisis de casos de uso

#### CdU 1: crearAula()

<div align=center>

|![](/images/RUP/01-analisis/casos-uso/crearAula/crearAula-analisis.svg)
|-

</div>

#### CdU 2: configurarPreferenciasProfesor()

<div align=center>

|![](/images/RUP/01-analisis/casos-uso/configurarPreferenciasProfesor/configurarPreferenciasProfesor-analisis.svg)
|-

</div>

#### CdU 3: editarAula()

<div align=center>

|![](/images/RUP/01-analisis/casos-uso/editarAula/editarAula-analisis.svg)
|-

</div>

### Diagrama de clases de análisis

<div align=center>

|Inventario (solo nombres)|Inventario + métodos|
|:-:|:-:|
|![](/images/RUP/01-analisis/clases-analisis.svg)|![](/images/RUP/01-analisis/clases-analisis-metodos.svg)|
|**Diagrama de clases** (+ relaciones)|**Diagrama de clases** + métodos|
|![](/images/RUP/01-analisis/clases-analisis-relaciones.svg)|![](/images/RUP/01-analisis/clases-analisis-metodos-relaciones.svg)|

</div>

## Diseño

> Stack de ejemplo: FastAPI + React (rama [`diseño-fastapi-react`](https://github.com/mmasias/pySigHor/tree/diseño-fastapi-react)).

### Diseño de casos de uso

#### CdU 1: crearAula()

<div align=center>

|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/casos-uso/crearAula/secuencia.svg)
|-

</div>

#### CdU 2: configurarPreferenciasProfesor()

<div align=center>

|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/casos-uso/configurarPreferenciasProfesor/secuencia.svg)
|-

</div>

#### CdU 3: editarAula()

<div align=center>

|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/casos-uso/editarAula/secuencia.svg)
|-

</div>

### Diagrama de clases de diseño

<div align=center>

|Inventario (solo nombres)|Inventario + atributos/métodos|
|:-:|:-:|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/clases-diseño.svg)|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/clases-diseño-metodos.svg)|
|**Diagrama de clases** (+ relaciones)|**Diagrama de clases** + atributos/métodos|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/clases-diseño-relaciones.svg)|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/clases-diseño-metodos-relaciones.svg)|

</div>

### Diagrama de despliegue

<div align=center>

|Estado actual (desarrollo local)|
|:-:|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/despliegue-actual.svg)|

</div>

<div align=center>

|Objetivo (un servidor, Docker)|Objetivo distribuido (dos servidores)|
|:-:|:-:|
|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/despliegue-objetivo.svg)|![](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/02-diseño/despliegue-objetivo-distribuido.svg)|

</div>

## Desarrollo

#### CdU 1: crearAula()

[Ver artefactos de código](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/03-desarrollo/casos-uso/crearAula/README.md)

#### CdU 2: configurarPreferenciasProfesor()

[Ver artefactos de código](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/03-desarrollo/casos-uso/configurarPreferenciasProfesor/README.md)

#### CdU 3: editarAula()

[Ver artefactos de código](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/RUP/03-desarrollo/casos-uso/editarAula/README.md)
