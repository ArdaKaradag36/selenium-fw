import pytest
from faker import Faker

from config import DEFAULT_TIMEOUT, LOGIN_PATH
from pages.login_page import LoginPage
from utils.csv_loader import load_csv

fake = Faker() # Faker kütüphanesinden bir örnek oluşturulur, bu örnek üzerinden rastgele veriler üretilebilir
@pytest.mark.regression
@pytest.mark.parametrize(
    "row",
    load_csv("tests/data/invalid_login.csv"),
    ids=lambda r: r["username"],
)
def test_login_invalid_from_csv(driver, base_url, row): # CSV dosyasından yüklenen her bir satır için test çalışır, row parametresi ile her satırın verileri alınır
    login_page = LoginPage(driver, timeout=DEFAULT_TIMEOUT)
    login_page.open(f"{base_url}{LOGIN_PATH}")

    login_page.login(row["username"], row["password"]) # CSV dosyasındaki username ve password değerleri kullanılarak login işlemi yapılır
    assert row["expect_error_contains"] in login_page.flash_message()


@pytest.mark.regression # Bu testin regression test kategorisine ait olduğunu belirtir
def test_login_invalid_with_faker(driver, base_url):
    """Dinamik negatif test verisi üretimine örnek."""

    username = fake.user_name()
    password = fake.password(length=12) # Faker kütüphanesi kullanılarak rastgele bir kullanıcı adı ve şifre oluşturulur, length parametresi ile şifrenin uzunluğu belirlenir

    login_page = LoginPage(driver, timeout=DEFAULT_TIMEOUT) # LoginPage sınıfından bir örnek oluşturulur, bu örnek üzerinden login sayfasına erişim sağlanır ve işlemler yapılır
    login_page.open(f"{base_url}{LOGIN_PATH}")

    login_page.login(username, password) # Faker ile oluşturulan kullanıcı adı ve şifre kullanılarak login işlemi yapılır, bu verilerin geçersiz olması beklenir
    assert "invalid" in login_page.flash_message().lower()
