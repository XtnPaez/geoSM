"""Ejecutar desde la raíz. Descarga dependencias fijadas y prepara vista local."""
from pathlib import Path
from urllib.request import urlretrieve
import shutil
root=Path(__file__).resolve().parents[1]; site=root/'site'; vendor=site/'assets/vendor'
for name,version,files in [('leaflet','1.9.4',['dist/leaflet.js','dist/leaflet.css','dist/images/layers.png','dist/images/layers-2x.png','dist/images/marker-icon.png','dist/images/marker-icon-2x.png','dist/images/marker-shadow.png','LICENSE']),('bootstrap','5.3.3',['dist/css/bootstrap.min.css','LICENSE'])]:
 for f in files:
  rel=f.removeprefix('dist/').removeprefix('css/'); dest=vendor/name/rel; dest.parent.mkdir(parents=True,exist_ok=True); urlretrieve(f'https://unpkg.com/{name}@{version}/{f}',dest)
shutil.copytree(root/'datos/publicados/geografias',site/'geografias',dirs_exist_ok=True,ignore=shutil.ignore_patterns('*.qmd'))
print('Preparado. Ejecutar: python -m http.server 8000 --directory site')
