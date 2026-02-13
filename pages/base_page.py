from dataclasses import dataclass
from typing import Optional, Tuple
from xml.sax.xmlreader import Locator

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

Lacotory = Tuple[str, str]  # Lacotor örneği: (By.ID,"surname")  By.ID, By.XPATH, By.CSS_SELECTOR, By.CLASS_NAME, By.NAME, By.TAG_NAME, By.LINK_TEXT, By.PARTIAL_LINK_TEXT

@dataclass
class BasePage:
    driver: WebDriver # WebDriver örneği
    timeout: int = 10 # Varsayılan bekleme süresi (saniye cinsinden)

    def _wait(self) -> WebDriverWait: # WebDriverWait nesnesi oluşturur.
        """WebDriverWait nesnesi oluşturur."""
        return WebDriverWait(self.driver, self.timeout)
    
    def open(self, url: Optional[str] = None):  # URL'ye gitmek için kullanılan yöntem.
        """Belirtilen URL'ye gider veya BASE_URL'yi kullanır."""
        self.driver.get(url or self.BASE_URL) 

    def find(self, locator: Locator) -> WebElement: # Belirtilen locator ile elementi bulur ve döndürür.
        """Eleman DOM'da oluşana kadar bekler."""
        return self._wait().until(EC.presence_of_element_located(locator)) 
    
    def visible(self, locator: Locator) -> WebElement: # Belirtilen locator ile elementi bulur ve görünür olana kadar bekler.
        """Eleman görünür olana kadar bekler."""
        return self._wait().until(EC.visibility_of_element_located(locator))
    
    def clickable(self, locator: Locator) -> WebElement: # Belirtilen locator ile elementi bulur ve tıklanabilir olana kadar bekler.
        """Eleman tıklanabilir olana kadar bekler."""
        return self._wait().until(EC.element_to_be_clickable(locator))
    
    def click(self, locator: Locator) ->None:
        self.clickable(locator).click() # Belirtilen locator ile elementi bulur, tıklanabilir olana kadar bekler ve tıklar.

    def type(self, locator: Locator, text: str, clear: bool = True) -> None:
        el = self.visible(locator) # Belirtilen locator ile elementi bulur ve görünür olana kadar bekler.
        if clear:
            el.clear() # Elemanın içeriğini temizler.
        el.send_keys(text) # Elemanın içine belirtilen metni yazar.

    def text_of(self, locator: Locator) -> str:
        return self.visible(locator).text # Belirtilen locator ile elementi bulur, görünür olana kadar bekler ve elemanın metnini döndürür.
    
    def is_visible(self, locator : Locator) -> bool:
        try:
            self.visible(locator) # Belirtilen locator ile elementi bulur ve görünür olana kadar bekler.
            return True # Eleman görünürse True döndürür.
        except Exception:
            return False # Eleman görünmezse veya bulunamazsa False döndürür.
        
    def wait_url_contains(self, fragment: str) -> None:
        self._wait().until(EC.url_contains(fragment)) # URL'nin belirtilen parçayı içermesini bekler.

    def wait_title_contains(self, fragment: str) -> None:
        self._wait().until(EC.title_contains(fragment)) # Sayfa başlığının belirtilen parçayı içermesini bekler.

    def screenshot(self, path: str) -> None:
        self.driver.save_screenshot(path) # Tarayıcının ekran görüntüsünü belirtilen dosya yoluna kaydeder.

    def maybe_get_text(self, locator: Locator) -> Optional[str]:
        try:
            return self.text_of(locator) # Belirtilen locator ile elementi bulur, görünür olana kadar bekler ve elemanın metnini döndürür.
        except Exception:
            return None # Eleman bulunamazsa veya görünmezse None döndürür.
