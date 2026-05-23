from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
import allure
import time

class OrderPage(BasePage):
    # ---------- Локаторы ----------
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")

    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # ---------- Методы для заполнения первой формы ----------
    @allure.step("Заполнить поле Имя: {name}")
    def set_name(self, name):
        self.add_text(self.NAME_FIELD, name)

    @allure.step("Заполнить поле Фамилия: {surname}")
    def set_surname(self, surname):
        self.add_text(self.SURNAME_FIELD, surname)

    @allure.step("Заполнить поле Адрес: {address}")
    def set_address(self, address):
        self.add_text(self.ADDRESS_FIELD, address)

    @allure.step("Выбрать станцию метро: {metro_station}")
    def select_metro_station(self, metro_station):
        self.click_element(self.METRO_FIELD)
        self.add_text(self.METRO_FIELD, metro_station)
        station_locator = (By.XPATH, f"//div[contains(text(), '{metro_station}')]")
        self.click_element(station_locator)

    @allure.step("Заполнить поле Телефон: {phone}")
    def set_phone(self, phone):
        self.add_text(self.PHONE_FIELD, phone)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        self.click_element(self.NEXT_BUTTON)

    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, metro, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.select_metro_station(metro)
        self.set_phone(phone)
        self.click_next()
        # Явное ожидание появления поля даты (вторая форма)
        self.wait.until(EC.visibility_of_element_located(self.DATE_FIELD))

    # ---------- Методы для заполнения второй формы ----------
    @allure.step("Когда привезти самокат: {date}")
    def set_date(self, date):
        date_field = self.wait.until(EC.visibility_of_element_located(self.DATE_FIELD))
        date_field.clear()
        date_field.send_keys(date)
        date_field.send_keys(Keys.RETURN)

    @allure.step("Выбрать срок аренды: {rental_days}")
    def select_rental_period(self, rental_days):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.RENTAL_PERIOD_DROPDOWN))
        self.driver.execute_script("arguments[0].click();", dropdown)

        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Dropdown-option")))

        option_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{rental_days}']")
        option = self.wait.until(EC.element_to_be_clickable(option_locator))
        self.driver.execute_script("arguments[0].click();", option)

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color):
        if color == "чёрный жемчуг" or color == "Чёрный жемчуг":
            self.click_element(self.COLOR_BLACK)
        elif color == "серая безысходность" or color == "Серая безысходность":
            self.click_element(self.COLOR_GREY)
        else:
            raise ValueError(f"Неизвестный цвет: {color}")

    @allure.step("Добавить комментарий: {comment}")
    def set_comment(self, comment):
        if comment:
            self.add_text(self.COMMENT_FIELD, comment)

    @allure.step("Нажать кнопку 'Заказать' (финальная)")
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, date, rental_days, color, comment):
        self.set_date(date)
        self.select_rental_period(rental_days)
        self.select_color(color)
        self.set_comment(comment)
        self.click_order_button()

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self.click_element(self.CONFIRM_BUTTON)

    @allure.step("Проверить, что заказ успешно создан")
    def is_order_successful(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE)).is_displayed()

    @allure.step("Оформить заказ полностью")
    def create_order(self, order_data):
        self.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        self.fill_second_form(
            order_data["date"],
            order_data["rental_days"],
            order_data["color"],
            order_data["comment"]
        )
        self.confirm_order()
        return self.is_order_successful()