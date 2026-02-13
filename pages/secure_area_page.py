from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SecureAreaPage(BasePage):
    HEADER = (By.CSS_SELECTOR, "div.example h2")
    FLASH = (By.ID, "flash")

    def wait_loaded(self) -> None:
        self.visible(self.HEADER) # Sayfanın yüklendiğinden emin olmak için HEADER elementinin görünür olmasını bekler.
    
    def header_text(self) -> str:
        return self.text_of(self.HEADER) # HEADER elementinin metnini döndürür.
    
    def flash_message(self) -> str:
        raw = self.text_of(self.FLASH)
        # '×' kapatma ikonunu ve gereksiz whitespace/newline'ları temizle
        return raw.replace("×", "").replace("\n", " ").strip()
