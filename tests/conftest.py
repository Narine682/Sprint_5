import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
CHROMEDRIVER_PATH = "C:\\Users\\Artar\\PycharmProjects\\Sprint_5\\WebDriver\\bin\\chromedriver.exe"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
