import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from datetime import datetime
from pathlib import Path
import pytest
from config import BASE_URL, DEFAULT_TIMEOUT
from utils.browser_factory import get_driver


@pytest.fixture
def base_url() -> str:
    return BASE_URL


@pytest.fixture
def driver(request):
    drv = get_driver()  # Tarayıcı sürücüsünü oluşturur
    drv.implicitly_wait(0)  # Implicit wait'i sıfırlar, explicit wait'ler kullanılacak
    yield drv  # Test fonksiyonuna sürücüyü sağlar
    drv.quit()  # Test tamamlandıktan sonra tarayıcıyı kapatır


# ⭐⭐⭐ SADECE BURASI DÜZELTİLDİ
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when != "call" or not rep.failed:
        return

    drv = item.funcargs.get("driver")
    if drv is None:
        return

    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_dir = Path("reports/screenshots")
    screenshot_dir.mkdir(exist_ok=True)

    filename = f"{item.name}_{ts}.png"
    filepath = screenshot_dir / filename

    try:
        drv.save_screenshot(str(filepath))
    except Exception:
        print(f"Failed to save screenshot: {filepath}")
