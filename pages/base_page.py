from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   # таймаут 10 секунд
    
    def open(self, url):
        """Открывает указанный URL."""
        self.driver.get(url)
        
    def find_element(self, locator):
        """Ожидает видимость элемента и возвращает его."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Кликает по элементу после ожидания его кликабельности."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def add_text(self, locator, text):
        """Вводит текст в поле после его появления."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Возвращает текст элемента."""
        return self.find_element(locator).text

    def scroll_to_element(self, locator):
        """Прокручивает страницу до элемента (чтобы избежать перекрытий)."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_url_contains(self, text):
        """Ожидает, что URL содержит указанную строку."""
        self.wait.until(EC.url_contains(text))