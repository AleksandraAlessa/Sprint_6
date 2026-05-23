import pytest
import allure
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.main_page import MainPage
from data import BASE_URL, FAQ_EXPECTED_ANSWERS


@allure.feature("Раздел «Вопросы о важном»")
class TestFAQ:

    @allure.title("Проверка текста ответа на вопрос №{index}")
    @pytest.mark.parametrize("index, expected_text", enumerate(FAQ_EXPECTED_ANSWERS))
    def test_faq_answer(self, driver: WebDriver, index: enumerate[str], expected_text: enumerate[str]):
        main_page = MainPage(driver)
        main_page.open(BASE_URL)
        main_page.accept_cookies()
        main_page.click_question(index)
        actual_text = main_page.get_answer_text(index)
        assert actual_text == expected_text, f"Ожидался текст: {expected_text}\nПолучен: {actual_text}"