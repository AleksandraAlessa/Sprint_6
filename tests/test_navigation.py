import allure
import pytest
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
        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()
        # Проверяем, что URL стал главной страницей
        assert main_page.get_current_url() == BASE_URL

    @allure.title("Переход на главную страницу Дзена по логотипу Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        # Кликаем на логотип Яндекса (внутри метода уже ожидается открытие новой вкладки)
        main_page.click_yandex_logo()
        # Переключаемся на новую вкладку
        main_page.switch_to_last_window()   # или main_page.switch_to_window(1)
        # Ждём, что URL содержит dzen.ru
        main_page.wait_for_url_contains("dzen.ru")
        # Проверяем URL
        assert "dzen.ru" in main_page.get_current_url()
        # Закрываем вкладку и возвращаемся обратно
        main_page.close_current_window()
        main_page.switch_to_original_window() 