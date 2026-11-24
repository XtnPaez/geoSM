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
