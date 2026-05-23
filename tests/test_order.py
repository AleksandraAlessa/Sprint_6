import pytest
import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import BASE_URL, ORDER_DATA


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа (кнопка {button_position})")
    @pytest.mark.parametrize("button_position", ["top", "bottom"])
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_order_scooter(self, driver: WebDriver, button_position: typing.Literal['top'] | typing.Literal['bottom'], order_data: dict[str, str]):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()

        if button_position == "top":
            main_page.click_top_order_button()
        else:
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