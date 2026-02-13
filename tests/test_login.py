import pytest
from config import DEFAULT_TIMEOUT, LOGIN_PATH
from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage
from utils.data_loader import load_json

def _login_cases(): # Verileri JSON dosyasından yükler
    data = load_json("tests/data/login.json")
    return data["cases"]

@pytest.mark.smoke # Bu testin smoke test kategorisine ait olduğunu belirtir
@pytest.mark.parametrize("case", _login_cases()) # Her test çalıştırıldığında _login_cases fonksiyonu çağrılır ve dönen her bir case için test çalışır
def test_login_data_driven(driver, base_url, case): # Test fonksiyonu, driver ve base_url fixture'larını kullanır ve case parametresi ile her test senaryosunu alır
    login_url = f"{base_url}{LOGIN_PATH}"
    login_page = LoginPage(driver, timeout=DEFAULT_TIMEOUT)
    login_page.open(login_url)
    login_page.login(case["username"], case["password"])

    if case["expect"] == "success": # Eğer beklenen sonuç "success" ise, SecureAreaPage'e geçilir ve doğrulamalar yapılır
        secure = SecureAreaPage(driver, timeout=DEFAULT_TIMEOUT)
        secure.wait_loaded()
        assert "Secure Area" in secure.header_text()
        assert "You logged into a secure area!" in secure.flash_message()
    else: # Eğer beklenen sonuç "success" değilse, login sayfasında kalınır ve hata mesajı doğrulanır
        msg = login_page.flash_message()
        assert case["error_contains"] in msg
