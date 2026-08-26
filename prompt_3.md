Construcción de eliminarPonderacionEvaluacion() y eliminarReferenciaBibliografica()
en RUP/02-analisis/casos-uso/ -- extiende la rebanada vertical de Guia (ya no son 7
casos, son 9) con la única pieza del mecanismo corregido en prompt_2.md que ningún
caso existente ejercita todavía: el camino de "quitar algo de la lista" y que
guardarBorradorGuia() lo desvincule por ausencia. No es completar catálogo -- es
cerrar el hueco de validación de la corrección anterior antes de pasar a Diseño.

No arrancar hasta confirmar que la corrección del pedido anterior está aplicada y
verificada -- este lote construye sobre guardarBorradorGuia() tal como queda tras
esa corrección.

Diseño de las dos, verificado contra especificacion.puml de Requisitos (sin
<<choice>>, patrón confirmar/cancelar -- rama verde y rama azul, ambas terminan en
el mismo estado de salida, PONDERACIONES_EVALUACION_ABIERTO/
REFERENCIAS_BIBLIOGRAFICAS_ABIERTO -- por eso sí llevan flujo de colaboración
numerado pese a no tener <<choice>>: "más de un camino posible entre los mismos
nodos" es uno de los disparadores ya fijados en RUP/02-analisis/README.md):

- No tocan la fila de PonderacionEvaluacion/ReferenciaBibliografica. No la borran,
  no la editan, no llaman a ningún repositorio de esa entidad.
- No tocan Guia.
- Su único efecto es quitar el ítem de la lista de trabajo de la sesión (la misma
  lista que abrirPonderacionesEvaluacion()/abrirReferenciasBibliograficas()/
  abrirGuia() construyen por fusión vinculado+pendiente, y que guardarBorradorGuia()
  recibirá completa al guardar). Rama verde (confirmar): lo quita. Rama azul
  (cancelar): no hace nada, misma salida.
- Consecuencia directa: estas dos son, deliberadamente, las primeras del catálogo
  sin ninguna clase de Modelo en su diagrama de colaboración -- Vista y Controlador
  únicamente. No fuerces una clase de Modelo por consistencia con el resto del lote;
  la ausencia es el reflejo correcto de que no hay ninguna entidad de dominio
  involucrada en esta operación. Explícalo así en el README de cada una (sección
  Propósito), para que no se lea como un olvido en la próxima auditoría.
- Nombrado: EliminarPonderacionEvaluacionView/PonderacionEvaluacionController y
  EliminarReferenciaBibliograficaView/ReferenciaBibliograficaController -- reutiliza
  los mismos Controladores ya usados en crear/editar de cada entidad, no crees
  controladores nuevos.

Ficheros a crear, mismo formato que los 7 ya construidos (colaboracion.puml +
README.md, entrada en RUP/02-analisis/casos-uso/README.md):
- RUP/02-analisis/casos-uso/eliminarPonderacionEvaluacion/
- RUP/02-analisis/casos-uso/eliminarReferenciaBibliografica/

Sigue fuera de alcance: abrirPonderacionesEvaluacion()/abrirReferenciasBibliograficas()
-- no aportan nada nuevo que validar (misma fusión que abrirGuia(), ya probada);
quedan para un lote posterior sin urgencia arquitectónica.
