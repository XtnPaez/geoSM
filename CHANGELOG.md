# Cambios
## 2026-11-24 — Estructura inicial (sin release de software)
- Consolidación de identidad de observatorio y cinco productos.
- Registro de decisiones, paleta, metodología propuesta y pendientes.
- Directorios reservados; sin datos ni aplicación implementada.

## 0.1.0 — prototipo local
- Portada institucional y cuatro productos; visor Leaflet y catálogo JSON.
- Partido y 29 localidades; eliminado duplicado de nivel distinto según confirmación.
- CSS responsive, controles de capas, consulta y encuadre.
- Pendiente instalación de bibliotecas y pruebas de navegador; no publicado.

## 0.1.1 — ajustes de interfaz
- Consulta en popup Leaflet; botón de consulta del partido para no interceptar localidades.
- Header y footer compartidos; navegación con bullets cromáticos y marca SM.
- Usuario confirmó funcionamiento de 0.1.0 y descarga de bibliotecas. Pruebas de esta revisión y responsive pendientes.

## 0.1.2 — 2026-11-24

- Header y footer persistentes; navegación con badges.
- Orden de capas mediante flechas; prioridad visual y de clic por pane Leaflet. Localidades arriba inicialmente.
- Eliminados botones de encuadre y consulta del partido; consulta directa.
- Fuentes informadas: IGN (partido), Poblaciones.org (localidades). Recurso exacto y licencias pendientes.
- Prueba de navegador y móvil pendiente; no publicar datos hasta verificar permisos.

## 0.1.3 — 2026-11-24

- Badges informativos sin enlace, fondo institucional y texto blanco; navegación independiente.
- Jerarquía de capas, header y footer aprobados por el responsable. Prueba móvil diferida.
- Datos declarados abiertos por el responsable; licencia específica, recurso exacto y condiciones de atribución aún no documentados ni verificados.
- GitHub Pages pendiente de publicación.

## 0.1.4 — 2026-11-24

- Los badges institucionales son los enlaces de navegación; se eliminan los textos inferiores. Sustituye la decisión de 0.1.3.
- Se conserva el fondo cromático y el texto blanco; la sección activa se distingue con un contorno blanco.
- Prueba visual pendiente. Responsive, GitHub Pages y dominio diferidos.

## 0.1.5 — 2026-11-27

- Badges de navegación sin cambios visuales por hover, clic o sección activa; se conserva foco de teclado.
- Portada simplificada y cuatro fichas con botones cromáticos.
- Página Proyecto accesible desde el footer; texto institucional propuesto.
- Visualizador y datos sin cambios. Responsive, publicación y DNS diferidos.

## 0.1.5 — Corrección de presentación (2026-11-27)
- El título institucional aprovecha el ancho disponible; el tamaño se adapta a pantallas estrechas.
- Eliminado el botón principal redundante «Explorar el mapa» de la portada.
- Botones cromáticos de las cuatro fichas con estilos explícitos.
- Footer simplificado a geoSM · GitHub · Prototipo 0.1.5 // Proyecto (badge naranja).
- Inclusión de la página Proyecto y carga de fragmentos sin caché para evitar mostrar versiones anteriores.
- Versionado de CSS y script de layout en las páginas para actualizar la caché del navegador.
- Responsive integral, GitHub Pages y dominio continúan diferidos.


## 0.2.0 — Catálogo de datos (2026-11-27)

Catálogo estático inspirado en CKAN; inventario compartido `site/assets/layers.json`. Descargas GeoJSON y GeoPackage; QMD diferido. Ejecutar `python tools/publicar_datos.py` para copiar recursos locales sin descargar bibliotecas. Licencias específicas pendientes de verificar antes de publicación pública.

## 0.2.1 — Licencias y cierre local (2026-11-27)

- El responsable confirmó todas las pruebas funcionales del catálogo 0.2.0 y el inventario compartido; navegador validado.
- Se adopta CC BY 4.0 para contenidos originales propios y MIT para código propio. Véase [política de licencias](LICENSE.md) en la raíz. Los materiales de terceros conservan sus condiciones; permisos concretos de redistribución pendientes.
- Proyecto explica la elección de licencias; footer actualizado.
- Metadatos ampliados, QMD y pruebas responsive diferidos. Próxima meta: preparar GitHub, Actions, Pages y dominio geosm.ar; sin publicación ni cambios remotos realizados.
