import json

from pathlib import Path

pass_db = json.loads(Path('api/data/pass_db.json').read_text())
simple_db = json.loads(Path('api/data/data.json').read_text())
