# geoSM
## Documento fundacional — Infraestructura de Datos Espaciales de iniciativa ciudadana de General San Martín

**Versión:** 0.1 — Propuesta inicial  
**Fecha:** 24 de noviembre de 2026  
**Ámbito:** Partido de General San Martín, provincia de Buenos Aires, Argentina  
**Naturaleza:** Iniciativa ciudadana independiente, no gubernamental  
**Estado:** Formulación y diseño

## 1. Fundamentación

La información geográfica de un territorio constituye un recurso para conocerlo, comprender sus desigualdades, reconocer sus equipamientos y participar de las discusiones sobre su desarrollo. Sin embargo, la información disponible suele encontrarse dispersa entre organismos, formatos, escalas y períodos de referencia diferentes. Su aprovechamiento exige conocimientos y herramientas que no siempre están al alcance de la ciudadanía.

geoSM nace como una iniciativa vecinal orientada a reunir, organizar, documentar y publicar información geográfica del partido de General San Martín. Se propone aprovechar fuentes existentes, capacidades técnicas SIG y tecnologías abiertas para reducir las barreras de acceso a la información territorial.

No se trata de sustituir a los organismos productores de información ni de construir un portal oficial paralelo. Se trata de generar un espacio independiente de consulta, integración y reutilización de datos territoriales, reconociendo su procedencia y sus limitaciones.

## 2. Misión y visión

**Misión:** facilitar el acceso público a información geográfica de General San Martín mediante un visualizador abierto y un conjunto de datos documentados y reutilizables.

**Visión:** consolidar progresivamente una infraestructura de datos espaciales ciudadana, sostenible, transparente y replicable en otros municipios, capaz de servir a vecinos, organizaciones comunitarias, instituciones educativas, investigadores y periodistas.

## 3. Objetivos

- Inventariar y evaluar fuentes de información geográfica relevantes para el municipio.
- Integrar y normalizar capas procedentes de distintas instituciones y períodos.
- Desarrollar un visualizador web de acceso público, sin registro obligatorio.
- Publicar datos descargables cuando las condiciones legales y técnicas lo permitan.
- Documentar fuentes, metodologías, calidad, vigencia y limitaciones.
- Construir procedimientos reproducibles de actualización y publicación.
- Mantener un costo monetario recurrente objetivo de cero durante la etapa inicial.
- Favorecer la participación y reutilización ciudadana sin comprometer la privacidad ni la calidad de los datos.

## 4. Principios rectores

| Principio | Aplicación |
|---|---|
| Independencia | No representar al gobierno municipal ni sugerir aval institucional inexistente. |
| Apertura | Código abierto y datos reutilizables según sus licencias. |
| Transparencia | Identificar fuentes, fechas, transformaciones y limitaciones. |
| Accesibilidad | Consulta gratuita, interfaz comprensible y diseño adaptable. |
| Rigor territorial | Validación espacial, identificadores estables y respeto por escalas y unidades geográficas. |
| Privacidad | Excluir datos personales y evaluar riesgos de reidentificación. |
| Sostenibilidad | Minimizar costos, mantenimiento y dependencias externas. |
| Reproducibilidad | Conservar originales y documentar procesos de transformación. |
| Neutralidad metodológica | Diferenciar hechos, estimaciones, interpretaciones y aportes ciudadanos. |

## 5. Alcance territorial y temático

El ámbito inicial es el partido de General San Martín. La información externa al límite municipal podrá incorporarse cuando sea necesaria para comprender relaciones territoriales, continuidad urbana o accesibilidad a servicios.

El siguiente catálogo es potencial: no implica que las capas estén disponibles, verificadas ni autorizadas para publicación.

| Eje | Capas candidatas |
|---|---|
| Referencia territorial | Límite municipal, localidades, barrios, calles y manzanas. |
| Población | Radios y fracciones censales, población, hogares e indicadores. |
| Educación | Establecimientos y equipamientos educativos. |
| Salud | Hospitales, centros de atención y otros efectores. |
| Movilidad | Red vial, transporte público, estaciones y recorridos. |
| Ambiente | Espacios verdes, cursos de agua, riesgo hídrico y arbolado. |
| Desarrollo urbano | Usos del suelo, normativa urbanística y parcelario autorizado. |
| Comunidad | Clubes, bibliotecas, centros culturales y organizaciones. |
| Infraestructura | Equipamientos y servicios urbanos con información publicable. |
| Historia territorial | Cartografía histórica y series temporales disponibles. |

## 6. Productos previstos

1. **Visualizador geográfico:** navegación, selección de capas, leyendas, consulta de atributos, fuentes y fechas de referencia. Incorporación gradual de búsquedas, filtros y descargas.
2. **Catálogo de datos:** inventario público con metadatos y enlaces a recursos reutilizables.
3. **Repositorio de procesos:** scripts, consultas y procedimientos de normalización, validación y publicación.
4. **Documentación:** arquitectura, metodología, decisiones, manuales y registro de cambios.

El visualizador será el primer producto visible, pero los datos y su trazabilidad constituyen el núcleo del proyecto.

## 7. Arquitectura tecnológica propuesta

Se propone una arquitectura estática como punto de partida. La producción se realiza localmente y la consulta pública no requiere que la computadora del responsable permanezca encendida.

```text
Fuentes oficiales y comunitarias autorizadas
                    |
                    v
        Originales preservados (raw)
                    |
                    v
         QGIS / PostgreSQL + PostGIS
                    |
                    v
       Normalización y control de calidad
                    |
                    v
       Exportación de productos publicados
        GeoJSON / PMTiles / CSV / JSON
                    |
                    v
       Repositorios y alojamiento estático
                    |
                    v
        Visualizador Leaflet o MapLibre
                    |
                    v
                Ciudadanía
```

Los servicios externos de mapas base y capas podrán consumirse directamente desde el visor, previa revisión de disponibilidad, licencia, atribución, CORS y condiciones de uso.

### 7.1 Alojamiento sin costo recurrente

| Alternativa | Función posible | Condición a verificar |
|---|---|---|
| GitHub Pages | Visualizador y archivos estáticos | Cuotas, tamaño de archivos, transferencia y solicitudes HTTP parciales. |
| Cloudflare Pages | Alojamiento estático alternativo | Límites por archivo, cantidad de archivos y comportamiento de caché. |
| Supabase | Base PostGIS y API dinámica futura | Cuotas, suspensión por inactividad, seguridad y transferencia. |

Referencias: [GitHub Pages](https://pages.github.com/), [Cloudflare Pages](https://pages.cloudflare.com/), [Supabase](https://supabase.com/), [PMTiles](https://docs.protomaps.com/pmtiles/).

La gratuidad es un objetivo de diseño, no una garantía contractual. Los límites vigentes deberán verificarse antes de adoptar cada plataforma. El tiempo de trabajo, la conectividad y el almacenamiento local no están incluidos en el objetivo de costo cero. No se prevé comprar dominio ni contratar servidores durante la primera etapa.

### 7.2 Formatos y rendimiento

GeoJSON será candidato para capas pequeñas y medianas; PMTiles para capas que justifiquen acceso por teselas. CSV y JSON podrán emplearse para tablas e indicadores. Los datos ráster, imágenes aéreas y archivos voluminosos requieren evaluación específica. La elección definitiva dependerá de mediciones reales de tamaño, velocidad, frecuencia de actualización y compatibilidad del alojamiento.

### 7.3 Organización de repositorios

Se propone evaluar una organización GitHub independiente con tres repositorios lógicos: `geosm-visor`, `geosm-datos` y `geosm-procesos`. También es viable comenzar con un único repositorio y separar componentes cuando la escala lo justifique. Los nombres y la estructura definitiva quedan pendientes de acuerdo.

## 8. Política de datos y calidad

Cada capa contará con un identificador estable y una ficha que incluya título, descripción, fuente original, licencia, cobertura, fecha de referencia, fecha de actualización, CRS, tipo de geometría, esquema de atributos, metodología, controles de calidad y limitaciones.

Los originales se conservarán sin alteraciones. Los procesos derivados serán documentados y, cuando sea posible, automatizados. Se verificarán geometrías, duplicados, consistencia de identificadores, valores faltantes, codificación y cobertura espacial. Las modificaciones de geometría y las estimaciones deberán quedar registradas.

La publicación distinguirá entre información oficial de origen, aportes ciudadanos y productos derivados por geoSM. No se asignará carácter oficial a interpretaciones propias. Se respetarán las licencias de terceros; una fuente públicamente accesible no es necesariamente de libre redistribución. Las licencias del código y de los productos propios deberán definirse antes de publicar.

## 9. Gobernanza y mantenimiento

En su etapa inicial, el proyecto será impulsado por su responsable técnico, con posibilidad de incorporar colaboradores. No se presume la existencia de una organización jurídica, convenios ni compromisos institucionales.

Las decisiones técnicas relevantes se registrarán con fecha, estado, justificación y alternativas. Los aportes externos deberán contar con un mecanismo de revisión antes de su publicación. Se procurará disponer de un canal de corrección de errores y actualización de fuentes, sin comprometer datos personales de quienes colaboren.

## 10. Hoja de ruta

| Etapa | Actividades | Criterio de cierre |
|---|---|---|
| 0. Definición | Identidad, alcance, principios y arquitectura preliminar. | Documento fundacional acordado. |
| 1. Inventario | Relevar fuentes, capas, tamaños, licencias y vigencia. | Catálogo inicial y selección de capas publicables. |
| 2. Normalización | Modelo de datos, controles y exportación reproducible. | Primer conjunto de capas validado. |
| 3. Prototipo | Visor estático, mapa base, capas, leyendas y consultas. | Prototipo accesible públicamente sin costo de hosting. |
| 4. Publicación | Metadatos, descargas autorizadas, documentación y pruebas. | Primera versión pública documentada. |
| 5. Consolidación | Actualizaciones, optimización y aportes revisados. | Procedimiento de mantenimiento reproducible. |
| 6. Evolución | Evaluar servicios dinámicos, nuevas capas e interoperabilidad. | Decisiones basadas en necesidades comprobadas. |

No se establecen plazos hasta conocer el inventario real y la disponibilidad de trabajo.

## 11. Indicadores de seguimiento

Se registrarán cantidad de fuentes relevadas, capas disponibles y publicadas, porcentaje de capas con metadatos completos, tamaño de los productos, errores de calidad detectados, antigüedad de los datos y costo monetario recurrente. También se evaluará el rendimiento del visor en dispositivos y conexiones representativos. Las metas cuantitativas se definirán después de establecer una línea de base.

## 12. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Cambios en planes gratuitos | Arquitectura portable, copias locales y alternativas documentadas. |
| Capas demasiado pesadas | Simplificación controlada, teselas y carga bajo demanda. |
| Fuentes discontinuadas | Preservación autorizada de originales y registro de procedencia. |
| Datos desactualizados o incorrectos | Fechas visibles, validaciones y canal de corrección. |
| Restricciones de licencia o privacidad | Revisión previa y exclusión de información no publicable. |
| Dependencia de una sola persona | Documentación y procesos reproducibles. |
| Confusión con un portal oficial | Identidad independiente y aviso visible en el sitio. |

## 13. Decisiones iniciales y asuntos pendientes

**Definiciones de partida:** iniciativa vecinal no gubernamental, ámbito municipal, visualizador público y objetivo de alojamiento sin costo monetario.

**Propuestas técnicas sujetas a validación:** arquitectura estática, GitHub Pages, procesamiento local, GeoJSON, PMTiles, Leaflet o MapLibre y organización de repositorios.

**Pendientes:** nombre público definitivo, inventario real de fuentes, volumen de datos, licencias, mapa base, selección de capas iniciales, estructura de repositorios y diseño de interfaz. No se ha realizado todavía una prueba de alojamiento ni una auditoría de los datos.

## 14. Declaración fundacional

geoSM propone que el conocimiento del territorio pueda construirse y compartirse también desde la ciudadanía. Su propósito es transformar información geográfica dispersa en recursos accesibles, documentados y útiles para comprender General San Martín, mediante tecnologías abiertas y una infraestructura sostenible.

El proyecto aspira a crecer a partir de resultados verificables, sin depender inicialmente de financiamiento externo ni de infraestructura gubernamental propia. Su valor no estará únicamente en la cantidad de mapas publicados, sino en la calidad, transparencia y posibilidad de reutilizar la información que los sostiene.
