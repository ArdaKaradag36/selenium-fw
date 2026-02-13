import os

# Merkezi yapılandırma (tek doğru kaynak)

BROWSER = os.getenv("BROWSER", "firefox")  # "firefox" | "chrome"
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"  # CI'da default True önerilir
BASE_URL = "https://the-internet.herokuapp.com"

# Test hedefleri
LOGIN_PATH = "/login"

# Demo site için varsayılan kullanıcı bilgileri
USERNAME = "tomsmith"
PASSWORD = "SuperSecretPassword!"

# Varsayılan bekleme süresi
DEFAULT_TIMEOUT = 10
