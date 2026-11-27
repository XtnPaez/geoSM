from pathlib import Path
import shutil
root = Path(__file__).resolve().parents[1]
src = root / 'datos/publicados/geografias'
dst = root / 'site/geografias'
dst.mkdir(parents=True, exist_ok=True)
for p in src.iterdir():
    if p.suffix.lower() in {'.geojson', '.gpkg'}:
        shutil.copy2(p, dst / p.name)
        print(p.name)
