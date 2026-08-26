Corrección de arquitectura para los 7 casos de la rebanada vertical de Guia.
Reemplaza el mecanismo de "borrador" (columna/JSON en Guia, materializarBorrador(),
create-vs-update por id) construido hasta ahora -- era más complejo de lo necesario.
Principio nuevo, más simple:

1. CREAR/EDITAR/ELIMINAR de PonderacionEvaluacion y ReferenciaBibliografica: CRUD
   real e inmediato contra su propio repositorio, sin tocar Guia en ningún momento.
   - crearReferenciaBibliografica()/editarReferenciaBibliografica(): sin validación
     de negocio (ya lo dice su propia ficha de Requisitos).
   - crearPonderacionEvaluacion()/editarPonderacionEvaluacion(): la única validación
     es "el máximo puntual" -- el valor introducido, por sí solo, no puede superar
     el ponderacionMaxima de su SistemaEvaluacion. Nada de sumar contra hermanas,
     nada de "excluir el valor anterior" en editar (eso solo hacía falta cuando
     la validación era una suma; ya no lo es). Quita de los tres diagramas ya
     construidos: obtenerPonderacionesDe(), calcularMargenDisponible(), y
     cualquier llamada a Guia dentro de estos cuatro casos de uso.
   - eliminarPonderacionEvaluacion()/eliminarReferenciaBibliografica() (fuera de
     este lote, pero deja esto anotado para cuando toquen): no borran la fila --
     quitan el ítem de la lista que el profesor está construyendo en la sub-vista.
     La fila puede seguir existiendo; lo que cambia es si aparece en la lista que
     se le pasa a guardarBorradorGuia().

2. abrirGuia(): lee lo ya vinculado a Guia MÁS lo pendiente-sin-vincular de la
   sesión (creado/editado en las sub-vistas), y lo muestra fusionado. No vincula
   nada -- solo lectura y presentación.

3. guardarBorradorGuia(): recibe, para cada colección (PonderacionEvaluacion,
   ReferenciaBibliografica), la lista completa tal como debería quedar -- no
   eventos de alta/baja por ítem. Sincroniza por diff contra lo que Guia ya
   tiene vinculado: lo que está en la lista y no estaba vinculado, se vincula;
   lo que estaba vinculado y ya no aparece en la lista, se desvincula. Sin
   ninguna validación de rango ni de suma -- nunca rechaza, siempre guarda.

4. enviarGuiaARevision(): dos pasos, en este orden.
   - Precondición: si queda algo sin guardar (pendiente sin vincular), rechaza
     -- "guarda el borrador primero". No materializa nada él mismo.
   - Si no hay pendientes: valida, contra lo ya vinculado, las dos reglas del
     dominio -- suma por SistemaEvaluacion dentro de [mínima, máxima] Y suma
     total = 100%. Si pasa: transiciona el estado de la Guia y persiste solo
     la Guia (ningún crear()/actualizar() de hijos -- eso ya lo hizo
     guardarBorradorGuia() antes).

Ficheros a corregir (colaboracion.puml + README.md de cada uno):
- crearReferenciaBibliografica, crearPonderacionEvaluacion,
  editarPonderacionEvaluacion: quitar toda llamada a Guia; dejar solo el CRUD
  contra su propio repositorio (+ validación de máximo puntual en las dos de
  PonderacionEvaluacion).
- abrirGuia: añadir la fusión vinculado+pendiente descrita en el punto 2.
- guardarBorradorGuia: reemplazar materializarBorrador()/crear()-actualizar()
  por id, por la sincronización de lista completa del punto 3.
- enviarGuiaARevision: quitar materializarBorrador() y los crear()/actualizar()
  de hijos; añadir la precondición de "sin pendientes" antes del <<choice>> de
  rango+100%.

Fuera de alcance de esta corrección: abrirPonderacionesEvaluacion(),
abrirReferenciasBibliograficas() (mismo mecanismo de fusión que abrirGuia(),
pero no construidos todavía) y eliminarPonderacionEvaluacion()/
eliminarReferenciaBibliografica() (mecanismo ya descrito arriba, construcción
pendiente).
