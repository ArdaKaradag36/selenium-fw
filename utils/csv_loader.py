import csv
from pathlib import Path
from typing import Dict, List

def load_csv(relative_path: str) -> List[Dict[str, str]]:
    root = Path(__file__).resolve().parents[1]
    p = root / relative_path
    with p.open("r", encoding="utf-8-sig", newline="") as f:  # ✅ BOM fix
        reader = csv.DictReader(f)
        return list(reader)
