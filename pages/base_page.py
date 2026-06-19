from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   # таймаут 10 секунд

    @allure.step("Открыть страницу по URL: {url}")
    def open(self, url):
        """Открывает указанный URL."""
        self.driver.get(url)

    @allure.step("Найти элемент {locator}")  
    def find_element(self, locator):
        """Ожидает видимость элемента и возвращает его."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть на элемент {locator}")
    def click_element(self, locator):
        """Кликает по элементу после ожидания его кликабельности."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввести текст '{text}' в поле {locator}")
    def add_text(self, locator, text):
        """Вводит текст в поле после его появления."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст из элемента {locator}")
    def get_text(self, locator):
        """Возвращает текст элемента."""
        return self.find_element(locator).text

    @allure.step("Прокрутить до элемента {locator}")
    def scroll_to_element(self, locator):
        """Прокручивает страницу до элемента (чтобы избежать перекрытий)."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Прокрутить до элемента {locator} с центрированием")
    def scroll_to_element_center(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Кликнуть на элемент через JavaScript (обходит перекрытие)")
    def click_by_js(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Выполнить JavaScript: {script}")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
     
    @allure.step("Ожидает, что URL содержит указанную строку '{text}'")
    def wait_for_url_contains(self, text):
        """Ожидает, что URL содержит указанную строку."""
        self.wait.until(EC.url_contains(text))
    
    @allure.step("Ожидать количество окон: {count}")
    def wait_for_number_of_windows(self, count):
        self.wait.until(EC.number_of_windows_to_be(count))

    @allure.step("Ждать, пока элемент станет кликабельным")
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ждать видимости элемента")
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить список окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться на окно с индексом {index}")
    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Закрыть текущее окно")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Переключиться на последнее открытое окно")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Ожидать, что URL содержит '{text}'")
    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))
    
    @allure.step("Переключиться на исходное окно")
    def switch_to_original_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])