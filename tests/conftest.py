import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tests.generators import generate_email, generate_password, generate_name

CHROMEDRIVER_PATH = "C:\\Users\\Artar\\PycharmProjects\\Sprint_5\\WebDriver\\bin\\chromedriver.exe"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
@pytest.fixture
def user_data():
    return {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name()
             }