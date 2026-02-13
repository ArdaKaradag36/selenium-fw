from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # ✅ Locator = element adresi
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def open(self, url: str) -> None:
        self.driver.get(url)

    def fill_username(self, username: str) -> None:
        self.type(self.USERNAME, username)

    def fill_password(self, password: str) -> None:
        self.type(self.PASSWORD, password)

    def submit(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.fill_username(username)
        self.fill_password(password)
        self.submit()

    def flash_message(self) -> str:
        return self.text_of(self.FLASH)
