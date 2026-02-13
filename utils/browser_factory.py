from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from config import BROWSER, HEADLESS


def get_driver():
    """Bir WebDriver örneği oluşturur.

    Neden factory?
    - Tarayıcı yapılandırmasını tek merkezde toplar (DRY)
    - Kolay genişletme sağlar (grid, remote, profile vb.)
    """

    browser = (BROWSER or "").lower().strip()

    if browser == "firefox":  # Firefox için seçenekler ve sürücü kurulumu
        options = FirefoxOptions()
        if HEADLESS:
            options.add_argument("-headless")

        # PATH içindeki geckodriver otomatik kullanılacak
        driver = webdriver.Firefox(
            options=options
        )

    elif browser == "chrome":  # Chrome için seçenekler ve sürücü kurulumu
        options = ChromeOptions()
        if HEADLESS:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")

        # PATH içindeki chromedriver otomatik kullanılacak
        driver = webdriver.Chrome(
            options=options
        )

    else:
        raise ValueError(f"Desteklenmeyen tarayıcı: {BROWSER}")

    driver.maximize_window()
    return driver

#.\.venv\Scripts\Activate.ps1