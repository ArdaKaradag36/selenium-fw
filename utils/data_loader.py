import json
from pathlib import Path
from typing import Any, Dict

def load_json(realtive_path: str) -> Dict[str, Any]:
    root = Path(__file__).resolve().parents[1] # utils klasörünün bir üst dizinini alır
    p = root / realtive_path # Verilen göreli yolu root dizini ile birleştirir
    with p.open("r", encoding="utf-8") as f: # Dosyayı açar
        return json.load(f) # Dosyanın içeriğini JSON formatında yükler ve döndürür
