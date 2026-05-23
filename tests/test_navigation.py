import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from data import BASE_URL

@allure.feature("Навигация по логотипам")
class TestNavigation:

    @allure.title("Переход на главную страницу по логотипу «Самокат»")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        # Переходим на любую другую страницу, например, заказа
        main_page.click_top_order_button()
        # Теперь кликаем на логотип Самоката
        main_page.click_scooter_logo()
        # Проверяем, что URL стал главной страницей
        assert driver.current_url == BASE_URL, f"Текущий URL: {driver.current_url}"

    @allure.title("Переход на главную страницу Дзена по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()
        # Переключаемся на новую вкладку
        driver.switch_to.window(driver.window_handles[1])
         # Ждём, что URL содержит dzen.ru
        WebDriverWait(driver, 10).until(EC.url_contains("dzen.ru"))
        # Проверяем, что URL содержит dzen.ru
        assert "dzen.ru" in driver.current_url
        # Закрываем вкладку и возвращаемся обратно (опционально)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])