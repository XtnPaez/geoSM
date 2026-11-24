# geoSM
**Observatorio Territorial de General San Martín**

![Estado](https://img.shields.io/badge/estado-formulación-yellow) ![Ámbito](https://img.shields.io/badge/ámbito-General%20San%20Martín-lightgrey)

Iniciativa ciudadana independiente, no gubernamental, de información geográfica, datos abiertos y diagnóstico territorial. Busca demostrar también la capacidad profesional de integrar SIG, ingeniería de datos, Git, IA e infraestructura eficiente sin resignar calidad.

| Producto | Función | Directorio |
|---|---|---|
| geoSM | Observatorio | `site/` |
| geoSMart | Visualizador | `visor/` |
| geoSM Datos | Catálogo y datos publicables | `datos/` |
| geoSM Informes | Análisis territoriales | `informes/` |
| geoSM Lab | Procesos y experimentación | `lab/` |

## Documentación
- [Documento fundacional vigente](docs/documento_fundacional.md)
- [Decisiones](docs/decisiones.md)
- [Roadmap](docs/roadmap.md)
- [Identidad visual](docs/identidad_visual.md)
- [Inventario y evaluación](docs/inventario.md)
- [Política editorial](docs/politica_editorial.md)
- [Infraestructura pendiente](docs/infraestructura.md)
- [Cambios](CHANGELOG.md)

Estado: estructura inicial; no hay visor, capas verificadas ni informes publicados. Repositorio: https://github.com/XtnPaez/geoSM . No representa al municipio. Licencias de código y productos propios pendientes de definición; la apertura prevista no equivale a una licencia concedida.

## Prototipo 0.1.0 (local, no publicar todavía)

Desde la raíz: `python tools/preparar.py` (requiere internet para descargar Leaflet 1.9.4 y Bootstrap 5.3.3 a archivos locales, con licencias). Luego `python -m http.server 8000 --directory site` y abrir http://localhost:8000/. Las teselas OSM requieren conexión. No abrir HTML por file://.

La aplicación vive en `site/`; las capas canónicas en `datos/publicados/geografias/`. El script copia las capas al sitio local. No hay despliegue automático: **no subir las capas a un repositorio público hasta confirmar permisos de redistribución**. El ZIP contiene datos para pruebas privadas. Para GitHub Pages se deberá preparar un artefacto estático desde site/ mediante Actions, tras autorización. DNS diferido.

El catálogo de capas es `site/assets/layers.json`. Los indicadores y su JOIN quedan previstos, no implementados. No se han ejecutado pruebas de navegador ni de red. El entorno de creación no pudo descargar bibliotecas; el script es requisito previo.

## Actualización 0.1.1
Superponer los archivos del ZIP de actualización en la raíz. No volver a ejecutar preparar.py si las dependencias y geografías ya están instaladas. Header y footer en `site/assets/partials/`; navegación resuelta desde layout.js para subrutas de GitHub Pages. Probar por HTTP, no file://.

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
