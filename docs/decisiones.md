# Registro de decisiones
Fecha de consolidación: 2026-11-24.

| ID | Estado | Decisión | Justificación |
|---|---|---|---|
| D01 | Acordada | Observatorio ciudadano con IDE como núcleo | Utilidad pública y conocimiento territorial |
| D02 | Acordada | Finalidad profesional explícita | Demostrar integración de capacidades y calidad |
| D03 | Acordada | Incorporación gradual sin calendario rígido | Sostenibilidad |
| D04 | Acordada | Diagnósticos rigurosos, no solo descripción | Potencial analítico |
| D05 | Acordada | OpenStreetMap como base | Referencia cartográfica común |
| D06 | Acordada | Cinco productos y color variable en SM | Identidad coherente |
| D07 | Delegada | Tonos accesibles y reglas visuales | Encargo explícito al asistente |
| D08 | Acordada | Repositorio XtnPaez/geoSM | Versionado público |
| D09 | Decisión de estructura delegada | Monorepo modular | Evitar fragmentación inicial; alternativa: repos separados |
| D10 | Propuesta | Comunicar capas en preparación | Transparencia sin prometer fechas |
| D11 | Propuesta | Instagram institucional y LinkedIn profesional | Dos públicos; sin cuentas creadas |
| D12 | Propuesta | Autoría visible y desarrollo abierto | Evidencia profesional |
| D13 | Pendiente | Arquitectura, proveedor OSM, licencias, tipografía, lanzamiento | Requieren evaluación |
| D14 | Propuesta | Modelo de inventario y criterios de evaluación | Validar durante relevamiento |

No se han publicado archivos en GitHub ni adoptado servicios de alojamiento. Las propuestas no constituyen compromisos.

## 2026-11-24 — Arquitectura inicial acordada
Dominio geosm.ar registrado; DNS diferido. Git como eje; GitHub Pages, HTML/CSS/JS, Bootstrap y Leaflet locales; otros recursos CDN según necesidad. QGIS/PostGIS, originales y respaldos locales. OSM base, GeoJSON inicial, diseño responsive, portada institucional. Dos capas iniciales; radios diferidos. Indicadores separados y JOIN previsto. Se elimina del prototipo el registro de localidad con código 06371010 según confirmación del responsable; se preservan dos códigos nulos. Fuente geométrica y licencias pendientes. Versiones de bibliotecas elegidas para el prototipo: Leaflet 1.9.4 y Bootstrap 5.3.3.

## 2026-11-24 — Ajustes de interfaz (acordados)
Consulta de polígonos fuera del panel lateral; navegación con bullets de cada producto; únicamente SM coloreado en nombres de marca; header y footer compartidos. Implementación elegida: popup Leaflet y fragmentos HTML cargados con JavaScript. Pruebas responsive pendientes.

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

## 2026-11-27 — Correcciones de portada v0.1.5 (acordadas)
- Encabezado institucional en una línea cuando el ancho de pantalla lo permita; adaptación de tipografía en dispositivos pequeños.
- Se elimina el CTA independiente «Explorar el mapa»; las cuatro tarjetas conservan sus enlaces como botones de color propio.
- Footer: `geoSM · GitHub · Prototipo 0.1.5 // Proyecto`. Proyecto es una sección institucional accesible desde el footer, representada con un badge naranja. No se agrega al navbar.
- Corrección técnica: evitar mostrar versiones antiguas de CSS y fragmentos compartidos por la caché del navegador.
- Pendiente: comprobación en navegador, pruebas responsive y publicación.


## 0.2.0 — Catálogo de datos (2026-11-27)

Catálogo estático inspirado en CKAN; inventario compartido `site/assets/layers.json`. Descargas GeoJSON y GeoPackage; QMD diferido. Ejecutar `python tools/publicar_datos.py` para copiar recursos locales sin descargar bibliotecas. Licencias específicas pendientes de verificar antes de publicación pública.

## 0.2.1 — Licencias y cierre local (2026-11-27)

- El responsable confirmó todas las pruebas funcionales del catálogo 0.2.0 y el inventario compartido; navegador validado.
- Se adopta CC BY 4.0 para contenidos originales propios y MIT para código propio. Véase [política de licencias](../LICENSE.md) en la raíz. Los materiales de terceros conservan sus condiciones; permisos concretos de redistribución pendientes.
- Proyecto explica la elección de licencias; footer actualizado.
- Metadatos ampliados, QMD y pruebas responsive diferidos. Próxima meta: preparar GitHub, Actions, Pages y dominio geosm.ar; sin publicación ni cambios remotos realizados.
