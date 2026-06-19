import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from data import ORDER_DATA

@pytest.fixture
def driver():
    """Фикстура для запуска браузера Firefox."""
    options = Options()
    options.add_argument('--width=1920')
    options.add_argument('--height=1080')
    # Можно добавить headless-режим при необходимости:
    # options.add_argument('--headless')
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()


