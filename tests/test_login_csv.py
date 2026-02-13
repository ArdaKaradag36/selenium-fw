import pytest
from config import DEFAULT_TIMEOUT, LOGIN_PATH
from pages.login_page import LoginPage
from utils.csv_loader import load_csv

cases = load_csv("tests/data/invalid_login.csv")

@pytest.mark.regression
@pytest.mark.parametrize("case", cases)
def test_invalid_login_csv(driver, base_url, case):
    login = LoginPage(driver, timeout=DEFAULT_TIMEOUT)
    login.open(f"{base_url}{LOGIN_PATH}")

    login.login(case["username"], case["password"])

    msg = login.flash_message().lower()
    expected = case["expect_error_contains"].lower()
    assert expected in msg
