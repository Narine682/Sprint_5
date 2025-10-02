import pytest
from selenium import webdriver
from generators import generate_email, generate_password, generate_name

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
