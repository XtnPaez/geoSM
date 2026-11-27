# Infraestructura — precisiones pendientes
Acordado: OSM como base, costo recurrente objetivo cero, calidad y portabilidad. No confundir licencia de datos OSM con política de teselas. Verificar atribución, caché, restricciones, CORS, disponibilidad y proveedor antes de publicar: https://operations.osmfoundation.org/policies/tiles/ y https://www.openstreetmap.org/copyright .

Evaluar procesamiento local QGIS/PostGIS, alojamiento estático GitHub Pages o alternativas, GeoJSON/PMTiles, Leaflet/MapLibre. Supabase solo ante necesidad dinámica comprobada. Medir tamaños, solicitudes parciales, cuotas, rendimiento móvil, mantenimiento y costos. No se han hecho pruebas ni seleccionado stack. Mantener originales fuera del repo público salvo autorización expresa; separar procesamiento y productos. Definir licencias propias antes de publicar. No guardar credenciales.

Actualización: decisiones acordadas en docs/decisiones.md. Vista local mediante servidor HTTP estático; preparación con tools/preparar.py. No hay backend ni base remota. Proveedor de teselas propuesto para pruebas: tile.openstreetmap.org; verificar política y capacidad antes de publicar. DNS y despliegue diferidos.

## Estado al 27 de noviembre de 2026

Stack acordado: QGIS/PostGIS local, HTML/CSS/JS, Leaflet y Bootstrap locales, OSM, GitHub Pages previsto. Catálogo y descargas validados localmente. Licencias propias adoptadas (ver LICENSE.md en raíz). Próxima etapa: revisar archivos publicables, permisos de terceros y política de teselas; configurar Actions, Pages, DNS y HTTPS. No se ha realizado despliegue. Metadatos ampliados y pruebas móviles diferidos.
