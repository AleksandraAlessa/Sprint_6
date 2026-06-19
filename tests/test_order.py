import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import BASE_URL, ORDER_DATA


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа (верхняя кнопка)")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_order_scooter_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_top_order_button()

        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        order_page.fill_second_form(
            order_data["date"],
            order_data["rental_days"],
            order_data["color"],
            order_data["comment"]
        )
        order_page.confirm_order()
        assert order_page.is_order_successful(), "Заказ не был создан"

    @allure.title("Позитивный сценарий заказа (нижняя кнопка)")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_order_scooter_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_bottom_order_button()

        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        order_page.fill_second_form(
            order_data["date"],
            order_data["rental_days"],
            order_data["color"],
            order_data["comment"]
        )
        order_page.confirm_order()
        assert order_page.is_order_successful(), "Заказ не был создан"