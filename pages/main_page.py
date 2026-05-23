from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
import allure


class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")  # принятие куки (если есть)

    # Кнопки заказа
    ORDER_TOP_BUTTON = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")  # верхняя кнопка
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")  # нижняя кнопка 

    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    # Вопросы и ответы (аккордеон)
    FAQ_QUESTIONS = (By.XPATH, "//div[@class='accordion__item']")
    
    # Используем шаблон локаторов с индексом
    def get_question_locator(self, index):
        return (By.ID, f"accordion__heading-{index}")

    def get_answer_locator(self, index):
        return (By.ID, f"accordion__panel-{index}")

    # Методы для работы с куки
    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click_element(self.COOKIE_BUTTON)
        except:
            pass  # если кнопки нет – ничего страшного

    # Методы для кнопок заказа
    @allure.step("Нажать верхнюю кнопку 'Заказать'")
    def click_top_order_button(self):
        self.click_element(self.ORDER_TOP_BUTTON)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_bottom_order_button(self):
        self.scroll_to_element(self.ORDER_BOTTOM_BUTTON)  # прокрутка до нижней кнопки
        self.click_element(self.ORDER_BOTTOM_BUTTON)

    # Методы для работы с аккордеоном (вопросы о важном)
    @allure.step("Кликнуть на вопрос с индексом {index}")
    def click_question(self, index):
        locator = self.get_question_locator(index)

    # Прокручиваем до элемента
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    # Кликаем через JS, чтобы обойти перекрытие
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текст ответа на вопрос {index}")
    def get_answer_text(self, index):
        locator = self.get_answer_locator(index)
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)

    # Методы для логотипов
    @allure.step("Кликнуть на логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип 'Яндекс'")
    def click_yandex_logo(self):
        element = self.wait.until(EC.element_to_be_clickable(self.YANDEX_LOGO))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(EC.number_of_windows_to_be(2))